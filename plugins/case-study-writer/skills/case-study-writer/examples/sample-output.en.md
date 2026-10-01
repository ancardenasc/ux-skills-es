## Gap table

| Section | Evidence | Missing |
|---|---|---|
| Context and role | `docs/brief.md`: audience, scope, constraints | Your exact role, whether anyone else worked on it, actual duration. The brief gives "6 weeks" only as time available. |
| Problem | `docs/brief.md`, `docs/research/README.md` | None |
| Process: Research | 5 interviews, 3 insights | No assistive-technology user. Research says an expert review in Phase 4 would compensate, but `docs/testing/README.md` records none. |
| Process: Design | `docs/design/README.md`, `docs/prd.md` | Figma link is pending. |
| Process: Validation | 2 rounds, findings backlog | Round 1 SUS, time on task, and whether round 2 used the same people. |
| Process: Build | Stack from `docs/brief.md`, ADR-0001 | Whether RF-03 was built. Repo and Storybook links. |
| Key decisions | ADR-0001 is complete. | Alternatives and rationale for the three design decisions. |
| Results | Task completion, SUS | Lighthouse run, RF-01's 2-second check, and a round 1 SUS ("before"). |
| Accessibility | Audit report and its JSON block | Which project version was audited. The report flags a `div` button, but ADR-0001 (2026-09-20) already replaced it with a native button. |
| Reflection | Only the limits the sources record | Your own account of what went wrong, what you'd change and what you learned. |
| Links | Audit report path | Demo, repo, Figma, Storybook. |

Left out on purpose: `docs/research/notas-crudas.md` holds a participant's name, a real employer and a phone number. I used none of it, and I didn't cite or quote it.

---

## 1. Full case

# Case study: Café Aurora

> **Sample project.** Café Aurora is a fictional project built for a portfolio, not a real client. All data in it (participants, scores, audited site) is sample data. [source: docs/brief.md, docs/research/README.md, docs/accessibility/informe-wcag22-2026-10-01.md]

## Context and role

Café Aurora is an online ordering flow for specialty coffee. It targets people aged 25 to 45 who buy single-origin coffee for home. [source: docs/brief.md] That audience is a proto-persona that was not validated with real research. [source: docs/brief.md]

Out of scope: online payments, user accounts and shipment tracking. [source: docs/brief.md] Constraints: 6 weeks available, HTML, CSS and JavaScript without a framework, and only OFL, MIT, CC0 or original content. [source: docs/brief.md]

- **Role:** [MISSING DATA: your exact role and whether anyone else worked on the project; no source says.]
- **Duration:** [MISSING DATA: actual duration; the brief only gives the 6 weeks available as a constraint.]

## Problem

People who order specialty coffee online don't know whether their order was saved, and they abandon the process. [source: docs/brief.md] In 5 interviews, 4 people abandoned or repeated the order because they saw no confirmation. [source: docs/research/README.md] An unconfirmed order is a lost sale and breeds distrust. [source: docs/brief.md]

## Process

### Research

I mean the project ran 5 moderated interviews with sample participants (P1 to P5), anonymised, with consent forms stored outside the repository. [source: docs/research/README.md] They produced three insights:

- **I-01:** people who save an order don't know if it worked. 4 of 5 abandoned or repeated the order. [source: docs/research/README.md]
- **I-02:** the month/day date format causes errors. 3 of 5 mistyped the delivery date. [source: docs/research/README.md]
- **I-03:** frequent buyers want to repeat their usual order. 2 of 5 asked for it unprompted. [source: docs/research/README.md]

No assistive-technology user was interviewed. The research notes say an expert review in Phase 4 would compensate. [source: docs/research/README.md] The testing document records no such review. [source: docs/testing/README.md]

Full detail: `docs/research/README.md`.

### Design

Three design decisions are documented: a status message next to the save button, using text and not only colour; a date selector that shows the month by name; and a single primary button per screen, labelled "Confirm order". [source: docs/design/README.md]

The PRD turned the insights into requirements:

- **RF-01:** show a save status beside the button, within 2 seconds (from I-01).
- **RF-02:** ask for the date as day/month/year with a picker (from I-02).
- **RF-03:** offer to repeat the last order (from I-03).

RF-01 and RF-02 were Must; RF-03 was Could. [source: docs/prd.md]

The high-fidelity design is in Figma: [MISSING DATA: Figma link; `docs/design/README.md` says there is no public file yet].

