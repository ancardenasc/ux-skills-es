# Heuristic review: Café Aurora order (fictional sample flow)

<!-- section:summary -->
## Summary

- **Verdict:** the flow works but gives no response when saving and lets the order be deleted without confirmation; fix those two points before release.
- **Failing findings:** 7 (Critical 0 · Serious 2 · Moderate 4 · Minor 1)
- **Need manual check:** 2
- **Coverage:** 8 of 10 applicable criteria in this mode

| Heuristic | Status | Findings |
|---|---|---|
| H1 Visibility of System Status | Problems found | 1 |
| H2 Match Between the System and the Real World | Problems found | 1 |
| H3 User Control and Freedom | Needs manual check | 0 |
| H4 Consistency and Standards | Problems found | 1 |
| H5 Error Prevention | Problems found | 1 |
| H6 Recognition Rather than Recall | Problems found | 1 |
| H7 Flexibility and Efficiency of Use | Needs manual check | 0 |
| H8 Aesthetic and Minimalist Design | No problems | 0 |
| H9 Help Users Recognize, Diagnose, and Recover from Errors | Problems found | 1 |
| H10 Help and Documentation | Problems found | 1 |

<!-- section:scope -->
## Scope

- **Mode:** Code or diff
- **What was reviewed:** `pedido.html` of a fictional flow
- **Task evaluated:** Create, save and, if needed, delete a coffee order.
- **Detected capabilities:** browser no · Figma no · axe no · script no
- **Date:** 2026-10-01

<!-- section:findings -->
## Findings

### Serious: Deleting the order asks for no confirmation and cannot be undone

- **Heuristic:** H5 Error Prevention, https://www.nngroup.com/articles/ten-usability-heuristics/
- **Where:** `pedido.html:17`
- **What happens:** A single click runs the deletion and reloads the page; there is no confirmation, trash or undo.
- **Confidence:** Medium, method: static_code
- **Who is affected:** Anyone who presses the button by mistake.
- **How to fix:** Ask for confirmation stating what will be deleted, or allow undo for a few seconds.

### Serious: Saving gives no feedback at all

- **Heuristic:** H1 Visibility of System Status, https://www.nngroup.com/articles/ten-usability-heuristics/
- **Where:** `pedido.html:22`
- **What happens:** The function sends the request and shows no progress, success or error; the person cannot tell whether the order was saved.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People who save without knowing if it worked and may repeat the action.
- **How to fix:** Show a loading state and a success or error message next to the button.

### Moderate: The error message is technical and offers no solution

- **Heuristic:** H9 Help Users Recognize, Diagnose, and Recover from Errors, https://www.nngroup.com/articles/ten-usability-heuristics/
- **Where:** `pedido.html:25`
- **What happens:** The text shows an internal code and mentions a parameter; it does not say what failed or how to fix it.
- **Confidence:** Medium, method: static_code
- **Who is affected:** Anyone outside the technical team.
- **How to fix:** State in plain words what happened and what to do, for example which field to correct.

### Moderate: The date asks for month/day/year

- **Heuristic:** H2 Match Between the System and the Real World, https://www.nngroup.com/articles/ten-usability-heuristics/
- **Where:** `pedido.html:13`
- **What happens:** The mm/dd/yyyy format is not the usual one for the local audience, which writes day, month and year; it invites mixing up dates such as 03/04.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People who write dates in the local order.
- **How to fix:** Use dd/mm/yyyy or a date picker that shows the month by name.

### Moderate: Two differently named buttons for similar actions

- **Heuristic:** H4 Consistency and Standards, https://www.nngroup.com/articles/ten-usability-heuristics/
- **Where:** `pedido.html:15`
- **What happens:** "Aceptar" and "Enviar" do not say what they do and compete with each other; it is unclear which one confirms the order.
- **Confidence:** Medium, method: static_code
- **Who is affected:** Anyone who must decide which button to press.
- **How to fix:** Keep a single primary button with a clear verb, for example "Confirm order".

### Moderate: The gear button does not say what it does

- **Heuristic:** H6 Recognition Rather than Recall, https://www.nngroup.com/articles/ten-usability-heuristics/
- **Where:** `pedido.html:18`
- **What happens:** The icon has no text or title; its function must be remembered or guessed.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People using the site for the first time.
- **How to fix:** Add a visible label or a descriptive title.

