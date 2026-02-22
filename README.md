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

The site automatically deploys to GitHub Pages when you push to the `main` branch.

See [DEPLOY.md](DEPLOY.md) for detailed deployment instructions.

### GitHub Actions

The workflow (`.github/workflows/build.yml`) will:
- ✅ Build the Jekyll site
- ✅ Check for broken links
- ✅ Deploy to GitHub Pages
- ✅ Display build status

## Site Configuration

Edit `_config.yml` to update:
- Site title and description
- Author information
- Navigation menu links
- Markdown and syntax highlighting settings

## Styling

- Main CSS: `assets/style.css`
- Color scheme: Gold (#FDB913) and dark gray
- Responsive design for mobile and desktop
- Hamburger menu on mobile (< 768px)

## Technologies

- **Jekyll** - Static site generator
- **Ruby** - Programming language
- **Markdown** - Content format
- **GitHub Pages** - Hosting & deployment
- **GitHub Actions** - CI/CD automation

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

**Live Site:** https://jubbp.github.io/WICENWA-Web/

**Repository:** https://github.com/jubbp/WICENWA-Web
