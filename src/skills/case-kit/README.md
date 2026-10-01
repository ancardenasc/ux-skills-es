# case-kit

Crea de un solo comando la estructura de un **caso de estudio de portafolio en 10 fases**, lista para llenar: de la idea a la narración final. Disponible en español e inglés.

## Qué recibes

Una carpeta nueva con:

```
README.md                  guía de las 10 fases y la definición de "listo para portafolio"
LICENSE  CHANGELOG.md  .gitignore
.github/ISSUE_TEMPLATE/accessibility.md
docs/
  brief.md                 Fase 0: encuadre, métricas, licencias y ética
  research/                Fase 1: investigación
  prd.md                   Fase 2: definición
  design/                  Fase 3: diseño
  testing/                 Fase 4: validación
  accessibility/           Fase 6: QA y conformidad
  decisions/               ADR de decisiones relevantes
  case-study.md            Fases 8 y 9: el caso que se publica
src/  tests/
```

Cada plantilla trae su criterio "Hecho cuando" y reglas de honestidad: nada de personas ni números inventados, consentimiento por escrito, solo licencias permitidas, sin material de empleadores.

## Cómo se usa

```
/case-kit ./mi-proyecto "Nombre del proyecto"
/case-kit ./my-project "Project name" --idioma en
```

Es un skill de **invocación manual**: el modelo no lo activa por su cuenta. No inicializa git ni crea repositorios, y no sobrescribe archivos existentes.

## Flujo completo con el resto de la colección

1. `case-kit` crea la estructura.
2. Llenas las fases; las auditorías de `wcag22-audit` y `heuristic-review-es` van en `docs/accessibility/` y `docs/testing/`.
3. `case-study-writer` redacta el caso desde lo que llenaste, sin inventar nada.

## Cómo se instala

| Ruta | Comando |
|---|---|
| Claude Code (plugin) | `/plugin marketplace add ancardenasc/ux-skills-es` y luego `/plugin install case-kit@ux-skills-es` |
| `npx skills` | `npx skills add ancardenasc/ux-skills-es --skill case-kit` |
| GitHub CLI | `gh skill install ancardenasc/ux-skills-es case-kit` |
| GitHub Copilot | copia la carpeta `skills/case-kit` a `.github/skills/` de tu proyecto |
| claude.ai | sube el zip `case-kit.zip` de la página de Releases |
