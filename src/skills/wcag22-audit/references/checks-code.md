# Verificaciones en código (modo A)

Aplica a HTML, JSX/TSX, Vue, plantillas y CSS. Por criterio: qué buscar, cuándo falla y qué **no** puedes decidir leyendo código (eso va a `manual`). La confianza máxima de este modo es `medium`.

En componentes de un framework, los atributos pueden venir de props o de librerías: si no ves el resultado renderizado, baja la confianza y dilo. En JSX los atributos son `htmlFor`, `className`, `tabIndex`; en Vue, `:aria-*` y `@click`.

## Contraste calculado

Solo si ambos colores son **valores literales** o variables que resuelves con certeza. Para cada canal sRGB: `c = valor/255`; si `c <= 0.04045` entonces `c/12.92`, si no `((c+0.055)/1.055)^2.4`. Luminancia `L = 0.2126·R + 0.7152·G + 0.0722·B`. Razón = `(L_claro + 0.05) / (L_oscuro + 0.05)`. Compara el valor **sin redondear hacia arriba** (4.499 falla; muéstralo como 4.49 o 4.50 solo si coincide con el cálculo). Texto grande: desde 24 px, o 18.66 px en negrita. Con transparencias, degradados, imágenes de fondo o estilos que no resuelves: no calcules, pasa a `manual`.

## Perceptible

| Criterio | Qué buscar | Falla cuando | No lo decides (manual) |
|---|---|---|---|
| 1.1.1 | `<img>`, `<input type="image">`, `<area>`, `<svg>` informativos, iconos de fuente, botones solo de icono | `<img>` sin `alt`; `alt` que es el nombre del archivo; botón de icono sin nombre accesible | Si el texto alternativo describe bien lo que comunica la imagen |
| 1.2.x | `<video>`, `<audio>`, iframes de reproductores | Sin `<track kind="captions">` ni transcripción cercana (1.2.2); sin alternativa para solo audio o solo video (1.2.1) | Subtítulos incrustados en el video, calidad y sincronía; audiodescripción; en vivo (1.2.4) |
| 1.3.1 | Títulos, listas, tablas, formularios, regiones | Títulos hechos con `<div>` o `<b>`; saltos de nivel; listas con `<br>`; tablas de datos sin `<th>`/`scope`; tablas de maquetación con semántica de datos; grupos de radio sin `fieldset`/`legend`; `aria-*` o roles incorrectos | Si la estructura visible coincide con la del código en todos los estados |
| 1.3.2 | `order`, `row-reverse`, `position: absolute`, `tabindex` mayor que 0 | Orden del DOM que cambia el sentido al leerse en secuencia | La secuencia real renderizada |
| 1.3.3 | Textos de instrucciones | "Pulsa el botón verde", "el de la derecha" como única pista | Todo el contenido en lenguaje natural |
| 1.3.4 | `@media (orientation)`, `screen.orientation.lock`, manifiesto con `orientation` | Se bloquea una orientación sin que sea esencial | Si hay una razón esencial |
| 1.3.5 | Campos de nombre, correo, teléfono, dirección, tarjeta | Falta un `autocomplete` válido en campos de datos del propio usuario | Campos que no piden datos del usuario |
| 1.4.1 | Enlaces dentro de texto, mensajes de error, estados | Enlace en texto corrido sin subrayado ni otra pista que no sea color; error indicado solo en rojo | Gráficos y gráficas |
| 1.4.2 | `autoplay` en `<audio>`/`<video>` | Suena más de 3 s sin controles ni silencio | Duración real |
| 1.4.3 | Colores de texto y fondo | Contraste calculado menor que 4.5:1 (3:1 si es texto grande); excluye texto deshabilitado y logotipos | Texto sobre imágenes, degradados o transparencias |
| 1.4.4 | `<meta viewport>`, unidades de fuente | `user-scalable=no` o `maximum-scale` menor que 2; contenedores de altura fija con `overflow: hidden` sobre texto | Comportamiento real al ampliar al 200 % |
| 1.4.5 | Imágenes con nombres como "banner-texto" | Texto real maquetado como imagen sin necesidad | Si la imagen contiene texto |
| 1.4.10 | `min-width`, `width` fijo mayor que 320 px, `overflow-x`, tablas anchas | Anchos fijos que obligan a scroll horizontal a 320 px | El reflujo real (modo URL) |
| 1.4.11 | Bordes de campos y botones, iconos, estados | Contraste literal menor que 3:1 del borde o icono necesario para entender el control | Gráficos con degradados |
| 1.4.12 | `line-height`, `letter-spacing`, alturas fijas | Alturas fijas o `!important` que impiden ajustar el espaciado y recortan texto | El recorte real |
| 1.4.13 | Tooltips y menús con `:hover` | Contenido que aparece solo con `:hover` (no con foco), que no se puede descartar o que desaparece al mover el puntero hacia él | Persistencia real |

## Operable

