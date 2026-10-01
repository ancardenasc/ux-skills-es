# Verificaciones en diseño (modo C)

Para Figma, capturas o imágenes pegadas. Confianza máxima: `medium` con datos de diseño (variables, medidas), `low` con una captura sola. En diseño **no se ve ARIA, semántica, teclado ni estados dinámicos**: eso va a `manual` o `not_tested`.

## Obtener los datos

- **Figma:** si hay herramientas de Figma en la sesión, usa las de lectura: variables y estilos definidos, contexto de diseño del frame y captura. Declara en `scope.capabilities.figma` que las usaste. Sin herramientas, pide capturas o exportaciones.
- **Capturas:** muestrea colores, mide tamaños en píxeles y anota a qué resolución y escala corresponden. Si una medida depende de la escala de la imagen, dilo y baja la confianza.
- Nunca asumas el contenido de un frame que no pudiste ver.

## Qué se evalúa bien en diseño

| Criterio | Cómo | Notas |
|---|---|---|
| 1.4.3, 1.4.11 | Contraste entre el color del texto (o del borde/icono) y su fondo, con la fórmula de [verificaciones en código](checks-code.md) | Si el fondo es imagen o degradado, `manual`. Evalúa también los estados (hover, foco, deshabilitado aparte, error) |
| 1.4.1 | Busca información que solo se distingue por color (estados, gráficas, errores) | |
| 1.4.4, 1.4.12 | Tamaño de texto base y márgenes para ampliar sin romper el layout | Solo indicios |
| 2.5.8 | Medidas de botones, iconos y campos en el frame, convertidas a píxeles CSS | `partial` si la escala no es 1:1 |
| 2.4.7, 2.4.11 | Existe un diseño del estado de foco y no queda cubierto por elementos fijos | Que esté diseñado no prueba que se implemente |
| 1.3.3 | Instrucciones que dependen de forma, color o posición | |
| 3.3.1, 3.3.2, 3.3.3 | Diseño de errores, etiquetas visibles y sugerencias | Verifica que el error no use solo color |
| 3.2.3, 3.2.4, 3.2.6 | Coherencia de navegación, identificación y ayuda entre pantallas del flujo | Requiere varias pantallas |
| 3.3.7, 3.3.8 | Flujos: se repite información ya dada; método de autenticación | |
| 2.5.7 | Interacciones de arrastrar con alternativa de un puntero | |

## Qué no se puede decidir

Nombre, rol y valor (4.1.2), orden del foco (2.4.3), lector de pantalla, reflujo real (1.4.10), movimiento y animaciones: `manual` o `not_tested`, con el procedimiento para comprobarlo cuando el diseño esté implementado.

## Recomendaciones útiles en diseño

Propón correcciones accionables sobre el propio diseño: el color alternativo que cumple el contraste (verifica el cálculo), el tamaño mínimo del objetivo, el estado de foco que falta, la anotación de accesibilidad que debe acompañar al handoff (orden de foco, nombre, rol, textos alternativos).
