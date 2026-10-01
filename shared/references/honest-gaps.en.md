# Honest gaps

The section is **mandatory and never empty**. It states plainly what could not be known. At minimum include:

- The mode used and its limits (for example, "static analysis: JavaScript behavior was not evaluated").
- Pages, states or components that were not reviewed (open menus, form errors, signed-in views).
- Tools that were not available (browser, script, axe).
- The criteria in `not_tested`, grouped.
- The footer sentence: this report is not a statement of conformance or legal advice.

## Coverage

`coverage = assessed criteria / applicable criteria`. Compute it by counting the findings in the JSON (`pass` and `fail` are assessed; `manual` and `not_tested` are not; `not_applicable` leaves the denominator). Do not estimate it or round it up.

## Tone

Direct and without apology: "I could not assess X because Y", and what would be needed to assess it.
