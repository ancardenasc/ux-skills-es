"""Compara un informe contra los resultados esperados de un fixture.

Uso: python tests/evals/compare.py informe.md tests/fixtures/html-seeded
Sale con 1 si el informe no valida, si falla algún must_find, si marca un señuelo o si un criterio manual no es manual.
Los fallos extra (fuera de must_find y may_find) se listan para revisión humana: pueden ser legítimos (así se completó el golden la primera vez).
"""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_report  # noqa: E402


def where(f):
    return {(e.get("file"), e.get("line")) for e in f.get("evidence", [])}


def near(f, item):
    """¿Alguna evidencia del hallazgo (línea o rango line..end_line) cubre la línea esperada, con su tolerancia?"""
    tol = item.get("tolerance", 0)
    for e in f.get("evidence", []):
        start = e.get("line")
        if e.get("file") == item["file"] and start is not None:
            end = e.get("end_line") or start
            if start - tol <= item["line"] <= end + tol:
                return True
    return False


def compare(text, expected):
    errors, stats = validate_report.validate_text(text)
    result = {"valid": not errors, "validation_errors": errors, "stats": stats,
              "missed": [], "decoys_flagged": [], "manual_wrong": [], "extra_fails": []}
    if errors and "bloque" in errors[0]:
        return result
    findings = json.loads(validate_report.BLOCK.search(text).group(1))["findings"]
    for w in expected["must_find"]:
        if not [f for f in findings if f["criterion"]["id"] == w["criterion"] and f["status"] == w["status"]
                and near(f, w)]:
            result["missed"].append(w)
    for d in expected["must_not_flag"]:
        if [f for f in findings if f["status"] == "fail" and f["criterion"]["id"] == d["criterion"] and near(f, d)]:
            result["decoys_flagged"].append(d)
    for m in expected["must_be_manual"]:
        statuses = {f["status"] for f in findings if f["criterion"]["id"] == m["criterion"]}
        if statuses != {"manual"}:
            result["manual_wrong"].append({"criterion": m["criterion"], "statuses": sorted(statuses)})
    allowed = [w for w in expected["must_find"] + expected.get("may_find", []) if w["status"] == "fail"]
    for f in findings:
        if f["status"] == "fail":
            e = f["evidence"][0]
            if not any(w["criterion"] == f["criterion"]["id"] and near(f, w) for w in allowed):
                result["extra_fails"].append(f"{f['id']} {f['criterion']['name']} {e.get('file')}:{e.get('line')}")
    total = len(expected["must_find"])
    result["recall"] = round((total - len(result["missed"])) / total, 2)
    return result


def main():
    report, fixture = Path(sys.argv[1]), Path(sys.argv[2])
    expected = yaml.safe_load((fixture / "expected.yml").read_text(encoding="utf-8"))
    r = compare(report.read_text(encoding="utf-8"), expected)
    print(json.dumps(r, indent=2, ensure_ascii=False))
    ok = r["valid"] and not (r["missed"] or r["decoys_flagged"] or r["manual_wrong"])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
