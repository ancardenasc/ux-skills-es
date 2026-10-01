# Audit report: Café Aurora (fictional sample site)

<!-- section:summary -->
## Summary

- **Verdict:** the subscribe form cannot be submitted with a keyboard or a screen reader; fix it before release.
- **Failing findings:** 8 (Critical 2 · Serious 3 · Moderate 3 · Minor 0)
- **Need manual check:** 1
- **Coverage:** 11 of 13 applicable criteria in this mode

<!-- section:scope -->
## Scope

- **Mode:** Code or diff
- **What was reviewed:** `index.html` and `styles.css` of a fictional site
- **Detected capabilities:** browser no · Figma no · axe no · script no
- **Date:** 2026-10-01

<!-- section:findings -->
## Findings

### Critical: The subscribe button is a div with no role or keyboard support

- **Criterion:** 4.1.2 Name, Role, Value, level A, https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html
- **Where:** `index.html:25`
- **What happens:** A div with onclick is not announced as a button and cannot receive keyboard focus, so the form cannot be submitted without a mouse.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People using a keyboard or a screen reader.
- **How to fix:** Use a <button type="submit"> with the same visible text.

### Critical: The subscribe button cannot be activated with a keyboard

- **Criterion:** 2.1.1 Keyboard, level A, https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html
- **Where:** `index.html:25`
- **What happens:** The div with onclick has no tabindex or keyboard handler, so it cannot receive focus or respond to Enter or Space.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People using a keyboard, switch devices or voice control.
- **How to fix:** Use a <button type="submit">, which is already keyboard operable.

### Serious: The note text has insufficient contrast

- **Criterion:** 1.4.3 Contrast (Minimum), level AA, https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- **Where:** `styles.css:8`
- **What happens:** Gray #999999 on the white background gives 2.85:1; normal text needs at least 4.5:1.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People with low vision or reading in bright light.
- **How to fix:** Darken the text color, for example to #595959 (7:1 on white).

### Serious: The email field has no label

- **Criterion:** 3.3.2 Labels or Instructions, level A, https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html
- **Where:** `index.html:22`
- **What happens:** The placeholder disappears while typing and does not count as a label; the field has no label or aria-label.
- **Confidence:** Medium, method: static_code
- **Who is affected:** Screen reader users and people with memory difficulties.
- **How to fix:** Associate a visible <label for> with the field, as is already done for the name field.

### Serious: The banner image has no text alternative

- **Criterion:** 1.1.1 Non-text Content, level A, https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- **Where:** `index.html:18`
- **What happens:** The banner image has no alt attribute, so a screen reader user cannot tell what it conveys.
- **Confidence:** Medium, method: static_code
- **Who is affected:** Blind or low-vision people using a screen reader.
- **How to fix:** Add an alt that says what the image communicates, or an empty alt if it is decorative.

### Moderate: Links lose the focus indicator

- **Criterion:** 2.4.7 Focus Visible, level AA, https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html
- **Where:** `styles.css:9`
- **What happens:** The a:focus rule removes the outline and there is no replacement style.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People who navigate with a keyboard.
- **How to fix:** Remove the rule or define a :focus-visible with a high-contrast border.

### Moderate: The close button is 18 by 18 pixels

- **Criterion:** 2.5.8 Target Size (Minimum), level AA, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- **Where:** `styles.css:11`
- **What happens:** The target is smaller than 24 by 24 CSS pixels and has no compensating space around it.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People with tremor or using a touch screen.
- **How to fix:** Enlarge the active area to at least 24 by 24 px, for example with padding.

### Moderate: The email field does not declare its purpose

- **Criterion:** 1.3.5 Identify Input Purpose, level AA, https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html
- **Where:** `index.html:22`
- **What happens:** The field has no autocomplete, so the browser cannot fill in the person's email.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People with motor or memory difficulties, and those who rely on data managers.
- **How to fix:** Add autocomplete="email" to the field.

<!-- section:manual -->
## Manual verification

| Criterion | Why it could not be decided | How to check |
|---|---|---|
| 2.4.3 Focus Order | Focus order depends on how the page renders and is traversed; code mode cannot decide it. | Walk the page with Tab and Shift+Tab only and check that the order follows the visual order. |

<!-- section:passed -->
## Passed criteria

