"""Comprueba shared/data/wcag22-criteria.json.

Sin banderas: comprobaciones estructurales sin red (puerta de cada PR).
--online: compara id, nombre y nivel con los datos legibles por máquina de W3C (deriva).
--urls:   comprueba que cada enlace "Understanding" responde 2xx.
"""
import json
import re
import sys
import urllib.request

from common import ROOT
from gen_wcag_data import load_w3c, w3c_criteria, W3C_URL

DATA = ROOT / "shared" / "data" / "wcag22-criteria.json"
EXPECTED = {"A": 31, "AA": 24}  # criterios A y AA de WCAG 2.2 (sin 4.1.1, eliminado). Cambiar solo a propósito.
ID = re.compile(r"^\d\.\d\.\d{1,2}$")
URL = re.compile(r"^https://www\.w3\.org/WAI/WCAG22/Understanding/[a-z0-9-]+\.html$")
MODES = {"yes", "partial", "no"}


def check_structure(doc):
    errors = []
    criteria = doc["criteria"]
    ids = [c["id"] for c in criteria]
    if len(ids) != len(set(ids)):
        errors.append("hay ids repetidos")
    if "4.1.1" in ids:
        errors.append("4.1.1 no debe estar: se eliminó en WCAG 2.2")
    counts = {lv: sum(1 for c in criteria if c["level"] == lv) for lv in EXPECTED}
    if counts != EXPECTED:
        errors.append(f"conteo por nivel {counts}, se esperaba {EXPECTED}")
    for c in criteria:
        cid = c["id"]
        if not ID.match(cid):
            errors.append(f"{cid}: id con formato inválido")
        if c["level"] not in EXPECTED:
            errors.append(f"{cid}: nivel {c['level']!r} fuera de alcance (solo A y AA)")
        if c["since"] not in ("2.0", "2.1", "2.2"):
            errors.append(f"{cid}: since inválido {c['since']!r}")
        if not URL.match(c["url"]):
            errors.append(f"{cid}: url inválida {c['url']!r}")
        for key in ("name_en", "label_es", "summary_es", "summary_en"):
            if not c.get(key):
                errors.append(f"{cid}: falta {key}")
        for key in ("summary_es", "summary_en"):
            if len(c.get(key, "").split()) > 25:
                errors.append(f"{cid}: {key} supera 25 palabras")
        for mode in ("code", "url", "design"):
            if c["assessable"].get(mode) not in MODES:
                errors.append(f"{cid}: assessable.{mode} inválido")
    return errors


def check_online(doc):
    expected = {(c["id"], c["name_en"], c["level"]) for c in doc["criteria"]}
    live = {(c["id"], c["name_en"], c["level"]) for c in w3c_criteria(load_w3c(W3C_URL))}
    errors = [f"solo en nuestros datos: {sorted(expected - live)}"] if expected - live else []
    if live - expected:
        errors.append(f"solo en W3C: {sorted(live - expected)}")
    return errors


def check_urls(doc):
    errors = []
    for c in doc["criteria"]:
        req = urllib.request.Request(c["url"], method="HEAD", headers={"User-Agent": "ux-skills-es/check"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                if not 200 <= r.status < 300:
                    errors.append(f"{c['id']}: {c['url']} respondió {r.status}")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{c['id']}: {c['url']} no responde ({e})")
    return errors


def main():
    doc = json.loads(DATA.read_text(encoding="utf-8"))
    errors = check_structure(doc)
    if "--online" in sys.argv:
        errors += check_online(doc)
    if "--urls" in sys.argv:
        errors += check_urls(doc)
    for e in errors:
        print("ERROR", e)
    print(f"{len(doc['criteria'])} criterios, {len(errors)} problema(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
