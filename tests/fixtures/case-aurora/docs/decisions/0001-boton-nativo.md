# ADR-0001: Usar un botón nativo para confirmar el pedido

- Estado: aceptada
- Fecha: 2026-09-20

## Contexto
La primera versión usaba un div con un manejador de clic, que no recibe foco ni se anuncia como botón.

## Decisión
Usar el elemento `<button type="submit">` para confirmar el pedido.

## Alternativas consideradas
- Mantener el div y añadirle `role="button"` y manejadores de teclado.

## Consecuencias
Mejora la operabilidad con teclado y lectores de pantalla sin código extra. Obliga a revisar los estilos del botón.
