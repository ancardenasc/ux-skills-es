import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import lint  # noqa: E402


def run(script):
    return subprocess.run([sys.executable, str(ROOT / "scripts" / script)], capture_output=True, text=True)


def tree_hash(path):
    h = hashlib.sha256()
    for f in sorted(p for p in path.rglob("*") if p.is_file()):
        h.update(f.relative_to(path).as_posix().encode())
        h.update(f.read_bytes())
    return h.hexdigest()


def test_build_is_idempotent():
    assert run("build.py").returncode == 0
    first = (tree_hash(ROOT / "skills"), tree_hash(ROOT / "plugins"))
    assert run("build.py").returncode == 0
    assert first == (tree_hash(ROOT / "skills"), tree_hash(ROOT / "plugins"))


def test_vendored_markdown_matches_shared_plus_header():
    run("build.py")
    vendored = (ROOT / "skills/wcag22-audit/references/_shared/report.es.md").read_text()
    original = (ROOT / "shared/templates/report.es.md").read_text()
    assert vendored.startswith("<!-- GENERADO") and vendored.endswith(original)


def test_vendored_json_is_a_byte_copy():
    run("build.py")
    vendored = ROOT / "skills/wcag22-audit/references/_shared/wcag22-criteria.json"
    assert vendored.read_bytes() == (ROOT / "shared/data/wcag22-criteria.json").read_bytes()


def test_plugin_copy_is_identical_to_flat_skill():
    run("build.py")
    assert tree_hash(ROOT / "skills/wcag22-audit") == tree_hash(ROOT / "plugins/wcag22-audit/skills/wcag22-audit")


def test_readme_not_shipped_with_skill():
    run("build.py")
    assert not (ROOT / "skills/wcag22-audit/README.md").exists()
    assert (ROOT / "skills/wcag22-audit/examples/sample-report.es.md").exists()


def test_forbidden_terms_regex():
    for bad in ("Jira", "GitLab", "BDD-123", "customfield_10543", "/Users/x", "devflow", "start-task"):
        assert lint.FORBIDDEN.search(bad), bad
    for ok in ("ancardenasc", "accesibilidad", "heurística"):
        assert not lint.FORBIDDEN.search(ok), ok


def test_lint_passes_on_clean_repo():
    run("build.py")
    assert run("lint.py").returncode == 0


def test_only_the_skill_root_readme_is_omitted():
    run("build.py")
    assert not (ROOT / "skills/heuristic-review-es/README.md").exists()
    nested = ROOT / "src/skills/heuristic-review-es/references/_probe/README.md"
    nested.parent.mkdir(exist_ok=True)
    nested.write_text("# probe\n")
    try:
        run("build.py")
        assert (ROOT / "skills/heuristic-review-es/references/_probe/README.md").exists()
    finally:
        nested.unlink()
        nested.parent.rmdir()
        run("build.py")


def test_case_kit_license_templates_carry_the_full_mit_text():
    for lang, placeholder in (("es", "[Año] [Tu nombre]"), ("en", "[Year] [Your Name]")):
        text = (ROOT / f"src/skills/case-kit/template/{lang}/LICENSE").read_text(encoding="utf-8")
        assert placeholder in text
        for clause in ("Permission is hereby granted, free of charge", "THE SOFTWARE IS PROVIDED \"AS IS\"",
                       "LIABILITY, WHETHER IN AN ACTION OF CONTRACT"):
            assert clause in text, f"{lang}: falta la cláusula {clause!r}"
        assert len(text) > 1000


def test_npx_listing_count_ignores_mentions_in_descriptions():
    import re
    output = "│    case-study-writer\n│\n│      Usa la estructura de case-kit para redactar.\n│\n│    case-kit\n│\n│      Crea carpetas.\n"
    assert len(re.findall(r"(?m)^[│\s]+case-kit\s*$", output)) == 1
