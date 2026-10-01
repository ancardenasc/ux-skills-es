<!-- GENERADO desde shared/references/honest-gaps.es.md por scripts/build.py. No editar a mano. -->
# Brechas honestas

La sección es **obligatoria y nunca queda vacía**. Dice con claridad qué no se pudo saber. Como mínimo incluye:

- El modo usado y sus límites (por ejemplo, "análisis estático: no se evaluó el comportamiento con JavaScript").
- Páginas, estados o componentes que no se revisaron (menús abiertos, errores de formulario, vistas con sesión).
- Herramientas que no estaban disponibles (navegador, script, axe).
- Los criterios en `not_tested`, agrupados.
- La frase del pie: este informe no es una declaración de conformidad ni un dictamen legal.

## Cobertura

`cobertura = criterios evaluados / criterios aplicables`. Se calcula contando los hallazgos del JSON (`pass` y `fail` son evaluados; `manual` y `not_tested` no; `not_applicable` sale del denominador). No la estimes ni la redondees hacia arriba.

## Tono

Directo y sin disculpas: "No pude evaluar X porque Y" y qué haría falta para evaluarlo.
