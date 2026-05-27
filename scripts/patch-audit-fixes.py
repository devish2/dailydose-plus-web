#!/usr/bin/env python3
"""Apply cross-page audit fixes to all 7 HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    'index.html', 'features.html', 'how-it-works.html', 'mealobox-sync.html',
    'for-providers.html', 'data-security.html', 'terms.html',
]

TAILWIND_OLD = """            'on-background': '#071e27',
          },
          borderRadius:"""

TAILWIND_NEW = """            'on-background': '#071e27',
            'water': '#00a651',
          },
          borderRadius:"""

TAILWIND_END_OLD = """            'label-sm': ['12px', { lineHeight: '16px', letterSpacing: '0.04em', fontWeight: '600' }],
          },
        },
      },
    };
  </script>"""

TAILWIND_END_NEW = """            'label-sm': ['12px', { lineHeight: '16px', letterSpacing: '0.04em', fontWeight: '600' }],
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
  </script>"""

NAV_ACTIVE_JS = """
      const page = window.location.pathname.split('/').pop() || 'index.html';
      document.querySelectorAll('[data-nav-link]').forEach((link) => {
        const href = link.getAttribute('href');
        const isActive = href === page || (page === '' && href === 'index.html');
        if (isActive) {
          link.classList.add('text-primary', 'font-semibold');
          link.classList.remove('text-on-surface-variant');
          link.setAttribute('aria-current', 'page');
        } else {
          link.classList.remove('text-primary', 'font-semibold');
          if (!link.classList.contains('hover:text-primary')) {
            link.classList.add('text-on-surface-variant');
          }
          link.removeAttribute('aria-current');
        }
      });
"""

MENU_TOGGLE_END = """          if (menuIcon) menuIcon.textContent = isOpen ? 'close' : 'menu';
        });
      }
"""


def patch_file(path: Path) -> list[str]:
    text = path.read_text(encoding='utf-8')
    changes = []

    if TAILWIND_OLD in text and "'water':" not in text:
        text = text.replace(TAILWIND_OLD, TAILWIND_NEW)
        changes.append('tailwind water token')
    if TAILWIND_END_OLD in text and 'boxShadow' not in text:
        text = text.replace(TAILWIND_END_OLD, TAILWIND_END_NEW)
        changes.append('tailwind boxShadow + focus plugin')

    if NAV_ACTIVE_JS.strip() not in text and MENU_TOGGLE_END in text:
        text = text.replace(MENU_TOGGLE_END, MENU_TOGGLE_END + NAV_ACTIVE_JS)
        changes.append('nav active JS')

    if path.name == 'terms.html' and '<header class="hero-gradient pt-32 pb-12' in text:
        text = text.replace(
            '<header class="hero-gradient pt-32 pb-12',
            '<section class="hero-gradient pt-32 pb-12',
        )
        text = text.replace(
            '</header>\n\n    <div class="max-w-7xl mx-auto px-container-padding py-section-margin grid',
            '</section>\n\n    <div class="max-w-7xl mx-auto px-container-padding py-section-margin grid',
            1,
        )
        changes.append('terms main landmark')

    if path.name == 'index.html':
        text = text.replace(
            '<h2 class="text-headline-lg text-on-surface">Smart Medication Alerts</h2>',
            '<h3 class="text-headline-lg text-on-surface">Smart Medication Alerts</h3>',
        )
        text = text.replace(
            'id="hero-med-btn" class="bg-tertiary-container',
            'id="hero-med-btn" aria-label="Mark medication as taken" class="bg-tertiary-container',
        )
        text = text.replace(
            'id="add-water-btn" class="bg-white',
            'id="add-water-btn" aria-label="Add water to daily goal" class="bg-white',
        )
        for label in ['Watch a product demo', 'Watch a product demo']:
            pass
        text = text.replace(
            '>Watch Demo</button>',
            ' aria-label="Watch product demo">Watch Demo</button>',
            2,
        )
        changes.append('index a11y headings')

    path.write_text(text, encoding='utf-8')
    return changes


def main():
    for name in PAGES:
        p = ROOT / name
        ch = patch_file(p)
        print(f'{name}: {", ".join(ch) or "no changes"}')


if __name__ == '__main__':
    main()
