---
name: case-study-writer
description: Redacta el caso de estudio de un proyecto de UX, accesibilidad o frontend desde sus documentos (la estructura de case-kit) o desde notas libres, y opcionalmente desde informes de auditoría. Entrega tres textos en español o inglés - el caso completo de 10 minutos, un resumen de 60 segundos y un blurb de portafolio. Nunca inventa métricas, personas ni resultados, marca lo que falta como dato faltante y cita el documento de cada afirmación. Úsalo cuando pidan escribir, redactar o armar un caso de estudio o texto de portafolio.
argument-hint: "[carpeta-del-proyecto | notas] [--idioma es|en] [--guardar]"
license: MIT
---

# case-study-writer

Convierte la evidencia de un proyecto en un caso de estudio honesto. **Lo que no está en las fuentes no se escribe**: se marca como dato faltante. No es un generador de texto bonito: es un redactor que responde ante sus fuentes.

## Antes de empezar

- **Idioma:** `--idioma es|en`, o el idioma de la petición; por defecto `es`.
- **Lee primero** las reglas y la estructura del idioma elegido: [reglas](references/rules.es.md) · [rules](references/rules.en.md) y [estructura](references/structure.es.md) · [structure](references/structure.en.md).
- **Ejemplo del resultado esperado:** [es](examples/sample-output.es.md) · [en](examples/sample-output.en.md).

## Pasos

### 1. Inventario de fuentes

- **Proyecto con la estructura de `case-kit`:** lee `docs/brief.md`, `docs/research/`, `docs/prd.md`, `docs/design/`, `docs/testing/`, `docs/accessibility/`, `docs/decisions/` y `docs/case-study.md` (la plantilla a llenar).
- **Notas libres:** pídelas pegadas o como archivo.
- **Informes de auditoría** (`wcag22-audit`, `heuristic-review-es`): si hay un bloque `json ux-skills-findings`, toma sus cifras de ese bloque (conteos por estado y gravedad, cobertura, brechas honestas) en vez de recalcularlas.
- **Notas crudas, consentimientos o datos de contacto:** léelos para entender el contexto, pero **nunca los cites ni repitas** nombres, empleadores, teléfonos ni correos que contengan.

### 2. Tabla de huecos (antes de escribir)

Para cada sección del caso (contexto y rol, problema, proceso, decisiones, resultado, accesibilidad, reflexión, enlaces) anota qué evidencia hay y cuál falta. Muéstrala. Pregunta **solo** lo imprescindible que ninguna fuente responde (tu rol exacto, la duración, los enlaces públicos). Si la persona prefiere no responder, deja el hueco marcado.

### 3. Redacta tres textos

| Texto | Para qué | Extensión |
|---|---|---|
| **Caso completo** | La página pública, con la estructura fija de la plantilla | Hasta unas 2 000 palabras: se ajusta a la evidencia; **no rellenes** para alcanzar un largo |
| **Resumen de 60 segundos** | Leerlo de un vistazo | 180 a 250 palabras |
| **Blurb de portafolio** | Tarjeta o bio del proyecto | Titular de una línea y máximo 60 palabras |

El resumen y el blurb solo pueden afirmar lo que dice el caso completo, con las mismas cifras.

### 4. Reglas que no se negocian

- **Cada afirmación factual o numérica del caso completo cita su fuente** con `[fuente: ruta/del/documento.md]`.
- **Ninguna cifra, persona, cita ni resultado se inventa.** Calcular un porcentaje a partir de dos cifras de la fuente es válido y debe poder rehacerse; "mejoró notablemente" sin dato no es válido.
- **Lo que falta** se escribe `[DATO FALTANTE: qué dato y dónde debería salir]` (en inglés, `[MISSING DATA: ...]`).
- **Proyecto de muestra:** si las fuentes dicen que los datos son de muestra o ficticios, el caso lo declara de forma visible.
- **Privacidad:** sin nombres de participantes (usa P1, P2…), sin empleadores ni clientes reales, sin datos de contacto.
- **Interpretación aparte:** separa lo que se observó de lo que se concluye; la reflexión es la voz de quien hizo el proyecto, no una invención.
- **Resultados:** "antes y después" solo con las dos cifras presentes; si falta una, `DATO FALTANTE`.

### 5. Entrega

- Muestra siempre los tres textos en el chat.
- Con `--guardar`, escribe `docs/case-study.md` (solo si aún es la plantilla sin llenar; si ya tiene contenido, **pregunta** antes), `docs/case-study-60s.md` y `docs/portfolio-blurb.md`. Nunca sobrescribas un archivo con contenido sin permiso.

### 6. Autoverificación

- [ ] Los encabezados siguen la plantilla, en orden, en el idioma elegido.
- [ ] Toda cifra del texto está en una fuente citada o es un cálculo rehacible de ellas.
- [ ] Cada cita `[fuente: ...]` apunta a un archivo que existe.
- [ ] Los huecos están marcados y la sección de resultados no inventa un "después".
- [ ] No aparece ningún nombre, empleador, teléfono o correo de las notas crudas.
- [ ] El resumen y el blurb no dicen nada que el caso completo no diga.
- [ ] Se declara que el proyecto es de muestra si lo es.

## No hagas

- No inventes métricas, personas, citas de usuarios ni resultados.
- No publiques ni subas nada; no hagas commit ni push.
- No copies texto ajeno ni presentes material de terceros o de empleadores como propio.
