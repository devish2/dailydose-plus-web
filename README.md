# DailyDose+ Web — Guided Vitality by MealOBox

> **DailyDose+** is a health-tech initiative by [MealOBox](https://mealobox.in) that helps users manage medication schedules, track daily hydration, sync tiffin meals with health data, and store medical records securely.

This repository contains the **marketing and informational web application** for DailyDose+. For the mobile app (React Native), see [mealobox/dailydose-app](https://github.com/mealobox/dailydose-app).

---

## 🌐 Live

| Environment | URL |
|---|---|
| Production | `https://dailydose.mealobox.in` |
| Staging | `https://staging.dailydose.mealobox.in` |

---

## 📄 Pages

| File | Route | Description |
|---|---|---|
| `index.html` | `/` | Landing page — hero, features bento, security strip, app preview |
| `features.html` | `/features` | Deep-dive feature grid with interactive demos |
| `how-it-works.html` | `/how-it-works` | 4-step alternating timeline |
| `mealobox-sync.html` | `/mealobox-sync` | MealOBox ↔ DailyDose+ AI nutrition sync |
| `for-providers.html` | `/for-providers` | B2B page for healthcare providers & corporates |
| `data-security.html` | `/data-security` | HIPAA, AES-256, data residency, privacy protocols |
| `terms.html` | `/terms` | Terms of Service (DPDP Act 2023, IT Act 2000) |

---

## 🎨 Design System — Vital Clarity

All pages implement the **Vital Clarity** design system (exported from Stitch). No external CSS files — tokens are embedded directly in each page's Tailwind config.

| Token type | Source |
|---|---|
| Colors | `vital_clarity/DESIGN.md` — Deep Blue primary, Soft Aqua surfaces, Coral medication accent |
| Typography | Lexend (Google Fonts) — 7-level type scale |
| Spacing | 8px baseline grid |
| Icons | Google Material Symbols Outlined |

Semantic color intent:
- `#005bbf` (primary) → trust, CTAs, active nav
- `#cf484a` (tertiary-container) → medication alerts, pill cards
- `#00a651` → hydration goals, positive progress

---

## 🛠 Tech Stack

```
HTML5 + Tailwind CSS v3 (CDN)   No build step
Vanilla JavaScript ES6+          No framework
Google Fonts (Lexend)            CDN
Material Symbols Outlined        CDN
```

This is a **zero-dependency static site**. No npm, no bundler, no node_modules. Every page is a self-contained HTML file that opens directly in a browser.

---

## 🚀 Getting Started

### View locally

```bash
git clone https://github.com/mealobox/dailydose-plus-web.git
cd dailydose-plus-web
open index.html          # macOS
# or
xdg-open index.html     # Linux
# or just drag the file into Chrome
```

No install step required.

### Serve locally (optional, for accurate relative paths)

```bash
# Python 3
python3 -m http.server 3000
# Then open http://localhost:3000
```

---

## 📁 Repository Structure

```
dailydose-plus-web/
│
├── index.html                  Landing page
├── features.html               Features deep-dive
├── how-it-works.html           4-step user journey
├── mealobox-sync.html          MealOBox AI sync page
├── for-providers.html          B2B / healthcare providers
├── data-security.html          Security & HIPAA
├── terms.html                  Terms of Service
│
├── _components.html            ⚠ Reference only — shared Navbar & Footer snippets
│                               (not a real page; used during development)
│
├── vital_clarity/
│   └── DESIGN.md               Full Vital Clarity design token specification
│
├── assets/
│   └── og-image.png            Open Graph preview image (1200×630)
│
├── .gitignore
├── CODEOWNERS
└── README.md
```

---

## ✅ Interactivity

Each page includes vanilla JS for:

| Feature | Pages |
|---|---|
| Mobile hamburger nav | All |
| Active nav link detection | All |
| Scroll-to-top button | All |
| "Mark as Taken" medication toggle | `index.html`, `features.html` |
| Water intake logger + SVG ring update | `index.html`, `features.html` |
| Accordion expand/collapse | `data-security.html` |
| IntersectionObserver ToS anchor nav | `terms.html` |
| Demo request form validation + success state | `for-providers.html` |

---

## ♿ Accessibility

- WCAG 2.1 AA target
- Semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- Single `<h1>` per page, logical heading hierarchy
- `aria-label` on all icon-only interactive elements
- `lang="en"` on all `<html>` tags
- Minimum 44×44px touch targets
- Focus: `outline-2 outline-primary` on all focusable elements
- Color never used as the sole state indicator (always paired with icon or text)

---

## 📱 Responsive Breakpoints

| Breakpoint | Behaviour |
|---|---|
| `< 768px` (mobile) | Single column, hamburger nav, bento grid stacks to 1 col |
| `768px+` (md) | 2-column layouts, bento grid 2 cols |
| `1024px+` (lg) | Full 12-col bento, side-by-side heroes, sticky ToS sidebar |

Tested at 375px (iPhone SE), 768px (iPad), 1440px (desktop).

---

## 🔗 Related Repositories

| Repo | Description |
|---|---|
| [`mealobox/mealobox-app`](https://github.com/mealobox/mealobox-app) | MealOBox customer mobile app (React Native) |
| [`mealobox/dailydose-app`](https://github.com/mealobox/dailydose-app) | DailyDose+ mobile app (React Native) |
| [`mealobox/mealobox-backend`](https://github.com/mealobox/mealobox-backend) | Node.js/Express API + MongoDB Atlas |
| [`mealobox/admin-dashboard`](https://github.com/mealobox/admin-dashboard) | Internal admin panel |

---

## 🌍 Deployment

This site is hosted as a static site. Recommended options:

```bash
# AWS S3 + CloudFront (current MealOBox infra)
aws s3 sync . s3://dailydose-mealobox-web --exclude ".git/*" --exclude "_components.html"
aws cloudfront create-invalidation --distribution-id <ID> --paths "/*"

# Or: Vercel (zero config)
vercel --prod

# Or: Netlify drag-and-drop
# Drag the project folder to app.netlify.com/drop
```

For S3: set `index.html` as the default root document. Enable static website hosting. Use CloudFront for HTTPS + CDN.

---

## 🤝 Contributing

1. Fork the repo and create a feature branch: `git checkout -b feat/your-feature`
2. Follow the Vital Clarity design system — do not introduce arbitrary hex values or Tailwind utilities outside the config tokens.
3. Test at 375px, 768px, and 1440px before submitting a PR.
4. Run a basic a11y audit (axe DevTools or Lighthouse) — fix any violations before raising a PR.
5. Open a pull request against `main` with a clear description.

---

## 📬 Contact

| | |
|---|---|
| Product | support@mealobox.in |
| Security | security@mealobox.in |
| Website | mealobox.in |
| Founder | Devesh — [@devish2](https://github.com/devish2) |

---

## 📝 License

© 2026 DailyDose+ — An initiative by **MealOBox Foodtech Private Limited**
CIN: U72900UP2020PTC132213 | Lucknow, Uttar Pradesh, India

All rights reserved. This codebase is proprietary. Do not reproduce or distribute without written permission from MealOBox Foodtech Pvt. Ltd.
