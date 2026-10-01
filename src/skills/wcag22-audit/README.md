# wcag22-audit

Audita la accesibilidad web contra **WCAG 2.2, niveles A y AA** (55 criterios) y entrega un informe en español, con evidencia y sin inventar nada.

## Qué recibes

Un informe en Markdown con siete secciones fijas y un bloque JSON al final:

- **Resumen:** veredicto, conteo por gravedad y cobertura calculada (criterios evaluados de los aplicables).
- **Hallazgos:** cada fallo con el criterio (número, nombre, nivel, enlace), dónde está (`archivo:línea` o selector), a quién afecta, cómo corregirlo, y qué tan segura es la conclusión.
- **Verificación manual:** lo que ninguna herramienta puede decidir (lector de pantalla, orden del foco, calidad de textos alternativos), con el procedimiento para comprobarlo.
- **Criterios aprobados**, **brechas honestas** (qué no se pudo revisar y por qué) y **próximos pasos**.

Mira un informe real de ejemplo (sitio ficticio): [español](examples/sample-report.es.md) · [inglés](examples/sample-report.en.md).

## Qué puedes pasarle

| Insumo | Ejemplo de petición | Qué cubre mejor |
|---|---|---|
| **Código o diff** | "Audita la accesibilidad de este PR" | marcado, etiquetas, nombre y rol, estilos de foco, contraste con valores literales |
| **URL** | "Audita https://tu-sitio.example" (necesita una herramienta de navegador) | contraste calculado, foco, reflujo, tamaño de objetivos, nombre accesible |
| **Diseño** | "Revisa este frame de Figma" o una captura | contraste entre colores, tamaño de objetivos, señales solo por color |

Con `--idioma en` (o `output_language: en` en `.ux-skills.yml`) el informe sale en inglés.

## Cómo se instala

| Ruta | Comando |
|---|---|
| Claude Code (plugin) | `/plugin marketplace add ancardenasc/ux-skills-es` y luego `/plugin install wcag22-audit@ux-skills-es` |
| `npx skills` | `npx skills add ancardenasc/ux-skills-es --skill wcag22-audit` |
| GitHub CLI | `gh skill install ancardenasc/ux-skills-es wcag22-audit` |
| GitHub Copilot | copia la carpeta `skills/wcag22-audit` a `.github/skills/` de tu proyecto |
| claude.ai | sube el zip `wcag22-audit.zip` de la página de Releases |

## Qué no hace

- No corrige código ni edita archivos.
- No es una declaración de conformidad ni un dictamen legal, y no reemplaza las pruebas con personas usuarias y lectores de pantalla reales.
- No cubre el nivel AAA.
- No ejecuta acciones con efectos: no envía formularios con datos reales, no inicia sesión por ti.
- Nunca carga `axe` desde un CDN: solo lo usa si ya está en tu proyecto o si lo apruebas.

## Cómo se evalúa a sí mismo

El repositorio incluye un sitio ficticio con violaciones sembradas y señuelos correctos (`tests/fixtures/html-seeded`), y una lista de resultados esperados. Las pruebas comprueban que el informe de ejemplo encuentra todo lo sembrado, no marca los señuelos y deja como verificación manual lo que corresponde.

## Atribución

Los criterios son de WCAG 2.2 (W3C). Este skill cita número, nombre, nivel y enlace, y usa resúmenes propios; no reproduce ni traduce el texto de la especificación. Ver [NOTICE](../../../NOTICE.md).
