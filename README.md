# ux-skills-es

[![validate](https://github.com/ancardenasc/ux-skills-es/actions/workflows/validate.yml/badge.svg)](https://github.com/ancardenasc/ux-skills-es/actions/workflows/validate.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![skills](https://img.shields.io/badge/skills-4-blue)
![tools](https://img.shields.io/badge/Claude%20Code%20%2B%20Copilot-compatible-8A63D2)
![docs](https://img.shields.io/badge/docs-ES%20%7C%20EN-lightgrey)

**Skills de UX y accesibilidad en español para Claude Code y GitHub Copilot.** Auditan accesibilidad con WCAG 2.2, revisan usabilidad con las heurísticas de Nielsen y ayudan a documentar un caso de estudio, **con evidencia, sin inventar nada y diciendo lo que no pudieron revisar**. Cada uno se instala por separado.

[Read in English](README.en.md)

## Por qué existe

La mayoría de las herramientas de auditoría con IA están en inglés y entregan listas de problemas sin decir qué tan seguros están ni qué se quedó sin mirar. Estas:

- **Dan evidencia:** cada fallo trae `archivo:línea`, selector o medida, y una recomendación concreta.
- **Dicen lo que no saben:** lo que ninguna herramienta puede decidir (lector de pantalla, orden del foco) queda como verificación manual, nunca como "pasa", y cada informe termina con sus brechas honestas.
- **No inventan:** `case-study-writer` marca lo que falta como dato faltante y cita el documento de cada afirmación.
- **Están en español primero**, con salida configurable a inglés.
- **Se prueban:** corren sobre proyectos ficticios con errores sembrados y partes correctas a propósito, y el CI verifica que encuentren lo esperado sin marcar lo correcto.

## Skills

<!-- catalog:start -->
| Skill | Qué hace | Instalar |
|---|---|---|
| [`wcag22-audit`](src/skills/wcag22-audit/README.md) | Audita accesibilidad web contra WCAG 2.2 A y AA desde código, URL o diseño; informe en español con evidencia, prueba manual y brechas honestas. | `/plugin install wcag22-audit@ux-skills-es` |
| [`heuristic-review-es`](src/skills/heuristic-review-es/README.md) | Revisión heurística de usabilidad con las 10 heurísticas de Nielsen desde código, URL o diseño; informe en español con evidencia y brechas honestas. | `/plugin install heuristic-review-es@ux-skills-es` |
| [`case-kit`](src/skills/case-kit/README.md) | Genera la estructura de un caso de estudio de portafolio en 10 fases (brief, investigación, PRD, diseño, pruebas, accesibilidad, caso), en español o inglés. | `/plugin install case-kit@ux-skills-es` |
| [`case-study-writer`](src/skills/case-study-writer/README.md) | Redacta el caso de estudio de un proyecto (completo, de 60 segundos y blurb) desde sus documentos y auditorías, sin inventar métricas, con citas y datos faltantes marcados. | `/plugin install case-study-writer@ux-skills-es` |
<!-- catalog:end -->

Cada skill tiene su propio README con ejemplos y un informe de muestra. Otras formas de instalar (`npx skills`, `gh skill`, GitHub Copilot, claude.ai) están en [primeros pasos](docs/es/getting-started.md).

## Un informe, de verdad

Extracto del informe de muestra de `wcag22-audit` sobre un sitio ficticio (código fuente en `tests/fixtures/html-seeded`):

> ### Crítico: El botón de suscripción es un div sin rol ni teclado
>
> - **Criterio:** 4.1.2 Name, Role, Value (Nombre), nivel A, https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html
> - **Dónde:** `index.html:25`
> - **Confianza:** Media, método: static_code
> - **Cómo corregirlo:** Usar un <button type="submit"> con el mismo texto visible.

Informe completo: [español](src/skills/wcag22-audit/examples/sample-report.es.md) · [inglés](src/skills/wcag22-audit/examples/sample-report.en.md).

## Cómo encajan

```
case-kit  →  (construyes el proyecto)  →  wcag22-audit + heuristic-review-es  →  case-study-writer
 estructura                                 auditorías con evidencia                 caso, 60 s y blurb
```

No hace falta usar los cuatro: las auditorías sirven en cualquier proyecto. Ver [productos](docs/es/products.md).

## Configuración

Opcional: un `.ux-skills.yml` en la raíz de tu proyecto.

```yaml
output_language: es      # es | en
default_branch: main
frontend_globs: ["**/*.{vue,jsx,tsx,html,css,scss}"]
```

## Lo que no hacen

No certifican conformidad ni dan dictamen legal, no sustituyen las pruebas con personas ni con lectores de pantalla reales, no corrigen código y no evalúan el nivel AAA. Qué está verificado y qué no, sin adornos: [límites y honestidad](docs/es/limits-and-honesty.md).

## Documentación

[Primeros pasos](docs/es/getting-started.md) · [Productos](docs/es/products.md) · [Esquema del informe](docs/es/report-schema.md) · [Autoría](docs/es/authoring.md) · [Límites y honestidad](docs/es/limits-and-honesty.md)

## Derechos de autor

WCAG es del W3C y las heurísticas, de Jakob Nielsen (Nielsen Norman Group). Este repositorio cita número, nombre, nivel y enlace con resúmenes propios, y no copia ni traduce sus textos. Ver [NOTICE](NOTICE.md).

## Seguridad

Los skills pueden usar herramientas (shell, git, navegador). Léelos antes de instalarlos y guarda tus tokens en tu propia configuración, nunca aquí. Ver [SECURITY.md](SECURITY.md).

## Contribuir y licencia

Ver [CONTRIBUTING.md](CONTRIBUTING.md) y [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). MIT, (c) 2026 Nicolas Cardenas.
