<!-- GENERADO desde shared/references/report-format.en.md por scripts/build.py. No editar a mano. -->
# Report format

Every audit produces **one Markdown report** with the template sections (`report.en.md`, same `<!-- section:id -->` markers) and **one final JSON block** labelled `ux-skills-findings` that validates against `report.schema.json`. The Markdown is for people; the JSON is for other tools. They must say the same thing.

## Rules

1. **Evidence or nothing.** A `fail` finding carries at least one real piece of evidence: `file:line`, selector, measurement or screenshot. Never invent lines, selectors or values.
2. **Own words.** Describe each criterion in your own words. Do not copy or translate WCAG or Nielsen text; cite number, name, level and link (see `legal-copyright-rules.md`).
3. **Never declare "pass" what you cannot decide.** Anything that needs a screen reader, judging focus order without a runtime, or the quality of text alternatives goes to `manual`, with `manual_check`.
4. **Statuses:** `fail`, `pass`, `manual`, `not_applicable` (the criterion cannot apply, e.g. there is no video) and `not_tested` (not looked at because the mode lacks the data; goes into the gaps).
5. **Ids:** `WCAG-<criterion>-<NNN>` or `NIELSEN-<Hn>-<NNN>`, NNN consecutive. `dedup_key`: `<criterion>|<file:line or selector>`.
6. **Labels per language** come from `labels.yml`. Machine keys and values in the JSON are always English.
7. **Fixed footer:** include the language's `disclaimer` label before the JSON block.
8. **Honest gaps** is never empty (see `honest-gaps.en.md`). Coverage (assessed / applicable) is computed from the findings, not asserted.

## Section order

summary, scope, findings (highest severity first), manual verification, passed criteria, honest gaps, next steps (at most 5).
