"""Verifica un caso de estudio redactado contra el proyecto fuente (fixture).

Uso: python tests/evals/check_case_study.py caso.md tests/fixtures/case-aurora [--idioma es|en]
Comprueba: encabezados de la plantilla en orden, citas [fuente: ruta] que existen, cifras que salen de las
fuentes (nada inventado), marcadores de datos faltantes donde faltan datos, ausencia de datos privados y mención
de que el proyecto es de muestra. Sale con 1 si falla alguna comprobación dura.
"""
import json
import re
import sys
from pathlib import Path

import yaml

CITATION = re.compile(r"\[(?:fuente|source):\s*([^\]]+)\]", re.I)
NUMBER = re.compile(r"(?<![\w.-])\d+(?:[.,]\d+)?(?![\w-])")


def numbers(text):
    return {n.replace(",", ".") for n in NUMBER.findall(text)}


def derivable(source):
    """Cifras con una derivación razonable a partir del texto fuente (no cualquier suma o resta):
    diferencias entre porcentajes presentes, porcentaje de una expresión "a de b" y el paso 100/b."""
    pct = {float(n) for n in re.findall(r"(\d+(?:[.,]\d+)?)\s*%", source.replace(",", "."))}
    out = {abs(a - b) for a in pct for b in pct}
    for a, b in re.findall(r"(\d+)\s+(?:de|of)\s+(\d+)", source):
        a, b = int(a), int(b)
        if b:
            out.add(round(100 * a / b))
            out.add(round(100 / b))
    return {str(int(v)) if float(v).is_integer() else str(v) for v in out}


def source_text(fixture):
    return "\n".join(p.read_text(encoding="utf-8") for p in sorted(fixture.rglob("*.md")) if "case-study.md" not in p.name)


def section(text, heading):
    m = re.search(rf"^#{{1,4}}\s+{re.escape(heading)}\s*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^#{1,2}\s+\S", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def check(text, fixture, expected, lang="es"):
    cfg = expected[lang]
    r = {"missing_headings": [], "bad_citations": [], "citations": 0, "invented_numbers": [], "missing_placeholders": [],
         "forbidden_found": [], "missing_sample_mention": False, "unused_numbers": [], "derived_numbers": []}
    pos = -1
    for h in cfg["headings"]:
        m = re.search(rf"^#{{1,4}}\s+{re.escape(h)}\s*$", text, re.M)
        if not m or m.start() < pos:
            r["missing_headings"].append(h)
        else:
            pos = m.start()
    cites = CITATION.findall(text)
    r["citations"] = len(cites)
    for c in cites:
        for part in re.split(r"[;,]", c):
            path = part.strip().strip("`").split("#")[0].strip()
            if path and not (fixture / path).exists():
                r["bad_citations"].append(path)
    body = CITATION.sub("", text)
    body = re.sub(r"\]\([^)]*\)", "]", body)
    known = numbers(source_text(fixture)) | set(expected.get("allowed_numbers", []))
    unknown = numbers(body) - known
    derived = derivable(source_text(fixture))
    r["derived_numbers"] = sorted(unknown & derived)   # revisar a mano: deben poder rehacerse
    r["invented_numbers"] = sorted(unknown - derived)
    for h in cfg["placeholders_in"]:
        s = section(text, h)
        if s is None or cfg["placeholder_marker"] not in s:
            r["missing_placeholders"].append(h)
    r["forbidden_found"] = [w for w in expected["forbidden_text"] if w in text]
    r["missing_sample_mention"] = not any(w in text.lower() for w in cfg["must_mention_any"])
    r["unused_numbers"] = [n for n in expected["must_use_numbers"] if n not in numbers(body)]
    return r


def hard_failures(r, min_citations):
    return (r["missing_headings"] or r["bad_citations"] or r["invented_numbers"] or r["missing_placeholders"]
            or r["forbidden_found"] or r["missing_sample_mention"] or r["citations"] < min_citations)


def main():
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    fixture = Path(sys.argv[2])
    lang = sys.argv[sys.argv.index("--idioma") + 1] if "--idioma" in sys.argv else "es"
    expected = yaml.safe_load((fixture / "expected.yml").read_text(encoding="utf-8"))
    r = check(text, fixture, expected, lang)
    print(json.dumps(r, indent=2, ensure_ascii=False))
    sys.exit(1 if hard_failures(r, expected["min_citations"]) else 0)


if __name__ == "__main__":
    main()
