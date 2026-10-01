## Tabla de huecos

| Sección | Evidencia | Falta |
|---|---|---|
| Contexto y rol | `docs/brief.md` (problema, alcance, restricciones) | Rol exacto, equipo, duración real. El brief solo dice "6 semanas disponibles". |
| Problema | `docs/brief.md`, `docs/research/README.md` | Nada. |
| Proceso | Investigación, diseño, validación y PRD, todos con datos | Figma "pendiente". No hay evidencia de si RF-03 se construyó. Enlaces a repo y Storybook. |
| Decisiones | ADR-0001 y decisiones de diseño | Alternativas de las decisiones de diseño. |
| Resultado | Dos rondas de prueba, SUS de la ronda 2 | Lighthouse, SUS de la ronda 1, tiempo en tarea. |
| Accesibilidad | Informe con bloque JSON | A qué versión corresponde el informe. |
| Reflexión | Ninguna | Todo: es voz de quien hizo el proyecto. |
| Enlaces | Ruta del informe | Demo, repo, Figma y Storybook. |

No hice preguntas. Los huecos quedan marcados y puedes llenarlos después. Las notas crudas solo me dieron contexto: no usé nombres, empleadores ni teléfonos.

---

## 1. Caso completo

# Caso de estudio: Café Aurora

> **Proyecto de muestra ficticio:** no es un cliente real y todos los datos (personas participantes, pruebas y métricas) son de muestra. [fuente: docs/brief.md]

## Contexto y rol
Café Aurora es un ejercicio de portafolio sobre el pedido en línea de café de especialidad, centrado en retroalimentación, formularios y accesibilidad. [fuente: docs/brief.md]
Quedaron fuera de alcance los pagos en línea, la cuenta de usuario y el seguimiento del envío. [fuente: docs/brief.md]
Las restricciones fueron 6 semanas disponibles, HTML, CSS y JavaScript sin framework, y licencias OFL, MIT, CC0 o contenido propio. [fuente: docs/brief.md]

[DATO FALTANTE: mi rol exacto, si hubo equipo y la duración real del proyecto; lo dice quien hizo el proyecto.]

## Problema
Quienes piden café de especialidad en línea no saben si su pedido quedó guardado y abandonan el proceso. [fuente: docs/brief.md]
En las entrevistas, 4 de 5 personas abandonaron o repitieron el pedido por no ver confirmación (insight I-01). [fuente: docs/research/README.md]
Un pedido sin confirmar es una venta perdida y genera desconfianza. [fuente: docs/brief.md]

## Proceso

### Investigación
Hice 5 entrevistas moderadas con personas de muestra (P1 a P5), anonimizadas, con consentimiento escrito guardado fuera del repositorio. [fuente: docs/research/README.md, docs/brief.md]
Salieron tres insights:
- **I-01:** 4 de 5 personas abandonaron o repitieron el pedido por no ver confirmación. [fuente: docs/research/README.md]
- **I-02:** 3 de 5 escribieron mal la fecha de entrega por el formato mes/día. [fuente: docs/research/README.md]
- **I-03:** 2 de 5 pidieron repetir su pedido habitual sin que se les preguntara. [fuente: docs/research/README.md]

La persona objetivo (compradores de café de origen para casa, de 25 a 45 años) es una proto-persona sin validar con investigación real. [fuente: docs/brief.md]
No fue posible entrevistar a ninguna persona usuaria de tecnología de apoyo. Se compensó con la revisión experta de la Fase 4. [fuente: docs/research/README.md]

### Diseño
El PRD convirtió los insights en requisitos:
- **RF-01 (Must):** mensaje de éxito o error junto al botón, en menos de 2 segundos.
- **RF-02 (Must):** fecha en día/mes/año con selector.
- **RF-03 (Could):** repetir el último pedido.

[fuente: docs/prd.md]

Las decisiones de diseño fueron:
- Mensaje de estado junto al botón de guardar, con texto y no solo color.
- Selector de fecha que muestra el mes con su nombre.
- Un único botón principal por pantalla, con el verbo "Confirmar pedido".

[fuente: docs/design/README.md]

Figma: pendiente, aún no hay archivo público. [fuente: docs/design/README.md]

### Validación
Hice dos rondas de 5 sesiones moderadas con personas de muestra. [fuente: docs/testing/README.md]
La ronda 1 dejó tres hallazgos, todos resueltos en la versión 2:
- **H-01:** guardar no da respuesta (crítico).
- **H-02:** la fecha pide el formato mes/día/año (mayor).
- **H-03:** eliminar el pedido no pide confirmación (mayor).

[fuente: docs/testing/README.md]

