#!/usr/bin/env python3
"""One-shot generator for DailyDose+ static pages — run once, then delete if desired."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TAILWIND_HEAD = r'''  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            surface: '#f3faff',
            'surface-dim': '#c7dde9',
            'surface-bright': '#f3faff',
            'surface-container-lowest': '#ffffff',
            'surface-container-low': '#e6f6ff',
            'surface-container': '#dbf1fe',
            'surface-container-high': '#d5ecf8',
            'surface-container-highest': '#cfe6f2',
            'on-surface': '#071e27',
            'on-surface-variant': '#414754',
            'inverse-surface': '#1e333c',
            'inverse-on-surface': '#dff4ff',
            outline: '#727785',
            'outline-variant': '#c1c6d6',
            'surface-tint': '#005bc0',
            primary: '#005bbf',
            'on-primary': '#ffffff',
            'primary-container': '#1a73e8',
            'on-primary-container': '#ffffff',
            'inverse-primary': '#adc7ff',
            secondary: '#546067',
            'on-secondary': '#ffffff',
            'secondary-container': '#d8e4ed',
            'on-secondary-container': '#5a666e',
            tertiary: '#ad2f34',
            'on-tertiary': '#ffffff',
            'tertiary-container': '#cf484a',
            'on-tertiary-container': '#140001',
            error: '#ba1a1a',
            'on-error': '#ffffff',
            'error-container': '#ffdad6',
            'on-error-container': '#93000a',
            'primary-fixed': '#d8e2ff',
            'primary-fixed-dim': '#adc7ff',
            'on-primary-fixed': '#001a41',
            'on-primary-fixed-variant': '#004493',
            'secondary-fixed': '#d8e4ed',
            'secondary-fixed-dim': '#bcc8d1',
            'on-secondary-fixed': '#121d23',
            'on-secondary-fixed-variant': '#3d484f',
            'tertiary-fixed': '#ffdad8',
            'tertiary-fixed-dim': '#ffb3b0',
            'on-tertiary-fixed': '#410006',
            'on-tertiary-fixed-variant': '#8c1520',
            background: '#f3faff',
            'on-background': '#071e27',
            'surface-variant': '#cfe6f2',
            water: '#00a651',
          },
          fontFamily: { sans: ['Lexend', 'sans-serif'] },
          fontSize: {
            display: ['34px', { lineHeight: '42px', letterSpacing: '-0.02em', fontWeight: '600' }],
            'headline-lg': ['24px', { lineHeight: '32px', fontWeight: '600' }],
            'headline-md': ['20px', { lineHeight: '28px', fontWeight: '500' }],
            'body-lg': ['18px', { lineHeight: '26px', letterSpacing: '0.01em' }],
            'body-md': ['16px', { lineHeight: '24px', letterSpacing: '0.01em' }],
            'label-lg': ['14px', { lineHeight: '20px', letterSpacing: '0.02em', fontWeight: '500' }],
            'label-sm': ['12px', { lineHeight: '16px', letterSpacing: '0.04em', fontWeight: '600' }],
          },
          borderRadius: {
            sm: '0.25rem',
            DEFAULT: '0.5rem',
            md: '0.75rem',
            lg: '1rem',
            xl: '1.5rem',
          },
          spacing: {
            'container-padding': '24px',
            'stack-gap': '16px',
            'inline-gap': '12px',
            'section-margin': '32px',
          },
          boxShadow: {
            'soft-shadow': '0 4px 20px rgba(0, 91, 191, 0.08)',
          },
        },
      },
      plugins: [
        function ({ addBase, theme }) {
          addBase({
            ':focus-visible': {
              outline: '2px solid',
              outlineOffset: '2px',
              outlineColor: theme('colors.primary'),
            },
          });
        },
      ],
    };
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" />
  <style>
    .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
    html { scroll-behavior: smooth; }
  </style>'''

NAVBAR = r'''  <header class="fixed w-full top-0 z-50 bg-surface shadow-sm">
    <nav class="relative max-w-6xl mx-auto px-container-padding flex items-center justify-between h-16 md:h-20" aria-label="Main navigation">
      <a href="index.html" class="flex items-center gap-2 text-primary font-semibold text-headline-md">
        <span class="material-symbols-outlined text-primary" aria-hidden="true">medication</span>
        DailyDose+
      </a>
      <button type="button" id="nav-toggle" class="md:hidden min-w-[44px] min-h-[44px] flex items-center justify-center text-on-surface rounded-lg" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
        <span class="material-symbols-outlined" id="nav-toggle-icon" aria-hidden="true">menu</span>
      </button>
      <div id="mobile-menu" class="hidden flex flex-col gap-4 p-container-padding absolute top-full left-0 right-0 bg-surface border-b border-outline-variant shadow-sm md:flex md:flex-row md:items-center md:gap-6 md:static md:border-0 md:shadow-none md:p-0 md:bg-transparent">
        <a href="index.html" data-nav-link class="text-body-md text-on-surface-variant hover:text-primary transition-colors">Home</a>
        <a href="features.html" data-nav-link class="text-body-md text-on-surface-variant hover:text-primary transition-colors">Features</a>
        <a href="how-it-works.html" data-nav-link class="text-body-md text-on-surface-variant hover:text-primary transition-colors">How it works</a>
        <a href="mealobox-sync.html" data-nav-link class="text-body-md text-on-surface-variant hover:text-primary transition-colors">MealOBox Sync</a>
        <a href="for-providers.html" data-nav-link class="text-body-md text-on-surface-variant hover:text-primary transition-colors">For providers</a>
        <a href="data-security.html" data-nav-link class="text-body-md text-on-surface-variant hover:text-primary transition-colors">Security</a>
        <a href="terms.html" data-nav-link class="text-body-md text-on-surface-variant hover:text-primary transition-colors">Terms</a>
        <a href="for-providers.html" class="bg-primary text-white px-6 py-3 rounded-full text-label-lg min-h-[44px] inline-flex items-center justify-center active:scale-[0.98] transition-transform">Request demo</a>
      </div>
    </nav>
  </header>'''

FOOTER = r'''  <footer class="bg-inverse-surface text-inverse-on-surface mt-section-margin">
    <div class="max-w-6xl mx-auto px-container-padding py-12 grid grid-cols-1 md:grid-cols-4 gap-8">
      <div class="md:col-span-2">
        <p class="text-headline-md font-semibold mb-2">DailyDose+</p>
        <p class="text-body-md text-inverse-on-surface/80 max-w-md">Guided vitality for medication, hydration, and meal-aware wellness — by MealOBox.</p>
      </div>
      <div>
        <p class="text-label-lg font-semibold mb-3">Explore</p>
        <ul class="space-y-2 text-body-md">
          <li><a href="features.html" class="hover:text-inverse-primary transition-colors">Features</a></li>
          <li><a href="how-it-works.html" class="hover:text-inverse-primary transition-colors">How it works</a></li>
          <li><a href="data-security.html" class="hover:text-inverse-primary transition-colors">Data security</a></li>
          <li><a href="terms.html" class="hover:text-inverse-primary transition-colors">Terms of service</a></li>
        </ul>
      </div>
      <div>
        <p class="text-label-lg font-semibold mb-3">Contact</p>
        <ul class="space-y-2 text-body-md">
          <li><a href="mailto:hello@mealobox.in" class="hover:text-inverse-primary transition-colors">hello@mealobox.in</a></li>
          <li><a href="https://mealobox.in" class="hover:text-inverse-primary transition-colors" rel="noopener noreferrer">mealobox.in</a></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-inverse-on-surface/20 px-container-padding py-6 text-center text-label-sm text-inverse-on-surface/70">
      © 2026 DailyDose+ — An initiative by MealOBox Foodtech Pvt. Ltd.
    </div>
  </footer>'''

SCROLL_SENTINEL = r'''    <div id="scroll-sentinel" class="absolute top-0 left-0 w-px h-px pointer-events-none" aria-hidden="true"></div>'''

SCROLL_BTN = r'''  <button type="button" id="scroll-top" class="fixed bottom-6 right-6 z-40 min-w-[48px] min-h-[48px] rounded-full bg-primary text-white shadow-soft-shadow flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-300" aria-label="Scroll to top">
    <span class="material-symbols-outlined" aria-hidden="true">arrow_upward</span>
  </button>'''

SHARED_JS = r'''    (function () {
      const toggle = document.getElementById('nav-toggle');
      const menu = document.getElementById('mobile-menu');
      const icon = document.getElementById('nav-toggle-icon');
      if (toggle && menu) {
        toggle.addEventListener('click', () => {
          const open = menu.classList.toggle('hidden');
          const isOpen = !open;
          toggle.setAttribute('aria-expanded', String(isOpen));
          toggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
          if (icon) icon.textContent = isOpen ? 'close' : 'menu';
        });
      }
      const page = window.location.pathname.split('/').pop() || 'index.html';
      document.querySelectorAll('[data-nav-link]').forEach((link) => {
        const href = link.getAttribute('href');
        if (href === page || (page === '' && href === 'index.html')) {
          link.classList.add('text-primary', 'font-semibold');
          link.classList.remove('text-on-surface-variant');
          link.setAttribute('aria-current', 'page');
        }
      });
      const scrollBtn = document.getElementById('scroll-top');
      const scrollSentinel = document.getElementById('scroll-sentinel');
      if (scrollBtn && scrollSentinel) {
        const scrollObserver = new IntersectionObserver(
          ([entry]) => {
            const show = !entry.isIntersecting;
            scrollBtn.classList.toggle('opacity-0', !show);
            scrollBtn.classList.toggle('pointer-events-none', !show);
            scrollBtn.classList.toggle('opacity-100', show);
          },
          { threshold: 0, rootMargin: '0px 0px 0px 0px' }
        );
        scrollObserver.observe(scrollSentinel);
        scrollBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
      }
    })();'''

MED_WATER_HTML = r'''
      <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
        <article class="bg-surface-container-lowest rounded-lg p-6 soft-shadow border-l-4 border-tertiary-container" id="med-card">
          <h3 class="text-headline-md text-on-surface mb-2">Morning — Metformin</h3>
          <p class="text-body-md text-on-surface-variant mb-4">500 mg · After breakfast</p>
          <button type="button" id="mark-taken" class="w-full bg-primary text-white min-h-[56px] rounded-xl text-label-lg font-medium active:scale-[0.98] transition-transform flex items-center justify-center gap-2">
            <span class="material-symbols-outlined" aria-hidden="true">check_circle</span>
            <span id="mark-taken-label">Mark as Taken</span>
          </button>
        </article>
        <article class="bg-surface-container-lowest rounded-lg p-6 soft-shadow">
          <h3 class="text-headline-md text-on-surface mb-4">Water today</h3>
          <div class="flex items-center gap-6">
            <svg class="w-28 h-28 -rotate-90" viewBox="0 0 100 100" role="img" aria-label="Water intake progress ring">
              <circle cx="50" cy="50" r="42" fill="none" class="stroke-surface-container-low stroke-[10px]" />
              <circle id="water-ring" cx="50" cy="50" r="42" fill="none" class="stroke-water stroke-[10px] stroke-linecap-round" stroke-dasharray="263.89" stroke-dashoffset="263.89"/>
            </svg>
            <div>
              <p class="text-display text-water" id="water-ml">0</p>
              <p class="text-label-lg text-on-surface-variant">of 2000 ml</p>
            </div>
          </div>
          <div class="flex flex-wrap gap-3 mt-4">
            <button type="button" class="water-add bg-surface-container-low text-on-surface min-h-[44px] px-4 rounded-xl text-label-lg active:scale-[0.98]" data-ml="250">+250 ml</button>
            <button type="button" class="water-add bg-surface-container-low text-on-surface min-h-[44px] px-4 rounded-xl text-label-lg active:scale-[0.98]" data-ml="500">+500 ml</button>
          </div>
        </article>
      </div>'''

MED_WATER_JS = r'''
    (function () {
      const markBtn = document.getElementById('mark-taken');
      const markLabel = document.getElementById('mark-taken-label');
      const medCard = document.getElementById('med-card');
      if (markBtn && markLabel) {
        markBtn.addEventListener('click', () => {
          const taken = markBtn.classList.toggle('taken');
          if (taken) {
            markBtn.classList.remove('bg-primary');
            markBtn.classList.add('bg-water', 'text-white');
            markLabel.textContent = 'Taken';
            medCard?.classList.add('opacity-75');
          } else {
            markBtn.classList.add('bg-primary');
            markBtn.classList.remove('bg-water', 'text-white');
            markLabel.textContent = 'Mark as Taken';
            medCard?.classList.remove('opacity-75');
          }
        });
      }
      const ring = document.getElementById('water-ring');
      const mlEl = document.getElementById('water-ml');
      const GOAL = 2000;
      const CIRC = 263.89;
      let ml = 0;
      const updateWater = () => {
        if (mlEl) mlEl.textContent = String(ml);
        if (ring) {
          const pct = Math.min(ml / GOAL, 1);
          ring.setAttribute('stroke-dashoffset', String(CIRC * (1 - pct)));
        }
      };
      document.querySelectorAll('.water-add').forEach((btn) => {
        btn.addEventListener('click', () => {
          ml = Math.min(ml + Number(btn.getAttribute('data-ml') || 0), GOAL);
          updateWater();
        });
      });
    })();'''


def page(title: str, desc: str, main: str, extra_js: str = '') -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <title>{title} — DailyDose+</title>
{TAILWIND_HEAD}
</head>
<body class="font-sans bg-surface text-on-surface antialiased">
{NAVBAR}
{SCROLL_SENTINEL}
  <main class="pt-24 md:pt-28 pb-section-margin">
{main}
  </main>
{FOOTER}
{SCROLL_BTN}
  <script>
{SHARED_JS}
{extra_js}
  </script>
</body>
</html>
'''


PAGES = {
    'index.html': page(
        'Home',
        'DailyDose+ helps you manage medications, hydration, and MealOBox meal sync with calm, guided vitality.',
        r'''    <section class="max-w-6xl mx-auto px-container-padding py-section-margin text-center">
      <p class="text-label-lg text-primary font-semibold uppercase tracking-wide mb-4">Guided Vitality</p>
      <h1 class="text-display text-on-surface max-w-3xl mx-auto mb-6">Your wellness concierge for pills, water, and meals</h1>
      <p class="text-body-lg text-on-surface-variant max-w-2xl mx-auto mb-8">DailyDose+ by MealOBox keeps medication schedules clear, hydration on track, and tiffin nutrition in sync — without clinical coldness.</p>
      <div class="flex flex-wrap justify-center gap-4">
        <a href="how-it-works.html" class="bg-primary text-white px-8 min-h-[56px] rounded-xl inline-flex items-center text-label-lg active:scale-[0.98]">See how it works</a>
        <a href="features.html" class="border-2 border-primary text-primary px-8 min-h-[56px] rounded-xl inline-flex items-center text-label-lg active:scale-[0.98]">Explore features</a>
      </div>
    </section>
    <section class="max-w-6xl mx-auto px-container-padding py-section-margin">
      <h2 class="text-headline-lg text-center mb-8">Try the app preview</h2>
''' + MED_WATER_HTML + r'''
    </section>
    <section class="max-w-6xl mx-auto px-container-padding py-section-margin bg-surface-container-low rounded-xl p-8">
      <h2 class="text-headline-lg mb-4">Built for trust</h2>
      <p class="text-body-md text-on-surface-variant mb-4">AES-256 encryption, India data residency, and DPDP-aligned privacy — <a href="data-security.html" class="text-primary underline">read our security overview</a>.</p>
    </section>''',
        MED_WATER_JS,
    ),
    'features.html': page(
        'Features',
        'Deep-dive into DailyDose+ medication reminders, hydration tracking, MealOBox sync, and secure records.',
        r'''    <section class="max-w-6xl mx-auto px-container-padding py-section-margin">
      <h1 class="text-display mb-4">Features that reduce daily health friction</h1>
      <p class="text-body-lg text-on-surface-variant max-w-2xl mb-12">Everything you need in one calm interface — designed for clarity at any age.</p>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
        <div class="bg-surface-container-lowest rounded-lg p-6 soft-shadow">
          <span class="material-symbols-outlined text-tertiary-container text-3xl mb-3" aria-hidden="true">medication</span>
          <h2 class="text-headline-md mb-2">Smart reminders</h2>
          <p class="text-body-md text-on-surface-variant">Gentle schedules with coral-accent medicine cards.</p>
        </div>
        <div class="bg-surface-container-lowest rounded-lg p-6 soft-shadow">
          <span class="material-symbols-outlined text-water text-3xl mb-3" aria-hidden="true">water_drop</span>
          <h2 class="text-headline-md mb-2">Hydration goals</h2>
          <p class="text-body-md text-on-surface-variant">Progress rings that celebrate every glass.</p>
        </div>
        <div class="bg-surface-container-lowest rounded-lg p-6 soft-shadow">
          <span class="material-symbols-outlined text-primary text-3xl mb-3" aria-hidden="true">restaurant</span>
          <h2 class="text-headline-md mb-2">MealOBox sync</h2>
          <p class="text-body-md text-on-surface-variant">AI nutrition insights from your tiffin orders.</p>
        </div>
      </div>
      <h2 class="text-headline-lg text-center mb-8">Interactive demos</h2>
''' + MED_WATER_HTML + r'''
    </section>''',
        MED_WATER_JS,
    ),
    'how-it-works.html': page(
        'How it works',
        'Four simple steps to set up DailyDose+ — medications, hydration, MealOBox, and secure records.',
        r'''    <section class="max-w-6xl mx-auto px-container-padding py-section-margin">
      <h1 class="text-display mb-4">How DailyDose+ works</h1>
      <p class="text-body-lg text-on-surface-variant max-w-2xl mb-16">From signup to daily rhythm in four guided steps.</p>
      <ol class="space-y-16">
        <li class="flex flex-col md:flex-row gap-8 items-center">
          <div class="md:w-1/2 bg-surface-container-lowest rounded-xl p-8 soft-shadow">
            <span class="text-label-sm text-primary font-bold">STEP 1</span>
            <h2 class="text-headline-lg mt-2 mb-3">Create your profile</h2>
            <p class="text-body-md text-on-surface-variant">Add conditions, allergies, and caregiver contacts in plain language.</p>
          </div>
          <span class="material-symbols-outlined text-5xl text-primary" aria-hidden="true">person</span>
        </li>
        <li class="flex flex-col md:flex-row-reverse gap-8 items-center">
          <div class="md:w-1/2 bg-surface-container-lowest rounded-xl p-8 soft-shadow">
            <span class="text-label-sm text-primary font-bold">STEP 2</span>
            <h2 class="text-headline-lg mt-2 mb-3">Set medication schedules</h2>
            <p class="text-body-md text-on-surface-variant">Dosage, timing, and meal pairing — with large, forgiving tap targets.</p>
          </div>
          <span class="material-symbols-outlined text-5xl text-tertiary-container" aria-hidden="true">alarm</span>
        </li>
        <li class="flex flex-col md:flex-row gap-8 items-center">
          <div class="md:w-1/2 bg-surface-container-lowest rounded-xl p-8 soft-shadow">
            <span class="text-label-sm text-primary font-bold">STEP 3</span>
            <h2 class="text-headline-lg mt-2 mb-3">Link MealOBox</h2>
            <p class="text-body-md text-on-surface-variant">Sync tiffin nutrition with your health goals automatically.</p>
          </div>
          <span class="material-symbols-outlined text-5xl text-primary" aria-hidden="true">sync</span>
        </li>
        <li class="flex flex-col md:flex-row-reverse gap-8 items-center">
          <div class="md:w-1/2 bg-inverse-surface text-inverse-on-surface rounded-xl p-8 soft-shadow">
            <span class="text-label-sm text-inverse-primary font-bold">STEP 4</span>
            <h2 class="text-headline-lg mt-2 mb-3">Stay on track daily</h2>
            <p class="text-body-md opacity-90">Mark doses taken, log water, and review progress with your care circle.</p>
          </div>
          <span class="material-symbols-outlined text-5xl text-water" aria-hidden="true">insights</span>
        </li>
      </ol>
    </section>''',
    ),
    'mealobox-sync.html': page(
        'MealOBox Sync',
        'Connect MealOBox tiffin orders with DailyDose+ for AI-powered nutrition and medication meal timing.',
        r'''    <section class="max-w-6xl mx-auto px-container-padding py-section-margin">
      <h1 class="text-display mb-4">MealOBox ↔ DailyDose+</h1>
      <p class="text-body-lg text-on-surface-variant max-w-2xl mb-12">When you order from MealOBox, nutrition data flows into DailyDose+ so meal timing aligns with your medication schedule.</p>
      <div class="grid lg:grid-cols-2 gap-8">
        <article class="bg-surface-container-lowest rounded-xl p-8 soft-shadow">
          <h2 class="text-headline-lg mb-4">What syncs</h2>
          <ul class="space-y-3 text-body-md text-on-surface-variant">
            <li class="flex gap-2"><span class="material-symbols-outlined text-water shrink-0" aria-hidden="true">check</span>Macros and calories per meal</li>
            <li class="flex gap-2"><span class="material-symbols-outlined text-water shrink-0" aria-hidden="true">check</span>Dietary tags (diabetic-friendly, low sodium)</li>
            <li class="flex gap-2"><span class="material-symbols-outlined text-water shrink-0" aria-hidden="true">check</span>Delivery time for dose-with-food reminders</li>
          </ul>
        </article>
        <article class="bg-inverse-surface text-inverse-on-surface rounded-xl p-8 soft-shadow">
          <h2 class="text-headline-lg mb-4">AI insights</h2>
          <p class="text-body-md opacity-90">Our models flag conflicts between prescriptions and recurring meal plans — always with human-readable explanations, never alarmist copy.</p>
          <a href="https://mealobox.in" class="inline-flex mt-6 text-inverse-primary underline text-label-lg" rel="noopener noreferrer">Visit mealobox.in</a>
        </article>
      </div>
    </section>''',
    ),
    'for-providers.html': page(
        'For providers',
        'Healthcare providers and corporates: partner with DailyDose+ for medication adherence and wellness programs.',
        r'''    <section class="max-w-6xl mx-auto px-container-padding py-section-margin">
      <h1 class="text-display mb-4">For healthcare providers & corporates</h1>
      <p class="text-body-lg text-on-surface-variant max-w-2xl mb-12">White-label wellness programs, adherence dashboards, and MealOBox meal benefits for your members.</p>
      <div class="grid lg:grid-cols-2 gap-12">
        <div>
          <h2 class="text-headline-lg mb-4">Why partner</h2>
          <ul class="space-y-4 text-body-md text-on-surface-variant">
            <li><strong class="text-on-surface">Adherence analytics</strong> — anonymized cohort insights</li>
            <li><strong class="text-on-surface">HIPAA-ready infrastructure</strong> — see <a href="data-security.html" class="text-primary">security</a></li>
            <li><strong class="text-on-surface">Meal + med alignment</strong> — unique MealOBox integration</li>
          </ul>
        </div>
        <div id="demo-form-wrap" class="bg-surface-container-lowest rounded-xl p-8 soft-shadow">
          <h2 class="text-headline-md mb-6">Request a demo</h2>
          <form id="demo-form" novalidate>
            <div class="mb-4">
              <label for="org-name" class="text-label-lg block mb-1">Organization name</label>
              <input id="org-name" name="org" type="text" required class="w-full border-2 border-outline-variant rounded-lg px-4 py-3 text-body-md focus:border-primary" />
              <p id="err-org" class="text-error text-label-sm mt-1 hidden" role="alert"></p>
            </div>
            <div class="mb-4">
              <label for="email" class="text-label-lg block mb-1">Work email</label>
              <input id="email" name="email" type="email" required class="w-full border-2 border-outline-variant rounded-lg px-4 py-3 text-body-md focus:border-primary" />
              <p id="err-email" class="text-error text-label-sm mt-1 hidden" role="alert"></p>
            </div>
            <button type="submit" class="w-full bg-primary text-white min-h-[56px] rounded-xl text-label-lg active:scale-[0.98]">Submit request</button>
          </form>
          <div id="demo-success" class="hidden text-center py-8" role="status">
            <span class="material-symbols-outlined text-water text-5xl mb-4" aria-hidden="true">check_circle</span>
            <h3 class="text-headline-md mb-2">Request received</h3>
            <p class="text-body-md text-on-surface-variant">Our team will reach you at hello@mealobox.in within two business days.</p>
          </div>
        </div>
      </div>
    </section>''',
        r'''
    (function () {
      const form = document.getElementById('demo-form');
      const success = document.getElementById('demo-success');
      const wrap = document.getElementById('demo-form-wrap');
      if (!form) return;
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const org = document.getElementById('org-name');
        const email = document.getElementById('email');
        const errOrg = document.getElementById('err-org');
        const errEmail = document.getElementById('err-email');
        let valid = true;
        if (!org?.value.trim()) {
          errOrg?.classList.remove('hidden');
          if (errOrg) errOrg.textContent = 'Organization name is required.';
          valid = false;
        } else errOrg?.classList.add('hidden');
        const em = email?.value.trim() || '';
        if (!em || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em)) {
          errEmail?.classList.remove('hidden');
          if (errEmail) errEmail.textContent = 'Enter a valid work email.';
          valid = false;
        } else errEmail?.classList.add('hidden');
        if (valid && success && wrap) {
          form.classList.add('hidden');
          success.classList.remove('hidden');
        }
      });
    })();''',
    ),
    'data-security.html': page(
        'Data security',
        'HIPAA-aligned practices, AES-256 encryption, India data residency, and DPDP privacy for DailyDose+.',
        r'''    <section class="max-w-3xl mx-auto px-container-padding py-section-margin">
      <h1 class="text-display mb-4">Your data, protected</h1>
      <p class="text-body-lg text-on-surface-variant mb-12">We treat health information with the same care we bring to daily wellness guidance.</p>
      <div class="space-y-4" id="security-accordion">
        <div class="accordion-item bg-surface-container-lowest rounded-lg soft-shadow overflow-hidden">
          <button type="button" class="accordion-trigger w-full flex justify-between items-center p-6 text-left min-h-[56px]" aria-expanded="false" aria-controls="acc-1" id="acc-btn-1">
            <span class="text-headline-md">Encryption at rest & in transit</span>
            <span class="material-symbols-outlined accordion-icon" aria-hidden="true">expand_more</span>
          </button>
          <div id="acc-1" class="accordion-panel hidden px-6 pb-6 text-body-md text-on-surface-variant" role="region" aria-labelledby="acc-btn-1">
            All records use AES-256 at rest and TLS 1.3 in transit. Keys are rotated on a defined schedule.
          </div>
        </div>
        <div class="accordion-item bg-surface-container-lowest rounded-lg soft-shadow overflow-hidden">
          <button type="button" class="accordion-trigger w-full flex justify-between items-center p-6 text-left min-h-[56px]" aria-expanded="false" aria-controls="acc-2" id="acc-btn-2">
            <span class="text-headline-md">Data residency</span>
            <span class="material-symbols-outlined accordion-icon" aria-hidden="true">expand_more</span>
          </button>
          <div id="acc-2" class="accordion-panel hidden px-6 pb-6 text-body-md text-on-surface-variant" role="region" aria-labelledby="acc-btn-2">
            Primary storage resides in India (ap-south-1) with no cross-border transfer without explicit consent.
          </div>
        </div>
        <div class="accordion-item bg-surface-container-lowest rounded-lg soft-shadow overflow-hidden">
          <button type="button" class="accordion-trigger w-full flex justify-between items-center p-6 text-left min-h-[56px]" aria-expanded="false" aria-controls="acc-3" id="acc-btn-3">
            <span class="text-headline-md">Privacy & DPDP</span>
            <span class="material-symbols-outlined accordion-icon" aria-hidden="true">expand_more</span>
          </button>
          <div id="acc-3" class="accordion-panel hidden px-6 pb-6 text-body-md text-on-surface-variant" role="region" aria-labelledby="acc-btn-3">
            We align with the Digital Personal Data Protection Act 2023. You may export or delete your data from in-app settings.
          </div>
        </div>
      </div>
    </section>''',
        r'''
    (function () {
      document.querySelectorAll('.accordion-trigger').forEach((btn) => {
        btn.addEventListener('click', () => {
          const panel = document.getElementById(btn.getAttribute('aria-controls') || '');
          const icon = btn.querySelector('.accordion-icon');
          const open = panel?.classList.toggle('hidden') === false;
          btn.setAttribute('aria-expanded', String(open));
          if (icon) icon.textContent = open ? 'expand_less' : 'expand_more';
        });
      });
    })();''',
    ),
    'terms.html': page(
        'Terms of Service',
        'DailyDose+ Terms of Service — DPDP Act 2023, IT Act 2000, and usage policies.',
        r'''    <section class="max-w-6xl mx-auto px-container-padding py-section-margin">
      <h1 class="text-display mb-8">Terms of Service</h1>
      <div class="lg:grid lg:grid-cols-12 gap-12">
        <nav class="lg:col-span-3 lg:sticky lg:top-28 h-fit" aria-label="Terms sections">
          <ul class="space-y-2 text-label-lg">
            <li><a href="#acceptance" data-tos-link class="text-on-surface-variant hover:text-primary block py-2">Acceptance</a></li>
            <li><a href="#services" data-tos-link class="text-on-surface-variant hover:text-primary block py-2">Services</a></li>
            <li><a href="#privacy" data-tos-link class="text-on-surface-variant hover:text-primary block py-2">Privacy</a></li>
            <li><a href="#liability" data-tos-link class="text-on-surface-variant hover:text-primary block py-2">Liability</a></li>
          </ul>
        </nav>
        <div class="lg:col-span-9 space-y-16">
          <section id="acceptance" class="tos-section scroll-mt-28">
            <h2 class="text-headline-lg mb-4">1. Acceptance</h2>
            <p class="text-body-md text-on-surface-variant">By using DailyDose+, you agree to these terms and our privacy practices under the DPDP Act 2023 and applicable Indian law.</p>
          </section>
          <section id="services" class="tos-section scroll-mt-28">
            <h2 class="text-headline-lg mb-4">2. Services</h2>
            <p class="text-body-md text-on-surface-variant">DailyDose+ provides medication reminders, hydration tracking, MealOBox nutrition sync, and secure record storage. It is not a substitute for professional medical advice.</p>
          </section>
          <section id="privacy" class="tos-section scroll-mt-28">
            <h2 class="text-headline-lg mb-4">3. Privacy</h2>
            <p class="text-body-md text-on-surface-variant">See <a href="data-security.html" class="text-primary underline">data security</a> for how we protect your information. Contact hello@mealobox.in for data requests.</p>
          </section>
          <section id="liability" class="tos-section scroll-mt-28">
            <h2 class="text-headline-lg mb-4">4. Liability</h2>
            <p class="text-body-md text-on-surface-variant">MealOBox Foodtech Pvt. Ltd. limits liability to the extent permitted under the IT Act 2000 and consumer protection regulations.</p>
          </section>
        </div>
      </div>
    </section>''',
        r'''
    (function () {
      const sections = document.querySelectorAll('.tos-section');
      const links = document.querySelectorAll('[data-tos-link]');
      if (!sections.length || !links.length) return;
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const id = entry.target.getAttribute('id');
              links.forEach((link) => {
                const active = link.getAttribute('href') === '#' + id;
                link.classList.toggle('text-primary', active);
                link.classList.toggle('font-semibold', active);
                link.classList.toggle('text-on-surface-variant', !active);
                if (active) link.setAttribute('aria-current', 'true');
                else link.removeAttribute('aria-current');
              });
            }
          });
        },
        { rootMargin: '-20% 0px -60% 0px', threshold: 0 }
      );
      sections.forEach((s) => observer.observe(s));
    })();''',
    ),
}

COMPONENTS_REF = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>DailyDose+ — Shared components (reference only)</title>
{TAILWIND_HEAD}
</head>
<body class="font-sans bg-surface text-on-surface">
  <p class="p-container-padding text-label-sm text-on-surface-variant">Reference only — copy into each page; not deployed.</p>
{NAVBAR}
{FOOTER}
{SCROLL_BTN}
</body>
</html>
'''


def main():
    for name, html in PAGES.items():
        (ROOT / name).write_text(html, encoding='utf-8')
        print(f'Wrote {name}')
    (ROOT / '_components.html').write_text(COMPONENTS_REF, encoding='utf-8')
    print('Wrote _components.html')


if __name__ == '__main__':
    main()
