#!/usr/bin/env python3
"""Scaffold 7 DailyDose+ HTML shells from _components.html spec."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEAD = r'''  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" type="image/png" href="assets/favicon.png" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/favicon-180x180.png" />
  <title>{title}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            'surface': '#f3faff',
            'surface-dim': '#c7dde9',
            'surface-bright': '#f3faff',
            'surface-container-lowest': '#ffffff',
            'surface-container-low': '#e6f6ff',
            'surface-container': '#dbf1fe',
            'surface-container-high': '#d5ecf8',
            'surface-container-highest': '#cfe6f2',
            'surface-variant': '#cfe6f2',
            'surface-tint': '#005bc0',
            'on-surface': '#071e27',
            'on-surface-variant': '#414754',
            'inverse-surface': '#1e333c',
            'inverse-on-surface': '#dff4ff',
            'primary': '#005bbf',
            'on-primary': '#ffffff',
            'primary-container': '#1a73e8',
            'on-primary-container': '#ffffff',
            'inverse-primary': '#adc7ff',
            'primary-fixed': '#d8e2ff',
            'primary-fixed-dim': '#adc7ff',
            'on-primary-fixed': '#001a41',
            'on-primary-fixed-variant': '#004493',
            'secondary': '#546067',
            'on-secondary': '#ffffff',
            'secondary-container': '#d8e4ed',
            'on-secondary-container': '#5a666e',
            'secondary-fixed': '#d8e4ed',
            'secondary-fixed-dim': '#bcc8d1',
            'on-secondary-fixed': '#121d23',
            'on-secondary-fixed-variant': '#3d484f',
            'tertiary': '#ad2f34',
            'on-tertiary': '#ffffff',
            'tertiary-container': '#cf484a',
            'on-tertiary-container': '#140001',
            'tertiary-fixed': '#ffdad8',
            'tertiary-fixed-dim': '#ffb3b0',
            'on-tertiary-fixed': '#410006',
            'on-tertiary-fixed-variant': '#8c1520',
            'error': '#ba1a1a',
            'on-error': '#ffffff',
            'error-container': '#ffdad6',
            'on-error-container': '#93000a',
            'outline': '#727785',
            'outline-variant': '#c1c6d6',
            'background': '#f3faff',
            'on-background': '#071e27',
          }},
          borderRadius: {{
            'sm': '0.25rem',
            DEFAULT: '0.5rem',
            'md': '0.75rem',
            'lg': '1rem',
            'xl': '1.5rem',
            'full': '9999px',
          }},
          spacing: {{
            'unit': '8px',
            'container-padding': '24px',
            'stack-gap': '16px',
            'inline-gap': '12px',
            'section-margin': '32px',
          }},
          fontFamily: {{
            sans: ['Lexend', 'sans-serif'],
            serif: ['Lexend', 'sans-serif'],
            mono: ['Lexend', 'sans-serif'],
          }},
          fontSize: {{
            'display': ['34px', {{ lineHeight: '42px', letterSpacing: '-0.02em', fontWeight: '600' }}],
            'headline-lg': ['24px', {{ lineHeight: '32px', letterSpacing: '0', fontWeight: '600' }}],
            'headline-md': ['20px', {{ lineHeight: '28px', letterSpacing: '0', fontWeight: '500' }}],
            'body-lg': ['18px', {{ lineHeight: '26px', letterSpacing: '0.01em', fontWeight: '400' }}],
            'body-md': ['16px', {{ lineHeight: '24px', letterSpacing: '0.01em', fontWeight: '400' }}],
            'label-lg': ['14px', {{ lineHeight: '20px', letterSpacing: '0.02em', fontWeight: '500' }}],
            'label-sm': ['12px', {{ lineHeight: '16px', letterSpacing: '0.04em', fontWeight: '600' }}],
          }},
        }},
      }},
    }};
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" />
  <style>
    * {{ font-family: 'Lexend', sans-serif; }}
    .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(12, 1fr); gap: 24px; }}
    .glass-card {{ background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.3); }}
    .soft-shadow {{ box-shadow: 0 4px 20px rgba(0,91,191,0.08); }}
    .floating-anim {{ animation: floating 3s ease-in-out infinite; }}
    @keyframes floating {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-15px); }} }}
    .hero-gradient {{ background: linear-gradient(135deg, #f3faff 0%, #e6f6ff 100%); }}
    .vitality-gradient {{ background: linear-gradient(135deg, #005bbf, #1a73e8); }}
    #mobile-menu {{ max-height: 0; overflow: hidden; transition: max-height 0.3s ease-in-out; }}
    #mobile-menu.is-open {{ max-height: 480px; }}
  </style>'''

NAV_LINKS = [
    ('index.html', 'Home'),
    ('features.html', 'Features'),
    ('how-it-works.html', 'How It Works'),
    ('mealobox-sync.html', 'MealOBox Sync'),
    ('for-providers.html', 'For Providers'),
    ('data-security.html', 'Security'),
]


def nav_link(href: str, label: str, active: str, mobile: bool = False) -> str:
    base = 'text-body-md transition-colors'
    if href == active:
        cls = f'{base} text-primary font-semibold'
        extra = ' aria-current="page"'
    else:
        cls = f'{base} text-on-surface-variant hover:text-primary'
        extra = ''
    pad = ' py-3 px-2' if mobile else ''
    return f'<a href="{href}" data-nav-link class="{cls}{pad}"{extra}>{label}</a>'


def navbar(active: str) -> str:
    desktop = '\n          '.join(nav_link(h, label, active) for h, label in NAV_LINKS)
    mobile = '\n          '.join(nav_link(h, label, active, mobile=True) for h, label in NAV_LINKS)
    return f'''  <header class="fixed w-full top-0 z-50 bg-surface shadow-sm">
    <div class="max-w-6xl mx-auto px-container-padding">
      <nav class="flex items-center justify-between h-16 md:h-20" aria-label="Main navigation">
        <a href="index.html" class="flex items-center gap-2 shrink-0">
          <span class="material-symbols-outlined text-primary text-3xl" aria-hidden="true">medication</span>
          <span class="flex flex-col leading-tight">
            <span class="text-primary font-semibold text-headline-md">DailyDose+</span>
            <span class="text-secondary text-label-sm">by MealOBox</span>
          </span>
        </a>
        <div class="hidden md:flex items-center gap-6">
          {desktop}
          <a href="index.html" class="bg-primary text-white rounded-full px-5 py-2 text-label-lg font-medium hover:opacity-95 active:scale-[0.98] transition-transform whitespace-nowrap">Get Started Free</a>
        </div>
        <button type="button" id="menu-toggle" class="md:hidden min-w-[44px] min-h-[44px] flex items-center justify-center rounded-lg text-on-surface" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
          <span class="material-symbols-outlined" id="menu-toggle-icon" aria-hidden="true">menu</span>
        </button>
      </nav>
      <div id="mobile-menu" class="md:hidden border-t border-outline-variant" aria-label="Mobile navigation">
        <div class="flex flex-col gap-1 py-4">
          {mobile}
          <a href="index.html" class="mt-2 bg-primary text-white rounded-full px-5 py-3 text-label-lg font-medium text-center active:scale-[0.98] transition-transform">Get Started Free</a>
        </div>
      </div>
    </div>
  </header>'''


FOOTER = r'''  <footer class="bg-surface-container-low border-t border-outline-variant mt-section-margin">
    <div class="max-w-6xl mx-auto px-container-padding py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div>
          <a href="index.html" class="flex items-center gap-2 mb-4">
            <span class="material-symbols-outlined text-primary text-2xl" aria-hidden="true">medication</span>
            <span class="text-primary font-semibold text-headline-md">DailyDose+</span>
          </a>
          <p class="text-body-md text-on-surface-variant mb-6">An initiative by MealOBox dedicated to guided vitality.</p>
          <div class="flex gap-3">
            <a href="mailto:hello@mealobox.in" class="w-11 h-11 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-colors" aria-label="Email hello@mealobox.in">
              <span class="material-symbols-outlined text-xl" aria-hidden="true">mail</span>
            </a>
            <a href="https://mealobox.in" class="w-11 h-11 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-colors" rel="noopener noreferrer" aria-label="Visit mealobox.in">
              <span class="material-symbols-outlined text-xl" aria-hidden="true">language</span>
            </a>
            <a href="https://mealobox.in" class="w-11 h-11 rounded-full bg-surface-container flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-colors" rel="noopener noreferrer" aria-label="MealOBox community">
              <span class="material-symbols-outlined text-xl" aria-hidden="true">groups</span>
            </a>
          </div>
        </div>
        <div>
          <p class="text-label-lg font-semibold text-on-surface mb-4">Product</p>
          <ul class="space-y-2 text-body-md">
            <li><a href="features.html" class="text-on-surface-variant hover:text-primary transition-colors">Features</a></li>
            <li><a href="how-it-works.html" class="text-on-surface-variant hover:text-primary transition-colors">How It Works</a></li>
            <li><a href="mealobox-sync.html" class="text-on-surface-variant hover:text-primary transition-colors">MealOBox Sync</a></li>
            <li><a href="for-providers.html" class="text-on-surface-variant hover:text-primary transition-colors">For Providers</a></li>
            <li><a href="features.html" class="text-on-surface-variant hover:text-primary transition-colors">App Tour</a></li>
          </ul>
        </div>
        <div>
          <p class="text-label-lg font-semibold text-on-surface mb-4">Legal</p>
          <ul class="space-y-2 text-body-md">
            <li><a href="data-security.html" class="text-on-surface-variant hover:text-primary transition-colors">Privacy Policy</a></li>
            <li><a href="terms.html" class="text-on-surface-variant hover:text-primary transition-colors">Terms of Service</a></li>
            <li><a href="data-security.html" class="text-on-surface-variant hover:text-primary transition-colors">Data Security</a></li>
            <li><a href="data-security.html" class="text-on-surface-variant hover:text-primary transition-colors">HIPAA Disclosure</a></li>
          </ul>
        </div>
        <div>
          <p class="text-label-lg font-semibold text-on-surface mb-4">Contact</p>
          <ul class="space-y-2 text-body-md">
            <li><a href="mailto:hello@mealobox.in" class="text-on-surface-variant hover:text-primary transition-colors">hello@mealobox.in</a></li>
            <li><a href="https://mealobox.in" class="text-on-surface-variant hover:text-primary transition-colors" rel="noopener noreferrer">mealobox.in</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-outline-variant mt-10 pt-6 text-center text-label-sm text-on-surface-variant">
        © 2026 DailyDose+ — An initiative by MealOBox Foodtech Pvt. Ltd. | All rights reserved.
      </div>
    </div>
  </footer>'''

PAGES = [
    ('index.html', 'DailyDose+ — Guided Vitality by MealOBox', 'index.html', 'index'),
    ('features.html', 'Features — DailyDose+', 'features.html', 'features'),
    ('how-it-works.html', 'How It Works — DailyDose+', 'how-it-works.html', 'how-it-works'),
    ('mealobox-sync.html', 'MealOBox Sync — DailyDose+', 'mealobox-sync.html', 'mealobox-sync'),
    ('for-providers.html', 'For Providers — DailyDose+', 'for-providers.html', 'for-providers'),
    ('data-security.html', 'Data Security — DailyDose+', 'data-security.html', 'data-security'),
    ('terms.html', 'Terms of Service — DailyDose+', '', 'terms'),
]


def shell(filename: str, title: str, active_href: str, page_name: str) -> str:
    nav = navbar(active_href)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD.format(title=title)}
</head>
<body class="bg-surface text-on-surface antialiased">
{nav}
  <main class="pt-24 md:pt-28 min-h-[50vh]">
    <!-- PAGE CONTENT: {page_name} -->
  </main>
{FOOTER}
  <script>
  </script>
</body>
</html>
'''


def main():
    for filename, title, active, name in PAGES:
        (ROOT / filename).write_text(shell(filename, title, active, name), encoding='utf-8')
        print(f'Scaffolded {filename}')


if __name__ == '__main__':
    main()
