"""Valida un informe de auditoría: bloque JSON contra el esquema, secciones, pie legal y reglas cruzadas.

Uso: python scripts/validate_report.py informe.md [otro.md ...]
"""
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from common import ROOT

SCHEMA = ROOT / "shared" / "schema" / "report.schema.json"
CRITERIA = ROOT / "shared" / "data" / "wcag22-criteria.json"
NIELSEN = ROOT / "shared" / "data" / "nielsen-heuristics.json"
LABELS = ROOT / "shared" / "i18n" / "labels.yml"
SECTIONS = ["summary", "scope", "findings", "manual", "passed", "honest-gaps", "next-steps"]
BLOCK = re.compile(r"```json ux-skills-findings\n(.*?)\n```", re.S)
COVERAGE = re.compile(r"\*\*(?:Cobertura|Coverage):\*\*\s*(\d+)\s*(?:de|of)\s*(\d+)")
ORDER = {"low": 0, "medium": 1, "high": 2}
CAP = {"axe": "high", "dom_runtime": "high", "token_script": "high",
       "static_code": "medium", "design_context": "medium", "screenshot": "low", "inferred": "low"}


def validate_text(text):
    """Devuelve (errores, estadísticas)."""
    errors, stats = [], {}
    blocks = BLOCK.findall(text)
    if len(blocks) != 1:
        return [f"debe haber exactamente un bloque 'ux-skills-findings' (hay {len(blocks)})"], stats
    try:
        data = json.loads(blocks[0])
    except json.JSONDecodeError as e:
        return [f"el bloque JSON no se puede leer: {e}"], stats

    validator = Draft202012Validator(json.loads(SCHEMA.read_text()))
    for e in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        where = "/".join(str(p) for p in e.absolute_path) or "(raíz)"
        errors.append(f"esquema en {where}: {e.message}")

    for section in SECTIONS:
        if f"<!-- section:{section} -->" not in text:
            errors.append(f"falta el marcador de sección <!-- section:{section} -->")

    lang = data.get("language")
    labels = yaml.safe_load(LABELS.read_text(encoding="utf-8"))
    if lang in labels and labels[lang]["disclaimer"] not in text:
        errors.append("falta el pie legal (etiqueta disclaimer de labels.yml)")

    wcag = {c["id"]: c for c in json.loads(CRITERIA.read_text(encoding="utf-8"))["criteria"]}
    nielsen = {}
    if NIELSEN.exists():
        nielsen = {h["id"]: h for h in json.loads(NIELSEN.read_text(encoding="utf-8"))["heuristics"]}

    seen = set()
    counts = {"pass": 0, "fail": 0, "manual": 0, "not_applicable": 0, "not_tested": 0}
    for f in data.get("findings", []):
        fid = f.get("id", "?")
        if fid in seen:
            errors.append(f"{fid}: id repetido")
        seen.add(fid)
        counts[f.get("status")] = counts.get(f.get("status"), 0) + 1
        crit = f.get("criterion", {})
        if crit.get("system") == "WCAG22":
            ref = wcag.get(crit.get("id"))
            if not ref:
                errors.append(f"{fid}: el criterio WCAG {crit.get('id')} no existe en los datos (solo A y AA de 2.2)")
            else:
                for field, key in (("name", "name_en"), ("level", "level"), ("url", "url")):
                    if crit.get(field) != ref[key]:
                        errors.append(f"{fid}: {field} {crit.get(field)!r} no coincide con los datos ({ref[key]!r}); "
                                      "en el JSON copia name_en, level y url tal cual, sin traducir")
        elif crit.get("system") == "NIELSEN" and nielsen:
            ref = nielsen.get(crit.get("id"))
            if not ref or crit.get("name") != ref["name_en"]:
                errors.append(f"{fid}: la heurística {crit.get('id')} no coincide con los datos")
        cap = CAP.get(f.get("method"))
        if cap and f.get("confidence") in ORDER and ORDER[f["confidence"]] > ORDER[cap]:
            errors.append(f"{fid}: confianza {f['confidence']} supera el techo {cap} del método {f['method']}")
        if f.get("severity") and f.get("status") != "fail":
            errors.append(f"{fid}: la gravedad solo se asigna a hallazgos fail")

    assessed = counts["pass"] + counts["fail"]
    applicable = assessed + counts["manual"] + counts["not_tested"]
    stats = {**counts, "assessed": assessed, "applicable": applicable,
             "coverage": round(assessed / applicable, 2) if applicable else None}
    declared = COVERAGE.search(text)
    if declared and (int(declared.group(1)), int(declared.group(2))) != (assessed, applicable):
        errors.append(f"la cobertura declarada ({declared.group(1)} de {declared.group(2)}) no coincide con la "
                      f"calculada desde los hallazgos ({assessed} de {applicable})")
    return errors, stats


def main():
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        print(__doc__)
        sys.exit(2)
    bad = 0
    for p in paths:
        errors, stats = validate_text(p.read_text(encoding="utf-8"))
        print(f"{p}: {'OK' if not errors else 'CON ERRORES'} {stats if not errors else ''}")
        for e in errors:
            print("  ERROR", e)
        bad += bool(errors)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
