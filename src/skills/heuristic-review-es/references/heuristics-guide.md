# Guía de revisión heurística

Texto propio, no de NN/g. Para cada heurística se da su nombre oficial en inglés (el que va en el JSON) y una etiqueta propia en español. Los enlaces y el nombre exacto están en `nielsen-heuristics.json`.

## Método

1. **Elige tareas reales.** Una tarea es lo que la persona quiere lograr, no una pantalla. Dos o tres bastan.
2. **Recorre sin saltarte pasos.** Para cada paso anota: qué ve, qué puede hacer, qué respuesta recibe.
3. **Evalúa heurística por heurística** contra lo anotado, no de memoria.
4. **Cada problema lleva evidencia**: línea de código, selector, frame o captura. Sin evidencia, no es un hallazgo.
5. **Un problema, una causa.** Si dos heurísticas se rompen por lo mismo, repórtalo una vez en la principal y menciona la otra.
6. **Recomienda algo concreto** que se pueda hacer y verificar.

## Gravedad (con la rúbrica compartida)

Pregúntate: ¿a cuánta gente afecta? ¿con qué frecuencia? ¿se puede salir del problema fácilmente? ¿tiene consecuencias que no se deshacen (pérdida de datos, dinero, confianza)? Un borrado sin confirmación suele ser `serious` o `critical`; una etiqueta inconsistente, `moderate`; un detalle estético, `minor`.

## Las diez heurísticas

### H1 · Visibility of System Status (Visibilidad del estado del sistema)
- **Qué mirar:** qué respuesta recibe la persona tras cada acción: cargando, éxito, error, progreso en procesos largos.
- **Señales de problema:** peticiones sin indicador de carga ni resultado; botones que no cambian al pulsarse; procesos largos sin avance; estados que cambian sin avisar.
- **En código:** `fetch`/`XMLHttpRequest` sin manejo visible del resultado; ausencia de estados de carga; contenido que cambia sin `aria-live` (relacionado con WCAG 4.1.3).

### H2 · Match Between the System and the Real World (Correspondencia con el mundo real)
- **Qué mirar:** palabras, iconos, orden y formatos frente a lo que la persona conoce.
- **Señales:** jerga técnica o interna; nombres de la base de datos como etiquetas; formatos de fecha, moneda o teléfono que no son los locales; metáforas que no corresponden.
- **Lente de contexto (propuesta propia):** registro y tratamiento coherentes (tú, usted o vos), formatos locales de fecha y de números, anglicismos innecesarios.

### H3 · User Control and Freedom (Control y libertad del usuario)
- **Qué mirar:** cómo se sale de un flujo, se cancela o se deshace.
- **Señales:** no hay "Cancelar" ni "Volver"; acciones destructivas sin deshacer; modales sin cierre; flujos que no permiten corregir un paso anterior.
- **Casi siempre requiere ejecutar el flujo:** en modo código suele quedar en `manual`.

### H4 · Consistency and Standards (Consistencia y estándares)
- **Qué mirar:** que lo igual se vea y se llame igual, y que se respeten las convenciones de la plataforma.
- **Señales:** botones distintos para la misma acción; el mismo concepto con nombres diferentes; patrones que contradicen lo habitual (enlaces que parecen botones, iconos con significado inusual).
- **Cuidado:** que algo sea consistente en un lugar y no en otro es un `fail` y un `pass` a la vez, con evidencias distintas.

### H5 · Error Prevention (Prevención de errores)
- **Qué mirar:** si el diseño evita el error antes de que ocurra.
- **Señales:** acciones destructivas sin confirmación; campos sin restricciones ni formato guía; valores por defecto peligrosos; botones de riesgo junto a los de uso común.
- **En código:** `DELETE`/borrado directo desde un clic; ausencia de validación previa; `type`, `min`, `max`, `pattern` que no se usan donde ayudarían.

### H6 · Recognition Rather than Recall (Reconocer en lugar de recordar)
- **Qué mirar:** si la persona puede ver sus opciones en vez de recordarlas.
- **Señales:** iconos sin etiqueta ni título; información que hay que memorizar de una pantalla a otra; comandos ocultos; formularios sin ejemplos de formato.
- **Relación con WCAG:** botones solo de icono sin nombre también incumplen 4.1.2; repórtalos aquí como problema de usabilidad y menciónalo.

### H7 · Flexibility and Efficiency of Use (Flexibilidad y eficiencia de uso)
- **Qué mirar:** atajos, valores recordados, personalización, acciones en lote para quien ya sabe usar el producto.
- **Señales:** quien repite una tarea la hace siempre igual de larga; no hay búsqueda, favoritos ni autocompletado.
- **Casi siempre `manual`:** hay que observar uso real.

### H8 · Aesthetic and Minimalist Design (Diseño estético y minimalista)
- **Qué mirar:** si cada elemento aporta o compite con lo importante.
- **Señales:** pantallas con muchas acciones al mismo nivel; texto largo donde bastaba una frase; elementos decorativos que distraen de la tarea; jerarquía visual poco clara.
- **Mejor en URL o diseño**: en código solo hay indicios.

### H9 · Help Users Recognize, Diagnose, and Recover from Errors (Reconocer, diagnosticar y recuperarse de errores)
- **Qué mirar:** el texto y el comportamiento cuando algo falla.
- **Señales:** códigos internos en lugar de explicaciones; mensajes que culpan a la persona; errores sin indicar qué campo corregir ni cómo; se pierde lo escrito al fallar.
- **Relación con WCAG:** 3.3.1 y 3.3.3 miran lo mismo desde accesibilidad; aquí se evalúa la claridad y la ayuda para recuperarse.
- **Lente de contexto (propuesta propia):** el mensaje se entiende en español claro, sin traducciones literales ni jerga.

### H10 · Help and Documentation (Ayuda y documentación)
- **Qué mirar:** si hay ayuda cuando se necesita y si es fácil de encontrar y de usar.
- **Señales:** no hay enlace de ayuda ni contacto; la ayuda es un documento largo sin buscador; no se ofrece ayuda en el punto donde surge la duda.

## Lentes de contexto (propuesta propia, no de NN/g)

Úsalas como preguntas adicionales dentro de las heurísticas anteriores, no como una undécima heurística:

- **Lenguaje:** ¿el texto está en español natural, con un registro coherente y sin términos internos?
- **Formatos locales:** ¿fechas, moneda, teléfonos, direcciones y separadores siguen lo que la audiencia espera?
- **Conectividad y dispositivos:** ¿el flujo aguanta una conexión lenta o intermitente y pantallas pequeñas, con respuesta visible mientras espera?
- **Confianza en pagos y datos:** ¿se explica por qué se pide un dato y qué pasará con él?
- **Lectura accesible:** ¿las frases son cortas y las instrucciones se entienden sin conocimiento previo?

## Lo que no es una revisión heurística

No mide tiempos ni éxito de tareas, no sustituye el contacto con personas usuarias y no evalúa el cumplimiento de WCAG. Si el problema es de accesibilidad técnica, derívalo a `wcag22-audit`.
