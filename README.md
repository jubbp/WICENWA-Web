# WICEN WA Website

Wireless Institute Civil Emergency Network - Western Australia

## Overview

This is the official Jekyll-based website for WICEN WA, a volunteer emergency communications organization.

## Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   bundle install
   ```

2. **Start the development server:**
   ```bash
   bundle exec jekyll serve
   ```

3. **View the site:**
   - Open `http://localhost:4000` in your browser
   - The site automatically reloads on file changes

### Project Structure

```
.
├── _config.yml          # Site configuration
├── _includes/           # Reusable components (header, footer)
├── _layouts/            # Page templates (default, post)
├── _posts/              # Blog posts (news articles)
├── assets/              # CSS, images, logo
├── _site/               # Generated site (auto-built)
├── index.md             # Homepage
├── about.md             # About page
├── get-involved.md      # Get involved page
├── news.md              # News listing page
├── members.md           # Members page
├── contact.md           # Contact page
└── future-events.md     # Events page
```

## Adding Content

### Creating Blog Posts

1. Create a file in `_posts/` with format: `YYYY-MM-DD-title.md`
2. Include YAML front matter:
   ```yaml
   ---
   layout: post
   title: "Post Title"
   date: 2026-02-25
   author: Your Name
   tags: tag1 tag2
   ---
   ```
3. Write your post content in Markdown

### Adding Pages

Create a new `.md` file in the root directory with:
```yaml
---
layout: default
title: Page Title
---

# Page Title

Your content here...
```

## Deployment

The live site at https://wicenwa.org is published by GitHub Pages' built-in
"pages build and deploy" job whenever `main` is pushed — usually live within a
minute or two. The custom domain is set by [CNAME](CNAME).

### GitHub Actions

The workflow (`.github/workflows/build.yml`) runs on pushes and pull requests to
`main`. It does **not** deploy; it only:
- ✅ Builds the Jekyll site, so build errors show up in the **Actions** tab
- ✅ Checks for broken internal links (HTML Proofer, non-blocking)

### Caching

GitHub Pages lets browsers cache assets for 10 minutes. The stylesheet link in
`_layouts/default.html` carries a build-time version (`style.css?v=...`) so style
changes show up immediately after a deploy — give any new site-wide CSS or JS
file the same `?v={{ site.time | date: '%s' }}` suffix.

## Operations Manual

The printable WICEN-WA Operations Manual (A4 PDF, wide left margin for binding,
revision footer on every page) is compiled from the PACE plan pages plus annexes:

```bash
python3 -I _tools/manual/build_manual.py "WICEN-WA Operations Manual - Rev 0.1 (Draft).pdf"
```

To issue a new revision, add an entry at the top of `_data/manual.yml` and rebuild.

The manual is offered for download at `assets/manual/WICEN-WA-Operations-Manual.pdf`
(linked from the PACE Overview and Member Info pages, which show the revision from
`_data/manual.yml`). **Whenever the manual is republished, the current version must
be republished to the website too.** Issue it with `python3 -I tools/export.py manual`
in WICENWA-Records — that writes the same PDF to Google Drive and to this repository —
then commit and push. `tools/export.py check` there reports if the website copy is
not the current release.

The exercise forms (Operator Sign-In Sheet, Safety Briefing and Job Hazard
Analysis) are also built as standalone PDFs, one per form, each with its own
revision from `_data/forms.yml`:

```bash
python3 -I _tools/manual/build_forms.py "Exercise Forms"
```
Needs macOS (Swift/PDFKit renders the scanned annexes), Google Chrome and the
Jekyll toolchain.

## Site Configuration

Edit `_config.yml` to update:
- Site title and description
- Author information
- Navigation menu links
- Markdown and syntax highlighting settings

## Styling

- Main CSS: `assets/style.css`, styled after the WICEN WA awareness poster:
  near-black ground, cream text, WICEN yellow (#FFD22E), Anton headings over
  Archivo body text (Google Fonts)
- Dark mode by default; the sun/moon toggle in the header switches to light mode
  and remembers the visitor's choice. Colours are CSS variables at the top of
  `style.css` — `:root` is dark, `:root[data-theme="light"]` is light — so use the
  variables rather than hard-coded colours in pages
- Responsive design for mobile and desktop; hamburger menu on mobile (< 768px)

## Technologies

- **Jekyll** - Static site generator
- **Ruby** - Programming language
- **Markdown** - Content format
- **GitHub Pages** - Hosting & deployment
- **GitHub Actions** - Build and link checks

## Contributing

1. Create a branch: `git checkout -b feature/your-feature`
2. Make changes and test locally
3. Push branch: `git push origin feature/your-feature`
4. Create a Pull Request
5. Merge to `main` when approved
6. Site automatically deploys!

## Support & Resources

- **Jekyll Docs:** https://jekyllrb.com/docs/
- **Markdown Guide:** https://www.markdownguide.org/
- **GitHub Pages:** https://pages.github.com/

## License

All content © WICEN WA. All rights reserved.

---

**Live Site:** https://wicenwa.org/

**Repository:** https://github.com/jubbp/WICENWA-Web