### Construcción
El stack fue HTML, CSS y JavaScript sin framework. [fuente: docs/brief.md]
La decisión técnica documentada es el botón nativo (ADR-0001, aceptada el 2026-09-20). [fuente: docs/decisions/0001-boton-nativo.md]
[DATO FALTANTE: estado de RF-03 (si se construyó o quedó fuera) y enlace al repositorio o Storybook; no figuran en las fuentes.]

## Decisiones clave
| Decisión | Alternativas consideradas | Por qué esta |
|---|---|---|
| Usar `<button type="submit">` para confirmar el pedido (la v1 usaba un div con manejador de clic, sin foco ni anuncio como botón) | Mantener el div con `role="button"` y manejadores de teclado | Mejora la operabilidad con teclado y lectores de pantalla sin código extra. Costo: hubo que revisar los estilos del botón. [fuente: docs/decisions/0001-boton-nativo.md] |
| Mensaje de estado junto al botón, con texto y no solo color | [DATO FALTANTE: alternativas; docs/design/README.md no las registra] | Responde al insight I-01. [fuente: docs/design/README.md, docs/prd.md] |
| Selector de fecha con el mes por nombre | [DATO FALTANTE: alternativas] | Responde a I-02: 3 de 5 personas escribieron mal la fecha. [fuente: docs/design/README.md, docs/research/README.md] |
| Un único botón principal con el verbo "Confirmar pedido" | [DATO FALTANTE: alternativas y motivo] | [DATO FALTANTE: el motivo no está en las fuentes.] [fuente: docs/design/README.md] |

## Resultado
Comparo con las metas definidas antes de diseñar. [fuente: docs/brief.md]

| Métrica | Meta | Antes (v1, ronda 1) | Después (v2, ronda 2) | Estado |
|---|---|---|---|---|
| Tarea completada sin errores | 80 % o más | 3 de 5 (60 %) | 5 de 5 (100 %) | Cumplida en la v2; +40 puntos porcentuales [fuente: docs/brief.md, docs/testing/README.md] |
| SUS | 68 o más | No se midió | 72 | Cumplida en la v2, sin "antes" para comparar [fuente: docs/brief.md, docs/testing/README.md] |
| Lighthouse a11y | 100 | [DATO FALTANTE] | [DATO FALTANTE] | Sin medir en las fuentes [fuente: docs/brief.md] |
| Criterios WCAG 2.2 AA aplicables cumplidos | 100 % | n/d | Ver "Accesibilidad" | No cumplida según el informe, con reservas sobre su alcance [fuente: docs/brief.md, docs/accessibility/informe-wcag22-2026-10-01.md] |

El tiempo en tarea no se midió en ninguna ronda. [fuente: docs/testing/README.md]

**Límites:** cada ronda tuvo 5 personas de muestra, así que los porcentajes saltan de 20 en 20 puntos y no son generalizables. La persona objetivo es una proto-persona sin validar. [fuente: docs/testing/README.md, docs/brief.md]

## Accesibilidad
El informe de auditoría WCAG 2.2 es del 2026-10-01 y se hizo en modo código (análisis estático de `index.html` y `styles.css`). [fuente: docs/accessibility/informe-wcag22-2026-10-01.md]
Resultado:
- 8 hallazgos que fallan: 2 críticos, 3 graves, 3 moderados y 0 menores.
- 1 criterio requiere prueba manual (2.4.3 Orden del foco).
- 1 criterio no se evaluó (1.4.10 Reflujo).
- 3 criterios aprobados.
- Cobertura: 11 de 13 criterios aplicables.

[fuente: docs/accessibility/informe-wcag22-2026-10-01.md]

Los fallos críticos son un div que hace de botón sin rol ni teclado (4.1.2 y 2.1.1). Los graves son el contraste de la nota (2.85:1 frente a 4.5:1 requerido), el campo de correo sin etiqueta y la imagen del banner sin alternativa textual. Los moderados son el foco visible, un botón de cerrar de 18 × 18 px (el mínimo es 24 × 24 px) y el campo de correo sin propósito declarado. [fuente: docs/accessibility/informe-wcag22-2026-10-01.md]

No declaro un nivel AA alcanzado. El informe no es una declaración de conformidad ni un dictamen legal. [fuente: docs/accessibility/informe-wcag22-2026-10-01.md]

**Brechas conocidas:**
- Análisis estático: no se evaluó el comportamiento de JavaScript ni el contraste con la cascada completa.
- No se evaluó el reflujo a 320 px.
- No se revisaron estados de error de formulario ni contenido que aparece al pasar el cursor o enfocar.
- Sin navegador: no se midió el foco ni el nombre accesible.
- No reemplaza las pruebas con personas usuarias ni con tecnologías de apoyo reales.

[fuente: docs/accessibility/informe-wcag22-2026-10-01.md]
Tampoco hubo una persona usuaria de tecnología de apoyo en la investigación. [fuente: docs/research/README.md]

