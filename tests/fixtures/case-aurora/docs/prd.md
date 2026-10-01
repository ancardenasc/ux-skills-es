# PRD - Fase 2: Definición

## Declaración del problema
Las personas que piden café en línea no saben si su pedido quedó guardado y abandonan el proceso (insight I-01).

## Requisitos funcionales
| ID | Requisito | Insight de origen | Criterio de aceptación |
|---|---|---|---|
| RF-01 | Mostrar el estado de guardado con éxito o error junto al botón | I-01 | Tras pulsar guardar aparece un mensaje en menos de 2 segundos |
| RF-02 | Pedir la fecha en formato día/mes/año con selector | I-02 | Ninguna persona escribe la fecha en el orden equivocado |
| RF-03 | Ofrecer repetir el último pedido | I-03 | Un botón repite el pedido anterior |

## Requisitos no funcionales
| ID | Requisito | Criterio de aceptación |
|---|---|---|
| RNF-02 | Accesibilidad nivel AA | Ver informes en `docs/accessibility/` |

## Alcance (MoSCoW)
- **Must:** RF-01, RF-02
- **Could:** RF-03
