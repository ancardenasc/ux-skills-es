# Productos

Cuatro skills independientes. Cada uno funciona solo; los de auditoría comparten el formato de informe.

| Producto | Qué hace | Qué le pasas | Qué recibes |
|---|---|---|---|
| **`wcag22-audit`** | Audita accesibilidad web contra WCAG 2.2 A y AA (55 criterios) | Código o diff, una URL, un diseño de Figma o capturas | Informe con hallazgos por gravedad, verificación manual, aprobados, brechas honestas y un bloque JSON |
| **`heuristic-review-es`** | Revisión heurística de usabilidad con las 10 heurísticas de Nielsen | Código, URL o diseño, y la tarea que hace la persona | El mismo formato de informe, con una tabla de las 10 heurísticas |
| **`case-kit`** | Crea la estructura de un caso de estudio en 10 fases | Una carpeta destino y el nombre del proyecto | Carpeta con brief, investigación, PRD, diseño, pruebas, accesibilidad y plantilla del caso (es o en) |
| **`case-study-writer`** | Redacta el caso de estudio desde tus documentos | La carpeta de `case-kit`, notas libres e informes de auditoría | Caso completo, resumen de 60 segundos y blurb, con citas y datos faltantes marcados |

## Cómo se combinan

1. `case-kit` crea la estructura del proyecto.
2. Construyes el proyecto y guardas las auditorías (`wcag22-audit`, `heuristic-review-es`) en `docs/accessibility/` y `docs/testing/`.
3. `case-study-writer` redacta el caso desde lo que llenaste.

No es obligatorio usar los cuatro: las auditorías sirven en cualquier proyecto, no solo en portafolio.

## Cuándo usar cuál

- **"¿Mi interfaz cumple WCAG?"** → `wcag22-audit`.
- **"¿Mi flujo se entiende y se puede usar?"** → `heuristic-review-es` (y `wcag22-audit` para lo técnico: son complementarios, no sustitutos).
- **"Voy a documentar un proyecto de portafolio."** → `case-kit`, luego `case-study-writer`.

## Ejemplos reales

Cada skill trae un ejemplo de su resultado, generado sobre proyectos ficticios y verificado por las pruebas del repositorio:

- [`wcag22-audit`](../../src/skills/wcag22-audit/examples/sample-report.es.md)
- [`heuristic-review-es`](../../src/skills/heuristic-review-es/examples/sample-report.es.md)
- [`case-study-writer`](../../src/skills/case-study-writer/examples/sample-output.es.md)
