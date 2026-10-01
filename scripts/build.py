"""Genera las salidas por herramienta desde src/, shared/ y catalog.yml.

src/skills/<id>/            -> skills/<id>/            (carpeta plana autocontenida: npx skills, gh skill, zip, Copilot)
shared/<src> (vendor)       -> skills/<id>/references/_shared/<archivo>   (copia, nunca symlink)
skills/<id>/                -> plugins/<plugin>/skills/<id>/              (mismos bytes, para el caché de Claude Code)
catalog.yml                 -> plugins/<plugin>/.claude-plugin/plugin.json y .claude-plugin/marketplace.json

README.md y CHANGELOG.md de cada skill son para humanos y no se incluyen en la salida.
La versión va solo en el manifiesto del plugin, no en la entrada del marketplace.
"""
import json
import shutil

from common import ROOT, load_catalog

IGNORE = shutil.ignore_patterns("README.md", "CHANGELOG.md", "__pycache__", "*.pyc", ".DS_Store")
HEADERS = {
    ".md": "<!-- GENERADO desde shared/{src} por scripts/build.py. No editar a mano. -->\n",
    ".yml": "# GENERADO desde shared/{src} por scripts/build.py. No editar a mano.\n",
    ".yaml": "# GENERADO desde shared/{src} por scripts/build.py. No editar a mano.\n",
}


def reset(path):
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def expand(entry):
    """Devuelve (src_rel, dest_rel) por cada idioma de una entrada vendor."""
    langs = entry.get("langs") or [None]
    for lang in langs:
        src = entry["src"].format(lang=lang) if lang else entry["src"]
        dest = entry.get("dest") or f"references/_shared/{src.rsplit('/', 1)[-1]}"
        yield src, dest


def vendor(asset, skill_dir):
    written = []
    for entry in asset.get("vendor") or []:
        for src, dest in expand(entry):
            source = ROOT / "shared" / src
            if not source.is_file():
                raise SystemExit(f"{asset['id']}: falta shared/{src}")
            target = skill_dir / dest
            target.parent.mkdir(parents=True, exist_ok=True)
            header = HEADERS.get(source.suffix)
            if header:
                target.write_text(header.format(src=src) + source.read_text())
            else:
                shutil.copy2(source, target)
            written.append(dest)
    if written:
        note = skill_dir / "references" / "_shared" / "GENERATED.txt"
        note.parent.mkdir(parents=True, exist_ok=True)
        note.write_text("Archivos copiados desde shared/ por scripts/build.py. No editar a mano.\n"
                        + "".join(f"- {w}\n" for w in sorted(written)))


def main():
    cat = load_catalog()
    for d in (ROOT / "skills", ROOT / "plugins"):
        reset(d)

    by_plugin = {}
    for asset in cat.get("assets") or []:
        if asset["type"] != "skill":
            raise SystemExit(f"tipo no soportado {asset['type']!r} en {asset['id']}")
        by_plugin.setdefault(asset["plugin"], []).append(asset)
        src = ROOT / "src" / "skills" / asset["id"]
        out = ROOT / "skills" / asset["id"]
        shutil.copytree(src, out, ignore=IGNORE)
        vendor(asset, out)

    for name, meta in cat["plugins"].items():
        assets = by_plugin.get(name)
        if not assets:
            raise SystemExit(f"el plugin {name} no tiene assets en el catálogo")
        plugin_dir = ROOT / "plugins" / name
        for asset in assets:
            shutil.copytree(ROOT / "skills" / asset["id"], plugin_dir / "skills" / asset["id"])
        manifest = plugin_dir / ".claude-plugin"
        manifest.mkdir(parents=True)
        (manifest / "plugin.json").write_text(json.dumps({
            "name": name,
            "version": meta["version"],
            "description": meta["description"],
            "author": {"name": cat["author"]["name"], "url": cat["author"]["url"]},
            "license": cat["license"],
        }, indent=2, ensure_ascii=False) + "\n")

    unknown = set(by_plugin) - set(cat["plugins"])
    if unknown:
        raise SystemExit(f"assets con plugin no declarado: {sorted(unknown)}")

    (ROOT / ".claude-plugin").mkdir(exist_ok=True)
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(json.dumps({
        "name": cat["marketplace"]["name"],
        "owner": {"name": cat["author"]["name"]},
        "description": cat["marketplace"]["description"],
        "plugins": [
            {"name": n, "source": f"./plugins/{n}", "description": m["description"]}
            for n, m in cat["plugins"].items()
        ],
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"construidos {sum(len(v) for v in by_plugin.values())} skills en {len(cat['plugins'])} plugins")


if __name__ == "__main__":
    main()
