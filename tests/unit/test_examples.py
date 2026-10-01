"""El informe de muestra debe coincidir con el fixture sembrado y con los resultados esperados."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_report  # noqa: E402

FIXTURE = ROOT / "tests/fixtures/html-seeded"
EXPECTED = yaml.safe_load((FIXTURE / "expected.yml").read_text(encoding="utf-8"))
EX = ROOT / "src/skills/wcag22-audit/examples"


def findings(lang):
    text = (EX / f"sample-report.{lang}.md").read_text(encoding="utf-8")
    return json.loads(validate_report.BLOCK.search(text).group(1))["findings"]


def where(f):
    return {(e["file"], e["line"]) for e in f.get("evidence", []) if "file" in e and "line" in e}


@pytest.mark.parametrize("lang", ["es", "en"])
def test_every_evidence_snippet_exists_on_its_fixture_line(lang):
    for f in findings(lang):
        for e in f.get("evidence", []):
            if "file" not in e:
                continue
            line = (FIXTURE / e["file"]).read_text(encoding="utf-8").splitlines()[e["line"] - 1]
            assert e["snippet"].strip() in line, f"{f['id']}: {e['file']}:{e['line']} no contiene el fragmento"


@pytest.mark.parametrize("lang", ["es", "en"])
def test_every_seeded_violation_is_found_with_the_right_status(lang):
    fs = findings(lang)
    for want in EXPECTED["must_find"]:
        hit = [f for f in fs if f["criterion"]["id"] == want["criterion"] and f["status"] == want["status"]
               and (want["file"], want["line"]) in where(f)]
        assert hit, f"falta {want}"


@pytest.mark.parametrize("lang", ["es", "en"])
def test_decoys_are_never_flagged_as_failures(lang):
    fs = findings(lang)
    for decoy in EXPECTED["must_not_flag"]:
        bad = [f for f in fs if f["status"] == "fail" and f["criterion"]["id"] == decoy["criterion"]
               and (decoy["file"], decoy["line"]) in where(f)]
        assert not bad, f"señuelo marcado como fallo: {decoy}"


@pytest.mark.parametrize("lang", ["es", "en"])
def test_manual_criteria_are_never_pass_or_fail(lang):
    fs = findings(lang)
    for want in EXPECTED["must_be_manual"]:
        statuses = {f["status"] for f in fs if f["criterion"]["id"] == want["criterion"]}
        assert statuses == {"manual"}, f"{want['criterion']}: {statuses}"


@pytest.mark.parametrize("lang", ["es", "en"])
def test_no_finding_outside_the_seeded_set_has_unexpected_fail(lang):
    seeded = {(w["criterion"], w["file"], w["line"]) for w in EXPECTED["must_find"] if w["status"] == "fail"}
    for f in findings(lang):
        if f["status"] == "fail":
            first = f["evidence"][0]
            assert (f["criterion"]["id"], first["file"], first["line"]) in seeded, f["id"]


def test_samples_are_reproducible_from_the_generator():
    def digest():
        return [hashlib.sha256((EX / f"sample-report.{l}.md").read_bytes()).hexdigest() for l in ("es", "en")]
    before = digest()
    subprocess.run([sys.executable, str(ROOT / "scripts/gen_sample_reports.py")], check=True, capture_output=True)
    assert digest() == before, "los ejemplos se editaron a mano: regenéralos con scripts/gen_sample_reports.py"


def test_compare_tool_accepts_the_sample_and_rejects_a_broken_one():
    sys.path.insert(0, str(ROOT / "tests/evals"))
    import compare
    text = (EX / "sample-report.es.md").read_text(encoding="utf-8")
    ok = compare.compare(text, EXPECTED)
    assert ok["valid"] and ok["recall"] == 1.0 and not ok["missed"] and not ok["decoys_flagged"]

    data = json.loads(validate_report.BLOCK.search(text).group(1))
    next(f for f in data["findings"] if f["criterion"]["id"] == "2.4.7")["criterion"]["id"] = "2.4.3"
    broken = validate_report.BLOCK.sub(lambda m: "```json ux-skills-findings\n" + json.dumps(data) + "\n```", text)
    result = compare.compare(broken, EXPECTED)
    assert result["missed"] and not result["valid"]
