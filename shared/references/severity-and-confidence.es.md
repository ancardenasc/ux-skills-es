# Gravedad y confianza

## Gravedad (por impacto, no por nivel WCAG)

Un fallo de nivel A en una página casi sin uso puede ser `moderate`; uno de nivel AA en el flujo de pago puede ser `critical`.

| Gravedad | Cuándo |
|---|---|
| `critical` | Bloquea una tarea central para un grupo de usuarios y no hay alternativa |
| `serious` | Barrera importante; existe un rodeo pero es difícil de encontrar o usar |
| `moderate` | Fricción o barrera con rodeo razonable |
| `minor` | Buena práctica o impacto bajo |
| `info` | Recomendación sin incumplimiento |

La gravedad solo se asigna a hallazgos `fail`.

## Confianza y techo por método

La confianza describe qué tan seguro es el hallazgo según cómo se obtuvo. Nunca supera el techo del método:

| Método | Techo | Motivo |
|---|---|---|
| `axe`, `dom_runtime`, `token_script` | alta | Se midió sobre la página real o con un cálculo determinista |
| `static_code`, `design_context` | media | Se leyó el código o los datos del diseño, sin ver el resultado renderizado |
| `screenshot`, `inferred` | baja | Solo imagen o deducción; no se ve ARIA, semántica ni teclado |

Regla práctica: `alta` exige evidencia directa (medida, o marcado inequívoco). Si dudas, baja un nivel y dilo en la descripción.
