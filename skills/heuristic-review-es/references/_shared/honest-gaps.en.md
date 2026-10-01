<!-- GENERADO desde shared/references/honest-gaps.en.md por scripts/build.py. No editar a mano. -->
# Honest gaps

The section is **mandatory and never empty**. It states plainly what could not be known. At minimum include:

- The mode used and its limits (for example, "static analysis: JavaScript behavior was not evaluated").
- Pages, states or components that were not reviewed (open menus, form errors, signed-in views).
- Tools that were not available (browser, script, axe).
- The criteria in `not_tested`, grouped.
- The footer sentence: this report is not a statement of conformance or legal advice.

## Coverage

`coverage = assessed criteria / applicable criteria`, counting **each criterion once** even if it has several findings. A criterion is assessed if it has at least one `pass` or `fail`; `manual` and `not_tested` do not count as assessed; a criterion with only `not_applicable` leaves the denominator. Compute it from the JSON; do not estimate it or round it up.

## Tone

Direct and without apology: "I could not assess X because Y", and what would be needed to assess it.
