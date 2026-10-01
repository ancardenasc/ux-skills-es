"""Genera shared/data/wcag22-criteria.json.

Hechos (id, nombre, nivel, versión): datos legibles por máquina de W3C, descargados en el momento.
Textos: shared/data/wcag22-own-text.yml (redacción propia).
No se guarda ningún texto de la especificación: solo número, nombre, nivel, versión y enlace.

Uso: python scripts/gen_wcag_data.py [--source RUTA_O_URL] [--date AAAA-MM-DD]
"""
import argparse
import json
import urllib.request
from datetime import date

import yaml

from common import ROOT

W3C_URL = "https://www.w3.org/WAI/WCAG22/wcag.json"
UNDERSTANDING = "https://www.w3.org/WAI/WCAG22/Understanding/{slug}.html"
OWN = ROOT / "shared" / "data" / "wcag22-own-text.yml"
OUT = ROOT / "shared" / "data" / "wcag22-criteria.json"
LEVELS = ("A", "AA")


def load_w3c(source):
    if source.startswith("http"):
        req = urllib.request.Request(source, headers={"User-Agent": "ux-skills-es/gen_wcag_data"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    with open(source, encoding="utf-8") as fh:
        return json.load(fh)


def w3c_criteria(data):
    """Criterios de nivel A y AA vigentes en 2.2, en orden de especificación."""
    out = []
    for p in data["principles"]:
        for g in p["guidelines"]:
            for sc in g["successcriteria"]:
                if sc.get("level") in LEVELS:
                    versions = sc["versions"]
                    if isinstance(versions, str):
                        versions = eval_list(versions)
                    if "2.2" not in versions:
                        continue
                    out.append({"id": sc["num"], "slug": sc["id"], "name_en": sc["handle"],
                                "level": sc["level"], "since": versions[0]})
    return out


def eval_list(text):
    return [v.strip(" '\"") for v in text.strip("[]").split(",") if v.strip(" '\"")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=W3C_URL)
    ap.add_argument("--date", default=date.today().isoformat())
    args = ap.parse_args()

    own = yaml.safe_load(OWN.read_text(encoding="utf-8"))
    facts = w3c_criteria(load_w3c(args.source))
    ids = [f["id"] for f in facts]
    if set(ids) != set(own):
        raise SystemExit(
            f"los textos propios no coinciden con W3C. Faltan: {sorted(set(ids) - set(own))} "
            f"Sobran: {sorted(set(own) - set(ids))}")

    criteria = []
    for f in facts:
        t = own[f["id"]]
        criteria.append({
            "id": f["id"],
            "name_en": f["name_en"],
            "level": f["level"],
            "since": f["since"],
            "url": UNDERSTANDING.format(slug=f["slug"]),
            "label_es": t["label_es"],
            "summary_es": t["es"],
            "summary_en": t["en"],
            "assessable": {"code": t["code"], "url": t["url"], "design": t["design"]},
        })
    doc = {
        "_comment": "GENERADO por scripts/gen_wcag_data.py. Hechos de W3C; resúmenes y etiquetas propios.",
        "wcag_version": "2.2",
        "levels": list(LEVELS),
        "source": {"url": W3C_URL, "retrieved_on": args.date,
                   "license_note": "Solo número, nombre, nivel y enlace de W3C; ningún texto de la especificación."},
        "criteria": criteria,
    }
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    levels = {lv: sum(1 for c in criteria if c["level"] == lv) for lv in LEVELS}
    print(f"{len(criteria)} criterios {levels} -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
