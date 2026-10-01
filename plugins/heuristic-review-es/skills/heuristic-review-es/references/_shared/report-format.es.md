<!-- GENERADO desde shared/references/report-format.es.md por scripts/build.py. No editar a mano. -->
# Formato del informe

Cada auditoría produce **un informe en Markdown** con las secciones de la plantilla (`report.es.md`, mismos marcadores `<!-- section:id -->`) y **un bloque JSON final** con la etiqueta `ux-skills-findings` que valida contra `report.schema.json`. El Markdown es para personas; el JSON es para otras herramientas. Deben decir lo mismo.

## Reglas

1. **Evidencia o nada.** Un hallazgo `fail` lleva al menos una evidencia real: `archivo:línea`, selector, medida o captura. No inventes líneas, selectores ni valores.
2. **Palabras propias.** Describe cada criterio con tus palabras. No copies ni traduzcas el texto de WCAG ni de Nielsen; cita número, nombre, nivel y enlace (ver `legal-copyright-rules.md`).
3. **Nunca declares "pasa" lo que no puedes decidir.** Lo que exige lector de pantalla, juicio sobre el orden del foco sin runtime o calidad de textos alternativos va a `manual`, con `manual_check`.
4. **Estados:** `fail`, `pass`, `manual`, `not_applicable` (el criterio no puede aplicar, por ejemplo no hay video) y `not_tested` (no se miró porque el modo no tiene el dato; va a las brechas).
5. **Ids:** `WCAG-<criterio>-<NNN>` o `NIELSEN-<Hn>-<NNN>`, con NNN consecutivo. `dedup_key`: `<criterio>|<archivo:línea o selector>`.
6. **Etiquetas por idioma** salen de `labels.yml`. Las claves y valores máquina del JSON van siempre en inglés: en `criterion.name` copia **exactamente** `name_en` de `wcag22-criteria.json` (por ejemplo `Keyboard`), nunca la etiqueta en español. La etiqueta propia `label_es` solo se muestra en el Markdown, junto al id y al nombre en inglés.
7. **Pie fijo:** incluye la etiqueta `disclaimer` del idioma antes del bloque JSON.
8. **Brechas honestas** nunca va vacía (ver `honest-gaps.es.md`). La cobertura (evaluados / aplicables) se calcula desde los hallazgos, no se afirma.

## Orden de las secciones

resumen, alcance, hallazgos (de mayor a menor gravedad), verificación manual, criterios aprobados, brechas honestas, próximos pasos (máximo 5).
