# Revisión heurística: pedido de Café Aurora (flujo ficticio de ejemplo)

<!-- section:summary -->
## Resumen

- **Veredicto:** el flujo funciona pero no da respuesta al guardar y permite borrar el pedido sin confirmar; corregir esos dos puntos antes de publicar.
- **Hallazgos que fallan:** 7 (Crítico 0 · Grave 2 · Moderado 4 · Menor 1)
- **Requieren prueba manual:** 2
- **Cobertura:** 8 de 10 criterios aplicables en este modo

| Heurística | Estado | Hallazgos |
|---|---|---|
| H1 Visibility of System Status (Visibilidad del estado del sistema) | Hay problemas | 1 |
| H2 Match Between the System and the Real World (Correspondencia con el mundo real) | Hay problemas | 1 |
| H3 User Control and Freedom (Control y libertad del usuario) | Requiere prueba manual | 0 |
| H4 Consistency and Standards (Consistencia y estándares) | Hay problemas | 1 |
| H5 Error Prevention (Prevención de errores) | Hay problemas | 1 |
| H6 Recognition Rather than Recall (Reconocer en lugar de recordar) | Hay problemas | 1 |
| H7 Flexibility and Efficiency of Use (Flexibilidad y eficiencia de uso) | Requiere prueba manual | 0 |
| H8 Aesthetic and Minimalist Design (Diseño estético y minimalista) | Sin problemas | 0 |
| H9 Help Users Recognize, Diagnose, and Recover from Errors (Reconocer, diagnosticar y recuperarse de errores) | Hay problemas | 1 |
| H10 Help and Documentation (Ayuda y documentación) | Hay problemas | 1 |

<!-- section:scope -->
## Alcance

- **Modo:** Código o diff
- **Qué se revisó:** `pedido.html` de un flujo ficticio
- **Tarea evaluada:** Hacer, guardar y, si hace falta, eliminar un pedido de café.
- **Capacidades detectadas:** navegador no · Figma no · axe no · script no
- **Fecha:** 2026-10-01

<!-- section:findings -->
## Hallazgos

### Grave: Eliminar el pedido no pide confirmación ni permite deshacer

- **Heurística:** H5 Error Prevention (Prevención de errores), https://www.nngroup.com/articles/ten-usability-heuristics/
- **Dónde:** `pedido.html:17`
- **Qué pasa:** Un solo clic ejecuta el borrado y recarga la página; no hay confirmación, papelera ni opción de deshacer.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Cualquier persona que pulse el botón por error.
- **Cómo corregirlo:** Pedir confirmación indicando qué se borra, o permitir deshacer durante unos segundos.

### Grave: Guardar no da ninguna respuesta

- **Heurística:** H1 Visibility of System Status (Visibilidad del estado del sistema), https://www.nngroup.com/articles/ten-usability-heuristics/
- **Dónde:** `pedido.html:22`
- **Qué pasa:** La función envía la petición y no muestra progreso, éxito ni error; la persona no sabe si el pedido quedó guardado.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Quien guarda sin saber si funcionó y puede repetir la acción.
- **Cómo corregirlo:** Mostrar un estado de carga y un mensaje de éxito o de error junto al botón.

### Moderado: El mensaje de error es técnico y no propone solución

- **Heurística:** H9 Help Users Recognize, Diagnose, and Recover from Errors (Reconocer, diagnosticar y recuperarse de errores), https://www.nngroup.com/articles/ten-usability-heuristics/
- **Dónde:** `pedido.html:25`
- **Qué pasa:** El texto muestra un código interno y habla de un parámetro; no dice qué falló ni cómo corregirlo.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Cualquier persona que no sea del equipo técnico.
- **Cómo corregirlo:** Decir con palabras claras qué pasó y qué hacer, por ejemplo qué campo corregir.

### Moderado: La fecha pide el formato mes/día/año

