---
name: case-kit
description: Genera la estructura de carpetas y documentos de un caso de estudio de portafolio en 10 fases (encuadre, investigación, definición, diseño, validación, construcción, QA de accesibilidad, lanzamiento, medición y narración), en español o inglés. Úsalo al empezar un proyecto de muestra de portafolio o cualquier proyecto que necesite documentación por fases. Solo invocación manual.
argument-hint: "<carpeta-destino> [nombre-del-proyecto] [--idioma es|en]"
disable-model-invocation: true
license: MIT
---

# case-kit

Crea en una carpeta nueva la estructura de un caso de estudio de portafolio en 10 fases, lista para llenar.

## Uso

`/case-kit <carpeta-destino> [nombre-del-proyecto] [--idioma es|en]`

- `carpeta-destino`: dónde crear el proyecto. Se crea si no existe. Si no te la dieron, **pregúntala antes de escribir nada**.
- `nombre-del-proyecto`: se inserta en el título de `docs/case-study.md` y en el del `README.md`. Pregúntalo si falta.
- `--idioma`: `es` (por defecto) o `en`. Elige la plantilla que se copia.

## Pasos

1. Elige la plantilla del idioma: `template/es/` o `template/en/`, junto a este archivo (en Claude Code: `${CLAUDE_SKILL_DIR}/template/<idioma>/`).
2. Copia todo su contenido a `carpeta-destino` conservando la estructura, **incluidos los archivos ocultos** (`.gitignore`, `.github/ISSUE_TEMPLATE/`, los `.gitkeep`).
3. Si diste un nombre, reemplaza el marcador `[Nombre del proyecto]` (o `[Project name]`) en `docs/case-study.md` y el título de la primera línea del `README.md` (`# Blueprint de portafolio` o `# Portfolio Blueprint`). Deja el resto del README intacto: es la guía de fases.
4. En `LICENSE`, reemplaza el año por el actual (`date +%Y`, sin preguntar) y `[Tu nombre]` o `[Your Name]` por el nombre de quien autoriza el proyecto; pregúntalo solo si no lo sabes.
5. **No sobrescribas** archivos que ya existan en `carpeta-destino`: lista cuáles omitiste.
6. Resume qué se creó y recuerda el orden: llenar `docs/brief.md` (Fase 0) antes que nada, y no avanzar de fase sin cumplir su criterio "Hecho cuando".

## Qué crea

`README.md` (guía de fases), `LICENSE`, `CHANGELOG.md`, `.gitignore`, `.github/ISSUE_TEMPLATE/accessibility.md`, `docs/` con `brief.md`, `prd.md`, `case-study.md`, `decisions/` (plantilla de ADR), `research/`, `design/`, `testing/` y `accessibility/`, y las carpetas `src/` y `tests/` con un `.gitkeep`.

## No hagas

- No inicialices git, no hagas commit y no crees repositorios remotos: eso lo decide quien usa el skill.
- No borres ni sobrescribas contenido existente sin avisar.
- No rellenes los documentos con datos inventados: las plantillas deben quedar vacías para que las llene la persona.

## Siguiente paso

Cuando los documentos estén llenos, el skill `case-study-writer` puede redactar el caso de estudio desde ellos.
