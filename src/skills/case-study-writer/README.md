# case-study-writer

Redacta el **caso de estudio** de un proyecto desde sus documentos, **sin inventar nada**: lo que falta queda marcado y cada afirmación cita el documento de donde sale.

## Qué recibes

Tres textos, en español o inglés:

| Texto | Para qué | Extensión |
|---|---|---|
| **Caso completo** | La página pública, con la estructura fija de `case-kit` | hasta unas 2 000 palabras; se ajusta a la evidencia |
| **Resumen de 60 segundos** | Leerlo de un vistazo | 180 a 250 palabras |
| **Blurb de portafolio** | Tarjeta o bio del proyecto | titular y máximo 60 palabras |

Antes de escribir te muestra una **tabla de huecos** (qué evidencia hay y cuál falta por sección) y después de escribir una lista de **cosas por revisar**, por ejemplo incoherencias entre tus propios documentos. Mira un resultado real sobre un proyecto ficticio: [español](examples/sample-output.es.md) · [inglés](examples/sample-output.en.md).

## Qué no hace

- **No inventa** métricas, personas, citas de usuarios ni resultados. Lo que falta sale como `[DATO FALTANTE: ...]`.
- No usa nombres de participantes, empleadores ni datos de contacto de tus notas crudas: las lee para entender el contexto y no las cita.
- No escribe la reflexión por ti: es tu voz. Si no hay material, te la pide.
- No publica ni hace commit. Con `--guardar` escribe en `docs/` y pregunta antes de tocar un archivo con contenido.

## Qué puedes pasarle

- Un proyecto con la estructura de `case-kit` (`docs/brief.md`, `research/`, `prd.md`, `design/`, `testing/`, `accessibility/`, `decisions/`).
- Notas libres (pegadas o en un archivo).
- Informes de `wcag22-audit` o `heuristic-review-es`: toma sus cifras del bloque JSON (conteos, cobertura, brechas honestas) en vez de recalcularlas.

## Cómo se usa

```
/case-study-writer ./mi-proyecto
/case-study-writer ./my-project --idioma en
/case-study-writer ./mi-proyecto --guardar
```

## Cómo se instala

| Ruta | Comando |
|---|---|
| Claude Code (plugin) | `/plugin marketplace add ancardenasc/ux-skills-es` y luego `/plugin install case-study-writer@ux-skills-es` |
| `npx skills` | `npx skills add ancardenasc/ux-skills-es --skill case-study-writer` |
| GitHub CLI | `gh skill install ancardenasc/ux-skills-es case-study-writer` |
| GitHub Copilot | copia la carpeta `plugins/case-study-writer/skills/case-study-writer` a `.github/skills/` de tu proyecto |
| claude.ai | sube el zip `case-study-writer.zip` de la página de Releases |

## Cómo se evalúa a sí mismo

El repositorio incluye un proyecto ficticio ya llenado, con datos parciales a propósito y con trampas (un nombre y un empleador inventados en unas notas crudas). Un comprobador verifica que el caso redactado: respeta los encabezados de la plantilla, cita archivos que existen, no usa ninguna cifra ajena a las fuentes (las derivadas se listan aparte para revisión), deja marcadores donde faltan datos, no filtra datos privados y declara que el proyecto es de muestra.
