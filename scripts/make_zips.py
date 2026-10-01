"""Crea un zip por skill (para subir a claude.ai o adjuntar a una Release) en dist/zips/<id>.zip.

El zip es determinista (mismas fechas y permisos), tiene la carpeta <id>/ en la raíz y SKILL.md dentro.
Uso: python scripts/make_zips.py [--only ID]
"""
import sys
import zipfile
from pathlib import Path

from common import ROOT, load_catalog

OUT = ROOT / "dist" / "zips"
FIXED_DATE = (1980, 1, 1, 0, 0, 0)


def build_zip(skill_dir, name, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(p for p in skill_dir.rglob("*") if p.is_file()):
            info = zipfile.ZipInfo(str(Path(name) / f.relative_to(skill_dir)), FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if f.stat().st_mode & 0o111 else 0o644) << 16
            z.writestr(info, f.read_bytes())
    return dest


def main():
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    built = 0
    for a in load_catalog()["assets"]:
        if only and a["id"] != only:
            continue
        skill_dir = ROOT / "plugins" / a["plugin"] / "skills" / a["id"]
        z = build_zip(skill_dir, a["id"], OUT / f"{a['id']}.zip")
        print(f"{z.relative_to(ROOT)}  {z.stat().st_size / 1024:.0f} KB")
        built += 1
    if only and not built:
        raise SystemExit(f"no hay un skill llamado {only}")


if __name__ == "__main__":
    main()
