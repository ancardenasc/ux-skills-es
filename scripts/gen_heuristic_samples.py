"""Genera los informes de muestra (ficticios) de heuristic-review-es desde los datos y el fixture flow-seeded.
Uso: python scripts/gen_heuristic_samples.py
"""
import json

import yaml

from common import ROOT as R

heur = {h["id"]: h for h in json.loads((R / "shared/data/nielsen-heuristics.json").read_text(encoding="utf-8"))["heuristics"]}
labels = yaml.safe_load((R / "shared/i18n/labels.yml").read_text(encoding="utf-8"))
FILE = "pedido.html"


def C(i):
    h = heur[i]
    return {"system": "NIELSEN", "id": i, "name": h["name_en"], "url": h["url"]}


def ev(line, snip):
    return {"kind": "code", "file": FILE, "line": line, "snippet": snip}


NAV = '<a href="/">Inicio</a> <a href="/pedido">Mi pedido</a> <a href="/cuenta">Cuenta</a>'
DEL = '<button type="button" onclick="borrarPedido()">Eliminar pedido</button>'
F = [  # (heurística, gravedad, evidencia, {idioma: (título, descripción, a quién afecta, corrección)})
    ("H5", "serious", [ev(17, DEL), ev(23, "function borrarPedido() { fetch('/pedido', {method: 'DELETE'}).then(() => location.reload()); }")],
     {"es": ("Eliminar el pedido no pide confirmación ni permite deshacer", "Un solo clic ejecuta el borrado y recarga la página; no hay confirmación, papelera ni opción de deshacer.", "Cualquier persona que pulse el botón por error.", "Pedir confirmación indicando qué se borra, o permitir deshacer durante unos segundos."),
      "en": ("Deleting the order asks for no confirmation and cannot be undone", "A single click runs the deletion and reloads the page; there is no confirmation, trash or undo.", "Anyone who presses the button by mistake.", "Ask for confirmation stating what will be deleted, or allow undo for a few seconds.")}),
    ("H1", "serious", [ev(22, "function guardar() { fetch('/guardar', {method: 'POST'}); }")],
     {"es": ("Guardar no da ninguna respuesta", "La función envía la petición y no muestra progreso, éxito ni error; la persona no sabe si el pedido quedó guardado.", "Quien guarda sin saber si funcionó y puede repetir la acción.", "Mostrar un estado de carga y un mensaje de éxito o de error junto al botón."),
      "en": ("Saving gives no feedback at all", "The function sends the request and shows no progress, success or error; the person cannot tell whether the order was saved.", "People who save without knowing if it worked and may repeat the action.", "Show a loading state and a success or error message next to the button.")}),
    ("H9", "moderate", [ev(25, "document.getElementById('estado').textContent = 'Error 0x80070057: parámetro incorrecto';")],
     {"es": ("El mensaje de error es técnico y no propone solución", "El texto muestra un código interno y habla de un parámetro; no dice qué falló ni cómo corregirlo.", "Cualquier persona que no sea del equipo técnico.", "Decir con palabras claras qué pasó y qué hacer, por ejemplo qué campo corregir."),
      "en": ("The error message is technical and offers no solution", "The text shows an internal code and mentions a parameter; it does not say what failed or how to fix it.", "Anyone outside the technical team.", "State in plain words what happened and what to do, for example which field to correct.")}),
    ("H2", "moderate", [ev(13, '<label for="fecha">Fecha de entrega (mm/dd/aaaa)</label>')],
     {"es": ("La fecha pide el formato mes/día/año", "El formato mm/dd/aaaa no es el habitual para el público local, que escribe día, mes y año; invita a confundir fechas como 03/04.", "Quienes escriben las fechas en el orden local.", "Usar dd/mm/aaaa o un selector de fecha que muestre el mes con su nombre."),
      "en": ("The date asks for month/day/year", "The mm/dd/yyyy format is not the usual one for the local audience, which writes day, month and year; it invites mixing up dates such as 03/04.", "People who write dates in the local order.", "Use dd/mm/yyyy or a date picker that shows the month by name.")}),
    ("H4", "moderate", [ev(15, '<button type="submit">Aceptar</button>')],
     {"es": ("Dos botones con nombres distintos para acciones parecidas", "«Aceptar» y «Enviar» no dicen qué hacen y compiten entre sí; no queda claro cuál confirma el pedido.", "Quien debe decidir qué botón pulsar.", "Dejar un solo botón principal con un verbo claro, por ejemplo «Confirmar pedido»."),
      "en": ("Two differently named buttons for similar actions", "\"Aceptar\" and \"Enviar\" do not say what they do and compete with each other; it is unclear which one confirms the order.", "Anyone who must decide which button to press.", "Keep a single primary button with a clear verb, for example \"Confirm order\".")}),
    ("H6", "moderate", [ev(18, '<button type="button" class="ico" title="">⚙</button>')],
     {"es": ("El botón de engranaje no dice qué hace", "El icono no tiene texto ni título; hay que recordar o adivinar su función.", "Quien usa el sitio por primera vez.", "Añadir una etiqueta visible o un título descriptivo."),
      "en": ("The gear button does not say what it does", "The icon has no text or title; its function must be remembered or guessed.", "People using the site for the first time.", "Add a visible label or a descriptive title.")}),
    ("H10", "minor", [ev(9, NAV)],
     {"es": ("No hay enlace de ayuda", "La navegación no ofrece ayuda ni contacto para quien tiene dudas con el pedido.", "Quien se queda atascado durante el pedido.", "Añadir un enlace a ayuda o contacto en la navegación."),
      "en": ("There is no help link", "The navigation offers no help or contact for people with doubts about the order.", "People who get stuck during the order.", "Add a help or contact link to the navigation.")}),
]
PASS = [("H4", 9, NAV, {"es": "Las etiquetas de la navegación son coherentes", "en": "The navigation labels are consistent"}),
        ("H8", 11, "<h1>Tu pedido</h1>", {"es": "La pantalla tiene una sola tarea", "en": "The screen has a single task"})]
