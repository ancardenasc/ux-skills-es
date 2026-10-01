# Estructura del caso de estudio

Sigue la plantilla de `case-kit` (`docs/case-study.md`). Encabezados exactos y en este orden. Debe leerse en 60 s (vistazo) y en 10 min (lectura completa).

| Encabezado | Qué va | Fuentes habituales |
|---|---|---|
| `# Caso de estudio: <nombre>` | Título; aviso de proyecto de muestra si aplica | `docs/brief.md` |
| `## Contexto y rol` | Qué es el proyecto, tu rol exacto, con quién trabajaste, duración | `docs/brief.md`; el rol y la duración los dice la persona |
| `## Problema` | El problema real en 2 o 3 frases, apoyado en el insight | `docs/brief.md`, `docs/research/` |
| `## Proceso` con `### Investigación`, `### Diseño`, `### Validación`, `### Construcción` | Qué se hizo en cada etapa, con enlace al documento | `docs/research/`, `docs/design/`, `docs/testing/`, `docs/prd.md` |
| `## Decisiones clave` | Tabla: decisión, alternativas consideradas, por qué esta | `docs/decisions/` |
| `## Resultado` | Métricas del brief, antes contra después, con sus límites | `docs/brief.md` (metas), `docs/testing/` |
| `## Accesibilidad` | Nivel alcanzado, cifras del informe y brechas conocidas | `docs/accessibility/` |
| `## Reflexión` | Qué salió mal, qué cambiarías, qué aprendiste | la persona; notas de retrospectiva |
| `## Enlaces` | Demo, repositorio, Figma, informe de accesibilidad | las fuentes; si no hay, `DATO FALTANTE` |

## Notas por sección
- **Resultado:** compara con las metas del brief (cumplida, no cumplida, sin medir). Lo no medido va como `DATO FALTANTE`.
- **Accesibilidad:** usa los conteos del bloque JSON del informe (fallos por gravedad, cobertura) y reproduce sus brechas honestas; no las suavices. Indica a qué versión del proyecto corresponde el informe.
- **Enlaces:** solo los que figuran en las fuentes. Un enlace "pendiente" es un dato faltante.
