import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import check_wcag_data  # noqa: E402
import validate_report  # noqa: E402

SAMPLE = (ROOT / "tests/fixtures/sample-report.es.md").read_text(encoding="utf-8")
BLOCK = validate_report.BLOCK


def with_data(mutate):
    """Devuelve el informe de muestra con el JSON modificado por `mutate`."""
    data = json.loads(BLOCK.search(SAMPLE).group(1))
    mutate(data)
    return BLOCK.sub(lambda m: "```json ux-skills-findings\n" + json.dumps(data, ensure_ascii=False) + "\n```", SAMPLE)


def errors_of(text):
    return validate_report.validate_text(text)[0]


def test_sample_report_is_valid():
    errors, stats = validate_report.validate_text(SAMPLE)
    assert errors == []
    assert stats["fail"] == 2 and stats["manual"] == 1 and stats["pass"] == 1
    assert stats["coverage"] == 0.75


def test_missing_section_marker_is_reported():
    assert any("section:passed" in e for e in errors_of(SAMPLE.replace("<!-- section:passed -->", "")))


def test_missing_disclaimer_is_reported():
    text = SAMPLE.replace("Este informe no es una declaración de conformidad ni un dictamen legal.", "")
    assert any("pie legal" in e for e in errors_of(text))


def test_fail_without_evidence_is_rejected():
    def m(d):
        d["findings"][0]["evidence"] = []
    assert errors_of(with_data(m))


def test_manual_without_manual_check_is_rejected():
    def m(d):
        del d["findings"][2]["manual_check"]
    assert errors_of(with_data(m))


def test_empty_honest_gaps_is_rejected():
    def m(d):
        d["honest_gaps"] = []
    assert errors_of(with_data(m))


def test_confidence_above_method_cap_is_rejected():
    def m(d):
        d["findings"][0]["confidence"] = "high"
    assert any("techo" in e for e in errors_of(with_data(m)))


def test_severity_on_pass_is_rejected():
    def m(d):
        d["findings"][3]["severity"] = "minor"
    assert any("solo se asigna" in e for e in errors_of(with_data(m)))


def test_wrong_criterion_name_is_rejected():
    def m(d):
        d["findings"][0]["criterion"]["name"] = "Contenido no textual"
    assert any("no coincide" in e for e in errors_of(with_data(m)))


def test_unknown_or_aaa_or_removed_criterion_is_rejected():
    for bad in ("4.1.1", "1.4.6", "9.9.9"):
        def m(d, bad=bad):
            d["findings"][0]["criterion"]["id"] = bad
        assert errors_of(with_data(m)), bad


def test_duplicate_ids_are_rejected():
    def m(d):
        d["findings"][1]["id"] = d["findings"][0]["id"]
    assert any("repetido" in e for e in errors_of(with_data(m)))


def test_two_json_blocks_are_rejected():
    assert errors_of(SAMPLE + "\n```json ux-skills-findings\n{}\n```\n")


def test_wcag_data_structure_is_valid():
    doc = json.loads((ROOT / "shared/data/wcag22-criteria.json").read_text(encoding="utf-8"))
    assert check_wcag_data.check_structure(doc) == []


def test_wcag_data_rejects_removed_criterion_and_long_summary():
    doc = json.loads((ROOT / "shared/data/wcag22-criteria.json").read_text(encoding="utf-8"))
    bad = copy.deepcopy(doc)
    bad["criteria"][0]["summary_es"] = "palabra " * 26
    assert any("25 palabras" in e for e in check_wcag_data.check_structure(bad))
    bad = copy.deepcopy(doc)
    bad["criteria"][1]["id"] = "4.1.1"
    assert any("4.1.1" in e for e in check_wcag_data.check_structure(bad))


def test_every_section_marker_in_templates_matches_validator():
    for lang in ("es", "en"):
        tpl = (ROOT / f"shared/templates/report.{lang}.md").read_text(encoding="utf-8")
        found = re.findall(r"<!-- section:([a-z-]+) -->", tpl)
        assert found == validate_report.SECTIONS


def test_declared_coverage_must_match_computed():
    bad = SAMPLE.replace("3 de 4 criterios aplicables", "4 de 4 criterios aplicables")
    assert any("cobertura declarada" in e for e in errors_of(bad))


def test_english_sample_is_valid():
    text = (ROOT / "tests/fixtures/sample-report.en.md").read_text(encoding="utf-8")
    errors, stats = validate_report.validate_text(text)
    assert errors == [] and stats["coverage"] == 1.0