MANUAL = [("H3", {"es": ("Cancelar o deshacer se comprueba recorriendo el flujo", "El control para volver atrás o deshacer solo se verifica ejecutando el flujo.", "Recorrer el pedido e intentar cancelar o deshacer en cada paso."),
                  "en": ("Cancel and undo are checked by walking the flow", "The control to go back or undo can only be verified by running the flow.", "Walk through the order and try to cancel or undo at each step.")}),
          ("H7", {"es": ("Atajos y personalización dependen del uso real", "No se pueden valorar leyendo el código; requieren observar a personas con experiencia.", "Observar a quienes repiten el pedido y preguntar qué atajos echan en falta."),
                  "en": ("Shortcuts and customization depend on real usage", "They cannot be judged from the code; they require observing experienced people.", "Observe people who repeat the order and ask which shortcuts they miss.")})]
TXT = {
    "es": dict(h="Revisión heurística: pedido de Café Aurora (flujo ficticio de ejemplo)", sev={"critical": "Crítico", "serious": "Grave", "moderate": "Moderado", "minor": "Menor"},
               verdict="el flujo funciona pero no da respuesta al guardar y permite borrar el pedido sin confirmar; corregir esos dos puntos antes de publicar.",
               scope="`pedido.html` de un flujo ficticio", task="Hacer, guardar y, si hace falta, eliminar un pedido de café.",
               gaps=["Revisión hecha leyendo código: no se vio el flujo ejecutándose, así que el ritmo, las animaciones y los textos que genera el servidor no se evaluaron.",
                     "Una sola persona evaluadora: la revisión heurística se enriquece con varias miradas y no sustituye las pruebas de usabilidad con personas usuarias.",
                     "Solo se revisó la tarea de hacer un pedido; no se revisaron la cuenta, el pago ni el seguimiento.",
                     "H3 y H7 quedan para verificación manual: requieren ejecutar el flujo y observar uso real."],
               next=["Pedir confirmación antes de eliminar y mostrar el resultado de guardar.", "Unificar los botones en una acción principal con verbo claro.", "Cambiar el formato de fecha y reescribir el mensaje de error en lenguaje claro.", "Probar el flujo con 5 personas usuarias para validar estos hallazgos."],
               states={"fail": "Hay problemas", "pass": "Sin problemas", "manual": "Requiere prueba manual", "none": "No evaluada"}, th=("Heurística", "Estado", "Hallazgos"),
               manual_hdr="Criterio | Por qué no se pudo decidir | Cómo comprobarlo"),
    "en": dict(h="Heuristic review: Café Aurora order (fictional sample flow)", sev={"critical": "Critical", "serious": "Serious", "moderate": "Moderate", "minor": "Minor"},
               verdict="the flow works but gives no response when saving and lets the order be deleted without confirmation; fix those two points before release.",
               scope="`pedido.html` of a fictional flow", task="Create, save and, if needed, delete a coffee order.",
               gaps=["The review was done by reading code: the flow was not seen running, so pacing, animations and server-generated texts were not evaluated.",
                     "A single evaluator: heuristic review improves with several perspectives and does not replace usability testing with real users.",
                     "Only the order task was reviewed; the account, payment and tracking were not.",
                     "H3 and H7 are left for manual verification: they require running the flow and observing real use."],
               next=["Ask for confirmation before deleting and show the result of saving.", "Unify the buttons into one primary action with a clear verb.", "Change the date format and rewrite the error message in plain language.", "Test the flow with 5 users to validate these findings."],
               states={"fail": "Problems found", "pass": "No problems", "manual": "Needs manual check", "none": "Not evaluated"}, th=("Heuristic", "Status", "Findings"),
               manual_hdr="Criterion | Why it could not be decided | How to check"),
}


