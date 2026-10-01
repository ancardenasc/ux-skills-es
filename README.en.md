# ux-skills-es

[![validate](https://github.com/ancardenasc/ux-skills-es/actions/workflows/validate.yml/badge.svg)](https://github.com/ancardenasc/ux-skills-es/actions/workflows/validate.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![skills](https://img.shields.io/badge/skills-4-blue)
![tools](https://img.shields.io/badge/Claude%20Code%20%2B%20Copilot-compatible-8A63D2)
![docs](https://img.shields.io/badge/docs-ES%20%7C%20EN-lightgrey)

**Spanish-first UX and accessibility skills for Claude Code and GitHub Copilot.** They audit accessibility against WCAG 2.2, review usability with Nielsen's heuristics and help document a case study, **with evidence, without inventing anything and saying what they could not review**. Each one installs on its own.

[Leer en español](README.md)

## Why it exists

Most AI audit tools are English-only and return lists of problems without saying how sure they are or what was left unexamined. These:

- **Give evidence:** every failure carries `file:line`, a selector or a measurement, and a concrete recommendation.
- **Say what they do not know:** whatever no tool can decide (screen readers, focus order) stays as manual verification, never as "pass", and every report ends with its honest gaps.
- **Do not invent:** `case-study-writer` marks what is missing as missing data and cites the document behind every claim.
- **Are Spanish-first**, with output configurable to English.
- **Are tested:** they run on fictional projects seeded with errors and deliberately correct parts, and CI checks that they find what is expected without flagging what is correct.

## Skills

<!-- catalog:start -->
| Skill | What it does | Install |
|---|---|---|
| [`wcag22-audit`](src/skills/wcag22-audit/README.md) | Audits web accessibility against WCAG 2.2 A and AA from code, a URL or a design; Spanish-first report with evidence, manual checks and honest gaps. | `/plugin install wcag22-audit@ux-skills-es` |
| [`heuristic-review-es`](src/skills/heuristic-review-es/README.md) | Usability heuristic review with Nielsen's 10 heuristics from code, a URL or a design; Spanish-first report with evidence and honest gaps. | `/plugin install heuristic-review-es@ux-skills-es` |
| [`case-kit`](src/skills/case-kit/README.md) | Scaffolds a 10-phase portfolio case-study structure (brief, research, PRD, design, testing, accessibility, case study), in Spanish or English. | `/plugin install case-kit@ux-skills-es` |
| [`case-study-writer`](src/skills/case-study-writer/README.md) | Drafts a project case study (full, 60-second and blurb) from its documents and audits, without inventing metrics, with citations and missing data marked. | `/plugin install case-study-writer@ux-skills-es` |
<!-- catalog:end -->

Each skill has its own README with examples and a sample report. Other ways to install (`npx skills`, `gh skill`, GitHub Copilot, claude.ai) are in [getting started](docs/en/getting-started.md).

## A real report

Excerpt of the `wcag22-audit` sample report on a fictional site (source in `tests/fixtures/html-seeded`):

> ### Critical: The subscribe button is a div with no role or keyboard support
>
> - **Criterion:** 4.1.2 Name, Role, Value, level A, https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html
> - **Where:** `index.html:25`
> - **Confidence:** Medium, method: static_code
> - **How to fix:** Use a <button type="submit"> with the same visible text.

Full report: [Spanish](src/skills/wcag22-audit/examples/sample-report.es.md) · [English](src/skills/wcag22-audit/examples/sample-report.en.md).

## How they fit together

```
case-kit  →  (you build the project)  →  wcag22-audit + heuristic-review-es  →  case-study-writer
 structure                                 audits with evidence                     case, 60 s and blurb
```

You do not have to use all four: the audits are useful on any project. See [products](docs/en/products.md).

## Configuration

Optional: a `.ux-skills.yml` at the root of your project.

```yaml
output_language: en      # es | en
default_branch: main
frontend_globs: ["**/*.{vue,jsx,tsx,html,css,scss}"]
```

## What they do not do

They do not certify conformance or give legal advice, do not replace testing with real people and real screen readers, do not fix code and do not evaluate level AAA. What is verified and what is not, plainly: [limits and honesty](docs/en/limits-and-honesty.md).

## Documentation

[Getting started](docs/en/getting-started.md) · [Products](docs/en/products.md) · [Report schema](docs/en/report-schema.md) · [Authoring](docs/en/authoring.md) · [Limits and honesty](docs/en/limits-and-honesty.md)

## Copyright

WCAG belongs to the W3C and the heuristics to Jakob Nielsen (Nielsen Norman Group). This repository cites number, name, level and link with own summaries, and does not copy or translate their text. See [NOTICE](NOTICE.md).

## Security

The skills can use tools (shell, git, browser). Read them before installing and keep your tokens in your own configuration, never here. See [SECURITY.md](SECURITY.md).

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). MIT, (c) 2026 Nicolas Cardenas.
