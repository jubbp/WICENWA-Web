# GitHub Pages Deployment Guide

## Automatic Deployment

The WICEN WA website is automatically built and deployed to GitHub Pages when you push changes to the `main` branch.

### How it works:

1. **GitHub Actions Workflow** (`.github/workflows/build.yml`)
   - Triggers on every push to `main` branch
   - Builds the Jekyll site
   - Runs HTML proofer to check for broken links
   - Automatically deploys to GitHub Pages

2. **Automatic Deployment**
   - The `_site/` folder is automatically deployed to GitHub Pages
   - Site becomes live at: `https://jubbp.github.io/WICENWA-Web/`

### Prerequisites

Ensure GitHub Pages is enabled:

1. Go to **Settings** > **Pages** (in your repository)
2. Under "Build and deployment":
   - Select "GitHub Actions" as the source
   - This is already configured by the workflow file

### Local Testing

Before pushing, test locally:

```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` in your browser.

### Making Changes

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test locally

3. Commit your changes:
   ```bash
   git add .
   git commit -m "Add description of changes"
   ```

4. Push to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request on GitHub

6. When ready, merge to `main` branch

7. The site automatically deploys within seconds!

### Adding Blog Posts

To add a new blog post:

1. Create a file in `_posts/` named: `YYYY-MM-DD-post-title.md`

2. Include front matter:
```yaml
---
layout: post
title: "Your Post Title"
date: 2026-02-25
author: Your Name
tags: tag1 tag2
---

Your post content here...
```

3. Commit and push - it automatically appears on the News page!

### Troubleshooting

If the build fails:

1. Check the **Actions** tab in your GitHub repository
2. Click the failed workflow run
3. Scroll down to see the error message
4. Common issues:
   - Missing gems (run `bundle install` locally)
   - Syntax errors in YAML front matter
   - Broken links (check HTML Proofer output)

### Support

For Jekyll documentation, visit: https://jekyllrb.com/
For GitHub Pages, visit: https://pages.github.com/
