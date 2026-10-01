"""Instala en carpetas temporales por cada ruta y verifica el resultado.

Rutas: carpeta de skill suelta, zip de un skill, caché de plugin, install.sh (claude y copilot) y,
con SMOKE_NPX=1, `npx skills add <repo> --list` (cada skill debe aparecer una sola vez).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import yaml

from common import ROOT, load_catalog, split_frontmatter

LINK = re.compile(r"\]\(((?:\.{1,2}/)?[A-Za-z0-9_.][^)#:\s]*)(?:#[^)]*)?\)")
errors = []


def err(msg):
    errors.append(msg)


def check_skill_dir(skill_dir, label):
    """Un skill suelto debe bastarse solo: SKILL.md válido y ningún enlace fuera de su carpeta."""
    skill = skill_dir / "SKILL.md"
    if not skill.exists():
        err(f"{label}: falta SKILL.md")
        return
    try:
        meta, _ = split_frontmatter(skill.read_text())
        if meta.get("name") != skill_dir.name:
            err(f"{label}: name {meta.get('name')!r} != carpeta {skill_dir.name!r}")
    except (ValueError, yaml.YAMLError) as e:
        err(f"{label}: frontmatter inválido ({e})")
    for md in skill_dir.rglob("*.md"):
        for m in LINK.finditer(md.read_text()):
            target = m.group(1)
            if "/" not in target and not re.search(r"\.[a-z]{2,4}$", target):
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                err(f"{label}: {md.relative_to(skill_dir)} enlace roto {target}")
            elif skill_dir.resolve() not in resolved.parents:
                err(f"{label}: {md.relative_to(skill_dir)} enlace sale del skill: {target}")
    for p in skill_dir.rglob("*"):
        if p.is_symlink():
            err(f"{label}: symlink {p.relative_to(skill_dir)}")


def main():
    cat = load_catalog()
    ids = [a["id"] for a in cat.get("assets") or []]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for i in ids:
            src = ROOT / "skills" / i
            lone = tmp / "lone" / i
            shutil.copytree(src, lone)
            check_skill_dir(lone, f"carpeta suelta {i}")

            zpath = tmp / f"{i}.zip"
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
                for f in sorted(src.rglob("*")):
                    if f.is_file():
                        z.write(f, Path(i) / f.relative_to(src))
            out = tmp / "unzipped"
            with zipfile.ZipFile(zpath) as z:
                z.extractall(out)
            check_skill_dir(out / i, f"zip {i}")
            if zpath.stat().st_size > 5 * 1024 * 1024:
                err(f"zip {i}: pesa más de 5 MB")

        for name in cat["plugins"]:
            cache = tmp / "cache" / name
            shutil.copytree(ROOT / "plugins" / name, cache)
            manifest = cache / ".claude-plugin" / "plugin.json"
            if not manifest.exists():
                err(f"plugin {name}: falta plugin.json")
                continue
            data = json.loads(manifest.read_text())
            if data.get("name") != name:
                err(f"plugin {name}: plugin.json name {data.get('name')!r}")
            if not data.get("version"):
                err(f"plugin {name}: plugin.json sin version")
            for skill in (cache / "skills").iterdir():
                check_skill_dir(skill, f"plugin {name}/{skill.name}")

        mk = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
        for entry in mk["plugins"]:
            if "version" in entry:
                err(f"marketplace: {entry['name']} no debe llevar version (va solo en el manifiesto)")
            if not (ROOT / entry["source"]).is_dir():
                err(f"marketplace: source inexistente {entry['source']}")

        for tool, dest in (("claude", ".claude"), ("copilot", ".github")):
            target = tmp / f"proj-{tool}"
            target.mkdir()
            subprocess.run([str(ROOT / "scripts" / "install.sh"), tool, str(target)],
                           check=True, capture_output=True)
            for i in ids:
                if not (target / dest / "skills" / i / "SKILL.md").exists():
                    err(f"install.sh {tool}: falta skills/{i}/SKILL.md")

        if os.environ.get("SMOKE_NPX") == "1":
            res = subprocess.run(["npx", "-y", "skills", "add", str(ROOT), "--list"],
                                 capture_output=True, text=True, timeout=240,
                                 stdin=subprocess.DEVNULL, env={**os.environ, "CI": "1"})
            output = re.sub(r"\x1b\[[0-9;?]*[a-zA-Z]", "", res.stdout + res.stderr)
            for i in ids:
                n = len(re.findall(rf"(?<![\w-]){re.escape(i)}(?![\w-])", output))
                if n != 1:
                    err(f"npx skills --list: {i} aparece {n} veces (esperado 1). "
                        f"Salida (código {res.returncode}):\n{output[-1500:]}")

    print(f"{len(ids)} skill(s) verificados por cada ruta")
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
