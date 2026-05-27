#!/bin/bash
# ============================================================
# DailyDose+ Web — GitHub Repo Setup Script
# Run this ONCE after cloning or after Codex/Cursor builds the pages.
# ============================================================

set -e

REPO_NAME="dailydose-plus-web"
GITHUB_USER="devish2"          # ← change to your GitHub username or org
DESCRIPTION="DailyDose+ web application — Guided Vitality initiative by MealOBox. Static multi-page site: landing, features, how-it-works, MealOBox sync, for providers, data security, and terms."

echo ""
echo "=== DailyDose+ Web — GitHub Repo Setup ==="
echo ""

# Step 1: Initialise git
git init
git add .
git commit -m "chore: initial repo scaffold — DailyDose+ web app

- README, .gitignore, CODEOWNERS
- GitHub Actions deploy workflow (validate + S3 + CloudFront)
- PR template and issue templates (bug, feature)
- Vital Clarity DESIGN.md design system spec
- Placeholder structure for 7 HTML pages"

echo "✅ Git initialised and first commit created."
echo ""

# Step 2: Create GitHub repo via CLI (requires gh auth login)
echo "Creating GitHub repository..."
gh repo create "$GITHUB_USER/$REPO_NAME" \
  --public \
  --description "$DESCRIPTION" \
  --source=. \
  --remote=origin \
  --push

echo ""
echo "✅ Repository created and pushed:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""

# Step 3: Set default branch to main
git branch -M main
git push -u origin main

echo ""
echo "=== Next steps ==="
echo ""
echo "1. Add GitHub Actions secrets in:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME/settings/secrets/actions"
echo ""
echo "   Secrets needed for S3/CloudFront deployment:"
echo "   - AWS_ACCESS_KEY_ID"
echo "   - AWS_SECRET_ACCESS_KEY"
echo "   - S3_BUCKET_STAGING         (e.g. dailydose-staging-mealobox)"
echo "   - CF_DISTRIBUTION_STAGING   (CloudFront distribution ID)"
echo ""
echo "2. Build the 7 HTML pages using the Cursor prompt (cursor_prompt_dailydose_plus.md)"
echo "   then commit and push:"
echo ""
echo "   git add ."
echo "   git commit -m 'feat: add all 7 DailyDose+ pages'"
echo "   git push"
echo ""
echo "3. Enable GitHub Pages (optional, for zero-config preview):"
echo "   Settings → Pages → Source: Deploy from branch → main → / (root)"
echo "   Preview URL: https://$GITHUB_USER.github.io/$REPO_NAME"
echo ""
echo "Done. 🎉"
