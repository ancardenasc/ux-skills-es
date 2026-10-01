#!/usr/bin/env bash
# Instalador manual. Uso: scripts/install.sh <claude|copilot> [carpeta-destino]
#   claude  -> copia cada skill a <destino>/.claude/skills   (por defecto: carpeta actual)
#   copilot -> copia cada skill a <destino>/.github/skills
# Instala todos los skills. Para uno solo: npx skills add <usuario>/ux-skills-es --skill <id>
set -euo pipefail
tool="${1:?uso: install.sh <claude|copilot> [carpeta-destino]}"
target="${2:-.}"
root="$(cd "$(dirname "$0")/.." && pwd)"
case "$tool" in
  claude)  dest="$target/.claude/skills" ;;
  copilot) dest="$target/.github/skills" ;;
  *) echo "herramienta desconocida: $tool" >&2; exit 1 ;;
esac
mkdir -p "$dest"
for skill in "$root"/plugins/*/skills/*/; do
  cp -R "${skill%/}" "$dest/"
done
echo "skills instalados en $dest"