- **Heurística:** H2 Match Between the System and the Real World (Correspondencia con el mundo real), https://www.nngroup.com/articles/ten-usability-heuristics/
- **Dónde:** `pedido.html:13`
- **Qué pasa:** El formato mm/dd/aaaa no es el habitual para el público local, que escribe día, mes y año; invita a confundir fechas como 03/04.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Quienes escriben las fechas en el orden local.
- **Cómo corregirlo:** Usar dd/mm/aaaa o un selector de fecha que muestre el mes con su nombre.

### Moderado: Dos botones con nombres distintos para acciones parecidas

- **Heurística:** H4 Consistency and Standards (Consistencia y estándares), https://www.nngroup.com/articles/ten-usability-heuristics/
- **Dónde:** `pedido.html:15`
- **Qué pasa:** «Aceptar» y «Enviar» no dicen qué hacen y compiten entre sí; no queda claro cuál confirma el pedido.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Quien debe decidir qué botón pulsar.
- **Cómo corregirlo:** Dejar un solo botón principal con un verbo claro, por ejemplo «Confirmar pedido».

### Moderado: El botón de engranaje no dice qué hace

- **Heurística:** H6 Recognition Rather than Recall (Reconocer en lugar de recordar), https://www.nngroup.com/articles/ten-usability-heuristics/
- **Dónde:** `pedido.html:18`
- **Qué pasa:** El icono no tiene texto ni título; hay que recordar o adivinar su función.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Quien usa el sitio por primera vez.
- **Cómo corregirlo:** Añadir una etiqueta visible o un título descriptivo.

### Menor: No hay enlace de ayuda

- **Heurística:** H10 Help and Documentation (Ayuda y documentación), https://www.nngroup.com/articles/ten-usability-heuristics/
- **Dónde:** `pedido.html:9`
- **Qué pasa:** La navegación no ofrece ayuda ni contacto para quien tiene dudas con el pedido.
- **Confianza:** Media, método: static_code
- **A quién afecta:** Quien se queda atascado durante el pedido.
- **Cómo corregirlo:** Añadir un enlace a ayuda o contacto en la navegación.

<!-- section:manual -->
## Verificación manual

| Criterio | Por qué no se pudo decidir | Cómo comprobarlo |
|---|---|---|
| H3 User Control and Freedom | El control para volver atrás o deshacer solo se verifica ejecutando el flujo. | Recorrer el pedido e intentar cancelar o deshacer en cada paso. |
| H7 Flexibility and Efficiency of Use | No se pueden valorar leyendo el código; requieren observar a personas con experiencia. | Observar a quienes repiten el pedido y preguntar qué atajos echan en falta. |

<!-- section:passed -->
## Criterios aprobados

- H4 Consistency and Standards: Las etiquetas de la navegación son coherentes (`pedido.html:9`).
- H8 Aesthetic and Minimalist Design: La pantalla tiene una sola tarea (`pedido.html:11`).

<!-- section:honest-gaps -->
## Brechas honestas

- Revisión hecha leyendo código: no se vio el flujo ejecutándose, así que el ritmo, las animaciones y los textos que genera el servidor no se evaluaron.
- Una sola persona evaluadora: la revisión heurística se enriquece con varias miradas y no sustituye las pruebas de usabilidad con personas usuarias.
- Solo se revisó la tarea de hacer un pedido; no se revisaron la cuenta, el pago ni el seguimiento.
- H3 y H7 quedan para verificación manual: requieren ejecutar el flujo y observar uso real.
- Este informe no es una declaración de conformidad ni un dictamen legal. No reemplaza las pruebas con personas usuarias ni con tecnologías de apoyo reales.

<!-- section:next-steps -->
## Próximos pasos

1. Pedir confirmación antes de eliminar y mostrar el resultado de guardar.
2. Unificar los botones en una acción principal con verbo claro.
3. Cambiar el formato de fecha y reescribir el mensaje de error en lenguaje claro.
4. Probar el flujo con 5 personas usuarias para validar estos hallazgos.

---

*Este informe no es una declaración de conformidad ni un dictamen legal. No reemplaza las pruebas con personas usuarias ni con tecnologías de apoyo reales.*

