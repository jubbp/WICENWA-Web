"""Exercise and field forms shared by the Operations Manual and the standalone form PDFs.

Each function returns the body HTML of one form (without the section heading).
"""
import html

# 5 x 5 risk matrix. Likelihood A (almost certain) .. E (rare); consequence 1 .. 5.
LIKELIHOOD = [("A", "Almost certain", "Expected to happen during the exercise"),
              ("B", "Likely", "Will probably happen"),
              ("C", "Possible", "Might happen"),
              ("D", "Unlikely", "Could happen but not expected"),
              ("E", "Rare", "Only in exceptional circumstances")]
CONSEQUENCE = [("1", "Insignificant", "No injury"),
               ("2", "Minor", "First aid only"),
               ("3", "Moderate", "Medical treatment"),
               ("4", "Major", "Serious injury, hospital"),
               ("5", "Catastrophic", "Death or permanent disability")]
MATRIX = {"A": "MHHEE", "B": "MMHHE", "C": "LMHHE", "D": "LLMHH", "E": "LLMMH"}
LEVEL = {"L": "Low", "M": "Medium", "H": "High", "E": "Extreme"}
ACTION = {"L": "Manage with routine procedures",
          "M": "Controls in place and briefed before starting",
          "H": "Safety officer approves the controls before starting",
          "E": "Do not proceed — change the plan"}

