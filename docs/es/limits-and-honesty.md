# Límites y honestidad

Esta colección está diseñada para **decir lo que no sabe**. Aquí está, sin adornos, qué hace y qué no.

## Qué no hacen

- **No certifican conformidad ni dan dictamen legal.** Un informe no es una declaración de conformidad. Lo dice cada informe en su pie.
- **No sustituyen las pruebas con personas ni con lectores de pantalla reales.** Una auditoría automática o heurística encuentra una parte de los problemas.
- **No corrigen código.** Los skills de auditoría son de solo lectura.
- **No evalúan el nivel AAA** de WCAG ni las técnicas de la especificación.
- **No inventan datos.** `case-study-writer` marca lo que falta como `[DATO FALTANTE: ...]` en vez de rellenarlo, y no repite nombres, empleadores ni teléfonos de tus notas.

## Derechos de autor

WCAG es del W3C y las 10 heurísticas son de Jakob Nielsen (Nielsen Norman Group). No existe traducción oficial de WCAG 2.2 al español y NN/g licencia las traducciones de sus textos. Por eso la colección **cita número, nombre, nivel y enlace**, y usa **resúmenes y etiquetas propios** de máximo 25 palabras; nunca copia ni traduce el texto original. Las etiquetas en español (`label_es`) son propias, no la traducción oficial. Ver [NOTICE](../../NOTICE.md).

## Qué se ha verificado y qué no

**Verificado:**

- Los 55 criterios WCAG 2.2 A y AA coinciden con los datos legibles por máquina de W3C (id, nombre y nivel) y sus enlaces responden; se vuelve a comprobar cada semana.
- Los nombres de las 10 heurísticas coinciden con la página de NN/g.
- Cada informe de ejemplo se valida y sus líneas de evidencia se comprueban contra el proyecto ficticio del que salen.
- Los skills se ejecutaron con un modelo real sobre proyectos sembrados con errores conocidos y con partes correctas a propósito: encontraron lo esperado sin marcar lo correcto. Esas ejecuciones destaparon errores del propio repositorio, que se corrigieron.
- La instalación se prueba por cada ruta: carpeta suelta, zip, plugin, `npx skills`, `gh skill` y el instalador.

**Sin verificar todavía:**

- La subida del zip a claude.ai.
- GitHub Copilot en una sesión real: los skills usan el formato abierto que Copilot lee, pero no se han ejecutado allí.
- `wcag22-audit` en modo diseño (Figma o capturas) y `heuristic-review-es` en modos URL y diseño.
- `case-kit` en inglés y `case-study-writer` con `--guardar`.

## Sesgos y límites de método

- Un análisis **estático** de código no ve cómo se renderiza ni cómo se comporta con JavaScript: su confianza máxima es media.
- Una **revisión heurística** hecha por una sola persona (o un modelo) encuentra solo parte de los problemas.
- Un modelo de lenguaje puede equivocarse. Por eso los informes exigen evidencia concreta, y las pruebas del repositorio comparan resultados reales con lo esperado. Revisa siempre los hallazgos críticos antes de actuar.
