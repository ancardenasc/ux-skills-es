# AGENTS.md

Colección de skills de UX y accesibilidad en español, instalables por separado (Claude Code y GitHub Copilot).

- Edita solo `src/`, `shared/`, `catalog.yml`, `docs/` y `scripts/`. `skills/`, `plugins/`, `.claude-plugin/` y las tablas de los README se generan.
- Tras cualquier cambio: `.venv/bin/python scripts/build.py && .venv/bin/python scripts/gen_readme.py && .venv/bin/python scripts/lint.py && .venv/bin/python -m pytest tests/unit -q && .venv/bin/python scripts/smoke_install.py`.
- Cada skill es autocontenido: nada de enlaces fuera de su carpeta ni symlinks. Lo compartido vive en `shared/` y se copia a `references/_shared/` por `build.py`.
- Nombres en kebab-case en inglés, iguales al nombre de la carpeta. SKILL.md de menos de 500 líneas; el detalle va en `references/`.
- Informes y textos para personas en español primero, con salida configurable a inglés.
- Nunca se copia ni se traduce texto de WCAG ni de Nielsen/NN/g: se cita número, nombre, nivel y enlace, con resumen propio de máximo 25 palabras.
- Nada de datos de empresas ni flujos internos de trabajo; el linter bloquea términos conocidos.
