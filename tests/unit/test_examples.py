"""Cada informe de muestra debe coincidir con su fixture sembrado y con los resultados esperados."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests/evals"))

import compare  # noqa: E402
import validate_report  # noqa: E402

# (skill, fixture, script generador)
CASES = [("wcag22-audit", "html-seeded", "gen_sample_reports.py"),
         ("heuristic-review-es", "flow-seeded", "gen_heuristic_samples.py")]
LANGS = ["es", "en"]
PARAMS = [(s, f, lang) for s, f, _ in CASES for lang in LANGS]


def expected(fixture):
    return yaml.safe_load((ROOT / "tests/fixtures" / fixture / "expected.yml").read_text(encoding="utf-8"))


def sample_path(skill, lang):
    return ROOT / f"src/skills/{skill}/examples/sample-report.{lang}.md"


def findings(skill, lang):
    text = sample_path(skill, lang).read_text(encoding="utf-8")
    return json.loads(validate_report.BLOCK.search(text).group(1))["findings"]


def where(f):
    return {(e["file"], e["line"]) for e in f.get("evidence", []) if "file" in e and "line" in e}


def near(f, item):
    tol = item.get("tolerance", 0)
    return any(e.get("file") == item["file"] and e.get("line") is not None
               and e["line"] - tol <= item["line"] <= (e.get("end_line") or e["line"]) + tol
               for e in f.get("evidence", []))


@pytest.mark.parametrize("skill,fixture,lang", PARAMS)
def test_sample_report_is_valid(skill, fixture, lang):
    errors, _ = validate_report.validate_text(sample_path(skill, lang).read_text(encoding="utf-8"))
    assert errors == []


@pytest.mark.parametrize("skill,fixture,lang", PARAMS)
def test_every_evidence_snippet_exists_on_its_fixture_line(skill, fixture, lang):
    for f in findings(skill, lang):
        for e in f.get("evidence", []):
            if "file" not in e:
                continue
            line = (ROOT / "tests/fixtures" / fixture / e["file"]).read_text(encoding="utf-8").splitlines()[e["line"] - 1]
            assert e["snippet"].strip() in line, f"{f['id']}: {e['file']}:{e['line']} no contiene el fragmento"


@pytest.mark.parametrize("skill,fixture,lang", PARAMS)
def test_every_seeded_item_is_found_with_the_right_status(skill, fixture, lang):
    fs = findings(skill, lang)
    for want in expected(fixture)["must_find"]:
        hit = [f for f in fs if f["criterion"]["id"] == want["criterion"] and f["status"] == want["status"]
               and near(f, want)]
        assert hit, f"falta {want}"


@pytest.mark.parametrize("skill,fixture,lang", PARAMS)
def test_decoys_are_never_flagged_as_failures(skill, fixture, lang):
    fs = findings(skill, lang)
    for decoy in expected(fixture)["must_not_flag"]:
        bad = [f for f in fs if f["status"] == "fail" and f["criterion"]["id"] == decoy["criterion"]
               and near(f, decoy)]
        assert not bad, f"señuelo marcado como fallo: {decoy}"


@pytest.mark.parametrize("skill,fixture,lang", PARAMS)
def test_manual_criteria_are_never_pass_or_fail(skill, fixture, lang):
    fs = findings(skill, lang)
    for want in expected(fixture)["must_be_manual"]:
        statuses = {f["status"] for f in fs if f["criterion"]["id"] == want["criterion"]}
        assert statuses == {"manual"}, f"{want['criterion']}: {statuses}"


@pytest.mark.parametrize("skill,fixture,lang", PARAMS)
def test_no_fail_outside_the_expected_set(skill, fixture, lang):
    exp = expected(fixture)
    allowed = [w for w in exp["must_find"] + exp.get("may_find", []) if w["status"] == "fail"]
    for f in findings(skill, lang):
        if f["status"] == "fail":
            assert any(w["criterion"] == f["criterion"]["id"] and near(f, w) for w in allowed), f["id"]


@pytest.mark.parametrize("skill,fixture,script", CASES)
def test_samples_are_reproducible_from_their_generator(skill, fixture, script):
    def digest():
        return [hashlib.sha256(sample_path(skill, lang).read_bytes()).hexdigest() for lang in LANGS]
    before = digest()
    subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True, capture_output=True)
    assert digest() == before, f"los ejemplos de {skill} se editaron a mano: regenéralos con scripts/{script}"


@pytest.mark.parametrize("skill,fixture,script", CASES)
def test_compare_tool_accepts_the_sample_and_rejects_a_broken_one(skill, fixture, script):
    text = sample_path(skill, "es").read_text(encoding="utf-8")
    ok = compare.compare(text, expected(fixture))
    assert ok["valid"] and ok["recall"] == 1.0 and not ok["missed"] and not ok["decoys_flagged"]

    data = json.loads(validate_report.BLOCK.search(text).group(1))
    victim = expected(fixture)["must_find"][0]
    for f in data["findings"]:
        if f["criterion"]["id"] == victim["criterion"]:
            f["status"] = "pass"
            f.pop("severity", None)
    broken = validate_report.BLOCK.sub(lambda m: "```json ux-skills-findings\n" + json.dumps(data) + "\n```", text)
    assert compare.compare(broken, expected(fixture))["missed"]