| Criterio | Qué buscar | Falla cuando | No lo decides (manual) |
|---|---|---|---|
| 2.1.1 | `onclick` en `div`/`span`, `<a>` sin `href`, eventos solo de ratón | Elemento interactivo sin `tabindex`, sin rol y sin manejador de teclado; acción solo con `mouseover`/`mousedown` | Comportamiento de componentes complejos |
| 2.1.2 | Modales, `focus()` forzado | Un componente captura el foco sin salida con teclado | Trampas dinámicas |
| 2.1.4 | `keydown`/`keypress` globales | Atajo de una sola tecla sin forma de desactivarlo o remapearlo | Que el atajo esté activo en uso real |
| 2.2.1 | `setTimeout`, `<meta http-equiv="refresh">`, caducidad de sesión | Límite de tiempo sin aviso ni forma de extender | Los límites impuestos por el servidor |
| 2.2.2 | Carruseles automáticos, `animation-iteration-count: infinite`, `<marquee>`, `<blink>` | Movimiento que dura más de 5 s sin control para pausar | Si el movimiento es esencial |
| 2.3.1 | Animaciones rápidas | Parpadeo evidente de alta frecuencia (rara vez decidible en código) | Casi siempre |
| 2.4.1 | Enlace de salto, landmarks (`main`, `nav`) | No hay enlace de salto ni regiones que permitan saltar bloques repetidos | Que el enlace funcione |
| 2.4.2 | `<title>` | Ausente, vacío o genérico ("Document", "Untitled") | Si describe bien la página |
| 2.4.3 | `tabindex` positivo, orden DOM frente al visual, modales sin gestión de foco | Indicios de orden ilógico | El orden real: siempre `manual` |
| 2.4.4 | Texto de los enlaces | "Aquí", "leer más", "clic" sin contexto programático (aria-label, texto oculto, párrafo contiguo) | Si el contexto es suficiente |
| 2.4.5 | Buscador, mapa del sitio, menú | Solo hay una forma de llegar a las páginas (en un conjunto) | Sitios completos |
| 2.4.6 | Títulos y etiquetas | Vacíos o genéricos | Si describen bien |
| 2.4.7 | `outline: none` o `0` en `:focus`/`:focus-visible` | Se quita el contorno y no hay un reemplazo visible (borde, sombra, fondo) | Si el reemplazo es suficientemente visible |
| 2.5.1 / 2.5.2 / 2.5.4 | `touchstart`, `pointerdown`, gestos multitáctiles, `devicemotion` | Gesto de varios puntos o trayectoria sin alternativa de un puntero; acción al presionar sin poder cancelar; función solo por movimiento | Comportamiento real |
| 2.5.3 | `aria-label`, texto visible | El nombre accesible no contiene el texto visible de la etiqueta | Etiquetas generadas |
| 2.5.7 | `draggable`, librerías de arrastrar y soltar | Acción que solo se logra arrastrando, sin botones alternos | Que la alternativa funcione |
| 2.5.8 | `width`/`height`/`padding` literales de botones, enlaces e iconos | Objetivo menor que 24×24 px CSS sin espacio compensatorio. Excepciones: enlace dentro de una frase, control nativo sin estilizar, equivalente accesible | Tamaños que resultan del layout |

## Comprensible

| Criterio | Qué buscar | Falla cuando | No lo decides (manual) |
|---|---|---|---|
| 3.1.1 | `<html lang>` | Ausente o con un código inválido | Si coincide con el idioma real |
| 3.1.2 | Pasajes en otro idioma | Sin atributo `lang` en el pasaje (salvo nombres propios y términos técnicos) | Detectar todos los pasajes |
| 3.2.1 / 3.2.2 | `onfocus`, `onchange` | Recibir foco o cambiar un valor navega, envía o cambia el contexto sin aviso | Comportamiento real |
| 3.2.3 / 3.2.4 / 3.2.6 | Plantillas de navegación y ayuda | Solo evaluable comparando varias páginas | Casi siempre |
| 3.3.1 | `aria-invalid`, `aria-describedby`, mensajes de error | Error comunicado solo con color o ícono; mensajes genéricos sin descripción | Mensajes generados por el servidor |
| 3.3.2 | `<label>`, `aria-label`, `placeholder`, `fieldset` | Campo sin etiqueta asociada; placeholder como única etiqueta; grupo sin leyenda | Que la etiqueta sea clara |
| 3.3.3 / 3.3.4 / 3.3.7 | Formularios de pago, borrado o datos largos | Indicios: envíos críticos sin confirmación ni revisión; se repiden datos ya dados | Flujos completos |
| 3.3.8 | `autocomplete="off"` en contraseñas, `onpaste` bloqueado, CAPTCHA de puzzle | Se impide pegar o usar gestor de contraseñas, o se exige una prueba cognitiva sin alternativa | Alternativas fuera del código |

## Robusto

| Criterio | Qué buscar | Falla cuando | No lo decides (manual) |
|---|---|---|---|
| 4.1.2 | `div`/`span` interactivos, `role`, `aria-*`, `<iframe>` | Elemento interactivo sin rol ni nombre; rol o `aria-*` inválido; botón de icono sin nombre; control propio sin estado (`aria-expanded`, `aria-checked`); `<iframe>` sin `title` | Cómo lo anuncia cada lector |
| 4.1.3 | Toasts, errores dinámicos, contadores | Mensaje que aparece sin `role="status"`, `role="alert"` o `aria-live` | El anuncio real |

## Notas de método

- Una **ausencia** en el código no es evidencia de que esté bien: para `pass` necesitas ver lo que cumple (la línea concreta).
- Un hallazgo estático con un solo indicio es `medium`; si dependes de una suposición sobre cómo se renderiza, `low`.
- Anota siempre `archivo:línea` y copia el fragmento mínimo (máx. 300 caracteres).
