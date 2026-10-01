# Blueprint de portafolio

Plantilla reutilizable para construir cada proyecto de muestra de un portafolio de UX, ingeniería y accesibilidad. Convierte un proceso de 10 fases en carpetas y documentos.

## Cómo usar

1. Copia este directorio como base de un proyecto nuevo (o genéralo con el skill `case-kit`).
2. Sigue las fases 0 a 9 en orden, llenando cada archivo de `docs/`.
3. No avances de fase sin cumplir el criterio "Hecho cuando" de la anterior (está en cada plantilla).
4. Al final, `docs/case-study.md` se convierte en la página pública del caso. El skill `case-study-writer` puede redactarlo desde lo que llenaste.

## Fases y entregables

| Fase | Carpeta o archivo | Hecho cuando |
|---|---|---|
| 0 Encuadre | `docs/brief.md` | Brief, métricas de éxito y licencias listadas |
| 1 Investigación | `docs/research/` | Guion, síntesis anonimizada e insights numerados |
| 2 Definición | `docs/prd.md` | PRD corto que traza insight, requisito y criterio |
| 3 Diseño | `docs/design/` | Figma o PDF con Research, Flows, Wireframes, UI, Components, A11y y Handoff |
| 4 Validación | `docs/testing/` | Informe de usabilidad con hallazgos y antes/después |
| 5 Construcción | `src/`, `tests/`, `.github/workflows/` | CI en verde, pruebas y demo desplegada |
| 6 QA de accesibilidad | `docs/accessibility/` | Informes de auditoría y declaración de accesibilidad |
| 7 Lanzamiento | - | URL pública estable y etiqueta `v1.0.0` |
| 8 Medición | `docs/case-study.md` (sección Resultado) | Números reales de antes y después |
| 9 Narración | `docs/case-study.md` y este README | Caso comprensible en 60 s y en 10 min |

## Reglas transversales

- Si un dato de investigación o una métrica viene de un proyecto de muestra (no de un cliente real), márcalo explícitamente. Nunca inventes personas ni números.
- Las personas participantes en pruebas deben ser reales (con 5 alcanza) y dar su consentimiento por escrito.
- Solo licencias OFL, MIT, CC0 o contenido propio para fuentes, iconos e imágenes.
- Sin datos personales de terceros, sin menores identificables y sin material de empleadores.
- Un ADR (`docs/decisions/NNNN-titulo.md`) por cada decisión de arquitectura o diseño relevante.

## Definición de terminado: "listo para portafolio"

- [ ] Demo pública estable y accesible
- [ ] README completo, LICENSE y CI en verde
- [ ] Figma público o PDF con el proceso
- [ ] Informe de accesibilidad con brechas honestas (no solo lo que salió bien)
- [ ] Caso de estudio publicado con evidencia enlazada
- [ ] Sin material de terceros ni de empleadores
