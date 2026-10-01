# Products

Four independent skills. Each one works alone; the audit skills share the report format.

| Product | What it does | What you give it | What you get |
|---|---|---|---|
| **`wcag22-audit`** | Audits web accessibility against WCAG 2.2 A and AA (55 criteria) | Code or a diff, a URL, a Figma design or screenshots | A report with findings by severity, manual verification, passed criteria, honest gaps and a JSON block |
| **`heuristic-review-es`** | Usability heuristic review with Nielsen's 10 heuristics | Code, a URL or a design, and the task the person performs | The same report format, with a table of the 10 heuristics |
| **`case-kit`** | Scaffolds a 10-phase case-study structure | A target folder and the project name | A folder with brief, research, PRD, design, testing, accessibility and the case template (es or en) |
| **`case-study-writer`** | Drafts the case study from your documents | The `case-kit` folder, free notes and audit reports | Full case, 60-second summary and blurb, with citations and missing data marked |

## How they combine

1. `case-kit` creates the project structure.
2. You build the project and save the audits (`wcag22-audit`, `heuristic-review-es`) in `docs/accessibility/` and `docs/testing/`.
3. `case-study-writer` drafts the case from what you filled in.

You do not have to use all four: the audits are useful on any project, not only portfolio ones.

## When to use which

- **"Does my interface meet WCAG?"** → `wcag22-audit`.
- **"Is my flow understandable and usable?"** → `heuristic-review-es` (and `wcag22-audit` for the technical side: they complement each other).
- **"I am documenting a portfolio project."** → `case-kit`, then `case-study-writer`.

## Real examples

Each skill ships an example of its output, produced on fictional projects and verified by the repository tests:

- [`wcag22-audit`](../../src/skills/wcag22-audit/examples/sample-report.en.md)
- [`heuristic-review-es`](../../src/skills/heuristic-review-es/examples/sample-report.en.md)
- [`case-study-writer`](../../src/skills/case-study-writer/examples/sample-output.en.md)
