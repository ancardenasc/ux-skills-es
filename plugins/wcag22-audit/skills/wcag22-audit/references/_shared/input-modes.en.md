<!-- GENERADO desde shared/references/input-modes.en.md por scripts/build.py. No editar a mano. -->
# Input modes

Detect, do not require. Step 0 of each audit picks the mode from what you have and states it in the Scope section.

## Capability detection

1. Were you given a path or a diff? A URL? A design (image or Figma link)?
2. Which tools exist in the session? A browser (Playwright, Chrome DevTools or similar), Figma (reading variables, design context and screenshots), `axe` already installed in the project, `python3` for scripts.
3. Record the result in `scope.capabilities` of the JSON.

## The three modes

| Mode | How | Max confidence | Covers well | Cannot cover |
|---|---|---|---|---|
| **A. Code or diff** | `git diff $(git merge-base <base> HEAD)` against the working tree (includes uncommitted work; `base...HEAD` compares only commits and would be empty) or given paths | medium | alt, labels, landmarks, titles, `lang`, name and role in markup, `outline:none`, autocomplete | real contrast through the cascade, focus order, reflow, anything JavaScript decides |
| **B. URL** | Browser: accessibility snapshot, computed styles, resize to 320 px, walk with Tab, emulate reduced motion | high for what is measured | computed contrast, visible focus, reflow, accessible name | screen readers, caption quality, login-gated pages without credentials |
| **C. Design** | Figma variables, context or screenshots, or pasted images | low to medium | contrast between sampled colors, target size, hierarchy, color-only cues | ARIA, semantics, keyboard, dynamic states |

The `assessable` field in `wcag22-criteria.json` says, per criterion, how much can be assessed in each mode (`yes`, `partial`, `no`). Whatever is `no` or `partial` in the current mode goes to `manual` or `not_tested`.

## Rules

- With no tool and no URL: use mode A or C and say so. With a URL but no browser: ask for HTML or screenshots; do not guess the content.
- **axe:** use it only if it is already in the project or the person approves a local `npx` run. Never inject it from a CDN.
- Never invent content from a page you could not see.
- A diff with no frontend changes is not approved: answer "not applicable" and say why.
