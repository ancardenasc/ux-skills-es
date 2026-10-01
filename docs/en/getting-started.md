# Getting started

Each skill installs on its own. Pick the route your tool uses.

## 1. Install

| Route | One skill | All |
|---|---|---|
| **Claude Code (plugin)** | `/plugin install wcag22-audit@ux-skills-es` | add the marketplace once: `/plugin marketplace add ancardenasc/ux-skills-es`, then install each plugin |
| **`npx skills`** | `npx skills add ancardenasc/ux-skills-es --skill wcag22-audit` | `npx skills add ancardenasc/ux-skills-es --all` |
| **GitHub CLI** | `gh skill install ancardenasc/ux-skills-es wcag22-audit` | `gh skill install ancardenasc/ux-skills-es --all` |
| **GitHub Copilot** | copy `plugins/<id>/skills/<id>` to `.github/skills/` | `scripts/install.sh copilot /path/to/your/project` |
| **claude.ai** | upload the `<id>.zip` from the Releases page | |
| **Claude Code without plugins** | copy the folder to `.claude/skills/` | `scripts/install.sh claude /path/to/your/project` |

Claude Code plugins are invoked with their namespace: `/wcag22-audit:wcag22-audit`. If you copy the files into `.claude/skills/`, the name is short: `/wcag22-audit`.

## 2. Your first audit

```
/wcag22-audit:wcag22-audit ./src --idioma en
```

The skill detects what you have (code, URL, design) and which tools exist (browser, Figma), states the mode in the scope and returns a report with findings, manual verification and honest gaps. See the [report schema](report-schema.md).

More examples:

```
/heuristic-review-es:heuristic-review-es ./order-flow --tarea "place an order"
/case-kit:case-kit ./my-project "Project name" --idioma en
/case-study-writer:case-study-writer ./my-project --idioma en
```

## 3. Optional configuration

A `.ux-skills.yml` file at the root of your project:

```yaml
output_language: en      # es | en; by default, the language of your request
default_branch: main     # base branch for diffs
frontend_globs: ["**/*.{vue,jsx,tsx,html,css,scss}"]
```

Everything is optional. Without a file, the skills infer what they need and ask when unsure.

## 4. What to expect

- Reports **cite evidence** (`file:line`, selector, measurement) and say what they could **not** review.
- Whatever no tool can decide (screen readers, focus order without running the page) stays as **manual verification**, never as "pass".
- The audit skills are **read-only**: they do not edit files or submit forms.

Next: [products](products.md).
