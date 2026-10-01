# Audit report: sample site (fictional)

<!-- section:summary -->
## Summary

- **Verdict:** one failing finding blocks a basic task; fix it before release.
- **Failing findings:** 1 (Critical 0 · Serious 1 · Moderate 0 · Minor 0)
- **Need manual check:** 0
- **Coverage:** 2 of 2 applicable criteria in this mode

<!-- section:scope -->
## Scope

- **Mode:** Code or diff
- **What was reviewed:** `index.html` of a fictional sample site
- **Detected capabilities:** browser no · Figma no · axe no · script no
- **Date:** 2026-10-01

<!-- section:findings -->
## Findings

### Serious: the banner image has no text alternative

- **Criterion:** 1.1.1 Non-text Content (level A), https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- **Where:** `index.html:14`
- **What happens:** the informative banner image has no `alt` attribute, so a screen reader user cannot tell what it conveys.
- **Confidence:** Medium, method: static_code
- **Who is affected:** blind or low-vision people using a screen reader.
- **How to fix:** add an `alt` that says what the image communicates, or an empty `alt` if it is decorative.

<!-- section:manual -->
## Manual verification

| Criterion | Why it could not be decided | How to check |
|---|---|---|
| none | | |

<!-- section:passed -->
## Passed criteria

- 3.1.1 Language of Page: `<html lang="en">` at `index.html:2`.

<!-- section:honest-gaps -->
## Honest gaps

- Static analysis: JavaScript behavior and real contrast through the cascade were not evaluated.
- This report is not a statement of conformance or legal advice. It does not replace testing with real users and assistive technology.

<!-- section:next-steps -->
## Next steps

1. Fix the banner `alt`.

---

*This report is not a statement of conformance or legal advice. It does not replace testing with real users and assistive technology.*

```json ux-skills-findings
{
  "schema_version": "1",
  "skill": "wcag22-audit",
  "language": "en",
  "mode": "code",
  "generated_on": "2026-10-01",
  "scope": {
    "summary": "index.html of a fictional sample site",
    "inputs": ["index.html"],
    "capabilities": { "browser": false, "figma": false, "axe": false, "script": false }
  },
  "findings": [
    {
      "id": "WCAG-1.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": { "system": "WCAG22", "id": "1.1.1", "name": "Non-text Content", "level": "A", "url": "https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html" },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "The banner image has no text alternative",
      "description": "The informative banner image has no alt attribute.",
      "evidence": [{ "kind": "code", "file": "index.html", "line": 14, "snippet": "<img src=\"banner.jpg\">" }],
      "affected_users": "Blind or low-vision people using a screen reader.",
      "recommendation": "Add an alt that says what the image communicates, or an empty alt if decorative.",
      "dedup_key": "1.1.1|index.html:14"
    },
    {
      "id": "WCAG-3.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": { "system": "WCAG22", "id": "3.1.1", "name": "Language of Page", "level": "A", "url": "https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html" },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "The page language is declared",
      "evidence": [{ "kind": "code", "file": "index.html", "line": 2, "snippet": "<html lang=\"en\">" }],
      "dedup_key": "3.1.1|index.html:2"
    }
  ],
  "honest_gaps": [
    "Static analysis: JavaScript behavior and real contrast through the cascade were not evaluated."
  ]
}
```