```json ux-skills-findings
{
  "schema_version": "1",
  "skill": "heuristic-review-es",
  "language": "es",
  "mode": "code",
  "generated_on": "2026-10-01",
  "scope": {
    "summary": "pedido.html de un flujo ficticio",
    "inputs": [
      "pedido.html"
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
      "id": "NIELSEN-H5-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H5",
        "name": "Error Prevention",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "Eliminar el pedido no pide confirmación ni permite deshacer",
      "description": "Un solo clic ejecuta el borrado y recarga la página; no hay confirmación, papelera ni opción de deshacer.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 17,
          "snippet": "<button type=\"button\" onclick=\"borrarPedido()\">Eliminar pedido</button>"
        },
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 23,
          "snippet": "function borrarPedido() { fetch('/pedido', {method: 'DELETE'}).then(() => location.reload()); }"
        }
      ],
      "affected_users": "Cualquier persona que pulse el botón por error.",
      "recommendation": "Pedir confirmación indicando qué se borra, o permitir deshacer durante unos segundos.",
      "dedup_key": "H5|pedido.html:17"
    },
    {
      "id": "NIELSEN-H1-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H1",
        "name": "Visibility of System Status",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "serious",
      "confidence": "medium",
      "method": "static_code",
      "title": "Guardar no da ninguna respuesta",
      "description": "La función envía la petición y no muestra progreso, éxito ni error; la persona no sabe si el pedido quedó guardado.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 22,
          "snippet": "function guardar() { fetch('/guardar', {method: 'POST'}); }"
        }
      ],
      "affected_users": "Quien guarda sin saber si funcionó y puede repetir la acción.",
      "recommendation": "Mostrar un estado de carga y un mensaje de éxito o de error junto al botón.",
      "dedup_key": "H1|pedido.html:22"
    },
    {
      "id": "NIELSEN-H9-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H9",
        "name": "Help Users Recognize, Diagnose, and Recover from Errors",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "El mensaje de error es técnico y no propone solución",
      "description": "El texto muestra un código interno y habla de un parámetro; no dice qué falló ni cómo corregirlo.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 25,
          "snippet": "document.getElementById('estado').textContent = 'Error 0x80070057: parámetro incorrecto';"
        }
      ],
      "affected_users": "Cualquier persona que no sea del equipo técnico.",
      "recommendation": "Decir con palabras claras qué pasó y qué hacer, por ejemplo qué campo corregir.",
      "dedup_key": "H9|pedido.html:25"
    },
    {
      "id": "NIELSEN-H2-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H2",
        "name": "Match Between the System and the Real World",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "La fecha pide el formato mes/día/año",
      "description": "El formato mm/dd/aaaa no es el habitual para el público local, que escribe día, mes y año; invita a confundir fechas como 03/04.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 13,
          "snippet": "<label for=\"fecha\">Fecha de entrega (mm/dd/aaaa)</label>"
        }
      ],
      "affected_users": "Quienes escriben las fechas en el orden local.",
      "recommendation": "Usar dd/mm/aaaa o un selector de fecha que muestre el mes con su nombre.",
      "dedup_key": "H2|pedido.html:13"
    },
    {
      "id": "NIELSEN-H4-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H4",
        "name": "Consistency and Standards",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "Dos botones con nombres distintos para acciones parecidas",
      "description": "«Aceptar» y «Enviar» no dicen qué hacen y compiten entre sí; no queda claro cuál confirma el pedido.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 15,
          "snippet": "<button type=\"submit\">Aceptar</button>"
        }
      ],
      "affected_users": "Quien debe decidir qué botón pulsar.",
      "recommendation": "Dejar un solo botón principal con un verbo claro, por ejemplo «Confirmar pedido».",
      "dedup_key": "H4|pedido.html:15"
    },
    {
      "id": "NIELSEN-H6-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H6",
        "name": "Recognition Rather than Recall",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "moderate",
      "confidence": "medium",
      "method": "static_code",
      "title": "El botón de engranaje no dice qué hace",
      "description": "El icono no tiene texto ni título; hay que recordar o adivinar su función.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 18,
          "snippet": "<button type=\"button\" class=\"ico\" title=\"\">⚙</button>"
        }
      ],
      "affected_users": "Quien usa el sitio por primera vez.",
      "recommendation": "Añadir una etiqueta visible o un título descriptivo.",
      "dedup_key": "H6|pedido.html:18"
    },
    {
      "id": "NIELSEN-H10-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H10",
        "name": "Help and Documentation",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "fail",
      "severity": "minor",
      "confidence": "medium",
      "method": "static_code",
      "title": "No hay enlace de ayuda",
      "description": "La navegación no ofrece ayuda ni contacto para quien tiene dudas con el pedido.",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 9,
          "snippet": "<a href=\"/\">Inicio</a> <a href=\"/pedido\">Mi pedido</a> <a href=\"/cuenta\">Cuenta</a>"
        }
      ],
      "affected_users": "Quien se queda atascado durante el pedido.",
      "recommendation": "Añadir un enlace a ayuda o contacto en la navegación.",
      "dedup_key": "H10|pedido.html:9"
    },
    {
      "id": "NIELSEN-H3-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H3",
        "name": "User Control and Freedom",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "manual",
      "confidence": "low",
      "method": "static_code",
      "title": "Cancelar o deshacer se comprueba recorriendo el flujo",
      "manual_check": {
        "reason": "El control para volver atrás o deshacer solo se verifica ejecutando el flujo.",
        "procedure": "Recorrer el pedido e intentar cancelar o deshacer en cada paso.",
        "suggested_tools": [
          "Flujo en ejecución"
        ]
      },
      "dedup_key": "H3|pedido.html"
    },
    {
      "id": "NIELSEN-H7-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H7",
        "name": "Flexibility and Efficiency of Use",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "manual",
      "confidence": "low",
      "method": "static_code",
      "title": "Atajos y personalización dependen del uso real",
      "manual_check": {
        "reason": "No se pueden valorar leyendo el código; requieren observar a personas con experiencia.",
        "procedure": "Observar a quienes repiten el pedido y preguntar qué atajos echan en falta.",
        "suggested_tools": [
          "Flujo en ejecución"
        ]
      },
      "dedup_key": "H7|pedido.html"
    },
    {
      "id": "NIELSEN-H4-002",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H4",
        "name": "Consistency and Standards",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "Las etiquetas de la navegación son coherentes",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 9,
          "snippet": "<a href=\"/\">Inicio</a> <a href=\"/pedido\">Mi pedido</a> <a href=\"/cuenta\">Cuenta</a>"
        }
      ],
      "dedup_key": "H4|pedido.html:9"
    },
    {
      "id": "NIELSEN-H8-001",
      "source_skill": "heuristic-review-es",
      "criterion": {
        "system": "NIELSEN",
        "id": "H8",
        "name": "Aesthetic and Minimalist Design",
        "url": "https://www.nngroup.com/articles/ten-usability-heuristics/"
      },
      "status": "pass",
      "confidence": "medium",
      "method": "static_code",
      "title": "La pantalla tiene una sola tarea",
      "evidence": [
        {
          "kind": "code",
          "file": "pedido.html",
          "line": 11,
          "snippet": "<h1>Tu pedido</h1>"
        }
      ],
      "dedup_key": "H8|pedido.html:11"
    }
  ],
  "honest_gaps": [
    "Revisión hecha leyendo código: no se vio el flujo ejecutándose, así que el ritmo, las animaciones y los textos que genera el servidor no se evaluaron.",
    "Una sola persona evaluadora: la revisión heurística se enriquece con varias miradas y no sustituye las pruebas de usabilidad con personas usuarias.",
    "Solo se revisó la tarea de hacer un pedido; no se revisaron la cuenta, el pago ni el seguimiento.",
    "H3 y H7 quedan para verificación manual: requieren ejecutar el flujo y observar uso real."
  ]
}
```
