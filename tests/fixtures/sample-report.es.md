# Informe de auditoría: sitio de ejemplo (ficticio)

<!-- section:summary -->
## Resumen

- **Veredicto:** hay dos fallos que bloquean tareas básicas; corregirlos antes de publicar.
- **Hallazgos que fallan:** 2 (Crítico 0 · Grave 1 · Moderado 1 · Menor 0)
- **Requieren prueba manual:** 1
- **Cobertura:** 3 de 4 criterios aplicables en este modo

<!-- section:scope -->
## Alcance

- **Modo:** Código o diff
- **Qué se revisó:** `index.html` y `styles.css` de un sitio ficticio de ejemplo
- **Capacidades detectadas:** navegador no · Figma no · axe no · script no
- **Fecha:** 2026-10-01

<!-- section:findings -->
## Hallazgos

### Grave: la imagen del banner no tiene alternativa textual

- **Criterio:** 1.1.1 Non-text Content (nivel A), https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- **Dónde:** `index.html:14`
- **Qué pasa:** la imagen informativa del banner carece de atributo `alt`, así que una persona con lector de pantalla no sabe qué comunica.
- **Confianza:** Media, método: static_code
- **A quién afecta:** personas ciegas o con baja visión que usan lector de pantalla.
- **Cómo corregirlo:** añadir un `alt` que diga lo que comunica la imagen, o `alt=""` si fuera decorativa.

### Moderado: el enlace pierde el indicador de foco

- **Criterio:** 2.4.7 Focus Visible (nivel AA), https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html
- **Dónde:** `styles.css:22`
- **Qué pasa:** la regla `a:focus { outline: none; }` quita el indicador y no hay un estilo de reemplazo.
- **Confianza:** Media, método: static_code
- **A quién afecta:** personas que navegan con teclado.
- **Cómo corregirlo:** eliminar la regla o definir un `:focus-visible` con borde de buen contraste.

<!-- section:manual -->
## Verificación manual

| Criterio | Por qué no se pudo decidir | Cómo comprobarlo |
|---|---|---|
| 2.1.1 Keyboard | El menú se abre con JavaScript y el modo código no ejecuta ese comportamiento | Recorrer el menú solo con Tab, Enter y Escape en el navegador |

<!-- section:passed -->
## Criterios aprobados

- 3.1.1 Language of Page: `<html lang="es">` en `index.html:2`.

<!-- section:honest-gaps -->
## Brechas honestas

- Análisis estático: no se evaluó el comportamiento que depende de JavaScript ni el contraste real con la cascada de estilos.
- No se revisaron menús abiertos ni estados de error de formularios.
- Sin navegador disponible: no se midió reflujo, foco ni nombre accesible calculado.
- Este informe no es una declaración de conformidad ni un dictamen legal. No reemplaza las pruebas con personas usuarias ni con tecnologías de apoyo reales.

<!-- section:next-steps -->
## Próximos pasos

1. Corregir el `alt` del banner y el indicador de foco.
2. Probar el menú solo con teclado.
3. Repetir la auditoría con una URL y un navegador para cubrir lo que el código no decide.

---

*Este informe no es una declaración de conformidad ni un dictamen legal. No reemplaza las pruebas con personas usuarias ni con tecnologías de apoyo reales.*

```json ux-skills-findings
{
  "schema_version": "1",
  "skill": "wcag22-audit",
  "language": "es",
  "mode": "code",
  "generated_on": "2026-10-01",
  "scope": {
    "summary": "index.html y styles.css de un sitio ficticio de ejemplo",
    "inputs": ["index.html", "styles.css"],
    "capabilities": { "browser": false, "figma": false, "axe": false, "script": false }
  },
  "findings": [
    {
      "id": "WCAG-1.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": { "system": "WCAG22", "id": "1.1.1", "name": "Non-text Content", "level": "A", "url": "https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html" },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "La imagen del banner no tiene alternativa textual",
      "description": "La imagen informativa del banner carece de atributo alt.",
      "evidence": [{ "kind": "code", "file": "index.html", "line": 14, "snippet": "<img src=\"banner.jpg\">" }],
      "affected_users": "Personas ciegas o con baja visión que usan lector de pantalla.",
      "recommendation": "Añadir un alt que diga lo que comunica la imagen, o alt vacío si es decorativa.",
      "dedup_key": "1.1.1|index.html:14"
    },
    {
      "id": "WCAG-2.4.7-001",
      "source_skill": "wcag22-audit",
      "criterion": { "system": "WCAG22", "id": "2.4.7", "name": "Focus Visible", "level": "AA", "url": "https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html" },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "El enlace pierde el indicador de foco",
      "description": "La regla a:focus quita el outline sin definir un reemplazo visible.",
      "evidence": [{ "kind": "code", "file": "styles.css", "line": 22, "snippet": "a:focus { outline: none; }" }],
      "affected_users": "Personas que navegan con teclado.",
      "recommendation": "Eliminar la regla o definir un :focus-visible con borde de buen contraste.",
      "dedup_key": "2.4.7|styles.css:22"
    },
    {
      "id": "WCAG-2.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": { "system": "WCAG22", "id": "2.1.1", "name": "Keyboard", "level": "A", "url": "https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html" },
      "status": "manual",
      "confidence": "low",
      "method": "static_code",
      "title": "El menú depende de JavaScript",
      "manual_check": {
        "reason": "El modo código no ejecuta el comportamiento del menú.",
        "procedure": "Recorrer el menú solo con Tab, Enter y Escape en el navegador.",
        "suggested_tools": ["Teclado", "Navegador"]
      },
      "dedup_key": "2.1.1|index.html:menu"
    },
    {
      "id": "WCAG-3.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": { "system": "WCAG22", "id": "3.1.1", "name": "Language of Page", "level": "A", "url": "https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html" },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "El idioma de la página está declarado",
      "evidence": [{ "kind": "code", "file": "index.html", "line": 2, "snippet": "<html lang=\"es\">" }],
      "dedup_key": "3.1.1|index.html:2"
    }
  ],
  "honest_gaps": [
    "Análisis estático: no se evaluó el comportamiento que depende de JavaScript ni el contraste real con la cascada de estilos.",
    "No se revisaron menús abiertos ni estados de error de formularios.",
    "Sin navegador disponible: no se midió reflujo, foco ni nombre accesible calculado."
  ]
}
```
