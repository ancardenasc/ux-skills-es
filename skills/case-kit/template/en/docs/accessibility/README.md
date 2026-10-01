# Phase 6: Accessibility QA and conformance

## Audit reports
Keep the reports here (with their date) so the case study can cite them:
- WCAG 2.2 A and AA audit: skill `wcag22-audit`, saved as `wcag22-report-YYYY-MM-DD.md`.
- Usability heuristic review: skill `heuristic-review-es`, saved as `heuristics-report-YYYY-MM-DD.md`.

## Manual tests
- [ ] Full keyboard navigation (tab, shift+tab, esc, arrows where applicable)
- [ ] Screen reader: VoiceOver (macOS/iOS), and NVDA if Windows is available
- [ ] 200% and 400% zoom without loss of content/function
- [ ] Reflow (no horizontal scroll at 320px width)
- [ ] `prefers-reduced-motion` respected
- [ ] High contrast / dark mode
- [ ] Color contrast measured (not just estimated)

## WCAG 2.2 A/AA criteria matrix
| WCAG criterion | Level | Status | Evidence | Local standard equivalent (optional) |
|---|---|---|---|---|
| 1.1.1 Non-text content | A | | | |
| 1.4.3 Contrast (minimum) | AA | | | |
| 2.1.1 Keyboard | A | | | |
| 2.4.7 Focus visible | AA | | | |
| 2.5.8 Target size (minimum) | AA | | | |
| 3.3.1 Error identification | A | | | |
| 4.1.2 Name, role, value | A | | | |

(Complete with the criteria that apply to the project; not every criterion applies to every project.)

## Conformance report (simplified ACR/VPAT style)
- Declared conformance level:
- Evaluation date:
- Method: automated (axe, Lighthouse) + manual

## Known gaps (honest, do not hide)
| Gap | Impact | Plan |
|---|---|---|
| | | |

## Accessibility statement (public)
<!-- Short text to publish on the site: what was tested, level reached, how to report a problem. -->
