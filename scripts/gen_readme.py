"""Rellena la tabla de skills entre <!-- catalog:start --> y <!-- catalog:end -->."""
import re

from common import ROOT, load_catalog

TEXT = {
    "es": {"head": "| Skill | Qué hace | Instalar |", "key": "description", "empty": "_Próximamente._"},
    "en": {"head": "| Skill | What it does | Install |", "key": "description_en", "empty": "_Coming soon._"},
}


def table(cat, lang):
    t = TEXT[lang]
    rows = [a for a in cat.get("assets") or [] if not a.get("hidden")]
    if not rows:
        return t["empty"]
    mk = cat["marketplace"]["name"]
    out = [t["head"], "|---|---|---|"]
    for a in rows:
        install = f"`/plugin install {a['plugin']}@{mk}`"
        out.append(f"| [`{a['id']}`](src/skills/{a['id']}/README.md) | {a[t['key']]} | {install} |")
    return "\n".join(out)


def main():
    cat = load_catalog()
    for fname, lang in (("README.md", "es"), ("README.en.md", "en")):
        p = ROOT / fname
        if not p.exists():
            continue
        text = re.sub(
            r"(<!-- catalog:start -->).*?(<!-- catalog:end -->)",
            lambda m: f"{m.group(1)}\n{table(cat, lang)}\n{m.group(2)}",
            p.read_text(), flags=re.S)
        p.write_text(text)


if __name__ == "__main__":
    main()