# (task, hazard, initial risk, controls, residual risk, responsible)
HAZARDS = [
    ("Travel to and from sites", "Vehicle crash — fatigue, unsealed roads, wildlife, towing trailers", "C4",
     ["Plan the route and times", "Rest before driving; no driving straight after a long shift",
      "Drive to conditions; 4WD only where needed", "Report safe arrival at the site and at home"], "D4", "Each driver"),
    ("Site set-up and pack-up", "Manual handling — batteries, generators, masts, equipment cases", "C3",
     ["Team lift anything over 20 kg", "Use trolleys; split heavy battery banks", "Lift with the legs, not the back"],
     "D2", "All"),
    ("Raising masts and antennas", "Contact with overhead powerlines", "D5",
     ["Look up before raising anything — Look Up and Live",
      "Site masts and wire antennas so they cannot reach a powerline if they fall, swing or blow over",
      "Never throw a line over a tree near powerlines", "If in doubt, move the antenna"], "E5", "Site lead"),
    ("Raising masts and antennas", "Falling mast or antenna, guy lines, strong wind", "C3",
     ["Two people to raise a mast", "Keep everyone clear by the mast's height while raising",
      "Guy and peg masts; flag guy lines", "Don't raise or work on masts in strong wind"], "D2", "Site lead"),
    ("Weather", "Lightning", "D5",
     ["Check the forecast before leaving", "Stop antenna work and disconnect feed lines when thunder is heard",
      "Shelter in a hard-top vehicle", "Resume 30 minutes after the last thunder"], "E5", "Safety officer"),
    ("Weather", "Heat stress, sunburn, dehydration", "B3",
     ["Bring enough water for the day plus a reserve", "Shade at every operating position",
      "Hat, sunscreen, long sleeves", "Regular breaks; watch each other for heat illness"], "D2", "All"),
    ("Weather", "Cold, wet, wind, working at night", "C2",
     ["Warm and waterproof clothing", "Shelter at each operating position"], "D1", "All"),
    ("Bushfire", "Fire started by a generator, vehicle or hot equipment; fire approaching a site", "C4",
     ["Check the Fire Danger Rating and any Total Fire Ban before leaving — cancel or move on Extreme or Catastrophic, "
      "or where a ban restricts generator use", "Park vehicles and run generators on cleared ground",
      "Fire extinguisher at each generator", "Know the way out; monitor Emergency WA"], "D4", "Exercise controller"),
    ("Generators and fuel", "Carbon monoxide poisoning", "D5",
     ["Never run a generator in a vehicle, tent, annex or any enclosed space",
      "Place generators downwind of operating positions"], "E5", "Site lead"),
    ("Generators and fuel", "Burns and fuel fires when refuelling", "C3",
     ["Shut down and let the generator cool before refuelling", "Approved fuel containers only; no smoking",
      "Extinguisher within reach"], "D2", "Site lead"),
    ("Electrical", "Electric shock from 240 V equipment", "D4",
     ["RCD on every 240 V outlet", "Tested and tagged leads; no damaged leads", "Keep connections off the ground and dry"],
     "E4", "Site lead"),
    ("Electrical", "Battery short circuit; lithium battery fire", "C3",
     ["Fuse at the battery and at each device", "Anderson Powerpole connectors, insulated terminals",
      "Don't charge or use damaged lithium batteries", "Secure batteries for transport"], "D3", "Equipment owner"),
    ("Radio operation", "RF exposure near transmitting antennas", "D3",
     ["Antennas away from people and walkways", "Never touch an antenna while it may transmit",
      "Lowest power that does the job; follow the ARPANSA RF exposure standard"], "E2", "Operators"),
    ("Moving around sites", "Slips, trips and falls — uneven ground, cables, darkness", "B2",
     ["Walk the site before setting up", "Cover or tape cables across walkways", "Enclosed boots; head torch after dark"],
     "C1", "All"),
    ("Moving around sites", "Snake bite, insect stings, severe allergic reaction", "C4",
     ["Boots and long trousers; watch where you step and reach",
      "First aid kit with pressure-immobilisation bandages at each site",
      "Know who has a severe allergy and where their adrenaline auto-injector is"], "D4", "First aider"),
    ("Remote and lone operation", "Injury or illness with no one nearby to help", "C4",
     ["Work in pairs wherever possible", "Check in with Net Control at the agreed interval",
      "Missed check-in: Net Control calls twice, then sends someone or escalates",
      "Satellite messenger or PLB at sites without mobile coverage"], "D3", "Net Control"),
    ("Roadside sites", "Struck by traffic", "D5",
     ["Set up well clear of the road", "Vehicles fully off the carriageway", "Hi-vis vest when near a road"],
     "E5", "Site lead"),
    ("Sites near water", "Falling into a river, dam or the sea", "D5",
     ["Stay back from banks and edges", "Life jacket when working close to water"], "E5", "Site lead"),
    ("Long operating periods", "Fatigue — errors, falls, driving while tired", "C4",
     ["Agreed shift lengths and breaks", "Rotate roles", "Rest before driving home"], "D3", "Exercise controller"),
    ("Exercise traffic", "Exercise traffic mistaken for a real emergency, or a real emergency missed", "C4",
     ["Start and end every exercise message with EXERCISE",
      "A real emergency is called NO DUFF — it stops the exercise immediately",
      "Use only the exercise channels in the comms plan"], "E4", "Net Control"),
    ("Any task", "Injury or illness on site", "C4",
     ["Named first aider and first aid kit at each site", "Call 000 (112 from a mobile); the Emergency+ app gives your location",
      "Know the nearest hospital and the access point for ambulances"], "D3", "First aider"),
]


def rating(code):
    level = MATRIX[code[0]][int(code[1]) - 1]
    return f'<span class="risk risk-{level}">{code} {LEVEL[level]}</span>'


def lines(n, cols):
    return "".join("<tr>" + "".join("<td></td>" for _ in range(cols)) + "</tr>" for _ in range(n))


