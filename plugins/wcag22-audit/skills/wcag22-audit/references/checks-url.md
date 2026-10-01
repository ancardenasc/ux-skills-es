# Verificaciones en una página real (modo B)

Requiere una herramienta de navegador (Playwright, Chrome DevTools, automatización de Chrome o similar). Los nombres cambian por herramienta: usa los equivalentes de **abrir página, capturar snapshot de accesibilidad, evaluar JavaScript en la página, redimensionar, pulsar teclas, emular medios y tomar captura**. Confianza: `high` en lo que mides; `medium` en lo que deduces.

## Reglas de seguridad

- Solo lectura. No envíes formularios con datos reales, no compres, no borres, no inicies sesión con credenciales que no te dieron.
- No dispares diálogos `alert/confirm/prompt`. Si el flujo los requiere, avisa y marca el criterio `manual`.
- Si la herramienta no responde tras 2 o 3 intentos, detente y pregunta.
- Los fragmentos de JavaScript de abajo **no modifican la página**, salvo el de espaciado de texto, que añade una hoja de estilos temporal: recarga la página al terminar.
- No cargues `axe` desde un CDN. Úsalo solo si ya está en el proyecto o si la persona aprueba una ejecución local.

## Preparación

Abre la URL, espera a que cargue y anota el estado que auditas (viewport, sesión, idioma). Si hay estados que la persona señaló (menú abierto, error de formulario), recréalos sin enviar datos reales. Cada estado auditado va en la sección Alcance.

## Qué medir

**Estructura y nombre (1.3.1, 2.4.2, 2.4.6, 3.1.1, 4.1.2).** Captura el snapshot de accesibilidad: roles, nombres, esquema de títulos y regiones. Un control sin nombre o con rol incorrecto es un fallo de 4.1.2; títulos saltados, de 1.3.1.

**Contraste (1.4.3, 1.4.11).** Evalúa en la página el color calculado del texto y el de su fondo efectivo (recorre ancestros mezclando alfa). Descarta los elementos con imagen o degradado de fondo (pasan a `manual`):

```javascript
const lum = c => { const f = v => (v /= 255) <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]); };
const parse = s => (s.match(/[\d.]+/g) || []).map(Number);
const over = (top, bottom) => { const a = top[3] ?? 1; return [0, 1, 2].map(i => top[i] * a + bottom[i] * (1 - a)); };
const bgOf = el => { let stack = []; for (let n = el; n; n = n.parentElement) { const s = getComputedStyle(n);
  if (s.backgroundImage !== 'none') return null; const c = parse(s.backgroundColor); if (c.length && (c[3] ?? 1) > 0) stack.push(c);
  if ((c[3] ?? 1) === 1) break; } return stack.reduceRight((acc, c) => over(c, acc), [255, 255, 255]); };
[...document.querySelectorAll('body *')].filter(e => e.childNodes.length && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
  .map(e => { const bg = bgOf(e); if (!bg) return null; const fg = over(parse(getComputedStyle(e).color), bg);
    const [a, b] = [lum(fg), lum(bg)].sort((x, y) => y - x); const ratio = (a + 0.05) / (b + 0.05);
    const px = parseFloat(getComputedStyle(e).fontSize), bold = parseInt(getComputedStyle(e).fontWeight) >= 700;
    const large = px >= 24 || (bold && px >= 18.66); return { sel: e.tagName.toLowerCase() + (e.className ? '.' + String(e.className).split(' ')[0] : ''), ratio: +ratio.toFixed(2), need: large ? 3 : 4.5 }; })
  .filter(r => r && r.ratio < r.need);
```
Compara sin redondear hacia arriba. Para 1.4.11 mide bordes e iconos de controles con el mismo cálculo (umbral 3:1).

**Foco visible y orden (2.4.3, 2.4.7, 2.1.1, 2.1.2).** Pulsa Tab repetidamente y, tras cada pulsación, registra el elemento enfocado (rol, nombre, selector) y toma una captura si hay duda. El indicador es visible si el contorno, sombra o fondo cambia de forma perceptible. Anota el orden real y compáralo con el visual. Si el foco queda atrapado (sin poder salir con teclado), es un fallo de 2.1.2. Todo lo que solo se activa con ratón es 2.1.1.

**Foco no oculto (2.4.11).** Con cada elemento enfocado, comprueba que no queda totalmente tapado por una cabecera fija, banner o diálogo: el punto central del elemento debe devolver el mismo elemento (o un descendiente) con `document.elementFromPoint`.

**Reflujo y zoom (1.4.4, 1.4.10).** Redimensiona el viewport a 320 px de ancho (equivale a un zoom del 400 % sobre 1280 px) y comprueba si `document.documentElement.scrollWidth > document.documentElement.clientWidth` (scroll horizontal) y si algo se corta o se superpone. A 640 px de ancho se aproxima el 200 % de zoom. Excepciones: tablas, mapas, editores, contenido que necesita dos dimensiones.

**Espaciado de texto (1.4.12).** Añade una hoja de estilos temporal con `line-height: 1.5`, `letter-spacing: .12em`, `word-spacing: .16em` y separación de párrafos de `2em` (todo con `!important`) y busca texto recortado o solapado (por ejemplo contenedores con `overflow: hidden` y altura fija). Recarga al terminar.

**Tamaño del objetivo (2.5.8).** Mide `getBoundingClientRect()` de enlaces, botones, campos y elementos con rol interactivo; los de menos de 24×24 px sin espacio compensatorio fallan. Excepciones: enlaces dentro de una frase, controles nativos sin estilizar y objetivos con equivalente accesible.

**Movimiento (2.2.2, 2.3.1).** Emula `prefers-reduced-motion: reduce` y comprueba que las animaciones se detienen o se reducen. Busca carruseles y animaciones infinitas sin control de pausa.

**Contenido al pasar el cursor o enfocar (1.4.13).** Activa el disparador con ratón y con teclado: el contenido debe poder descartarse (Esc), seguir visible mientras el puntero esté sobre él y permanecer hasta cerrarse.

**Formularios (3.3.1, 3.3.2, 3.3.7, 1.3.5).** Comprueba etiquetas, `autocomplete` y mensajes de error. Para ver los errores, provoca validación solo con datos obviamente falsos y solo si la persona lo permitió; si no, deja el criterio en `manual`.

**Mensajes de estado (4.1.3).** Busca regiones `role="status"`, `role="alert"` o `aria-live` y comprueba en el snapshot que los mensajes dinámicos las usan. El anuncio real por lector de pantalla queda `manual`.

## Lo que este modo no cubre

Calidad de lectores de pantalla y de textos alternativos, subtítulos, audiodescripción, páginas con sesión sin credenciales, estados que dependen de datos reales y todo lo que exige juicio humano. Va a `manual` o a las brechas.
