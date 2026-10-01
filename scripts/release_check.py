"""Valida una etiqueta de release antes de publicar: <plugin>--vX.Y.Z debe coincidir con el catálogo.

Uso: python scripts/release_check.py <plugin> <version>
"""
import re
import sys

from common import load_catalog

TAG = re.compile(r"^(?P<plugin>[a-z0-9]+(?:-[a-z0-9]+)*)--v(?P<version>\d+\.\d+\.\d+)$")


def parse_tag(tag):
    m = TAG.match(tag)
    return (m["plugin"], m["version"]) if m else None


def check(plugin, version):
    plugins = load_catalog()["plugins"]
    if plugin not in plugins:
        return [f"el plugin {plugin!r} no existe en el catálogo"]
    if plugins[plugin]["version"] != version:
        return [f"la etiqueta dice {version} pero catalog.yml dice {plugins[plugin]['version']}: sube la versión en el catálogo antes de etiquetar"]
    return []


def main():
    plugin, version = sys.argv[1], sys.argv[2]
    errors = check(plugin, version)
    for e in errors:
        print("ERROR", e)
    print(f"{plugin} {version}: {'OK' if not errors else 'NO coincide'}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
