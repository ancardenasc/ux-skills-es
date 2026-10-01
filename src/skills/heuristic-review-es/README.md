# heuristic-review-es

Revisión heurística de usabilidad en español con las **10 heurísticas de Nielsen**. Recorre tus tareas principales, evalúa cada heurística con evidencia y entrega un informe priorizado, sin inventar nada.

## Qué recibes

El mismo formato de informe que `wcag22-audit` (siete secciones y un bloque JSON), con una **tabla de las 10 heurísticas** en el resumen: estado y número de hallazgos por cada una.

- **Hallazgos:** qué heurística se rompe, dónde (`archivo:línea`, selector o frame), a quién afecta, cómo corregirlo y qué tan segura es la conclusión.
- **Verificación manual:** lo que solo se aprecia observando personas o ejecutando el flujo (atajos reales, ritmo, comprensión).
- **Brechas honestas:** qué no se pudo revisar y por qué.

Mira un informe de ejemplo (flujo ficticio): [español](examples/sample-report.es.md) · [inglés](examples/sample-report.en.md).

## Qué puedes pasarle

| Insumo | Ejemplo | Cómo se aprovecha |
|---|---|---|
| **Código o diff** | "Revisa la usabilidad de este flujo de pedido" | señales en el marcado y los manejadores; mucho queda como verificación manual |
| **URL** | "Revisa https://tu-sitio.example, tarea: reservar una mesa" (necesita navegador) | recorrido real del flujo, sin enviar datos |
| **Diseño** | "Revisa estos frames de Figma" o capturas | consistencia, jerarquía, claridad de textos |

Conviene decirle la tarea que hace la persona (`--tarea "..."`); sin tarea, el skill propone dos o tres y las confirma contigo.

## Cómo se instala

| Ruta | Comando |
|---|---|
| Claude Code (plugin) | `/plugin marketplace add ancardenasc/ux-skills-es` y luego `/plugin install heuristic-review-es@ux-skills-es` |
| `npx skills` | `npx skills add ancardenasc/ux-skills-es --skill heuristic-review-es` |
| GitHub CLI | `gh skill install ancardenasc/ux-skills-es heuristic-review-es` |
| GitHub Copilot | copia la carpeta `skills/heuristic-review-es` a `.github/skills/` de tu proyecto |
| claude.ai | sube el zip `heuristic-review-es.zip` de la página de Releases |

## Qué no hace

- No sustituye las pruebas de usabilidad con personas usuarias: una revisión heurística es juicio experto y una sola persona evaluadora encuentra solo parte de los problemas.
- No evalúa accesibilidad técnica; para eso está `wcag22-audit`.
- No edita código ni envía formularios con datos reales.

## Atribución

Las 10 heurísticas son de Jakob Nielsen (Nielsen Norman Group). Este skill cita su nombre oficial con un enlace a la fuente y usa redacción propia; no reproduce ni traduce los textos de NN/g. Las "lentes de contexto" son una propuesta propia y no forman parte de las heurísticas. Ver [NOTICE](../../../NOTICE.md).
