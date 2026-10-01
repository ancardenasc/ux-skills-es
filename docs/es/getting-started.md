# Primeros pasos

Cada skill se instala por separado. Elige la ruta que use tu herramienta.

## 1. Instalar

| Ruta | Un skill | Todos |
|---|---|---|
| **Claude Code (plugin)** | `/plugin install wcag22-audit@ux-skills-es` | agrega el marketplace una vez: `/plugin marketplace add ancardenasc/ux-skills-es` y luego instala cada plugin |
| **`npx skills`** | `npx skills add ancardenasc/ux-skills-es --skill wcag22-audit` | `npx skills add ancardenasc/ux-skills-es --all` |
| **GitHub CLI** | `gh skill install ancardenasc/ux-skills-es wcag22-audit` | `gh skill install ancardenasc/ux-skills-es --all` |
| **GitHub Copilot** | copia `plugins/<id>/skills/<id>` a `.github/skills/` | `scripts/install.sh copilot /ruta/a/tu/proyecto` |
| **claude.ai** | sube el zip `<id>.zip` de la página de Releases | |
| **Claude Code sin plugin** | copia la carpeta a `.claude/skills/` | `scripts/install.sh claude /ruta/a/tu/proyecto` |

Los plugins de Claude Code se invocan con su espacio de nombres: `/wcag22-audit:wcag22-audit`. Si copias los archivos a `.claude/skills/`, el nombre es corto: `/wcag22-audit`.

## 2. Tu primera auditoría

```
/wcag22-audit:wcag22-audit ./src --idioma es
```

El skill detecta qué tienes (código, URL, diseño) y qué herramientas hay (navegador, Figma), declara el modo en el alcance y entrega un informe con hallazgos, verificación manual y brechas honestas. Ver [esquema del informe](report-schema.md).

Otros ejemplos:

```
/heuristic-review-es:heuristic-review-es ./flujo-de-pedido --tarea "hacer un pedido"
/case-kit:case-kit ./mi-proyecto "Nombre del proyecto"
/case-study-writer:case-study-writer ./mi-proyecto
```

## 3. Configuración opcional

Un archivo `.ux-skills.yml` en la raíz de tu proyecto:

```yaml
output_language: es      # es | en; por defecto, el idioma de tu petición
default_branch: main     # rama base para los diffs
frontend_globs: ["**/*.{vue,jsx,tsx,html,css,scss}"]
```

Todo es opcional. Sin archivo, los skills deducen lo necesario y preguntan si hay dudas.

## 4. Qué esperar

- Los informes **citan evidencia** (`archivo:línea`, selector, medida) y dicen qué **no** pudieron revisar.
- Lo que ninguna herramienta puede decidir (lector de pantalla, orden del foco sin ejecutar) queda como **verificación manual**, nunca como "pasa".
- Los skills de auditoría son de **solo lectura**: no editan archivos ni envían formularios.

Siguiente: [productos](products.md).
