# Severity and confidence

## Severity (by impact, not by WCAG level)

A level A failure on a rarely used page can be `moderate`; a level AA failure in the checkout flow can be `critical`.

| Severity | When |
|---|---|
| `critical` | Blocks a core task for a user group and there is no alternative |
| `serious` | Major barrier; a workaround exists but is hard to find or use |
| `moderate` | Friction or barrier with a reasonable workaround |
| `minor` | Best practice or low impact |
| `info` | Recommendation with no violation |

Severity is only assigned to `fail` findings.

## Confidence and the cap per method

Confidence describes how sure the finding is given how it was obtained. It never exceeds the method's cap:

| Method | Cap | Reason |
|---|---|---|
| `axe`, `dom_runtime`, `token_script` | high | Measured on the real page or by a deterministic calculation |
| `static_code`, `design_context` | medium | Read the code or design data, without seeing the rendered result |
| `screenshot`, `inferred` | low | Image only or deduction; ARIA, semantics and keyboard are not visible |

Rule of thumb: `high` requires direct evidence (a measurement, or unambiguous markup). When in doubt, go one level lower and say so in the description.