**Alcance por aclarar:** el informe describe "un sitio ficticio" con un formulario de suscripción, mientras que el brief habla de un flujo de pedido. [fuente: docs/accessibility/informe-wcag22-2026-10-01.md, docs/brief.md] [DATO FALTANTE: a qué versión del proyecto corresponde el informe y si cubre el flujo de pedido. El ADR del 2026-09-20 cambió el div por un botón nativo, pero el informe del 2026-10-01 aún reporta un div.] [fuente: docs/decisions/0001-boton-nativo.md]

## Reflexión
[DATO FALTANTE: qué salió mal, qué cambiaría y qué aprendí. Es la voz de quien hizo el proyecto y ninguna fuente la contiene.]
Las fuentes ya documentan límites que esta sección puede retomar: Figma sin publicar, sin SUS en la ronda 1, sin tiempo en tarea, sin persona usuaria de tecnología de apoyo y una auditoría solo estática. [fuente: docs/design/README.md, docs/testing/README.md, docs/research/README.md, docs/accessibility/informe-wcag22-2026-10-01.md]

## Enlaces
- Demo: [DATO FALTANTE: no figura en las fuentes]
- Repositorio: [DATO FALTANTE: no figura en las fuentes]
- Figma: [DATO FALTANTE: "pendiente", aún no hay archivo público] [fuente: docs/design/README.md]
- Storybook: [DATO FALTANTE: no figura en las fuentes]
- Informe de accesibilidad: `docs/accessibility/informe-wcag22-2026-10-01.md`

---

## 2. Resumen de 60 segundos

**Café Aurora: de "¿se guardó mi pedido?" a una tarea sin errores**

*Proyecto de muestra ficticio: no es un cliente real y todos los datos son de muestra.*

**Problema.** Quien pide café de especialidad en línea no sabe si su pedido quedó guardado y abandona. En 5 entrevistas con personas de muestra, 4 de 5 abandonaron o repitieron el pedido por no ver confirmación.

**Qué se hizo.** El PRD fijó tres requisitos: mensaje de estado junto al botón (Must), fecha día/mes/año con selector (Must) y repetir el último pedido (Could). El estado de este último no figura en las fuentes. El stack fue HTML, CSS y JavaScript sin framework. Se reemplazó un div que hacía de botón por un `<button type="submit">` nativo, para que se opere con teclado y lector de pantalla.

**Validación.** Dos rondas de 5 personas de muestra. La tarea sin errores pasó de 3 de 5 (60 %) en la v1 a 5 de 5 (100 %) en la v2, con una meta de 80 %. El SUS de la v2 fue 72, con una meta de 68. La ronda 1 no midió SUS, así que no hay "antes" para comparar.

**Accesibilidad.** La auditoría estática del 2026-10-01 reporta 8 fallos (2 críticos, 3 graves, 3 moderados) y cobertura de 11 de 13 criterios. La meta de 100 % de criterios AA no se cumple en ese informe. Lighthouse no se midió. No hubo persona usuaria de tecnología de apoyo.

**Límites.** Muestras de 5 personas, proto-persona sin validar y tiempo en tarea sin medir.

**Pendiente.** Rol, duración, enlaces y reflexión.

---

## 3. Blurb de portafolio

**Café Aurora: confirmar un pedido de café sin dudas**

Proyecto de muestra ficticio. Cierra la incertidumbre de "¿se guardó mi pedido?" con retroalimentación visible, fecha clara y un botón nativo. En dos rondas de 5 personas de muestra, la tarea sin errores subió de 60 % a 100 % y el SUS fue 72. Auditoría WCAG estática con 8 fallos reportados.

---

## Autoverificación

- Encabezados: siguen la plantilla, en orden y en español.
- Cifras: todas salen de las fuentes citadas. El 40 % de diferencia es 100 − 60 puntos porcentuales.
- Citas: todas apuntan a archivos que existen.
- Privacidad: no aparece ningún nombre, empleador ni teléfono de las notas crudas, ni su cita textual.
- Muestra: el aviso de proyecto ficticio está en los tres textos.
- Resumen y blurb: solo usan cifras del caso completo. El resumen dice "5 entrevistas", dato presente en el caso.

## Por revisar antes de publicar

1. **Informe de accesibilidad.** Describe un formulario de suscripción en un "sitio ficticio" y reporta un div como botón, diez días después de que el ADR lo corrigiera. Puede ser otro artefacto o una versión anterior. Hasta que lo aclares, la sección de accesibilidad queda con reserva y la meta WCAG figura como no cumplida.
2. **Voz.** Como no sé tu rol ni si hubo equipo, usé primera persona solo en las acciones documentadas como propias del proceso. Ajusta la voz cuando llenes el rol.
3. **Reflexión.** Necesito tu texto. Puedo redactarla si me cuentas qué cambiarías.
