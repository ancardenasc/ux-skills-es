# Case study structure

Follow the `case-kit` template (`docs/case-study.md`). Exact headings, in this order. It must read in 60 s (skim) and in 10 min (full read).

| Heading | What goes in | Usual sources |
|---|---|---|
| `# Case study: <name>` | Title; sample-project notice if it applies | `docs/brief.md` |
| `## Context and role` | What the project is, your exact role, who you worked with, duration | `docs/brief.md`; the role and duration come from the person |
| `## Problem` | The real problem in 2 or 3 sentences, backed by the insight | `docs/brief.md`, `docs/research/` |
| `## Process` with `### Research`, `### Design`, `### Validation`, `### Build` | What was done at each stage, with a link to the document | `docs/research/`, `docs/design/`, `docs/testing/`, `docs/prd.md` |
| `## Key decisions` | Table: decision, alternatives considered, why this one | `docs/decisions/` |
| `## Results` | Brief metrics, before versus after, with their limits | `docs/brief.md` (targets), `docs/testing/` |
| `## Accessibility` | Level reached, report figures and known gaps | `docs/accessibility/` |
| `## Reflection` | What went wrong, what you would change, what you learned | the person; retrospective notes |
| `## Links` | Demo, repository, Figma, accessibility report | the sources; if none, `MISSING DATA` |

## Notes per section
- **Results:** compare with the brief's targets (met, not met, not measured). Anything not measured goes as `MISSING DATA`.
- **Accessibility:** use the counts in the report's JSON block (failures by severity, coverage) and reproduce its honest gaps; do not soften them. State which version of the project the report belongs to.
- **Links:** only those in the sources. A "pending" link is missing data.