def build(lang):
    t, L, es = TXT[lang], labels[lang], lang == "es"
    findings, n = [], {}

    def nid(h):
        n[h] = n.get(h, 0) + 1
        return f"NIELSEN-{h}-{n[h]:03d}"
    for h, sev, evd, tx in F:
        title, desc, who, fix = tx[lang]
        findings.append({"id": nid(h), "source_skill": "heuristic-review-es", "criterion": C(h), "status": "fail", "severity": sev, "confidence": "medium",
                         "method": "static_code", "title": title, "description": desc, "evidence": evd, "affected_users": who, "recommendation": fix,
                         "dedup_key": f"{h}|{FILE}:{evd[0]['line']}"})
    for h, tx in MANUAL:
        title, reason, proc = tx[lang]
        findings.append({"id": nid(h), "source_skill": "heuristic-review-es", "criterion": C(h), "status": "manual", "confidence": "low", "method": "static_code",
                         "title": title, "manual_check": {"reason": reason, "procedure": proc, "suggested_tools": ["Flujo en ejecución" if es else "Running flow"]},
                         "dedup_key": f"{h}|{FILE}"})
    for h, line, snip, name in PASS:
        findings.append({"id": nid(h), "source_skill": "heuristic-review-es", "criterion": C(h), "status": "pass", "confidence": "medium", "method": "static_code",
                         "title": name[lang], "evidence": [ev(line, snip)], "dedup_key": f"{h}|{FILE}:{line}"})
    data = {"schema_version": "1", "skill": "heuristic-review-es", "language": lang, "mode": "code", "generated_on": "2026-10-01",
            "scope": {"summary": t["scope"].replace("`", ""), "inputs": [FILE], "capabilities": {"browser": False, "figma": False, "axe": False, "script": False}},
            "findings": findings, "honest_gaps": t["gaps"]}
    fails = [f for f in findings if f["status"] == "fail"]
    cnt = {s: sum(1 for f in fails if f["severity"] == s) for s in ("critical", "serious", "moderate", "minor")}
    assessed = len({f["criterion"]["id"] for f in findings if f["status"] in ("fail", "pass")})
    applicable = len({f["criterion"]["id"] for f in findings})

    def state(h):
        st = {f["status"] for f in findings if f["criterion"]["id"] == h}
        key = "fail" if "fail" in st else "manual" if "manual" in st else "pass" if "pass" in st else "none"
        return t["states"][key], sum(1 for f in fails if f["criterion"]["id"] == h)
    o = [f"# {t['h']}\n", "<!-- section:summary -->", "## " + L["sections"]["summary"] + "\n",
         f"- **{'Veredicto' if es else 'Verdict'}:** {t['verdict']}",
         f"- **{'Hallazgos que fallan' if es else 'Failing findings'}:** {len(fails)} ({L['severity']['critical']} {cnt['critical']} · {L['severity']['serious']} {cnt['serious']} · {L['severity']['moderate']} {cnt['moderate']} · {L['severity']['minor']} {cnt['minor']})",
         f"- **{'Requieren prueba manual' if es else 'Need manual check'}:** {len(MANUAL)}",
         f"- **{'Cobertura' if es else 'Coverage'}:** {assessed} {'de' if es else 'of'} {applicable} {'criterios aplicables en este modo' if es else 'applicable criteria in this mode'}\n",
         f"| {t['th'][0]} | {t['th'][1]} | {t['th'][2]} |", "|---|---|---|"]
    for h in heur:
        s, c = state(h)
        o.append(f"| {h} {heur[h]['name_en']} ({heur[h]['label_es']}) | {s} | {c} |" if es else f"| {h} {heur[h]['name_en']} | {s} | {c} |")
    o += ["", "<!-- section:scope -->", "## " + L["sections"]["scope"] + "\n",
          f"- **{'Modo' if es else 'Mode'}:** {L['mode']['code']}", f"- **{'Qué se revisó' if es else 'What was reviewed'}:** {t['scope']}",
          f"- **{'Tarea evaluada' if es else 'Task evaluated'}:** {t['task']}",
          f"- **{'Capacidades detectadas' if es else 'Detected capabilities'}:** " + ("navegador no · Figma no · axe no · script no" if es else "browser no · Figma no · axe no · script no"),
          f"- **{'Fecha' if es else 'Date'}:** 2026-10-01\n", "<!-- section:findings -->", "## " + L["sections"]["findings"] + "\n"]
    for f in fails:
        c, e = f["criterion"], f["evidence"][0]
        label = f" ({heur[c['id']]['label_es']})" if es else ""
        o += [f"### {t['sev'][f['severity']]}: {f['title']}\n",
              f"- **{'Heurística' if es else 'Heuristic'}:** {c['id']} {c['name']}{label}, {c['url']}",
              f"- **{'Dónde' if es else 'Where'}:** `{e['file']}:{e['line']}`",
              f"- **{'Qué pasa' if es else 'What happens'}:** {f['description']}",
              f"- **{'Confianza' if es else 'Confidence'}:** {L['confidence'][f['confidence']]}, {'método' if es else 'method'}: {f['method']}",
              f"- **{'A quién afecta' if es else 'Who is affected'}:** {f['affected_users']}",
              f"- **{'Cómo corregirlo' if es else 'How to fix'}:** {f['recommendation']}\n"]
    o += ["<!-- section:manual -->", "## " + L["sections"]["manual"] + "\n", f"| {t['manual_hdr']} |", "|---|---|---|"]
    for f in findings:
        if f["status"] == "manual":
            c, mc = f["criterion"], f["manual_check"]
            o.append(f"| {c['id']} {c['name']} | {mc['reason']} | {mc['procedure']} |")
    o += ["", "<!-- section:passed -->", "## " + L["sections"]["passed"] + "\n"]
    o += [f"- {h} {heur[h]['name_en']}: {name[lang]} (`{FILE}:{line}`)." for h, line, snip, name in PASS]
    o += ["", "<!-- section:honest-gaps -->", "## " + L["sections"]["honest-gaps"] + "\n"] + [f"- {g}" for g in t["gaps"]] + [f"- {L['disclaimer']}", "",
          "<!-- section:next-steps -->", "## " + L["sections"]["next-steps"] + "\n"] + [f"{i}. {x}" for i, x in enumerate(t["next"], 1)]
    o += ["", "---", "", f"*{L['disclaimer']}*", "", "```json ux-skills-findings", json.dumps(data, ensure_ascii=False, indent=2), "```", ""]
    out = R / f"src/skills/heuristic-review-es/examples/sample-report.{lang}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(o), encoding="utf-8")
    print(out.name, len(findings), "hallazgos")


for lang in ("es", "en"):
    build(lang)
