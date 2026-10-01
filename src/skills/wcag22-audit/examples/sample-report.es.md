# Informe de auditoría: Café Aurora (sitio ficticio de ejemplo)

<!-- section:summary -->
## Resumen

- **Veredicto:** el formulario de suscripción no se puede enviar con teclado ni lector de pantalla; corregirlo antes de publicar.
- **Hallazgos que fallan:** 8 (Crítico 2 · Grave 3 · Moderado 3 · Menor 0)
- **Requieren prueba manual:** 1
- **Cobertura:** 11 de 13 criterios aplicables en este modo

<!-- section:scope -->
## Alcance

- **Modo:** Código o diff
- **Qué se revisó:** `index.html` y `styles.css` de un sitio ficticio
- **Capacidades detectadas:** navegador no · Figma no · axe no · script no
- **Fecha:** 2026-10-01

<!-- section:findings -->
## Hallazgos

### Crítico: El botón de suscripción es un div sin rol ni teclado

- **Criterio:** 4.1.2 Name, Role, Value (Nombre), nivel A, https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html
- **Dónde:** `index.html:25`
- **Qué pasa:** Un div con onclick no se anuncia como botón y no recibe foco del teclado, así que el formulario no se puede enviar sin ratón.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas que usan teclado o lector de pantalla.
- **Cómo corregirlo:** Usar un <button type="submit"> con el mismo texto visible.

### Crítico: El botón de suscripción no se puede activar con teclado

- **Criterio:** 2.1.1 Keyboard (Teclado), nivel A, https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html
- **Dónde:** `index.html:25`
- **Qué pasa:** El div con onclick no tiene tabindex ni manejador de teclado, así que no recibe foco ni responde a Enter o Espacio.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas que usan teclado, conmutadores o control por voz.
- **Cómo corregirlo:** Usar un <button type="submit">, que ya es operable con teclado.

### Grave: El texto de la nota tiene contraste insuficiente

- **Criterio:** 1.4.3 Contrast (Minimum) (Contraste mínimo del texto), nivel AA, https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- **Dónde:** `styles.css:8`
- **Qué pasa:** El gris #999999 sobre el fondo blanco da 2.85:1; el texto normal necesita al menos 4.5:1.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas con baja visión o que leen con mucha luz.
- **Cómo corregirlo:** Oscurecer el color del texto, por ejemplo a #595959 (7:1 sobre blanco).

### Grave: El campo de correo no tiene etiqueta

- **Criterio:** 3.3.2 Labels or Instructions (Etiquetas o instrucciones), nivel A, https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html
- **Dónde:** `index.html:22`
- **Qué pasa:** El placeholder desaparece al escribir y no cuenta como etiqueta; el campo no tiene label ni aria-label.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas con lector de pantalla y con dificultades de memoria.
- **Cómo corregirlo:** Asociar un <label for> visible al campo, como ya se hace con el campo de nombre.

### Grave: La imagen del banner no tiene alternativa textual

- **Criterio:** 1.1.1 Non-text Content (Contenido no textual), nivel A, https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- **Dónde:** `index.html:18`
- **Qué pasa:** La imagen del banner carece de atributo alt, así que una persona con lector de pantalla no sabe qué comunica.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas ciegas o con baja visión que usan lector de pantalla.
- **Cómo corregirlo:** Añadir un alt que diga lo que comunica la imagen, o alt vacío si fuera decorativa.

### Moderado: Los enlaces pierden el indicador de foco

- **Criterio:** 2.4.7 Focus Visible (Foco visible), nivel AA, https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html
- **Dónde:** `styles.css:9`
- **Qué pasa:** La regla a:focus quita el contorno y no hay un estilo de reemplazo.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas que navegan con teclado.
- **Cómo corregirlo:** Eliminar la regla o definir un :focus-visible con borde de buen contraste.

### Moderado: El botón de cerrar mide 18 por 18 píxeles

- **Criterio:** 2.5.8 Target Size (Minimum) (Tamaño del objetivo), nivel AA, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- **Dónde:** `styles.css:11`
- **Qué pasa:** El objetivo mide menos de 24 por 24 píxeles CSS y no tiene espacio compensatorio a su alrededor.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas con temblor o que usan pantalla táctil.
- **Cómo corregirlo:** Ampliar el área activa a al menos 24 por 24 px, por ejemplo con padding.

### Moderado: El campo de correo no declara su propósito

- **Criterio:** 1.3.5 Identify Input Purpose (Propósito de los campos), nivel AA, https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html
- **Dónde:** `index.html:22`
- **Qué pasa:** El campo no tiene autocomplete, así que el navegador no puede rellenar el correo de la persona.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Personas con dificultades motoras o de memoria, y quienes usan gestores de datos.
- **Cómo corregirlo:** Añadir autocomplete="email" al campo.

<!-- section:manual -->
## Verificación manual

| Criterio | Por qué no se pudo decidir | Cómo comprobarlo |
|---|---|---|
| 2.4.3 Focus Order | El orden del foco depende de cómo se renderiza y se recorre la página; el modo código no lo decide. | Recorrer la página solo con Tab y Mayús+Tab y comprobar que el orden sigue el orden visual. |

