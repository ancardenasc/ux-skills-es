---
name: wcag22-audit
description: Audita la accesibilidad web contra WCAG 2.2 niveles A y AA a partir de código o un diff, una URL o un diseño (Figma o capturas). Entrega un informe en español con hallazgos priorizados y evidencia (archivo:línea, selector, medida), los criterios que requieren prueba manual, las brechas honestas y un bloque JSON. Úsalo cuando pidan auditar accesibilidad, revisar WCAG, contraste, teclado, foco, lectores de pantalla o la accesibilidad de un PR. No corrige código ni certifica conformidad.
argument-hint: "[ruta | diff | URL | enlace de Figma] [--idioma es|en]"
license: MIT
---

# wcag22-audit

Audita accesibilidad web contra **WCAG 2.2, niveles A y AA** (55 criterios) y entrega un informe con evidencia. Es de **solo lectura**: no edita archivos, no envía formularios y no certifica conformidad.

## Antes de empezar

- **Idioma del informe:** `--idioma es|en` en la petición, o `output_language` en `.ux-skills.yml` de la raíz del proyecto, o el idioma de la petición; por defecto `es`.
- **Archivos de apoyo** (junto a este archivo, ya copiados en `references/_shared/`):
  - Datos de los 55 criterios: [`wcag22-criteria.json`](references/_shared/wcag22-criteria.json). Cada criterio trae id, nombre, nivel, enlace y qué tanto se puede evaluar en cada modo (`assessable`).
  - Formato del informe: [es](references/_shared/report-format.es.md) · [en](references/_shared/report-format.en.md). Plantilla: [es](references/_shared/report.es.md) · [en](references/_shared/report.en.md). Etiquetas: [`labels.yml`](references/_shared/labels.yml). Esquema del bloque JSON: [`report.schema.json`](references/_shared/report.schema.json).
  - Gravedad y confianza: [es](references/_shared/severity-and-confidence.es.md) · [en](references/_shared/severity-and-confidence.en.md).
  - Modos de entrada: [es](references/_shared/input-modes.es.md) · [en](references/_shared/input-modes.en.md).
  - Brechas honestas: [es](references/_shared/honest-gaps.es.md) · [en](references/_shared/honest-gaps.en.md).
  - Reglas de citas y derechos de autor: [`legal-copyright-rules.md`](references/_shared/legal-copyright-rules.md). **Léelas: no copies ni traduzcas el texto de WCAG.**
- **Informe de ejemplo** (formato exacto a seguir): [es](examples/sample-report.es.md) · [en](examples/sample-report.en.md).
- Lee solo la variante del idioma elegido.

## Pasos

### 1. Detecta capacidades y elige el modo

Sigue [modos de entrada](references/_shared/input-modes.es.md). Determina qué te dieron (ruta o diff, URL, diseño) y qué herramientas hay (navegador, Figma, `axe` ya instalado, `python3`). Si falta algo que cambiaría el resultado, dilo; no adivines.

- **Código o diff** (modo A): lee [verificaciones en código](references/checks-code.md).
- **URL** (modo B): lee [verificaciones en una página real](references/checks-url.md). Sin navegador, pide HTML o capturas.
- **Diseño** (modo C): lee [verificaciones en diseño](references/checks-design.md).
- Si combinas modos, el modo del informe es `mixed` y cada hallazgo declara su método.

### 2. Delimita el alcance

Qué archivos, páginas, estados o frames entran. Para un diff usa el working tree contra el merge-base (`git diff $(git merge-base <rama-base> HEAD)`), que incluye lo no commiteado; `base...HEAD` compara solo commits y saldría vacío. Si el diff no toca frontend, responde "no aplica" y explica por qué. Nunca apruebes por un diff vacío.

### 3. Recoge evidencia y evalúa por principios

Recorre los criterios A y AA por principio (Perceptible, Operable, Comprensible, Robusto). Para cada criterio consulta `assessable` en el JSON de datos:

- `yes` o `partial` en tu modo: evalúalo con la guía del modo. Con `partial`, lo que no puedas decidir va a `manual`.
- `no` en tu modo: `not_tested` (y a las brechas) o `manual` si hay un procedimiento claro para comprobarlo.
- Si el criterio no puede aplicar (por ejemplo, no hay video para 1.2.x): `not_applicable`.

### 4. Clasifica cada criterio

- `fail`: hay evidencia directa. Exige `archivo:línea` o selector, medida si corresponde, y una recomendación concreta.
- `pass`: lo verificaste con evidencia. No declares `pass` por ausencia de problemas visibles.
- `manual`: no se puede decidir en este modo (lector de pantalla, calidad de textos alternativos, orden del foco sin runtime…). Incluye `manual_check` con motivo y procedimiento.
- `not_tested`: no se miró porque el modo no tiene el dato.
- Asigna **gravedad por impacto** y **confianza** con su techo por método (ver gravedad y confianza). Con una sola evidencia estática, la confianza no pasa de `medium`.

### 5. Escribe el informe

Usa la plantilla del idioma: siete secciones con sus marcadores `<!-- section:id -->`, el pie legal y, al final, un único bloque `json ux-skills-findings` que valida contra el esquema. El Markdown y el JSON deben decir lo mismo. La cobertura (evaluados / aplicables) se calcula contando los hallazgos; no la estimes. Describe cada criterio con palabras propias.

### 6. Autoverificación antes de entregar

- [ ] Hay exactamente un bloque JSON y es válido según el esquema.
- [ ] Todo `fail` tiene evidencia real (nada inventado) y recomendación.
- [ ] Nombre, nivel y enlace de cada criterio salen del JSON de datos, sin retocar.
- [ ] La gravedad solo está en los `fail`; la confianza respeta el techo del método.
- [ ] Todo lo que no pudiste decidir está en `manual` o `not_tested`, nunca en `pass`.
- [ ] Las brechas honestas no están vacías y la cobertura coincide con el conteo.
- [ ] El pie legal está presente y no copiaste ni tradujiste texto de WCAG.

## Límites

- Solo niveles A y AA de WCAG 2.2. AAA y las técnicas de la especificación quedan fuera.
- No sustituye pruebas con personas usuarias ni con lectores de pantalla reales.
- No es una declaración de conformidad ni un dictamen legal.
- No ejecutes acciones con efectos: no envíes formularios con datos reales, no compres, no inicies sesión con credenciales que no te dieron, no dispares diálogos del navegador.
- **axe:** úsalo solo si ya está en el proyecto o la persona aprueba una ejecución local con `npx`. Nunca lo cargues desde un CDN.
