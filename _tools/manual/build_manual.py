"""Build the WICEN-WA Operations Manual (A4 PDF) from the PACE plan pages.

usage (from the repository root):
    python3 -I _tools/manual/build_manual.py <output.pdf>

Steps: build the Jekyll site, assemble the plan chapters and annexes into one
HTML document, print it to PDF with headless Chrome (A4, wide binding margin,
revision footer on every page), then run a second pass to put page numbers
in the table of contents.

Revision number, date and history come from _data/manual.yml.
"""
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SITE_URL = "https://wicenwa.org"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PARTS = [
    ("Part 1 — The Plan", [
        ("overview", "Overview"),
        ("domain-summary", "PACE Domain Summary"),
    ]),
    ("Part 2 — Activation and Deployment", [
        ("activation", "Activation"),
        ("activation-flowchart", "Activation Flowchart"),
        ("deployment-model", "Deployment Model"),
        ("demobilisation", "Demobilisation"),
    ]),
    ("Part 3 — Communications Networks", [
        ("operational", "Operational Communications"),
        ("radio-frequency-plans", "Radio Network and Frequencies"),
        ("HF-propagation-plan", "HF Propagation Plan"),
        ("digital-messaging-architecture", "Digital Messaging"),
        ("cross-state-coordination", "Cross-State Coordination"),
        ("event-support", "Event Support"),
    ]),
    ("Part 4 — Procedures", [
        ("message-handling", "Message Handling"),
        ("voice-procedure", "Voice Procedure (RATEL)"),
        ("incident-information-handling", "Incident Information"),
    ]),
    ("Part 5 — Training", [
        ("training", "Training and Exercises"),
    ]),
]
CHAPTERS = [(slug, title) for _, chs in PARTS for slug, title in chs]
CH_NUM = {slug: n for n, (slug, _) in enumerate(CHAPTERS, 1)}

ANNEXES = [
    ("known-gaps", "Known Gaps"),
    ("glossary", "Glossary"),
    ("message-form", "Message Form"),
    ("station-log", "Station and Net Log"),
    ("checkpoint-report", "Event Checkpoint Report"),
    ("frequency-card", "Frequency Quick Reference"),
    ("prep-checklist", "General Preparation Checklist"),
    ("ratel", "Archived RATEL Procedure (c. 2002)"),
]
ANNEX_LETTER = {slug: chr(65 + i) for i, (slug, _) in enumerate(ANNEXES)}

GENERIC_DRAFT = re.compile(
    r'<h2 id="draft-only">DRAFT ONLY</h2>\s*<p>This Plan is currently only a DRAFT and has not been '
    r'accepted or implemented by WICEN WA\. It is largely incomplete\.</p>', re.S)


