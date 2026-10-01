# Modos de entrada

Detecta, no exijas. El paso 0 de cada auditoría decide el modo según lo que tengas y lo declara en la sección Alcance.

## Detección de capacidades

1. ¿Te dieron una ruta o un diff? ¿Una URL? ¿Un diseño (imagen o enlace a Figma)?
2. ¿Qué herramientas hay en la sesión? Navegador (Playwright, Chrome DevTools o similar), Figma (lectura de variables, contexto de diseño y capturas), `axe` ya instalado en el proyecto, `python3` para scripts.
3. Anota el resultado en `scope.capabilities` del JSON.

## Los tres modos

| Modo | Cómo | Confianza máx. | Cubre bien | No puede cubrir |
|---|---|---|---|---|
| **A. Código o diff** | `git diff $(git merge-base <base> HEAD)` contra el working tree (incluye lo no commiteado; `base...HEAD` solo compara commits y saldría vacío) o rutas indicadas | media | alt, etiquetas, puntos de referencia, títulos, `lang`, nombre y rol en el marcado, `outline:none`, autocomplete | contraste real con la cascada, orden del foco, reflujo, todo lo que decide JavaScript |
| **B. URL** | Navegador: snapshot de accesibilidad, estilos calculados, redimensionar a 320 px, recorrer con Tab, emular movimiento reducido | alta en lo medido | contraste calculado, foco visible, reflujo, nombre accesible | lector de pantalla, calidad de subtítulos, páginas con login sin credenciales |
| **C. Diseño** | Variables, contexto o capturas de Figma, o imágenes pegadas | baja a media | contraste entre colores muestreados, tamaño de objetivos, jerarquía, señales solo por color | ARIA, semántica, teclado, estados dinámicos |

El campo `assessable` de `wcag22-criteria.json` indica, por criterio, qué tanto se puede evaluar en cada modo (`yes`, `partial`, `no`). Lo que sea `no` o `partial` en el modo actual va a `manual` o `not_tested`.

## Reglas

- Sin herramienta ni URL: usa el modo A o C y dilo. Con URL pero sin navegador: pide HTML o capturas, no adivines el contenido.
- **axe:** úsalo solo si ya está en el proyecto o la persona aprueba una ejecución local con `npx`. Nunca lo inyectes desde un CDN.
- Nunca inventes contenido de una página que no pudiste ver.
- Un diff sin cambios de frontend no se aprueba: responde "no aplica" y di por qué.
