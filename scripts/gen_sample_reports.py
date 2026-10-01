"""Genera los informes de muestra (ficticios) de wcag22-audit desde los datos oficiales y el fixture html-seeded.
Uso: python scripts/gen_sample_reports.py
"""
import json
import yaml
from pathlib import Path
from common import ROOT as R
crit = {c["id"]: c for c in json.loads((R/"shared/data/wcag22-criteria.json").read_text())["criteria"]}
labels = yaml.safe_load((R/"shared/i18n/labels.yml").read_text())

def C(i): c=crit[i]; return {"system":"WCAG22","id":i,"name":c["name_en"],"level":c["level"],"url":c["url"]}
def ev(file,line,snip,**kw): return {"kind":"code","file":file,"line":line,"snippet":snip,**kw}

F = [  # (id, status, severity, confidence, method, evidence, texts per lang)
 ("4.1.2","fail","critical","medium","static_code",[ev("index.html",25,'<div class="btn" onclick="enviar()">Suscribirme</div>')],
  {"es":("El botón de suscripción es un div sin rol ni teclado","Un div con onclick no se anuncia como botón y no recibe foco del teclado, así que el formulario no se puede enviar sin ratón.","Personas que usan teclado o lector de pantalla.","Usar un <button type=\"submit\"> con el mismo texto visible."),
   "en":("The subscribe button is a div with no role or keyboard support","A div with onclick is not announced as a button and cannot receive keyboard focus, so the form cannot be submitted without a mouse.","People using a keyboard or a screen reader.","Use a <button type=\"submit\"> with the same visible text.")}),
 ("2.1.1","fail","critical","medium","static_code",[ev("index.html",25,'<div class="btn" onclick="enviar()">Suscribirme</div>')],
  {"es":("El botón de suscripción no se puede activar con teclado","El div con onclick no tiene tabindex ni manejador de teclado, así que no recibe foco ni responde a Enter o Espacio.","Personas que usan teclado, conmutadores o control por voz.","Usar un <button type=\"submit\">, que ya es operable con teclado."),
   "en":("The subscribe button cannot be activated with a keyboard","The div with onclick has no tabindex or keyboard handler, so it cannot receive focus or respond to Enter or Space.","People using a keyboard, switch devices or voice control.","Use a <button type=\"submit\">, which is already keyboard operable.")}),
 ("1.4.3","fail","serious","medium","static_code",[ev("styles.css",8,".nota { color: #999999; }",measured={"ratio":2.85,"required":4.5,"fg":"#999999","bg":"#ffffff"}),ev("styles.css",1,":root { --fondo: #ffffff; --texto: #1a1a1a; }")],
  {"es":("El texto de la nota tiene contraste insuficiente","El gris #999999 sobre el fondo blanco da 2.85:1; el texto normal necesita al menos 4.5:1.","Personas con baja visión o que leen con mucha luz.","Oscurecer el color del texto, por ejemplo a #595959 (7:1 sobre blanco)."),
   "en":("The note text has insufficient contrast","Gray #999999 on the white background gives 2.85:1; normal text needs at least 4.5:1.","People with low vision or reading in bright light.","Darken the text color, for example to #595959 (7:1 on white).")}),
 ("3.3.2","fail","serious","medium","static_code",[ev("index.html",22,'<input type="email" name="correo" placeholder="Tu correo">')],
  {"es":("El campo de correo no tiene etiqueta","El placeholder desaparece al escribir y no cuenta como etiqueta; el campo no tiene label ni aria-label.","Personas con lector de pantalla y con dificultades de memoria.","Asociar un <label for> visible al campo, como ya se hace con el campo de nombre."),
   "en":("The email field has no label","The placeholder disappears while typing and does not count as a label; the field has no label or aria-label.","Screen reader users and people with memory difficulties.","Associate a visible <label for> with the field, as is already done for the name field.")}),
 ("1.1.1","fail","serious","medium","static_code",[ev("index.html",18,'<img class="banner" src="banner.jpg">')],
  {"es":("La imagen del banner no tiene alternativa textual","La imagen del banner carece de atributo alt, así que una persona con lector de pantalla no sabe qué comunica.","Personas ciegas o con baja visión que usan lector de pantalla.","Añadir un alt que diga lo que comunica la imagen, o alt vacío si fuera decorativa."),
   "en":("The banner image has no text alternative","The banner image has no alt attribute, so a screen reader user cannot tell what it conveys.","Blind or low-vision people using a screen reader.","Add an alt that says what the image communicates, or an empty alt if it is decorative.")}),
 ("2.4.7","fail","moderate","medium","static_code",[ev("styles.css",9,"a:focus { outline: none; }")],
  {"es":("Los enlaces pierden el indicador de foco","La regla a:focus quita el contorno y no hay un estilo de reemplazo.","Personas que navegan con teclado.","Eliminar la regla o definir un :focus-visible con borde de buen contraste."),
   "en":("Links lose the focus indicator","The a:focus rule removes the outline and there is no replacement style.","People who navigate with a keyboard.","Remove the rule or define a :focus-visible with a high-contrast border.")}),
 ("2.5.8","fail","moderate","medium","static_code",[ev("styles.css",11,".icono { width: 18px; height: 18px; padding: 0; border: 0; background: transparent; }",measured={"width_px":18,"height_px":18,"required_px":24})],
  {"es":("El botón de cerrar mide 18 por 18 píxeles","El objetivo mide menos de 24 por 24 píxeles CSS y no tiene espacio compensatorio a su alrededor.","Personas con temblor o que usan pantalla táctil.","Ampliar el área activa a al menos 24 por 24 px, por ejemplo con padding."),
   "en":("The close button is 18 by 18 pixels","The target is smaller than 24 by 24 CSS pixels and has no compensating space around it.","People with tremor or using a touch screen.","Enlarge the active area to at least 24 by 24 px, for example with padding.")}),
 ("1.3.5","fail","moderate","medium","static_code",[ev("index.html",22,'<input type="email" name="correo" placeholder="Tu correo">')],
  {"es":("El campo de correo no declara su propósito","El campo no tiene autocomplete, así que el navegador no puede rellenar el correo de la persona.","Personas con dificultades motoras o de memoria, y quienes usan gestores de datos.","Añadir autocomplete=\"email\" al campo."),
   "en":("The email field does not declare its purpose","The field has no autocomplete, so the browser cannot fill in the person's email.","People with motor or memory difficulties, and those who rely on data managers.","Add autocomplete=\"email\" to the field.")}),
]
PASS = [("2.4.1",10,'<a class="skip" href="#contenido">Saltar al contenido</a>',{"es":"Hay un enlace de salto al contenido","en":"There is a skip link to the content"}),
        ("2.4.2",6,"<title>Café Aurora – Inicio</title>",{"es":"La página tiene título descriptivo","en":"The page has a descriptive title"}),
        ("3.1.1",2,'<html lang="es">',{"es":"El idioma de la página está declarado","en":"The page language is declared"})]
