# Esquema del informe

`wcag22-audit` y `heuristic-review-es` entregan el mismo formato: un informe en Markdown con siete secciones fijas y **un bloque JSON final** con la etiqueta `ux-skills-findings`. El Markdown es para personas; el JSON es para otras herramientas. Dicen lo mismo y se validan con `scripts/validate_report.py`.

## Las siete secciones

| Marcador | Contenido |
|---|---|
| `summary` | Veredicto, conteo por gravedad y cobertura calculada |
| `scope` | Modo usado, qué se revisó, capacidades detectadas, fecha |
| `findings` | Un bloque por fallo, de mayor a menor gravedad |
| `manual` | Lo que no se pudo decidir y cómo comprobarlo |
| `passed` | Criterios verificados como correctos, con evidencia |
| `honest-gaps` | Qué no se revisó y por qué; nunca queda vacía |
| `next-steps` | Máximo 5 acciones priorizadas |

## Estados de cada criterio

| Estado | Significado |
|---|---|
| `fail` | Hay evidencia directa de un incumplimiento |
| `pass` | Se verificó con evidencia que se cumple |
| `manual` | Ninguna herramienta puede decidirlo en este modo (con `manual_check`) |
| `not_applicable` | El criterio no puede aplicar (por ejemplo, no hay video) |
| `not_tested` | No se miró porque el modo no tiene el dato |

## Gravedad y confianza

La **gravedad** es por impacto, no por el nivel de WCAG: `critical`, `serious`, `moderate`, `minor`, `info`; solo se asigna a los `fail`.

La **confianza** (`high`, `medium`, `low`) nunca supera el techo del método:

| Método | Techo |
|---|---|
| `axe`, `dom_runtime`, `token_script` | alta |
| `static_code`, `design_context` | media |
| `screenshot`, `inferred` | baja |

## Cobertura

`cobertura = criterios evaluados / criterios aplicables`, contando **cada criterio una sola vez** aunque tenga varios hallazgos. Un criterio está evaluado si tiene al menos un `pass` o un `fail`. Se calcula desde el JSON; el validador rechaza una cobertura que no coincida.

## El bloque JSON

```json
{
  "schema_version": "1",
  "skill": "wcag22-audit",
  "language": "es",
  "mode": "code",
  "scope": { "summary": "...", "inputs": ["index.html"], "capabilities": { "browser": false, "figma": false, "axe": false, "script": false } },
  "findings": [{
    "id": "WCAG-1.1.1-001",
    "criterion": { "system": "WCAG22", "id": "1.1.1", "name": "Non-text Content", "level": "A", "url": "https://..." },
    "status": "fail", "severity": "serious", "confidence": "medium", "method": "static_code",
    "evidence": [{ "kind": "code", "file": "index.html", "line": 18, "snippet": "<img ...>" }],
    "recommendation": "..."
  }],
  "honest_gaps": ["..."]
}
```

Reglas del JSON: las claves y valores van **siempre en inglés**, y `criterion.name` es el `name_en` exacto de los datos (por ejemplo `Keyboard`), nunca una traducción. El esquema completo está en `shared/schema/report.schema.json`.

## Qué valida el validador

Un solo bloque JSON válido contra el esquema, las siete secciones, el pie legal, que cada criterio exista con su nombre, nivel y enlace exactos, los techos de confianza, que la gravedad solo esté en los `fail`, que no haya ids repetidos y que la cobertura declarada coincida con la calculada.
