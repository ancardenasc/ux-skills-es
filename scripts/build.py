"""Genera las salidas por herramienta desde src/, shared/ y catalog.yml.

src/skills/<id>/            -> plugins/<plugin>/skills/<id>/   (autocontenido; lo leen Claude Code, npx skills, gh skill y el zip)
shared/<src> (vendor)       -> plugins/<plugin>/skills/<id>/references/_shared/<archivo>   (copia, nunca symlink)
catalog.yml                 -> plugins/<plugin>/.claude-plugin/plugin.json y .claude-plugin/marketplace.json

No hay una copia plana en skills/: duplicaba cada skill ante `gh skill` (lo descubría por skills/ y por plugins/).

README.md y CHANGELOG.md de la raíz de cada skill son para humanos y no se incluyen en la salida (los de subcarpetas, como template/, sí).
La versión va solo en el manifiesto del plugin, no en la entrada del marketplace.
"""
import json
import shutil
from pathlib import Path

from common import ROOT, load_catalog

HUMAN_ONLY = {"README.md", "CHANGELOG.md"}  # solo se omiten en la raíz del skill; dentro de template/ o references/ se conservan


def make_ignore(skill_root):
    def ignore(directory, names):
        at_root = Path(directory) == skill_root
        return [n for n in names
                if (at_root and n in HUMAN_ONLY) or n in {"__pycache__", ".DS_Store"} or n.endswith(".pyc")]
    return ignore



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
    for d in (ROOT / "plugins",):
        reset(d)
    legacy = ROOT / "skills"
    if legacy.exists():
        shutil.rmtree(legacy)

    by_plugin = {}
    for asset in cat.get("assets") or []:
        if asset["type"] != "skill":
            raise SystemExit(f"tipo no soportado {asset['type']!r} en {asset['id']}")
        by_plugin.setdefault(asset["plugin"], []).append(asset)

    unknown = set(by_plugin) - set(cat["plugins"])
    if unknown:
        raise SystemExit(f"assets con plugin no declarado: {sorted(unknown)}")

    for name, meta in cat["plugins"].items():
        assets = by_plugin.get(name)
        if not assets:
            raise SystemExit(f"el plugin {name} no tiene assets en el catálogo")
        plugin_dir = ROOT / "plugins" / name
        for asset in assets:
            src = ROOT / "src" / "skills" / asset["id"]
            out = plugin_dir / "skills" / asset["id"]
            shutil.copytree(src, out, ignore=make_ignore(src))
            vendor(asset, out)
        manifest = plugin_dir / ".claude-plugin"
        manifest.mkdir(parents=True)
        (manifest / "plugin.json").write_text(json.dumps({
            "name": name,
            "version": meta["version"],
            "description": meta["description"],
            "author": {"name": cat["author"]["name"], "url": cat["author"]["url"]},
            "license": cat["license"],
        }, indent=2, ensure_ascii=False) + "\n")

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