TXT = {
 "es": dict(h="Informe de auditoría: Café Aurora (sitio ficticio de ejemplo)", sev={"critical":"Crítico","serious":"Grave","moderate":"Moderado"},
   verdict="el formulario de suscripción no se puede enviar con teclado ni lector de pantalla; corregirlo antes de publicar.",
   scope="`index.html` y `styles.css` de un sitio ficticio", manual_reason="El orden del foco depende de cómo se renderiza y se recorre la página; el modo código no lo decide.",
   manual_proc="Recorrer la página solo con Tab y Mayús+Tab y comprobar que el orden sigue el orden visual.",
   gaps=["Análisis estático: no se evaluó el comportamiento de JavaScript (la función enviar() no está en los archivos revisados) ni el contraste real con la cascada completa.",
         "No se evaluó el reflujo a 320 px (1.4.10): requiere un navegador o un viewport real.",
         "No se revisaron estados de error de formulario ni contenido que aparece al pasar el cursor o enfocar.",
         "Sin navegador disponible: no se midió el foco ni el nombre accesible calculado."],
   next=["Reemplazar el div por un botón real y etiquetar el campo de correo.","Añadir el alt del banner y oscurecer el texto de la nota.","Restaurar el indicador de foco y ampliar el botón de cerrar.","Repetir la auditoría en modo URL con un navegador para cubrir reflujo, foco y orden de tabulación."],
   nt_title="El reflujo a 320 px no se pudo evaluar", ),
 "en": dict(h="Audit report: Café Aurora (fictional sample site)", sev={"critical":"Critical","serious":"Serious","moderate":"Moderate"},
   verdict="the subscribe form cannot be submitted with a keyboard or a screen reader; fix it before release.",
   scope="`index.html` and `styles.css` of a fictional site", manual_reason="Focus order depends on how the page renders and is traversed; code mode cannot decide it.",
   manual_proc="Walk the page with Tab and Shift+Tab only and check that the order follows the visual order.",
   gaps=["Static analysis: JavaScript behavior was not evaluated (the enviar() function is not in the reviewed files) nor real contrast through the full cascade.",
         "Reflow at 320 px (1.4.10) was not evaluated: it needs a browser or a real viewport.",
         "Form error states and content shown on hover or focus were not reviewed.",
         "No browser available: focus and the computed accessible name were not measured."],
   next=["Replace the div with a real button and label the email field.","Add the banner alt and darken the note text.","Restore the focus indicator and enlarge the close button.","Repeat the audit in URL mode with a browser to cover reflow, focus and tab order."],
   nt_title="Reflow at 320 px could not be evaluated"),
}
def build(lang):
    t = TXT[lang]; L = labels[lang]
    findings = []; n = {}
    for cid, st, sev, conf, meth, evd, tx in F:
        n[cid] = n.get(cid, 0)+1
        title, desc, who, fix = tx[lang]
        findings.append({"id":f"WCAG-{cid}-{n[cid]:03d}","source_skill":"wcag22-audit","criterion":C(cid),"status":st,"severity":sev,"confidence":conf,"method":meth,
            "title":title,"description":desc,"evidence":evd,"affected_users":who,"recommendation":fix,"dedup_key":f"{cid}|{evd[0]['file']}:{evd[0]['line']}"})
    findings.append({"id":"WCAG-2.4.3-001","source_skill":"wcag22-audit","criterion":C("2.4.3"),"status":"manual","confidence":"low","method":"static_code",
        "title":"El orden del foco requiere recorrer la página" if lang=="es" else "Focus order requires walking the page",
        "manual_check":{"reason":t["manual_reason"],"procedure":t["manual_proc"],"suggested_tools":["Teclado" if lang=="es" else "Keyboard","Navegador" if lang=="es" else "Browser"]},"dedup_key":"2.4.3|index.html"})
    findings.append({"id":"WCAG-1.4.10-001","source_skill":"wcag22-audit","criterion":C("1.4.10"),"status":"not_tested","confidence":"low","method":"inferred","title":t["nt_title"],"dedup_key":"1.4.10|index.html"})
    for cid, line, snip, name in PASS:
        findings.append({"id":f"WCAG-{cid}-001","source_skill":"wcag22-audit","criterion":C(cid),"status":"pass","confidence":"medium","method":"static_code",
            "title":name[lang],"evidence":[ev("index.html",line,snip)],"dedup_key":f"{cid}|index.html:{line}"})
    data = {"schema_version":"1","skill":"wcag22-audit","language":lang,"mode":"code","generated_on":"2026-10-01",
            "scope":{"summary":t["scope"].replace("`",""),"inputs":["index.html","styles.css"],"capabilities":{"browser":False,"figma":False,"axe":False,"script":False}},
            "findings":findings,"honest_gaps":t["gaps"]}
    fails=[f for f in findings if f["status"]=="fail"]
    cnt={s:sum(1 for f in fails if f["severity"]==s) for s in ("critical","serious","moderate")}
    assessed=len(fails)+len(PASS); applicable=assessed+2
    es = lang=="es"
    o=[f"# {t['h']}\n","<!-- section:summary -->","## "+L["sections"]["summary"]+"\n",
       f"- **{'Veredicto' if es else 'Verdict'}:** {t['verdict']}",
       f"- **{'Hallazgos que fallan' if es else 'Failing findings'}:** {len(fails)} ({L['severity']['critical']} {cnt['critical']} · {L['severity']['serious']} {cnt['serious']} · {L['severity']['moderate']} {cnt['moderate']} · {L['severity']['minor']} 0)",
       f"- **{'Requieren prueba manual' if es else 'Need manual check'}:** 1",
       f"- **{'Cobertura' if es else 'Coverage'}:** {assessed} {'de' if es else 'of'} {applicable} {'criterios aplicables en este modo' if es else 'applicable criteria in this mode'}\n",
       "<!-- section:scope -->","## "+L["sections"]["scope"]+"\n",
       f"- **{'Modo' if es else 'Mode'}:** {L['mode']['code']}",
       f"- **{'Qué se revisó' if es else 'What was reviewed'}:** {t['scope']}",
       f"- **{'Capacidades detectadas' if es else 'Detected capabilities'}:** {'navegador no · Figma no · axe no · script no' if es else 'browser no · Figma no · axe no · script no'}",
       f"- **{'Fecha' if es else 'Date'}:** 2026-10-01\n","<!-- section:findings -->","## "+L["sections"]["findings"]+"\n"]
    for f in fails:
        c=f["criterion"]; e=f["evidence"][0]
        o+= [f"### {L['severity'][f['severity']]}: {f['title']}\n",
             f"- **{'Criterio' if es else 'Criterion'}:** {c['id']} {c['name']} ({'nivel' if es else 'level'} {c['level']}), {c['url']}",
             f"- **{'Dónde' if es else 'Where'}:** `{e['file']}:{e['line']}`",
             f"- **{'Qué pasa' if es else 'What happens'}:** {f['description']}",
             f"- **{'Confianza' if es else 'Confidence'}:** {L['confidence'][f['confidence']]}, {'método' if es else 'method'}: {f['method']}",
             f"- **{'A quién afecta' if es else 'Who is affected'}:** {f['affected_users']}",
             f"- **{'Cómo corregirlo' if es else 'How to fix'}:** {f['recommendation']}\n"]
    m=[f for f in findings if f["status"]=="manual"][0]; mc=m["manual_check"]
    o+=["<!-- section:manual -->","## "+L["sections"]["manual"]+"\n",
        "| "+("Criterio | Por qué no se pudo decidir | Cómo comprobarlo" if es else "Criterion | Why it could not be decided | How to check")+" |","|---|---|---|",
        f"| {m['criterion']['id']} {m['criterion']['name']} | {mc['reason']} | {mc['procedure']} |\n",
        "<!-- section:passed -->","## "+L["sections"]["passed"]+"\n"]
    for cid,line,snip,name in PASS: o.append(f"- {cid} {crit[cid]['name_en']}: {name[lang]} (`index.html:{line}`).")
    o+=["","<!-- section:honest-gaps -->","## "+L["sections"]["honest-gaps"]+"\n"]+[f"- {g}" for g in t["gaps"]]+[f"- {L['disclaimer']}","","<!-- section:next-steps -->","## "+L["sections"]["next-steps"]+"\n"]
    o+=[f"{i}. {x}" for i,x in enumerate(t["next"],1)]
    o+=["","---","",f"*{L['disclaimer']}*","","```json ux-skills-findings",json.dumps(data,ensure_ascii=False,indent=2),"```",""]
    out=R/f"src/skills/wcag22-audit/examples/sample-report.{lang}.md"
    out.write_text("\n".join(o),encoding="utf-8"); print(out.name, len(findings),"findings")
for lang in ("es","en"): build(lang)