### Minor: There is no help link

- **Heuristic:** H10 Help and Documentation, https://www.nngroup.com/articles/ten-usability-heuristics/
- **Where:** `pedido.html:9`
- **What happens:** The navigation offers no help or contact for people with doubts about the order.
- **Confidence:** Medium, method: static_code
- **Who is affected:** People who get stuck during the order.
- **How to fix:** Add a help or contact link to the navigation.

<!-- section:manual -->
## Manual verification

| Criterion | Why it could not be decided | How to check |
|---|---|---|
| H3 User Control and Freedom | The control to go back or undo can only be verified by running the flow. | Walk through the order and try to cancel or undo at each step. |
| H7 Flexibility and Efficiency of Use | They cannot be judged from the code; they require observing experienced people. | Observe people who repeat the order and ask which shortcuts they miss. |

<!-- section:passed -->
## Passed criteria

- H4 Consistency and Standards: The navigation labels are consistent (`pedido.html:9`).
- H8 Aesthetic and Minimalist Design: The screen has a single task (`pedido.html:11`).

<!-- section:honest-gaps -->
## Honest gaps

- The review was done by reading code: the flow was not seen running, so pacing, animations and server-generated texts were not evaluated.
- A single evaluator: heuristic review improves with several perspectives and does not replace usability testing with real users.
- Only the order task was reviewed; the account, payment and tracking were not.
- H3 and H7 are left for manual verification: they require running the flow and observing real use.
- This report is not a statement of conformance or legal advice. It does not replace testing with real users and assistive technology.

<!-- section:next-steps -->
## Next steps

1. Ask for confirmation before deleting and show the result of saving.
2. Unify the buttons into one primary action with a clear verb.
3. Change the date format and rewrite the error message in plain language.
4. Test the flow with 5 users to validate these findings.

---

*This report is not a statement of conformance or legal advice. It does not replace testing with real users and assistive technology.*

