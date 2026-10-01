<!-- GENERADO desde shared/templates/report.es.md por scripts/build.py. No editar a mano. -->
# Informe de auditoría: {objetivo}

<!-- section:summary -->
## Resumen

- **Veredicto:** {una línea con el estado general y la decisión recomendada}
- **Hallazgos que fallan:** {n} (Crítico {n} · Grave {n} · Moderado {n} · Menor {n})
- **Requieren prueba manual:** {n}
- **Cobertura:** {evaluados} de {aplicables} criterios aplicables en este modo

<!-- section:scope -->
## Alcance

- **Modo:** {Código o diff | URL | Diseño | Mixto}
- **Qué se revisó:** {archivos, páginas, estados o frames}
- **Capacidades detectadas:** navegador {sí/no} · Figma {sí/no} · axe {sí/no} · script {sí/no}
- **Fecha:** {AAAA-MM-DD}

<!-- section:findings -->
## Hallazgos

### {Gravedad}: {título}

- **Criterio:** {id} {nombre} (nivel {A|AA}), {enlace}
- **Dónde:** {archivo:línea o selector}
- **Qué pasa:** {descripción en palabras propias}
- **Confianza:** {Alta | Media | Baja}, método: {método}
- **A quién afecta:** {frase corta}
- **Cómo corregirlo:** {recomendación concreta}

<!-- section:manual -->
## Verificación manual

| Criterio | Por qué no se pudo decidir | Cómo comprobarlo |
|---|---|---|
| {id} {nombre} | {motivo} | {procedimiento y herramienta sugerida} |

<!-- section:passed -->
## Criterios aprobados

{lista de criterios verificados como correctos y con qué evidencia}

<!-- section:honest-gaps -->
## Brechas honestas

- {límites del modo usado}
- {páginas, estados o criterios que no se revisaron}
- {herramientas que no estaban disponibles}

<!-- section:next-steps -->
## Próximos pasos

1. {acción priorizada, máximo 5}

---

*{pie legal: ver etiqueta disclaimer en labels.yml}*

```json ux-skills-findings
{bloque JSON que valida contra report.schema.json}
```