### Validation

There were two rounds of 5 moderated sessions each, with anonymised sample participants (P1 to P5). [source: docs/testing/README.md]

- **Round 1 (version 1):** 3 of 5 people (60%) completed the task without errors. SUS was not measured. [source: docs/testing/README.md]
- **Round 2 (version 2, with changes from the findings):** 5 of 5 (100%) completed it without errors, and SUS was 72. [source: docs/testing/README.md]
- Time on task was not measured in either round. [source: docs/testing/README.md]

Round 1 produced three findings, all marked resolved in version 2:

- **H-01 (Critical):** saving gives no response.
- **H-02 (Major):** the date asks for month/day/year.
- **H-03 (Major):** deleting the order asks for no confirmation.

[source: docs/testing/README.md]

Full detail: `docs/testing/README.md`.

### Build

The stack is HTML, CSS and JavaScript without a framework. [source: docs/brief.md] The main documented build decision is ADR-0001, accepted on 2026-09-20 (see below). [source: docs/decisions/0001-boton-nativo.md] Whether the Could-priority RF-03 was built: [MISSING DATA: not stated in docs/prd.md or docs/testing/README.md].

## Key decisions

| Decision | Alternatives considered | Why this one |
|---|---|---|
| Use a native `<button type="submit">` to confirm the order | Keep the `div` and add `role="button"` and keyboard handlers [source: docs/decisions/0001-boton-nativo.md] | The first version's `div` neither received focus nor was announced as a button. The native element improves keyboard and screen-reader operation with no extra code. The cost is reviewing the button styles. [source: docs/decisions/0001-boton-nativo.md] |
| Show a save status next to the button, in text and not only colour | [MISSING DATA: alternatives not documented] | Responds to I-01 (4 of 5 abandoned or repeated the order). [source: docs/design/README.md, docs/research/README.md] |
| Date selector that shows the month by name, in day/month/year order | [MISSING DATA: alternatives not documented] | Responds to I-02 (3 of 5 mistyped the date). [source: docs/design/README.md, docs/prd.md, docs/research/README.md] |
| One primary button per screen, labelled "Confirm order" | [MISSING DATA: alternatives not documented] | [MISSING DATA: rationale not documented in docs/design/README.md] |

## Results

| Metric (target from the brief) | Before | After | Status |
|---|---|---|---|
| Task completed without errors (80% or more) | Round 1: 3 of 5 (60%) | Round 2: 5 of 5 (100%), +40 percentage points | Not met in round 1, met in round 2 |
| SUS (68 or more) | Not measured | Round 2: 72 | Met in round 2; no "before" exists to compare |
| Lighthouse accessibility (100) | [MISSING DATA: no run in the sources] | [MISSING DATA] | Not measured |
| WCAG 2.2 AA criteria met (100% of the applicable ones) | n/a | 8 failing findings in the audit | Not met in the audited files (see Accessibility) |

[source: docs/brief.md, docs/testing/README.md, docs/accessibility/informe-wcag22-2026-10-01.md]

Limits:

- Each round had 5 people, all sample participants, in a sample project. [source: docs/testing/README.md, docs/brief.md]
- Time on task was never measured. [source: docs/testing/README.md]
- The sources don't say whether round 2 used the same people as round 1. [source: docs/testing/README.md]
- The RF-01 criterion (a message in under 2 seconds) has no recorded measurement. [source: docs/prd.md] [MISSING DATA: any measurement of the 2-second criterion.]
- H-02 is marked resolved in version 2, but the testing document gives no count of date errors in round 2. [source: docs/testing/README.md]

## Accessibility

**Level reached:** no WCAG 2.2 AA conformance can be claimed from the sources. The only audit is a static-code review dated 2026-10-01 of `index.html` and `styles.css` of a fictional site. [source: docs/accessibility/informe-wcag22-2026-10-01.md]

Figures from the report's JSON block:

- 8 failing findings: 2 critical, 3 serious, 3 moderate, 0 minor.
- 1 criterion needs a manual check (2.4.3 Focus Order).
- 1 criterion was not tested (1.4.10 Reflow).
- 3 criteria passed (2.4.1, 2.4.2, 3.1.1).
- Coverage was 11 of 13 applicable criteria in this mode.

[source: docs/accessibility/informe-wcag22-2026-10-01.md]