```json ux-skills-findings
{
  "schema_version": "1",
  "skill": "heuristic-review-es",
  "language": "en",
  "mode": "code",
  "generated_on": "2026-10-01",
  "scope": {
    "summary": "pedido.html of a fictional flow",
    "inputs": [
      "pedido.html"
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
      "id": "NIELSEN-H5-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H5",
        "name": "Error Prevention",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "Deleting the order asks for no confirmation and cannot be undone",
      "description": "A single click runs the deletion and reloads the page; there is no confirmation, trash or undo.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 17,
          "snippet": "<button type=\"button\" onclick=\"borrarPedido()\">Eliminar pedido</button>"
        },
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 23,
          "snippet": "function borrarPedido() { fetch('/pedido', {method: 'DELETE'}).then(() => location.reload()); }"
        }
      ],
      "affected_users": "Anyone who presses the button by mistake.",
      "recommendation": "Ask for confirmation stating what will be deleted, or allow undo for a few seconds.",
      "dedup_key": "H5|pedido.html:17"
    },
    {
      "id": "NIELSEN-H1-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H1",
        "name": "Visibility of System Status",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "Saving gives no feedback at all",
      "description": "The function sends the request and shows no progress, success or error; the person cannot tell whether the order was saved.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 22,
          "snippet": "function guardar() { fetch('/guardar', {method: 'POST'}); }"
        }
      ],
      "affected_users": "People who save without knowing if it worked and may repeat the action.",
      "recommendation": "Show a loading state and a success or error message next to the button.",
      "dedup_key": "H1|pedido.html:22"
    },
    {
      "id": "NIELSEN-H9-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H9",
        "name": "Help Users Recognize, Diagnose, and Recover from Errors",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "The error message is technical and offers no solution",
      "description": "The text shows an internal code and mentions a parameter; it does not say what failed or how to fix it.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 25,
          "snippet": "document.getElementById('estado').textContent = 'Error 0x80070057: parámetro incorrecto';"
        }
      ],
      "affected_users": "Anyone outside the technical team.",
      "recommendation": "State in plain words what happened and what to do, for example which field to correct.",
      "dedup_key": "H9|pedido.html:25"
    },
    {
      "id": "NIELSEN-H2-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H2",
        "name": "Match Between the System and the Real World",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "The date asks for month/day/year",
      "description": "The mm/dd/yyyy format is not the usual one for the local audience, which writes day, month and year; it invites mixing up dates such as 03/04.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 13,
          "snippet": "<label for=\"fecha\">Fecha de entrega (mm/dd/aaaa)</label>"
        }
      ],
      "affected_users": "People who write dates in the local order.",
      "recommendation": "Use dd/mm/yyyy or a date picker that shows the month by name.",
      "dedup_key": "H2|pedido.html:13"
    },
    {
      "id": "NIELSEN-H4-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H4",
        "name": "Consistency and Standards",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "Two differently named buttons for similar actions",
      "description": "\"Aceptar\" and \"Enviar\" do not say what they do and compete with each other; it is unclear which one confirms the order.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 15,
          "snippet": "<button type=\"submit\">Aceptar</button>"
        }
      ],
      "affected_users": "Anyone who must decide which button to press.",
      "recommendation": "Keep a single primary button with a clear verb, for example \"Confirm order\".",
      "dedup_key": "H4|pedido.html:15"
    },
    {
      "id": "NIELSEN-H6-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H6",
        "name": "Recognition Rather than Recall",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "The gear button does not say what it does",
      "description": "The icon has no text or title; its function must be remembered or guessed.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 18,
          "snippet": "<button type=\"button\" class=\"ico\" title=\"\">⚙</button>"
        }
      ],
      "affected_users": "People using the site for the first time.",
      "recommendation": "Add a visible label or a descriptive title.",
      "dedup_key": "H6|pedido.html:18"
    },
    {
      "id": "NIELSEN-H10-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H10",
        "name": "Help and Documentation",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "minor",
      "confidence": "medium",
      "method": "static_code",
      "title": "There is no help link",
      "description": "The navigation offers no help or contact for people with doubts about the order.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 9,
          "snippet": "<a href=\"/\">Inicio</a> <a href=\"/pedido\">Mi pedido</a> <a href=\"/cuenta\">Cuenta</a>"
        }
      ],
      "affected_users": "People who get stuck during the order.",
      "recommendation": "Add a help or contact link to the navigation.",
      "dedup_key": "H10|pedido.html:9"
    },
    {
      "id": "NIELSEN-H3-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H3",
        "name": "User Control and Freedom",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "manual",
      "confidence": "low",
      "method": "static_code",
      "title": "Cancel and undo are checked by walking the flow",
      "manual_check": {
        "reason": "The control to go back or undo can only be verified by running the flow.",
        "procedure": "Walk through the order and try to cancel or undo at each step.",
        "suggested_tools": [
          "Running flow"
        ]
      },
      "dedup_key": "H3|pedido.html"
    },
    {
      "id": "NIELSEN-H7-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H7",
        "name": "Flexibility and Efficiency of Use",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "manual",
      "confidence": "low",
      "method": "static_code",
      "title": "Shortcuts and customization depend on real usage",
      "manual_check": {
        "reason": "They cannot be judged from the code; they require observing experienced people.",
        "procedure": "Observe people who repeat the order and ask which shortcuts they miss.",
        "suggested_tools": [
          "Running flow"
        ]
      },
      "dedup_key": "H7|pedido.html"
    },
    {
      "id": "NIELSEN-H4-002",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H4",
        "name": "Consistency and Standards",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "The navigation labels are consistent",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 9,
          "snippet": "<a href=\"/\">Inicio</a> <a href=\"/pedido\">Mi pedido</a> <a href=\"/cuenta\">Cuenta</a>"
        }
      ],
      "dedup_key": "H4|pedido.html:9"
    },
    {
      "id": "NIELSEN-H8-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H8",
        "name": "Aesthetic and Minimalist Design",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "The screen has a single task",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 11,
          "snippet": "<h1>Tu pedido</h1>"
        }
      ],
      "dedup_key": "H8|pedido.html:11"
    }
  ],
  "honest_gaps": [
    "The review was done by reading code: the flow was not seen running, so pacing, animations and server-generated texts were not evaluated.",
    "A single evaluator: heuristic review improves with several perspectives and does not replace usability testing with real users.",
    "Only the order task was reviewed; the account, payment and tracking were not.",
    "H3 and H7 are left for manual verification: they require running the flow and observing real use."
  ]
}
```
