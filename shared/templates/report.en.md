# Audit report: {target}

<!-- section:summary -->
## Summary

- **Verdict:** {one line with overall state and recommended decision}
- **Failing findings:** {n} (Critical {n} · Serious {n} · Moderate {n} · Minor {n})
- **Need manual check:** {n}
- **Coverage:** {assessed} of {applicable} applicable criteria in this mode

<!-- section:scope -->
## Scope

- **Mode:** {Code or diff | URL | Design | Mixed}
- **What was reviewed:** {files, pages, states or frames}
- **Detected capabilities:** browser {yes/no} · Figma {yes/no} · axe {yes/no} · script {yes/no}
- **Date:** {YYYY-MM-DD}

<!-- section:findings -->
## Findings

### {Severity}: {title}

- **Criterion:** {id} {name} (level {A|AA}), {link}
- **Where:** {file:line or selector}
- **What happens:** {description in your own words}
- **Confidence:** {High | Medium | Low}, method: {method}
- **Who is affected:** {short sentence}
- **How to fix:** {concrete recommendation}

<!-- section:manual -->
## Manual verification

| Criterion | Why it could not be decided | How to check |
|---|---|---|
| {id} {name} | {reason} | {procedure and suggested tool} |

<!-- section:passed -->
## Passed criteria

{list of criteria verified as correct and the evidence}

<!-- section:honest-gaps -->
## Honest gaps

- {limits of the mode used}
- {pages, states or criteria not reviewed}
- {tools that were not available}

<!-- section:next-steps -->
## Next steps

1. {prioritized action, at most 5}

---

*{legal footer: see the disclaimer label in labels.yml}*

```json ux-skills-findings
{JSON block that validates against report.schema.json}
```
