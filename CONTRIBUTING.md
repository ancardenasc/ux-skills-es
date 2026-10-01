# Contribuir

1. Escribe el skill en `src/skills/<id>/` (SKILL.md para el modelo, README.md para personas) y agrégalo a `catalog.yml`.
2. `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
3. Ejecuta los comandos de [AGENTS.md](AGENTS.md).
4. Haz commit de lo generado junto con la fuente; el CI falla si no coinciden.
