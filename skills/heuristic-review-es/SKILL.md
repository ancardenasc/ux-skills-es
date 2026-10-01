---
name: heuristic-review-es
description: Revisión heurística de usabilidad en español con las 10 heurísticas de Nielsen, a partir de código, una URL o un diseño (Figma o capturas). Recorre las tareas principales, evalúa cada heurística con evidencia y entrega un informe con hallazgos priorizados, verificación manual y brechas honestas. Úsalo cuando pidan revisar usabilidad, evaluar un flujo, heurísticas de Nielsen, revisión de UX o detectar problemas de experiencia en una pantalla. No cubre accesibilidad técnica ni reemplaza pruebas con personas.
argument-hint: "[ruta | diff | URL | enlace de Figma] [--tarea \"qué hace la persona\"] [--idioma es|en]"
license: MIT
---

# heuristic-review-es

Revisión heurística de usabilidad con las **10 heurísticas de Nielsen**. Es juicio experto sobre tareas concretas: encuentra problemas probables, no mide cómo se comportan las personas. **Solo lectura**: no edita nada.

## Antes de empezar

- **Idioma:** `--idioma es|en`, o `output_language` en `.ux-skills.yml`, o el idioma de la petición; por defecto `es`.
- **Archivos de apoyo** (ya copiados en `references/_shared/`):
  - Datos de las 10 heurísticas: [`nielsen-heuristics.json`](references/_shared/nielsen-heuristics.json) (id, nombre oficial, enlace, etiqueta propia, qué se evalúa en cada modo).
  - Formato del informe: [es](references/_shared/report-format.es.md) · [en](references/_shared/report-format.en.md). Plantilla: [es](references/_shared/report.es.md) · [en](references/_shared/report.en.md). Etiquetas: [`labels.yml`](references/_shared/labels.yml). Esquema JSON: [`report.schema.json`](references/_shared/report.schema.json).
  - Gravedad y confianza: [es](references/_shared/severity-and-confidence.es.md) · [en](references/_shared/severity-and-confidence.en.md).
  - Modos de entrada: [es](references/_shared/input-modes.es.md) · [en](references/_shared/input-modes.en.md).
  - Brechas honestas: [es](references/_shared/honest-gaps.es.md) · [en](references/_shared/honest-gaps.en.md).
  - Derechos de autor: [`legal-copyright-rules.md`](references/_shared/legal-copyright-rules.md). **Léelo: no copies ni traduzcas el texto de Nielsen / NN/g.**
- **Guía de método y de cada heurística:** [guía de heurísticas](references/heuristics-guide.md). Léela completa.
- **Informe de ejemplo** (formato exacto): [es](examples/sample-report.es.md) · [en](examples/sample-report.en.md).

## Pasos

### 1. Define la tarea y detecta el modo

Pregunta o deduce **2 o 3 tareas principales** de quien usa el producto (por ejemplo "hacer y confirmar un pedido"). Sin tarea no hay revisión heurística útil. Detecta el modo según [modos de entrada](references/_shared/input-modes.es.md): código o diff, URL (necesita navegador) o diseño. Declara el modo y las herramientas en el alcance.

### 2. Recorre cada tarea

Sigue el flujo paso a paso (en código, leyendo el marcado y los manejadores; en URL, navegando sin enviar datos reales; en diseño, siguiendo los frames). Anota en cada paso qué ve y qué puede hacer la persona.

### 3. Evalúa H1 a H10

Para cada heurística consulta `assessable` en el JSON de datos y usa la guía:

- `yes` o `partial` en tu modo: evalúala con evidencia (`archivo:línea`, selector o frame).
- `no` en tu modo, o si requiere observar uso real: `manual` o `not_tested`.
- Una heurística puede tener un `fail` y un `pass` a la vez en lugares distintos; reporta ambos.

### 4. Aplica las lentes de contexto (opcional)

La guía incluye lentes de contexto propias para productos en español (registro, formatos locales, claridad del texto, conectividad). Úsalas como pistas dentro de la heurística que corresponda (H2, H4, H9…); **no son parte de las heurísticas de NN/g** y se rotulan "propuesta propia".

### 5. Clasifica

- `fail`: hay evidencia concreta de un problema. Requiere evidencia, gravedad y recomendación accionable.
- `pass`: lo verificaste con evidencia de que se hace bien. No declares `pass` por no ver problemas.
- `manual`: no se puede decidir en este modo (ritmo, atajos reales, comprensión del texto).
- `not_tested`: el modo no tiene el dato.
- **Gravedad por impacto** según la rúbrica compartida. **Confianza** con el techo del método: leer código no pasa de `medium`.
- Si varios hallazgos comparten causa, agrúpalos en uno y cita todas las evidencias.

### 6. Escribe el informe

Usa la plantilla del idioma (siete secciones con marcadores y un único bloque `json ux-skills-findings`). En el **Resumen** añade la tabla de las 10 heurísticas con estado y número de hallazgos, como en el ejemplo. En el JSON: `criterion.system` es `NIELSEN`, `criterion.id` es `H1` a `H10`, **`criterion.name` es el `name_en` exacto del archivo de datos** (en inglés) y no se usa `level`. En el Markdown en español escribe `id name_en (label_es)`. La cobertura se calcula contando heurísticas distintas, cada una una vez; no la estimes.

### 7. Autoverificación

- [ ] Un solo bloque JSON válido; `system: NIELSEN`, ids `H1`–`H10`, `name` y `url` copiados sin traducir.
- [ ] Todo `fail` tiene evidencia real y una recomendación concreta; nada inventado.
- [ ] Gravedad solo en `fail`; confianza dentro del techo del método.
- [ ] Lo que exige observar personas o ejecutar el flujo está en `manual` o `not_tested`.
- [ ] La tabla de heurísticas y los conteos coinciden con los hallazgos; la cobertura cuenta cada heurística una vez; las brechas honestas no están vacías.
- [ ] No copiaste ni tradujiste texto de NN/g y el pie legal está presente.

## Límites

- Una sola persona evaluadora (tú) encuentra solo una parte de los problemas. Dilo en las brechas.
- No sustituye las pruebas de usabilidad con personas usuarias.
- No evalúa accesibilidad técnica: para eso usa `wcag22-audit`.
- No ejecutes acciones con efectos: no envíes formularios con datos reales, no compres ni inicies sesión con credenciales que no te dieron.
