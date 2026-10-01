# Limits and honesty

This collection is designed to **say what it does not know**. Here is, plainly, what it does and does not do.

## What they do not do

- **They do not certify conformance or give legal advice.** A report is not a statement of conformance. Each report says so in its footer.
- **They do not replace testing with real people and real screen readers.** An automated or heuristic audit finds only part of the problems.
- **They do not fix code.** The audit skills are read-only.
- **They do not evaluate WCAG level AAA** or the specification's techniques.
- **They do not invent data.** `case-study-writer` marks what is missing as `[MISSING DATA: ...]` instead of filling it in, and it does not repeat names, employers or phone numbers from your notes.

## Copyright

WCAG belongs to the W3C and the 10 heuristics to Jakob Nielsen (Nielsen Norman Group). There is no official Spanish translation of WCAG 2.2 and NN/g licenses translations of its texts. So the collection **cites number, name, level and link**, and uses **own summaries and labels** of at most 25 words; it never copies or translates the original text. The Spanish labels (`label_es`) are our own, not the official translation. See [NOTICE](../../NOTICE.md).

## What has been verified and what has not

**Verified:**

- The 55 WCAG 2.2 A and AA criteria match W3C's machine-readable data (id, name and level) and their links respond; this is rechecked every week.
- The names of the 10 heuristics match the NN/g page.
- Each sample report is validated and its evidence lines are checked against the fictional project they come from.
- The skills were run with a real model on projects seeded with known errors and with deliberately correct parts: they found what was expected without flagging what was correct. Those runs exposed errors in the repository itself, which were fixed.
- Installation is tested for every route: loose folder, zip, plugin, `npx skills`, `gh skill` and the install script.

**Not verified yet:**

- Uploading the zip to claude.ai.
- GitHub Copilot in a real session: the skills use the open format Copilot reads, but have not been run there.
- `wcag22-audit` in design mode (Figma or screenshots) and `heuristic-review-es` in URL and design modes.
- `case-kit` in English and `case-study-writer` with `--guardar`.

## Biases and method limits

- A **static** code analysis cannot see how a page renders or how it behaves with JavaScript: its maximum confidence is medium.
- A **heuristic review** done by a single person (or a model) finds only part of the problems.
- A language model can be wrong. That is why reports require concrete evidence, and the repository tests compare real results with what is expected. Always review critical findings before acting.