def signin_html():
    return f"""
<table class="form header">
<tr><td colspan="2"><label>Exercise / event</label>&nbsp;</td><td><label>Date</label>&nbsp;</td><td><label>Sheet</label>____ of ____</td></tr>
<tr><td><label>Location</label>&nbsp;</td><td><label>Exercise controller</label>&nbsp;</td><td><label>Safety officer</label>&nbsp;</td><td><label>First aider</label>&nbsp;</td></tr>
</table>
<p class="declaration"><strong>Fitness for duty.</strong> By signing in, I confirm I am fit to take part — not impaired by fatigue, alcohol, drugs, medication or illness — that I have received the safety briefing, and that I will sign out before leaving. I will tell the safety officer privately about any medical condition they should know of.</p>
<table class="form log signin"><thead><tr>
<th class="c-n">#</th><th class="c-name">Name</th><th class="c-call">Call sign</th><th class="c-phone">Mobile</th>
<th class="c-role">Role / site</th><th class="c-ec">Emergency contact — name and phone</th><th class="c-rego">Vehicle rego</th>
<th class="c-tick">Briefed</th><th class="c-time">Time in</th><th class="c-sig">Signature</th><th class="c-time">Time out</th>
</tr></thead><tbody>""" + "".join(
        f'<tr><td class="c-n">{i}</td>' + "<td></td>" * 6 + '<td class="c-tick">&#9744;</td>' + "<td></td>" * 3 + "</tr>"
        for i in range(1, 12)) + """</tbody></table>
<p class="form-note">This sheet holds personal information. The exercise controller keeps it, uses it for roll calls and emergencies only, and stores or destroys it securely after the exercise <span class="gap-ref">GAP-032</span> <span class="gap-ref">GAP-033</span>.</p>
"""