<!-- section:passed -->
## Criterios aprobados

- 2.4.1 Bypass Blocks: Hay un enlace de salto al contenido (`index.html:10`).
- 2.4.2 Page Titled: La página tiene título descriptivo (`index.html:6`).
- 3.1.1 Language of Page: El idioma de la página está declarado (`index.html:2`).

<!-- section:honest-gaps -->
## Brechas honestas

- Análisis estático: no se evaluó el comportamiento de JavaScript (la función enviar() no está en los archivos revisados) ni el contraste real con la cascada completa.
- No se evaluó el reflujo a 320 px (1.4.10): requiere un navegador o un viewport real.
- No se revisaron estados de error de formulario ni contenido que aparece al pasar el cursor o enfocar.
- Sin navegador disponible: no se midió el foco ni el nombre accesible calculado.
- Este informe no es una declaración de conformidad ni un dictamen legal. No reemplaza las pruebas con personas usuarias ni con tecnologías de apoyo reales.

<!-- section:next-steps -->
## Próximos pasos

1. Reemplazar el div por un botón real y etiquetar el campo de correo.
2. Añadir el alt del banner y oscurecer el texto de la nota.
3. Restaurar el indicador de foco y ampliar el botón de cerrar.
4. Repetir la auditoría en modo URL con un navegador para cubrir reflujo, foco y orden de tabulación.

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
    "summary": "index.html y styles.css de un sitio ficticio",
    "inputs": [
      "index.html",
      "styles.css"
    ],
    "capabilities": {
      "browser": false,
      "figma": false,
      "axe": false,
      "script": false
    }
  },
  "findings": [
    {
      "id": "WCAG-4.1.2-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "4.1.2",
        "name": "Name, Role, Value",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html"
      },
      "status": "fail",
      "severity": "critical",
      "confidence": "medium",
      "method": "static_code",
      "title": "El botón de suscripción es un div sin rol ni teclado",
      "description": "Un div con onclick no se anuncia como botón y no recibe foco del teclado, así que el formulario no se puede enviar sin ratón.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 25,
          "snippet": "<div class=\"btn\" onclick=\"enviar()\">Suscribirme</div>"
        }
      ],
      "affected_users": "Personas que usan teclado o lector de pantalla.",
      "recommendation": "Usar un <button type=\"submit\"> con el mismo texto visible.",
      "dedup_key": "4.1.2|index.html:25"
    },
    {
      "id": "WCAG-2.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.1.1",
        "name": "Keyboard",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html"
      },
      "status": "fail",
      "severity": "critical",
      "confidence": "medium",
      "method": "static_code",
      "title": "El botón de suscripción no se puede activar con teclado",
      "description": "El div con onclick no tiene tabindex ni manejador de teclado, así que no recibe foco ni responde a Enter o Espacio.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 25,
          "snippet": "<div class=\"btn\" onclick=\"enviar()\">Suscribirme</div>"
        }
      ],
      "affected_users": "Personas que usan teclado, conmutadores o control por voz.",
      "recommendation": "Usar un <button type=\"submit\">, que ya es operable con teclado.",
      "dedup_key": "2.1.1|index.html:25"
    },
    {
      "id": "WCAG-1.4.3-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.4.3",
        "name": "Contrast (Minimum)",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "El texto de la nota tiene contraste insuficiente",
      "description": "El gris #999999 sobre el fondo blanco da 2.85:1; el texto normal necesita al menos 4.5:1.",
      "evidence": [
        {
          "kind": "code",
          "file": "styles.css",
          "line": 8,
          "snippet": ".nota { color: #999999; }",
          "measured": {
            "ratio": 2.85,
            "required": 4.5,
            "fg": "#999999",
            "bg": "#ffffff"
          }
        },
        {
          "kind": "code",
          "file": "styles.css",
          "line": 1,
          "snippet": ":root { --fondo: #ffffff; --texto: #1a1a1a; }"
        }
      ],
      "affected_users": "Personas con baja visión o que leen con mucha luz.",
      "recommendation": "Oscurecer el color del texto, por ejemplo a #595959 (7:1 sobre blanco).",
      "dedup_key": "1.4.3|styles.css:8"
    },
    {
      "id": "WCAG-3.3.2-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "3.3.2",
        "name": "Labels or Instructions",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "El campo de correo no tiene etiqueta",
      "description": "El placeholder desaparece al escribir y no cuenta como etiqueta; el campo no tiene label ni aria-label.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 22,
          "snippet": "<input type=\"email\" name=\"correo\" placeholder=\"Tu correo\">"
        }
      ],
      "affected_users": "Personas con lector de pantalla y con dificultades de memoria.",
      "recommendation": "Asociar un <label for> visible al campo, como ya se hace con el campo de nombre.",
      "dedup_key": "3.3.2|index.html:22"
    },
    {
      "id": "WCAG-1.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.1.1",
        "name": "Non-text Content",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "La imagen del banner no tiene alternativa textual",
      "description": "La imagen del banner carece de atributo alt, así que una persona con lector de pantalla no sabe qué comunica.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 18,
          "snippet": "<img class=\"banner\" src=\"banner.jpg\">"
        }
      ],
      "affected_users": "Personas ciegas o con baja visión que usan lector de pantalla.",
      "recommendation": "Añadir un alt que diga lo que comunica la imagen, o alt vacío si fuera decorativa.",
      "dedup_key": "1.1.1|index.html:18"
    },
    {
      "id": "WCAG-2.4.7-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.7",
        "name": "Focus Visible",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "Los enlaces pierden el indicador de foco",
      "description": "La regla a:focus quita el contorno y no hay un estilo de reemplazo.",
      "evidence": [
        {
          "kind": "code",
          "file": "styles.css",
          "line": 9,
          "snippet": "a:focus { outline: none; }"
        }
      ],
      "affected_users": "Personas que navegan con teclado.",
      "recommendation": "Eliminar la regla o definir un :focus-visible con borde de buen contraste.",
      "dedup_key": "2.4.7|styles.css:9"
    },
    {
      "id": "WCAG-2.5.8-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.5.8",
        "name": "Target Size (Minimum)",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "El botón de cerrar mide 18 por 18 píxeles",
      "description": "El objetivo mide menos de 24 por 24 píxeles CSS y no tiene espacio compensatorio a su alrededor.",
      "evidence": [
        {
          "kind": "code",
          "file": "styles.css",
          "line": 11,
          "snippet": ".icono { width: 18px; height: 18px; padding: 0; border: 0; background: transparent; }",
          "measured": {
            "width_px": 18,
            "height_px": 18,
            "required_px": 24
          }
        }
      ],
      "affected_users": "Personas con temblor o que usan pantalla táctil.",
      "recommendation": "Ampliar el área activa a al menos 24 por 24 px, por ejemplo con padding.",
      "dedup_key": "2.5.8|styles.css:11"
    },
    {
      "id": "WCAG-1.3.5-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.3.5",
        "name": "Identify Input Purpose",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "El campo de correo no declara su propósito",
      "description": "El campo no tiene autocomplete, así que el navegador no puede rellenar el correo de la persona.",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 22,
          "snippet": "<input type=\"email\" name=\"correo\" placeholder=\"Tu correo\">"
        }
      ],
      "affected_users": "Personas con dificultades motoras o de memoria, y quienes usan gestores de datos.",
      "recommendation": "Añadir autocomplete=\"email\" al campo.",
      "dedup_key": "1.3.5|index.html:22"
    },
    {
      "id": "WCAG-2.4.3-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.3",
        "name": "Focus Order",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html"
      },
      "status": "manual",
      "confidence": "low",
      "method": "static_code",
      "title": "El orden del foco requiere recorrer la página",
      "manual_check": {
        "reason": "El orden del foco depende de cómo se renderiza y se recorre la página; el modo código no lo decide.",
        "procedure": "Recorrer la página solo con Tab y Mayús+Tab y comprobar que el orden sigue el orden visual.",
        "suggested_tools": [
          "Teclado",
          "Navegador"
        ]
      },
      "dedup_key": "2.4.3|index.html"
    },
    {
      "id": "WCAG-1.4.10-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "1.4.10",
        "name": "Reflow",
        "level": "AA",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/reflow.html"
      },
      "status": "not_tested",
      "confidence": "low",
      "method": "inferred",
      "title": "El reflujo a 320 px no se pudo evaluar",
      "dedup_key": "1.4.10|index.html"
    },
    {
      "id": "WCAG-2.4.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.1",
        "name": "Bypass Blocks",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "Hay un enlace de salto al contenido",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 10,
          "snippet": "<a class=\"skip\" href=\"#contenido\">Saltar al contenido</a>"
        }
      ],
      "dedup_key": "2.4.1|index.html:10"
    },
    {
      "id": "WCAG-2.4.2-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "2.4.2",
        "name": "Page Titled",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "La página tiene título descriptivo",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 6,
          "snippet": "<title>Café Aurora – Inicio</title>"
        }
      ],
      "dedup_key": "2.4.2|index.html:6"
    },
    {
      "id": "WCAG-3.1.1-001",
      "source_skill": "wcag22-audit",
      "criterion": {
        "system": "WCAG22",
        "id": "3.1.1",
        "name": "Language of Page",
        "level": "A",
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "El idioma de la página está declarado",
      "evidence": [
        {
          "kind": "code",
          "file": "index.html",
          "line": 2,
          "snippet": "<html lang=\"es\">"
        }
      ],
      "dedup_key": "3.1.1|index.html:2"
    }
  ],
  "honest_gaps": [
    "Análisis estático: no se evaluó el comportamiento de JavaScript (la función enviar() no está en los archivos revisados) ni el contraste real con la cascada completa.",
    "No se evaluó el reflujo a 320 px (1.4.10): requiere un navegador o un viewport real.",
    "No se revisaron estados de error de formulario ni contenido que aparece al pasar el cursor o enfocar.",
    "Sin navegador disponible: no se midió el foco ni el nombre accesible calculado."
  ]
}
```
