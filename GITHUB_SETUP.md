# GitHub Setup Instructions

## Initial GitHub Pages Configuration

Follow these steps to enable GitHub Pages for your repository:

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/jubbp/WICENWA-Web`
2. Click **Settings** (gear icon in top right)
3. In the left sidebar, click **Pages**
4. Under "Build and deployment":
   - Source: Select **GitHub Actions**
   - This enables automatic deployment using our workflow

### Step 2: Verify GitHub Actions

1. Go to the **Actions** tab in your repository
2. You should see "Build Jekyll Site" workflow listed
3. Click on it to see the workflow file
4. The workflow will automatically run on:
   - Every push to `main` branch
   - Every pull request to `main` branch

### Step 3: Check Deployment

After pushing your first change:

1. Go to **Actions** tab
2. Click the latest "Build Jekyll Site" workflow run
3. Wait for it to complete (usually takes 30-60 seconds)
4. Once complete, your site is live at:
   - `https://jubbp.github.io/WICENWA-Web/`

## Workflow Features

### Automatic Build
- Builds Jekyll site every time you push code
- Uses Ruby 3.2 with proper gem dependencies
- Builds with `JEKYLL_ENV=production` for optimized output

### Link Checking
- HTML Proofer checks for broken internal links
- Won't block deployment if issues found (can be changed)
- Helps catch issues early

### Automatic Deployment
- Deploys to GitHub Pages automatically
- Only deployments run on pushes to `main` branch
- Pull request don't trigger deployment

## Branch Protection (Optional)

To protect the `main` branch and require pull requests:

1. Go to **Settings** > **Branches**
2. Click **Add rule** under "Branch protection rules"
3. Pattern: `main`
4. Check:
   - ✅ "Require pull request reviews before merging"
   - ✅ "Dismiss stale pull request approvals when new commits are pushed"
   - ✅ "Require status checks to pass before merging"
   - ✅ "Build Jekyll Site" (under status checks)

## Secrets & Environment Variables

The workflow uses `GITHUB_TOKEN` (automatically available) for deployment.

To add custom environment variables:

1. Go to **Settings** > **Secrets and variables** > **Actions**
2. Click **New repository secret**
3. Add any secrets needed (none required for this setup)

## Monitoring Builds

### View Build Status

1. Go to **Actions** tab
2. See all workflow runs
3. Click a run to see detailed logs
4. Red ❌ = failed build
5. Green ✅ = successful build and deployment

### Common Issues

**Build fails with "bundle not found"**
- Run `bundle install` locally
- Commit `Gemfile.lock` to repository

**Build fails with "liquid syntax error"**
- Check for unclosed Jekyll template tags
- Verify YAML front matter syntax

**Site doesn't update after push**
- Check the Actions tab to ensure workflow completed
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Wait a few minutes for GitHub Pages to update

## Development Workflow

### Standard Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/add-new-blog-post
   ```

2. **Make your changes:**
   - Edit files, add blog posts, etc.

3. **Test locally:**
   ```bash
   bundle exec jekyll serve
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add new blog post about event"
   git push origin feature/add-new-blog-post
   ```

5. **Create Pull Request:**
   - Go to GitHub
   - You'll see a prompt to create a PR
   - Add description of changes
   - Click "Create pull request"

6. **Review and Merge:**
   - GitHub will automatically run the build workflow
   - Ensure build passes (green checkmark)
   - Merge the PR when ready

7. **Automatic Deployment:**
   - Once merged to `main`, deployment runs automatically
   - Site updates within 1-2 minutes

## Rollback (If Needed)

If something breaks on the live site:

1. Go to your repository on GitHub
2. Click **Code** tab
3. Find the commit that caused the issue
4. Click on it to view the changes
5. Use `git revert <commit-hash>` to undo
6. Push the revert commit
7. Site automatically redeploys with the fix

## Custom Domain (Optional)

To use a custom domain like `wicenwa.org`:

1. Go to **Settings** > **Pages**
2. Under "Custom domain", enter your domain
3. Click **Save**
4. Update your domain's DNS settings to point to GitHub Pages
5. Enable HTTPS when DNS is configured

## Further Customization

### Modify Workflow

Edit `.github/workflows/build.yml` to:
- Add notifications (Slack, email)
- Deploy to multiple environments
- Run additional tests
- Add deployment previews

### GitHub Actions Marketplace

Explore pre-built actions at: https://github.com/marketplace?type=actions

Popular Jekyll actions:
- Ruby setup
- HTML Proofer
- Jekyll deployment
- Dependency updates

## Support

- **GitHub Actions Docs:** https://docs.github.com/en/actions
- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **Jekyll Docs:** https://jekyllrb.com/docs/

---

**Your workflow is ready!** Push changes to see automatic builds and deployments in action. 🚀