- 2.4.1 Bypass Blocks: There is a skip link to the content (`index.html:10`).
- 2.4.2 Page Titled: The page has a descriptive title (`index.html:6`).
- 3.1.1 Language of Page: The page language is declared (`index.html:2`).

<!-- section:honest-gaps -->
## Honest gaps

- Static analysis: JavaScript behavior was not evaluated (the enviar() function is not in the reviewed files) nor real contrast through the full cascade.
- Reflow at 320 px (1.4.10) was not evaluated: it needs a browser or a real viewport.
- Form error states and content shown on hover or focus were not reviewed.
- No browser available: focus and the computed accessible name were not measured.
- This report is not a statement of conformance or legal advice. It does not replace testing with real users and assistive technology.

<!-- section:next-steps -->
## Next steps

1. Replace the div with a real button and label the email field.
2. Add the banner alt and darken the note text.
3. Restore the focus indicator and enlarge the close button.
4. Repeat the audit in URL mode with a browser to cover reflow, focus and tab order.

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
    "summary": "index.html and styles.css of a fictional site",
    "inputs": [
      "index.html",
      "styles.css"
    ],
    "capabilities": {
      "browser": false,
      "figma": false,
      "axe": false,
      "script": false
    }
  },
  "findings": [
    {
      "id": "WCAG-4.1.2-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "4.1.2",
        "name": "Name, Role, Value",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html"
      },
      "status": "fail",
      "severity": "critical",
      "confidence": "medium",
      "method": "static_code",
      "title": "The subscribe button is a div with no role or keyboard support",
      "description": "A div with onclick is not announced as a button and cannot receive keyboard focus, so the form cannot be submitted without a mouse.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 25,
          "snippet": "<div class=\"btn\" onclick=\"enviar()\">Suscribirme</div>"
        }
      ],
      "affected_users": "People using a keyboard or a screen reader.",
      "recommendation": "Use a <button type=\"submit\"> with the same visible text.",
      "dedup_key": "4.1.2|index.html:25"
    },
    {
      "id": "WCAG-2.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.1.1",
        "name": "Keyboard",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html"
      },
      "status": "fail",
      "severity": "critical",
      "confidence": "medium",
      "method": "static_code",
      "title": "The subscribe button cannot be activated with a keyboard",
      "description": "The div with onclick has no tabindex or keyboard handler, so it cannot receive focus or respond to Enter or Space.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 25,
          "snippet": "<div class=\"btn\" onclick=\"enviar()\">Suscribirme</div>"
        }
      ],
      "affected_users": "People using a keyboard, switch devices or voice control.",
      "recommendation": "Use a <button type=\"submit\">, which is already keyboard operable.",
      "dedup_key": "2.1.1|index.html:25"
    },
    {
      "id": "WCAG-1.4.3-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.4.3",
        "name": "Contrast (Minimum)",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "The note text has insufficient contrast",
      "description": "Gray #999999 on the white background gives 2.85:1; normal text needs at least 4.5:1.",
      "evidence": [
        {
          "kind": "code",
          "file": "styles.css",
          "line": 8,
          "snippet": ".nota { color: #999999; }",
          "measured": {
            "ratio": 2.85,
            "required": 4.5,
            "fg": "#999999",
            "bg": "#ffffff"
          }
        },
        {
          "kind": "code",
          "file": "styles.css",
          "line": 1,
          "snippet": ":root { --fondo: #ffffff; --texto: #1a1a1a; }"
        }
      ],
      "affected_users": "People with low vision or reading in bright light.",
      "recommendation": "Darken the text color, for example to #595959 (7:1 on white).",
      "dedup_key": "1.4.3|styles.css:8"
    },
    {
      "id": "WCAG-3.3.2-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "3.3.2",
        "name": "Labels or Instructions",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "The email field has no label",
      "description": "The placeholder disappears while typing and does not count as a label; the field has no label or aria-label.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 22,
          "snippet": "<input type=\"email\" name=\"correo\" placeholder=\"Tu correo\">"
        }
      ],
      "affected_users": "Screen reader users and people with memory difficulties.",
      "recommendation": "Associate a visible <label for> with the field, as is already done for the name field.",
      "dedup_key": "3.3.2|index.html:22"
    },
    {
      "id": "WCAG-1.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.1.1",
        "name": "Non-text Content",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "The banner image has no text alternative",
      "description": "The banner image has no alt attribute, so a screen reader user cannot tell what it conveys.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 18,
          "snippet": "<img class=\"banner\" src=\"banner.jpg\">"
        }
      ],
      "affected_users": "Blind or low-vision people using a screen reader.",
      "recommendation": "Add an alt that says what the image communicates, or an empty alt if it is decorative.",
      "dedup_key": "1.1.1|index.html:18"
    },
    {
      "id": "WCAG-2.4.7-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.7",
        "name": "Focus Visible",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "Links lose the focus indicator",
      "description": "The a:focus rule removes the outline and there is no replacement style.",
      "evidence": [
        {
          "kind": "code",
          "file": "styles.css",
          "line": 9,
          "snippet": "a:focus { outline: none; }"
        }
      ],
      "affected_users": "People who navigate with a keyboard.",
      "recommendation": "Remove the rule or define a :focus-visible with a high-contrast border.",
      "dedup_key": "2.4.7|styles.css:9"
    },
    {
      "id": "WCAG-2.5.8-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.5.8",
        "name": "Target Size (Minimum)",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "The close button is 18 by 18 pixels",
      "description": "The target is smaller than 24 by 24 CSS pixels and has no compensating space around it.",
      "evidence": [
        {
          "kind": "code",
          "file": "styles.css",
          "line": 11,
          "snippet": ".icono { width: 18px; height: 18px; padding: 0; border: 0; background: transparent; }",
          "measured": {
            "width_px": 18,
            "height_px": 18,
            "required_px": 24
          }
        }
      ],
      "affected_users": "People with tremor or using a touch screen.",
      "recommendation": "Enlarge the active area to at least 24 by 24 px, for example with padding.",
      "dedup_key": "2.5.8|styles.css:11"
    },
    {
      "id": "WCAG-1.3.5-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.3.5",
        "name": "Identify Input Purpose",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "The email field does not declare its purpose",
      "description": "The field has no autocomplete, so the browser cannot fill in the person's email.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 22,
          "snippet": "<input type=\"email\" name=\"correo\" placeholder=\"Tu correo\">"
        }
      ],
      "affected_users": "People with motor or memory difficulties, and those who rely on data managers.",
      "recommendation": "Add autocomplete=\"email\" to the field.",
      "dedup_key": "1.3.5|index.html:22"
    },
    {
      "id": "WCAG-2.4.3-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.3",
        "name": "Focus Order",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html"
      },
      "status": "manual",
      "confidence": "low",
      "method": "static_code",
      "title": "Focus order requires walking the page",
      "manual_check": {
        "reason": "Focus order depends on how the page renders and is traversed; code mode cannot decide it.",
        "procedure": "Walk the page with Tab and Shift+Tab only and check that the order follows the visual order.",
        "suggested_tools": [
          "Keyboard",
          "Browser"
        ]
      },
      "dedup_key": "2.4.3|index.html"
    },
    {
      "id": "WCAG-1.4.10-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.4.10",
        "name": "Reflow",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/reflow.html"
      },
      "status": "not_tested",
      "confidence": "low",
      "method": "inferred",
      "title": "Reflow at 320 px could not be evaluated",
      "dedup_key": "1.4.10|index.html"
    },
    {
      "id": "WCAG-2.4.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.1",
        "name": "Bypass Blocks",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "There is a skip link to the content",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 10,
          "snippet": "<a class=\"skip\" href=\"#contenido\">Saltar al contenido</a>"
        }
      ],
      "dedup_key": "2.4.1|index.html:10"
    },
    {
      "id": "WCAG-2.4.2-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.2",
        "name": "Page Titled",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "The page has a descriptive title",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 6,
          "snippet": "<title>Café Aurora – Inicio</title>"
        }
      ],
      "dedup_key": "2.4.2|index.html:6"
    },
    {
      "id": "WCAG-3.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "3.1.1",
        "name": "Language of Page",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "The page language is declared",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 2,
          "snippet": "<html lang=\"es\">"
        }
      ],
      "dedup_key": "3.1.1|index.html:2"
    }
  ],
  "honest_gaps": [
    "Static analysis: JavaScript behavior was not evaluated (the enviar() function is not in the reviewed files) nor real contrast through the full cascade.",
    "Reflow at 320 px (1.4.10) was not evaluated: it needs a browser or a real viewport.",
    "Form error states and content shown on hover or focus were not reviewed.",
    "No browser available: focus and the computed accessible name were not measured."
  ]
}
```