The report's verdict: the subscription form can't be submitted by keyboard or screen reader, and should be fixed before publishing. [source: docs/accessibility/informe-wcag22-2026-10-01.md]

- **Critical:** a `div` acting as the subscription button fails 4.1.2 and 2.1.1.
- **Serious:**
  - Note text contrast is 2.85:1 against the 4.5:1 required.
  - The email field has no label.
  - The banner image has no alternative text.
- **Moderate:**
  - Links lose the focus indicator.
  - The close button is 18 by 18 px against the 24 by 24 px minimum.
  - The email field has no `autocomplete`.

[source: docs/accessibility/informe-wcag22-2026-10-01.md]

Known gaps, as the report states them:

- It is static analysis. JavaScript behaviour and real contrast under the full cascade were not evaluated.
- Reflow at 320 px was not evaluated.
- Form error states and hover/focus content were not reviewed.
- No browser was available, so focus and computed accessible names were not measured.
- It is not a conformance statement or legal opinion, and it doesn't replace testing with people or real assistive technology.

[source: docs/accessibility/informe-wcag22-2026-10-01.md]

**Version conflict:** ADR-0001 (2026-09-20) replaced the `div` with a native button. [source: docs/decisions/0001-boton-nativo.md] The audit of 2026-10-01 still flags a `div` button at `index.html:25`. [source: docs/accessibility/informe-wcag22-2026-10-01.md] [MISSING DATA: which version of the project the audited files belong to; the report doesn't say.]

## Reflection

The sources record these limits:

- SUS was not measured in round 1, so there's no before/after for it. [source: docs/testing/README.md]
- Time on task was never measured. [source: docs/testing/README.md]
- No assistive-technology user took part in the research. [source: docs/research/README.md]
- The Figma file isn't public. [source: docs/design/README.md]

[MISSING DATA: what went wrong, what you would change and what you learned, in your own words. No retrospective notes exist in the sources.]

## Links

- Demo: [MISSING DATA: no link in the sources]
- Repository: [MISSING DATA: no link in the sources]
- Figma: [MISSING DATA: pending per docs/design/README.md]
- Storybook: [MISSING DATA: no link in the sources]
- Accessibility report: `docs/accessibility/informe-wcag22-2026-10-01.md`

---

## 2. 60-second summary

**Sample project:** Café Aurora is fictional, built for a portfolio. All data is sample data.

**Problem.** People ordering specialty coffee online don't know whether their order was saved, and they abandon. In five interviews, four people abandoned or repeated the order because they saw no confirmation.

**Process.** The interviews produced three insights: no save confirmation, a month/day date format that caused mistakes, and a wish to repeat the usual order. The first two became must-have requirements; repeating the order was a could-have. One key decision replaced a clickable div with a native button, so keyboards and screen readers work without extra code.

**Validation.** Two usability rounds with five people each. Round 1 found three issues, one critical: saving gave no response. All three were marked resolved in version 2.

**Results.** Task completion without errors rose from 3 of 5 (60%) to 5 of 5 (100%), against an 80% target. SUS in round 2 was 72, against a target of 68. Round 1 SUS was not measured, so there is no before and after. Lighthouse was not measured.

**Accessibility.** A static code audit on 2026-10-01 found 8 failing findings (2 critical, 3 serious, 3 moderate). The 100% WCAG 2.2 AA target was not met in the audited files. The sources don't say which project version was audited.

**Limits.** Five sample participants per round, no assistive-technology user in the research, time on task not measured, and no demo, repository or Figma links yet.

---

## 3. Portfolio blurb

**Café Aurora: showing coffee shoppers that their order was saved**

Sample portfolio project. Online coffee orders gave no sign they were saved, and 4 of 5 interviewees abandoned or repeated them. Two usability rounds raised error-free task completion from 60% to 100% (5 people per round). A static accessibility audit found 8 failing issues, so the AA target was not met.

---

## What you need to supply

1. Your exact role and the real duration.
2. A decision on the version conflict: which version the audit covers, or re-run it on the version with the native button.
3. Reflection in your own words.
4. Links (demo, repo, Figma, Storybook) and a Lighthouse run, if they exist.

I saved nothing, as you asked. One mistake in the draft: the first sentence under "Research" reads "I mean the project ran…". Change it to "The project ran…" before you publish. The sources don't say how many people worked on the project, so I wrote the process in neutral voice instead of first person.
