"""Build the WICEN-WA exercise and field forms as standalone A4 PDFs.

usage (from the repository root):
    python3 -I _tools/manual/build_forms.py <output-directory>

Writes one PDF per form in _data/forms.yml, named "<title> - Rev <n> (<status>).pdf",
with the form's own revision in the footer of every page.
"""
import html
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import forms  # noqa: E402
from build_manual import CHROME, load_yaml  # noqa: E402

BODIES = {"sign-in": (forms.signin_html, "landscape"), "safety-jha": (forms.jha_html, "")}


def main():
    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    base_css = (HERE / "manual.css").read_text()
    logo = (REPO / "assets/WicenLogoBlackYellowTrans.png").as_uri()

    for form in load_yaml(REPO / "_data/forms.yml"):
        rev = form["revisions"][0]
        body_fn, page_class = BODIES[form["id"]]
        css = (base_css.replace("{{FOOTER_LEFT}}", f'WICEN-WA {form["short"]} — {form["status"]}')
                       .replace("{{FOOTER_CENTRE}}", f'Revision {rev["revision"]} — {rev["date"]}'))
        doc = f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8">
<title>{html.escape(form["title"])}</title><style>{css}
.form-title {{ display: flex; align-items: center; gap: 4mm; }}
.form-title img {{ width: 14mm; }}
.form-title h1 {{ flex: 1; margin: 0; }}
</style></head><body>
<section class="form standalone {page_class}">
<div class="form-title"><img src="{logo}"><h1>{html.escape(form["title"])}</h1></div>
{body_fn()}
</section></body></html>"""
        name = f'{form["title"]} - Rev {rev["revision"]} ({form["status"].title()}).pdf'
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "form.html"
            src.write_text(doc)
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--no-first-run",
                            "--allow-file-access-from-files", "--virtual-time-budget=5000",
                            f"--print-to-pdf={out_dir / name}", src.as_uri()], check=True, capture_output=True)
        print("wrote", out_dir / name)


if __name__ == "__main__":
    main()
