# Authoring: adding or changing a skill

## Setup

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

## Workflow

1. Write the skill in `src/skills/<id>/`: `SKILL.md` (for the model), `README.md` (for people), `references/` for detail and `examples/` for a real output.
2. Add a plugin and an asset to `catalog.yml`. Shared files are declared under `vendor`; the build copies them into `references/_shared/`.
3. Generate and check:

```
.venv/bin/python scripts/build.py && .venv/bin/python scripts/gen_readme.py
.venv/bin/python scripts/lint.py && .venv/bin/python -m pytest tests/unit -q
.venv/bin/python scripts/smoke_install.py && .venv/bin/python scripts/check_wcag_data.py
claude plugin validate . --strict
```

4. Commit the source **and** the generated output; CI fails if they disagree.

Edit only `src/`, `shared/`, `catalog.yml`, `docs/`, `scripts/` and `tests/`. `plugins/` and `.claude-plugin/` are generated.

## Skill rules

- `name` in English kebab-case equal to the folder name; `description` at most 1024 characters. If the description contains `: `, quote it (the linter catches it).
- `SKILL.md` under 500 lines; detail goes in `references/`.
- **Self-contained:** no link leaves the skill folder and there are no symlinks. Shared files are copied through `vendor`.
- **Read-only** unless its job is to write.
- **Fail loudly:** if an input is missing the result is "incomplete", never "no findings".
- **Evidence over claims;** never "pass" because no problems were seen.

## Cite, do not copy

A criterion is cited by number, name, level and link, and described with your own summary of at most 25 words. No WCAG or NN/g text is pasted or translated. The linter blocks work-related or internal-workflow terms and `check_wcag_data.py` validates the data.

## How a skill is tested

1. **Seeded fixture** (`tests/fixtures/<name>/`): a fictional project with known errors, deliberately correct parts (decoys) and an `expected.yml` with `must_find`, `must_not_flag` and `must_be_manual`.
2. **Sample report generated** by a script (`scripts/gen_*_samples.py`) from the official data; tests verify that its evidence exists in the fixture and that it is not edited by hand.
3. **Real run** with `python tests/evals/run_eval.py <skill> <fixture>`: it uses your Claude Code session and compares against what is expected. If the model finds something legitimate the golden lacked, it is added to the golden; if something fails, the skill or the test tool is fixed.

## Versioning and releases

SemVer **per plugin**, in `catalog.yml`. A `<plugin>--vX.Y.Z` tag triggers the release flow: it checks that the version matches the catalog, runs the linter and tests, builds the skill zip and publishes the Release. A change in `shared/` affects every skill that copies it: bump each one's version.