def jha_html():
    checks = [("Fire Danger Rating (today, for the area)", ""), ("Total Fire Ban in force?", "&#9744; No &nbsp; &#9744; Yes — restrictions:"),
              ("Weather — wind, heat, thunderstorms", ""), ("Site access and landholder permission", ""),
              ("Mobile coverage at each site", ""), ("Nearest hospital", ""), ("Ambulance access point", ""),
              ("Assembly point / way out", ""), ("Check-in interval", "every ______ minutes"),
              ("Safety officer", ""), ("First aider(s)", "")]
    check_rows = "".join(f"<tr><th>{html.escape(k)}</th><td>{v}</td></tr>" for k, v in checks)

    brief = ["Exercise aims, limits and timings",
             "EXERCISE at the start and end of every exercise message; <strong>NO DUFF</strong> for a real emergency; ENDEX ends the exercise",
             "<strong>Anyone can stop the exercise</strong> for a safety concern — no questions asked",
             "Sign-in, fitness for duty, and sign-out before leaving",
             "Hazards and controls in this JHA, including today's site-specific hazards",
             "Weather and fire danger, and what would cancel or stop the exercise",
             "Check-in schedule and what happens if a check-in is missed",
             "First aid, emergency numbers, nearest hospital and assembly point",
             "Questions"]
    brief_rows = "".join(f"<li>&#9744; {b}</li>" for b in brief)

    head = "".join(f'<th class="m-c">{c}<br><span>{n}</span></th>' for c, n, _ in CONSEQUENCE)
    body = "".join(f'<tr><th class="m-l">{l} {n}<br><span>{d}</span></th>' +
                   "".join(f'<td class="risk-{MATRIX[l][i]}">{LEVEL[MATRIX[l][i]]}</td>' for i in range(5)) + "</tr>"
                   for l, n, d in LIKELIHOOD)
    actions = "".join(f'<tr><td class="risk-{k}">{LEVEL[k]}</td><td>{ACTION[k]}</td></tr>' for k in "LMHE")
    conseq = "; ".join(f"<strong>{c}</strong> {n.lower()} — {d.lower()}" for c, n, d in CONSEQUENCE)

    rows = "".join(
        f'<tr><td class="c-n">{i}</td><td>{html.escape(t)}</td><td>{html.escape(h)}</td><td class="c-risk">{rating(r0)}</td>'
        f'<td><ul>{"".join(f"<li>{html.escape(c)}</li>" for c in cs)}</ul></td><td class="c-risk">{rating(r1)}</td>'
        f'<td class="c-who">{html.escape(w)}</td></tr>'
        for i, (t, h, r0, cs, r1, w) in enumerate(HAZARDS, 1))

    return f"""
<p class="form-note">Complete before every exercise or field deployment. The exercise controller and safety officer check the conditions and the site-specific hazards; the safety officer gives the briefing; every participant signs the briefing record. Draft — the hazard list is for committee review <span class="gap-ref">GAP-028</span>.</p>
<table class="form header">
<tr><td colspan="2"><label>Exercise / event</label>&nbsp;</td><td><label>Date</label>&nbsp;</td></tr>
<tr><td><label>Location / sites</label>&nbsp;</td><td><label>Exercise controller</label>&nbsp;</td><td><label>Safety officer</label>&nbsp;</td></tr>
</table>

<h2>1 Conditions on the day</h2>
<table class="data checks"><tbody>{check_rows}</tbody></table>
<table class="form go"><tr>
<td><label>Go / no-go decision</label>&#9744; GO &nbsp;&nbsp; &#9744; GO WITH CHANGES &nbsp;&nbsp; &#9744; NO-GO</td>
<td><label>Exercise controller — signature and time</label>&nbsp;</td></tr></table>

<h2>2 Briefing order</h2>
<ul class="checklist">{brief_rows}</ul>

<h2>3 Emergency information</h2>
<table class="data emergency"><tbody>
<tr><th>Real emergency on air</th><td><strong>NO DUFF, NO DUFF, NO DUFF</strong> — then the message. All exercise traffic stops.</td></tr>
<tr><th>Emergency services</th><td><strong>000</strong> (112 from a mobile). Use the Emergency+ app for your location.</td></tr>
<tr><th>Nearest hospital</th><td>&nbsp;</td></tr>
<tr><th>Assembly point</th><td>&nbsp;</td></tr>
<tr><th>Safety officer / first aider</th><td>&nbsp;</td></tr>
</tbody></table>

<h2>4 Risk matrix</h2>
<table class="matrix"><thead><tr><th>Likelihood ↓ &nbsp; Consequence →</th>{head}</tr></thead><tbody>{body}</tbody></table>
<table class="data actions"><tbody>{actions}</tbody></table>
<p class="form-note">Risk is written as likelihood and consequence, e.g. <strong>C4</strong> = possible, major. Consequence: {conseq}.</p>

<div class="landscape">
<h2>5 Job hazard analysis</h2>
<table class="data jha"><thead><tr><th class="c-n">#</th><th class="c-task">Task</th><th class="c-hazard">Hazard</th><th class="c-risk">Risk</th><th>Controls</th><th class="c-risk">Risk after controls</th><th class="c-who">Who</th></tr></thead>
<tbody>{rows}</tbody></table>

<h2>6 Site-specific hazards for this exercise</h2>
<table class="form log jha-blank"><thead><tr><th class="c-task">Task / site</th><th>Hazard</th><th class="c-risk">Risk</th><th>Controls</th><th class="c-risk">Risk after controls</th><th class="c-who">Who</th></tr></thead>
<tbody>{lines(6, 6)}</tbody></table>
</div>

<h2>7 Briefing record</h2>
<p class="declaration">I have been briefed on the hazards and controls in this document, I know how to call a real emergency (NO DUFF) and that I can stop the exercise for a safety concern.</p>
<table class="form log"><thead><tr><th>Name</th><th class="c-call">Call sign</th><th>Signature</th><th class="c-time">Time</th><th>Name</th><th class="c-call">Call sign</th><th>Signature</th><th class="c-time">Time</th></tr></thead>
<tbody>{lines(10, 8)}</tbody></table>
<table class="form"><tr>
<td><label>Briefing given by — name and signature</label>&nbsp;</td><td><label>Reviewed by safety officer — name and signature</label>&nbsp;</td><td class="c-time"><label>Date</label>&nbsp;</td>
</tr></table>
"""
