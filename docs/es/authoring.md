# Autoría: agregar o cambiar un skill

## Preparación

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

## Flujo

1. Escribe el skill en `src/skills/<id>/`: `SKILL.md` (para el modelo), `README.md` (para personas), `references/` para el detalle y `examples/` para un resultado real.
2. Agrega un plugin y un asset en `catalog.yml`. Lo compartido se declara en `vendor`; el build lo copia a `references/_shared/`.
3. Genera y verifica:

```
.venv/bin/python scripts/build.py && .venv/bin/python scripts/gen_readme.py
.venv/bin/python scripts/lint.py && .venv/bin/python -m pytest tests/unit -q
.venv/bin/python scripts/smoke_install.py && .venv/bin/python scripts/check_wcag_data.py
claude plugin validate . --strict
```

4. Haz commit de la fuente **y** de lo generado; el CI falla si no coinciden.

Edita solo `src/`, `shared/`, `catalog.yml`, `docs/`, `scripts/` y `tests/`. `plugins/` y `.claude-plugin/` se generan.

## Reglas de un skill

- `name` en kebab-case en inglés, igual al nombre de la carpeta; `description` de máximo 1024 caracteres. Si la descripción contiene `: `, ponla entre comillas (el linter lo detecta).
- `SKILL.md` de menos de 500 líneas; el detalle va en `references/`.
- **Autocontenido:** ningún enlace sale de la carpeta del skill y no hay symlinks. Lo compartido se copia por `vendor`.
- **Solo lectura** salvo que su trabajo sea escribir.
- **Fallar en voz alta:** si falta un insumo, el resultado es "incompleto", nunca "sin hallazgos".
- **Evidencia antes que afirmaciones;** nunca "pasa" por no ver problemas.

## Citar, no copiar

Un criterio se cita con número, nombre, nivel y enlace, y se describe con un resumen propio de máximo 25 palabras. No se pega ni se traduce texto de WCAG ni de NN/g. El linter bloquea términos de trabajo o de flujos internos y `check_wcag_data.py` valida los datos.

## Cómo se prueba un skill

1. **Fixture sembrado** (`tests/fixtures/<nombre>/`): un proyecto ficticio con errores conocidos, partes correctas a propósito (señuelos) y un `expected.yml` con `must_find`, `must_not_flag` y `must_be_manual`.
2. **Informe de ejemplo generado** por un script (`scripts/gen_*_samples.py`) desde los datos oficiales; las pruebas verifican que su evidencia exista en el fixture y que no se edite a mano.
3. **Ejecución real** con `python tests/evals/run_eval.py <skill> <fixture>`: usa tu sesión de Claude Code y compara contra lo esperado. Si el modelo encuentra algo legítimo que el golden no tenía, se añade al golden; si falla algo, se corrige el skill o la herramienta de prueba.

## Versionado y releases

SemVer **por plugin**, en `catalog.yml`. Una etiqueta `<plugin>--vX.Y.Z` dispara el flujo de release: verifica que la versión coincida con el catálogo, ejecuta el linter y las pruebas, crea el zip del skill y publica la Release. Un cambio en `shared/` afecta a todos los skills que lo copian: sube la versión de cada uno.
