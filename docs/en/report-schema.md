# Report schema

`wcag22-audit` and `heuristic-review-es` return the same format: a Markdown report with seven fixed sections and **one final JSON block** labelled `ux-skills-findings`. The Markdown is for people; the JSON is for other tools. They say the same thing and are checked with `scripts/validate_report.py`.

## The seven sections

| Marker | Content |
|---|---|
| `summary` | Verdict, count by severity and computed coverage |
| `scope` | Mode used, what was reviewed, detected capabilities, date |
| `findings` | One block per failure, highest severity first |
| `manual` | What could not be decided and how to check it |
| `passed` | Criteria verified as correct, with evidence |
| `honest-gaps` | What was not reviewed and why; never empty |
| `next-steps` | At most 5 prioritized actions |

## Status of each criterion

| Status | Meaning |
|---|---|
| `fail` | There is direct evidence of a violation |
| `pass` | Verified with evidence that it is met |
| `manual` | No tool can decide it in this mode (with `manual_check`) |
| `not_applicable` | The criterion cannot apply (for example, there is no video) |
| `not_tested` | Not looked at because the mode lacks the data |

## Severity and confidence

**Severity** is by impact, not by WCAG level: `critical`, `serious`, `moderate`, `minor`, `info`; it is only assigned to `fail`.

**Confidence** (`high`, `medium`, `low`) never exceeds the method's cap:

| Method | Cap |
|---|---|
| `axe`, `dom_runtime`, `token_script` | high |
| `static_code`, `design_context` | medium |
| `screenshot`, `inferred` | low |

## Coverage

`coverage = assessed criteria / applicable criteria`, counting **each criterion once** even if it has several findings. A criterion is assessed if it has at least one `pass` or `fail`. It is computed from the JSON; the validator rejects a coverage that does not match.

## The JSON block

```json
{
  "schema_version": "1",
  "skill": "wcag22-audit",
  "language": "en",
  "mode": "code",
  "scope": { "summary": "...", "inputs": ["index.html"], "capabilities": { "browser": false, "figma": false, "axe": false, "script": false } },
  "findings": [{
    "id": "WCAG-1.1.1-001",
    "criterion": { "system": "WCAG22", "id": "1.1.1", "name": "Non-text Content", "level": "A", "url": "https://..." },
    "status": "fail", "severity": "serious", "confidence": "medium", "method": "static_code",
    "evidence": [{ "kind": "code", "file": "index.html", "line": 18, "snippet": "<img ...>" }],
    "recommendation": "..."
  }],
  "honest_gaps": ["..."]
}
```

JSON rules: keys and values are **always English**, and `criterion.name` is the exact `name_en` from the data (for example `Keyboard`), never a translation. The full schema is in `shared/schema/report.schema.json`.

## What the validator checks

A single JSON block valid against the schema, the seven sections, the legal footer, that each criterion exists with its exact name, level and link, the confidence caps, that severity is only on `fail`, that there are no repeated ids and that the declared coverage matches the computed one.