def load_yaml(path):
    out = subprocess.run(["ruby", "-ryaml", "-rjson", "-rdate", "-e",
                          "puts JSON.generate(YAML.load_file(ARGV[0], permitted_classes: [Date]))", str(path)],
                         check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def page_content(path):
    s = path.read_text()
    start = s.index('<div class="page-content">') + len('<div class="page-content">')
    depth = 1
    for m in re.finditer(r"<(/?)div\b", s[start:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return s[start:start + m.start()]
    raise ValueError(f"no page-content in {path}")


def fix_links(body):
    def repl(m):
        pre, href, post, text = m.groups()
        if 'class="gap-ref"' in pre + post:
            gid = href.split("#")[-1]
            return f'<a class="gap-ref" href="#{gid}">{text}</a>'
        path = href.split("#")[0]
        slug = path.rstrip("/").split("/")[-1].removesuffix(".html")
        internal = href.startswith(("/PACE/", "./")) or not re.match(r"[a-z]+:|/|#", href)
        if internal and slug in CH_NUM:
            return f'<a href="#ch-{slug}">{text}</a> (Chapter {CH_NUM[slug]})'
        if internal and slug == "known-gaps":
            return f'<a href="#annex-known-gaps">{text}</a> (Annex {ANNEX_LETTER["known-gaps"]})'
        if href.startswith("/"):
            href = SITE_URL + href
        return f'<a{pre}href="{href}"{post}>{text}</a>'

    return re.sub(r'<a([^>]*?)href="([^"]*)"([^>]*)>(.*?)</a>', repl, body, flags=re.S)


def chapter_html(site, slug, title, part=None):
    n = CH_NUM[slug]
    body = page_content(site / "PACE" / f"{slug}.html")
    body = re.sub(r"<style.*?</style>|<script.*?</script>", "", body, flags=re.S)
    body = GENERIC_DRAFT.sub("", body)
    body = re.sub(r'<h2 id="draft-only">DRAFT ONLY</h2>\s*<p>(.*?)</p>',
                  r'<div class="draft-note"><strong>Draft.</strong> \1</div>', body, flags=re.S)
    body = re.sub(r"<h1\b", "<h2", body).replace("</h1>", "</h2>")
    # Drop a leading heading that only repeats the chapter title.
    body = re.sub(r'^\s*<h2[^>]*>\s*' + re.escape(title.split(" (")[0]) + r'\s*</h2>', "", body, flags=re.I)
    counter = iter(range(1, 1000))
    body = re.sub(r"<h2([^>]*)>(.*?)</h2>", lambda m: f'<h2{m.group(1)}><span class="num">{n}.{next(counter)}</span> {m.group(2)}</h2>', body, flags=re.S)
    body = fix_links(body)
    head = f'<p class="part-label">{html.escape(part)}</p>' if part else ""
    return (f'<section class="chapter" id="ch-{slug}">{head}'
            f'<h1><span class="mk">MK-ch-{slug}-X</span><span class="num">{n}</span> {html.escape(title)}</h1>'
            f'<p class="source">Website: {SITE_URL}/PACE/{slug}</p>{body}</section>')


def annex_open(slug, title, extra=""):
    letter = ANNEX_LETTER[slug]
    return (f'<section class="annex{extra}" id="annex-{slug}">'
            f'<h1><span class="mk">MK-annex-{slug}-X</span><span class="num">Annex {letter}</span> {html.escape(title)}</h1>')


def ruled_rows(cols, n):
    return "".join("<tr>" + "".join("<td></td>" for _ in range(cols)) + "</tr>" for _ in range(n))


def annexes_html(gaps, scans):
    out = []

    rows = "".join(f'<tr id="{g["id"].lower()}"><td class="nowrap">{g["id"]}</td><td>{html.escape(g["title"])}</td>'
                   f'<td>{html.escape(g["domain"])}</td><td>{html.escape(g["status"])}</td></tr>' for g in gaps)
    out.append(annex_open("known-gaps", "Known Gaps") +
               "<p>This manual is a draft. Where a chapter is incomplete or waiting on a decision, the text is marked "
               "with a gap ID such as <span class=\"gap-ref\">GAP-004</span>. Gaps are discussed and decided by the committee "
               "in the PACE Gap Register (a members' working document); the current list is also at "
               f"{SITE_URL}/PACE/known-gaps.</p>"
               f'<table class="data"><thead><tr><th>ID</th><th>Gap</th><th>Domain</th><th>Status</th></tr></thead>'
               f"<tbody>{rows}</tbody></table></section>")

    glossary = [
        ("ACMA", "Australian Communications and Media Authority — regulates amateur radio licensing"),
        ("AFAC", "Australasian Fire and Emergency Service Authorities Council — publisher of AIIMS"),
        ("AIIMS", "Australasian Inter-Service Incident Management System — the incident management system used by Australian emergency services"),
        ("APRS", "Automatic Packet Reporting System — position and short-message system on VHF"),
        ("AREDN", "Amateur Radio Emergency Data Network — Wi-Fi-based amateur mesh network"),
        ("DFES", "Department of Fire and Emergency Services (WA)"),
        ("DIS", "Digital Information Station — distributes incident information to members (Chapter 3)"),
        ("DNF", "Did not finish — a competitor withdrawn from an event"),
        ("DTG", "Date-time group — when a message was written"),
        ("HF", "High frequency (3–30 MHz) — long-distance radio"),
        ("ICS", "Incident Command System (US) — source of the ICS-2xx forms"),
        ("IMT", "Incident management team — the controlling agency's team running an incident"),
        ("ISG", "Incident Support Group — agencies supporting an incident management team"),
        ("JS8Call", "Weak-signal HF keyboard messaging mode with store-and-forward"),
        ("LEMC", "Local Emergency Management Committee — a local government's emergency management committee"),
        ("LSB / USB", "Lower / upper sideband — HF voice modes"),
        ("NCS", "Net Control Station"),
        ("NVIS", "Near-vertical incidence skywave — HF propagation for regional (roughly 0–800 km) coverage"),
        ("PACE", "Primary, Alternate, Contingency, Emergency — the plan's layered communications model"),
        ("RATEL", "Radiotelephone procedure — WICEN's voice procedure (Chapter 14)"),
        ("RMS", "Radio Message Server — a Winlink gateway station"),
        ("SC", "State Coordinator (WICEN WA)"),
        ("SEMC", "State Emergency Management Committee (WA)"),
        ("SITREP", "Situation report — the regular AIIMS summary of an incident"),
        ("UHF CB", "UHF citizens band radio (476–477 MHz), licence-free; channels 5 and 35 are emergency channels"),
        ("VARA", "HF modem used by Winlink"),
        ("VHF / UHF", "Very / ultra high frequency — local and repeater radio"),
        ("WIA", "Wireless Institute of Australia"),
        ("WICEN", "Wireless Institute Civil Emergency Network"),
        ("Winlink", "Radio email system using HF and VHF gateways"),
    ]
    out.append(annex_open("glossary", "Glossary") + '<table class="data glossary"><tbody>' +
               "".join(f"<tr><th>{html.escape(t)}</th><td>{html.escape(d)}</td></tr>" for t, d in glossary) +
               "</tbody></table></section>")

    out.append(annex_open("message-form", "Message Form", " form") + """
<p class="form-note">Based on the RATEL message form (Annex A of the archived manual, Annex H). See Chapter 13 for how to complete and send it.</p>
<table class="form">
<tr><td class="w33"><label>Serial number</label>IN&nbsp;/&nbsp;OUT&nbsp;&nbsp;______ / ______</td>
<td class="w33"><label>Precedence <span class="gap-ref">GAP-012</span></label>&#9744; ROUTINE<br>&#9744; PRIORITY<br>&#9744; EMERGENCY</td>
<td class="w33"><label>Date-time group</label>&nbsp;</td></tr>
<tr><td><label>Originator's number</label>&nbsp;</td><td colspan="2"><label>Transmission instructions (e.g. READ BACK, RELAY TO)</label>&nbsp;</td></tr>
<tr><td colspan="3"><label>From</label>&nbsp;</td></tr>
<tr><td colspan="3"><label>To</label>&nbsp;</td></tr>
<tr><td colspan="3"><label>Info</label>&nbsp;</td></tr>
<tr><td colspan="3" class="text-box"><label>Text</label></td></tr>
<tr><td colspan="2"><label>Releasing officer — name and signature</label>&nbsp;</td><td><label>Time released</label>&nbsp;</td></tr>
</table>
<table class="form ops">
<tr><th></th><th>Date</th><th>Time</th><th>System / frequency</th><th>Operator</th></tr>
<tr><th>R — received</th><td></td><td></td><td></td><td></td></tr>
<tr><th>D — despatched</th><td></td><td></td><td></td><td></td></tr>
</table>
</section>""")

    out.append(annex_open("station-log", "Station and Net Log", " form") + """
<table class="form header">
<tr><td><label>Station call sign</label>&nbsp;</td><td><label>Location</label>&nbsp;</td><td><label>Date</label>&nbsp;</td></tr>
<tr><td colspan="2"><label>Event / incident</label>&nbsp;</td><td><label>Sheet</label>____ of ____</td></tr>
<tr><td colspan="3"><label>Operators</label>&nbsp;</td></tr>
</table>
<p class="form-note">Log every transmission — time, stations, serial number and a brief summary. The log stays with the station. Net Control also logs every check-in (Chapter 13).</p>
<table class="form log"><thead><tr><th class="c-time">Time</th><th class="c-call">From</th><th class="c-call">To</th><th class="c-serial">Serial no.</th><th>Brief summary</th><th class="c-op">Op</th></tr></thead>
<tbody>""" + ruled_rows(6, 18) + """</tbody></table>

</section>""")

    out.append(annex_open("checkpoint-report", "Event Checkpoint Report", " form") + """
<table class="form header">
<tr><td colspan="2"><label>Event</label>&nbsp;</td><td><label>Date / day</label>&nbsp;</td></tr>
<tr><td><label>Checkpoint</label>&nbsp;</td><td><label>Operator / call sign</label>&nbsp;</td><td><label>Sheet</label>____ of ____</td></tr>
</table>
<p class="form-note">Read bib numbers digit by digit (“Two One Four”); Net Control reads them back. Report in batches at the agreed interval, and report the sweep as it passes. Do not send competitor names or medical details over the air. Draft format <span class="gap-ref">GAP-048</span> — see Chapter 12.</p>
<table class="form log"><thead><tr><th class="c-time">Time</th><th class="c-serial">Bib no.</th><th class="c-status">Through / Withdrawn</th><th>Notes (reason for withdrawal, condition)</th><th class="c-time">Sent to net</th></tr></thead>
<tbody>""" + ruled_rows(5, 18) + """</tbody></table>

</section>""")

    out.append(annex_open("frequency-card", "Frequency Quick Reference") + """
<p>Compiled from Chapters 8–10. Frequencies may change with interference and propagation; Net Control directs any change. <span class="gap-ref">GAP-041</span></p>
<table class="data"><thead><tr><th>Use</th><th>Day (0700–1800 WST)</th><th>Night (1800–0700 WST)</th><th>Mode</th></tr></thead><tbody>
<tr><td>Statewide coordination</td><td>7.110 MHz</td><td>3.600 MHz</td><td>LSB</td></tr>
<tr><td>Alternate coordination</td><td>7.090 MHz</td><td>3.650 MHz</td><td>LSB</td></tr>
<tr><td>Tactical operations</td><td>7.130 MHz</td><td>3.580 MHz</td><td>LSB</td></tr>
<tr><td>Interstate liaison</td><td colspan="2">14.300 MHz (alternate 14.250 MHz)</td><td>USB</td></tr>
</tbody></table>
<table class="data"><thead><tr><th>Digital</th><th>40m</th><th>80m</th><th>20m (interstate)</th></tr></thead><tbody>
<tr><td>JS8Call</td><td>7.078 MHz</td><td>3.578 MHz</td><td>14.078 MHz</td></tr>
<tr><td>Winlink (VARA)</td><td>7.095 MHz</td><td>3.595 MHz</td><td>14.095 MHz</td></tr>
</tbody></table>
<table class="data"><thead><tr><th>Net schedule</th><th></th></tr></thead><tbody>
<tr><td>On the hour</td><td>Statewide status net <span class="gap-ref">GAP-042</span></td></tr>
<tr><td>Half past the hour</td><td>Operational coordination net</td></tr>
</tbody></table>
<table class="data"><thead><tr><th>Band selection</th><th></th></tr></thead><tbody>
<tr><td>Under 300 km</td><td>80m or VHF</td></tr>
<tr><td>300–800 km</td><td>80m NVIS or 40m</td></tr>
<tr><td>800–2000 km</td><td>40m</td></tr>
<tr><td>Interstate</td><td>20m</td></tr>
</tbody></table>
<p class="form-note">Changing frequency: Net Control orders CHANGE TO (frequency); all stations acknowledge; Net Control gives CHANGE NOW. Nobody moves on the first order alone.</p>
</section>""")

    for slug, intro in (("prep-checklist", "WICEN WA's General Preparation Checklist, reproduced as issued."),
                        ("ratel", "WICEN WA's archived <em>Radiotelephone (RATEL) Procedure for Operators in WICEN</em> "
                                  "(about 2002), reproduced for reference. Where it differs from Chapter 14, Chapter 14 applies.")):
        imgs = scans[slug]
        first = f'<p class="form-note">{intro}</p><div class="scan first"><img src="{imgs[0]}"></div>'
        rest = "".join(f'<div class="scan"><img src="{i}"></div>' for i in imgs[1:])
        out.append(annex_open(slug, dict(ANNEXES)[slug], " scans") + first + rest + "</section>")
    return "\n".join(out)


def front_html(manual, logo, pages):
    rev = manual["revisions"][0]
    pg = lambda key: pages.get(key, "")
    hist = "".join(f'<tr><td>{html.escape(str(r["revision"]))}</td><td class="nowrap">{html.escape(str(r["date"]))}</td>'
                   f'<td>{html.escape(r["by"])}</td><td>{html.escape(r["changes"])}</td></tr>' for r in manual["revisions"])
    toc = []
    for part, chs in PARTS:
        toc.append(f'<tr class="toc-part"><td colspan="2">{html.escape(part)}</td><td></td></tr>')
        for slug, title in chs:
            toc.append(f'<tr><td class="toc-n">{CH_NUM[slug]}</td><td><a href="#ch-{slug}">{html.escape(title)}</a></td>'
                       f'<td class="toc-p">{pg("ch-" + slug)}</td></tr>')
    toc.append('<tr class="toc-part"><td colspan="2">Annexes</td><td></td></tr>')
    for slug, title in ANNEXES:
        toc.append(f'<tr><td class="toc-n">{ANNEX_LETTER[slug]}</td><td><a href="#annex-{slug}">{html.escape(title)}</a></td>'
                   f'<td class="toc-p">{pg("annex-" + slug)}</td></tr>')
    mapping = "".join(f"<tr><td>{CH_NUM[s]}</td><td>{html.escape(t)}</td><td>{SITE_URL}/PACE/{s}</td></tr>" for s, t in CHAPTERS)
    return f"""
<section class="cover">
  <img class="logo" src="{logo}">
  <p class="cover-org">Wireless Institute Civil Emergency Network — Western Australia</p>
  <h1 class="cover-title">{html.escape(manual["title"])}</h1>
  <p class="cover-sub">Emergency Communications Plan (PACE) and operating procedures</p>
  <p class="cover-status">{html.escape(manual["status"])}</p>
  <table class="cover-meta">
    <tr><th>Revision</th><td>{html.escape(str(rev["revision"]))}</td></tr>
    <tr><th>Date</th><td>{html.escape(str(rev["date"]))}</td></tr>
    <tr><th>Master copy</th><td>{SITE_URL}/PACE/overview</td></tr>
  </table>
  <p class="cover-note">Uncontrolled when printed. Check the revision in the footer against the current issue before relying on this copy.</p>
</section>
<section class="front" id="document-control">
  <h1>Document control</h1>
  <table class="data">
    <tr><th>Document</th><td>{html.escape(manual["title"])}</td></tr>
    <tr><th>Status</th><td>{html.escape(manual["status"])} — not yet adopted by WICEN WA</td></tr>
    <tr><th>Current revision</th><td>{html.escape(str(rev["revision"]))} — {html.escape(str(rev["date"]))}</td></tr>
    <tr><th>Source</th><td>Compiled from the PACE plan at {SITE_URL}/PACE/overview</td></tr>
    <tr><th>Changes and gaps</th><td>PACE Gap Register — Google Drive › WICEN-WA › PACE_Plan › Working_Docs</td></tr>
  </table>
  <h2>Revision history</h2>
  <table class="data"><thead><tr><th>Revision</th><th>Date</th><th>By</th><th>Changes</th></tr></thead><tbody>{hist}</tbody></table>
  <h2>About this manual</h2>
  <p>This manual brings WICEN WA's emergency communications plan and its supporting forms into one printable document for operators. It follows the <strong>PACE</strong> model — Primary, Alternate, Contingency, Emergency — set out in Chapters 1 and 2.</p>
  <p>The plan is a <strong>draft</strong>. Where something is incomplete or waiting on a committee decision, the text carries a gap ID such as <span class="gap-ref">GAP-004</span>. Annex A lists every gap.</p>
  <p>The website is the master copy. To propose a change, raise it with the committee through the PACE Gap Register. When the plan changes, a new revision of this manual is issued and recorded in the table above.</p>
  <p>Printed for binding on the left-hand edge, single-sided.</p>
  <h2>Chapters and website pages</h2>
  <table class="data small"><thead><tr><th>Ch.</th><th>Chapter</th><th>Website page</th></tr></thead><tbody>{mapping}</tbody></table>
</section>
<section class="front" id="contents">
  <h1>Contents</h1>
  <table class="toc"><tbody>{"".join(toc)}</tbody></table>
</section>"""


def render(html_path, pdf_path):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--no-first-run",
                    "--allow-file-access-from-files", "--virtual-time-budget=10000",
                    f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                   check=True, capture_output=True)


def main():
    out_pdf = Path(sys.argv[1]).resolve()
    manual = load_yaml(REPO / "_data/manual.yml")
    gaps = load_yaml(REPO / "_data/gaps.yml")
    rev = manual["revisions"][0]

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        site = tmp / "site"
        subprocess.run(["bundle", "exec", "jekyll", "build", "-q", "-d", str(site)], cwd=REPO, check=True)

        scans = {}
        for slug, src in (("prep-checklist", "assets/General Prep Checkllist.pdf"),
                          ("ratel", "assets/WICENWA-RATEL-Procedures.pdf")):
            d = tmp / slug
            subprocess.run(["swift", str(HERE / "pdftool.swift"), "render", str(REPO / src), str(d), "130"],
                           check=True, capture_output=True)
            scans[slug] = [p.as_uri() for p in sorted(d.glob("page-*.jpg"))]

        css = (HERE / "manual.css").read_text()
        css = css.replace("{{FOOTER_LEFT}}", f'{manual["title"]} — {manual["status"]}')
        css = css.replace("{{FOOTER_CENTRE}}", f'Revision {rev["revision"]} — {rev["date"]}')

        chapters = []
        for part, chs in PARTS:
            for i, (slug, title) in enumerate(chs):
                chapters.append(chapter_html(site, slug, title, part if i == 0 else None))
        body_rest = "\n".join(chapters) + annexes_html(gaps, scans)
        logo = (REPO / "assets/WicenLogoBlackYellowTrans.png").as_uri()

        html_path = tmp / "manual.html"
        pages = {}
        for _ in range(2):
            doc = (f'<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>{html.escape(manual["title"])}</title>'
                   f"<style>{css}</style></head><body>{front_html(manual, logo, pages)}{body_rest}</body></html>")
            html_path.write_text(doc)
            render(html_path, out_pdf)
            found = subprocess.run(["swift", str(HERE / "pdftool.swift"), "find", str(out_pdf), "MK-"],
                                   check=True, capture_output=True, text=True).stdout
            pages = {m.group(1): m.group(2) for m in re.finditer(r"MK-(\S+?)-X\S* (\d+)", found)}
        missing = [s for s, _ in CHAPTERS if f"ch-{s}" not in pages] + [s for s, _ in ANNEXES if f"annex-{s}" not in pages]
        if missing:
            print("warning: no page found for", missing, file=sys.stderr)
        total = subprocess.run(["swift", str(HERE / "pdftool.swift"), "pages", str(out_pdf)],
                               check=True, capture_output=True, text=True).stdout.strip()
        if "--keep-html" in sys.argv:
            shutil.copy(html_path, out_pdf.with_suffix(".html"))
    print(f"wrote {out_pdf} ({total} pages, revision {rev['revision']})")


if __name__ == "__main__":
    main()
