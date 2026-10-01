"""Valida fuentes y salida generada. Sale con código 1 si hay algún problema."""
import os
import re
import sys

import yaml

from common import ROOT, load_catalog, split_frontmatter

NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Términos de trabajo o de flujos internos que no deben llegar a un repo público.
FORBIDDEN = re.compile(
    r"tirant|BDD-|c06e3789|\bncardenas\b|customfield_\d+|/Users/|jira|gitlab|devflow"
    r"|execute-task|start-task|review-ticket|task-reviewers",
    re.I,
)
SKIP_FORBIDDEN = {"scripts/lint.py", "tests/unit/test_build.py"}
SKIP_DIRS = {".git", ".venv", ".pytest_cache", "__pycache__", "node_modules"}
LINK = re.compile(r"\]\(((?:\.{1,2}/)?[A-Za-z0-9_.][^)#:\s]*)(?:#[^)]*)?\)")
errors = []


def err(msg):
    errors.append(msg)


def walk():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames + dirnames:
            yield os.path.join(dirpath, name)


def check_links(md, boundary):
    """Cada enlace relativo debe resolver y quedarse dentro de `boundary`."""
    for m in LINK.finditer(md.read_text()):
        target = m.group(1)
        if "/" not in target and not re.search(r"\.[a-z]{2,4}$", target):
            continue  # marcador tipo [titulo](url), no una ruta
        resolved = (md.parent / target).resolve()
        rel = md.relative_to(ROOT).as_posix()
        if not resolved.exists():
            err(f"{rel}: enlace roto {target}")
        elif boundary and boundary not in resolved.parents and resolved != boundary:
            err(f"{rel}: el enlace {target} sale de {boundary.relative_to(ROOT).as_posix()}")


def main():
    cat = load_catalog()

    for a in cat.get("assets") or []:
        i = a["id"]
        if not NAME.match(i) or len(i) > 64:
            err(f"{i}: el nombre debe ser kebab-case y de máx. 64 caracteres")
        if a["type"] != "skill":
            err(f"{i}: tipo no soportado {a['type']}")
            continue
        if a["plugin"] not in cat["plugins"]:
            err(f"{i}: plugin desconocido {a['plugin']}")
        for k in ("description", "description_en"):
            if not a.get(k):
                err(f"{i}: falta {k} en el catálogo")
        base = ROOT / "src" / "skills" / i
        skill = base / "SKILL.md"
        if not skill.exists():
            err(f"{i}: falta src/skills/{i}/SKILL.md")
            continue
        if not (base / "README.md").exists():
            err(f"{i}: falta src/skills/{i}/README.md (guía para humanos)")
        text = skill.read_text()
        try:
            meta, _ = split_frontmatter(text)
        except (ValueError, yaml.YAMLError) as e:
            err(f"src/skills/{i}/SKILL.md: frontmatter inválido ({str(e).splitlines()[0]})")
            continue
        if meta.get("name") != i:
            err(f"src/skills/{i}/SKILL.md: name != {i}")
        if not meta.get("description") or len(str(meta["description"])) > 1024:
            err(f"src/skills/{i}/SKILL.md: description vacía o > 1024 caracteres")
        if text.count("\n") > 500:
            err(f"src/skills/{i}/SKILL.md: más de 500 líneas; mover detalle a references/")
        for entry in a.get("vendor") or []:
            langs = entry.get("langs") or [None]
            for lang in langs:
                src = entry["src"].format(lang=lang) if lang else entry["src"]
                if not (ROOT / "shared" / src).is_file():
                    err(f"{i}: vendor apunta a shared/{src}, que no existe")

    ids = {a["id"] for a in cat.get("assets") or []}
    for kind in ("skills",):
        base = ROOT / kind
        if base.exists():
            for d in base.iterdir():
                if d.is_dir() and d.name not in ids:
                    err(f"{kind}/{d.name}: carpeta generada que no está en el catálogo")

    for path in walk():
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        if os.path.islink(path):
            err(f"{rel}: los symlinks están prohibidos (no sobreviven al caché ni al zip)")
            continue
        if not os.path.isfile(path) or rel in SKIP_FORBIDDEN:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                for n, line in enumerate(fh, 1):
                    if FORBIDDEN.search(line):
                        err(f"{rel}:{n}: término prohibido: {line.strip()[:80]}")
        except UnicodeDecodeError:
            pass

    for skill_dir in sorted((ROOT / "skills").glob("*")):
        for md in skill_dir.rglob("*.md"):
            check_links(md, skill_dir)
    for plugin_dir in sorted((ROOT / "plugins").glob("*")):
        for md in plugin_dir.rglob("*.md"):
            check_links(md, plugin_dir)
    docs = [ROOT / n for n in ("README.md", "README.en.md", "CONTRIBUTING.md", "AGENTS.md")]
    docs += (ROOT / "docs").rglob("*.md")
    for md in docs:
        if md.exists():
            check_links(md, None)

    es = {p.name for p in (ROOT / "docs" / "es").glob("*.md")}
    en = {p.name for p in (ROOT / "docs" / "en").glob("*.md")}
    for name in sorted(es ^ en):
        err(f"docs: {name} existe solo en {'es' if name in es else 'en'} (paridad es/en)")

    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} problema(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
