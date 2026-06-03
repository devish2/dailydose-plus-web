/**
 * DailyDose+ wellness demos — water glass pour + prescription course duration
 */
(function (global) {
  const WATER_GOAL_L = 2.0;
  const ADD_L = 0.25;
  const POUR_MS = 1100;

  function formatLiters(n) {
    return `${n.toFixed(1)} L`;
  }

  function parseDate(str) {
    if (!str) return null;
    const d = new Date(str + 'T12:00:00');
    return Number.isNaN(d.getTime()) ? null : d;
  }

  function toInputDate(d) {
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }

  function addDays(date, days) {
    const d = new Date(date);
    d.setDate(d.getDate() + days);
    return d;
  }

  function daysBetween(a, b) {
    const ms = b.getTime() - a.getTime();
    return Math.max(0, Math.round(ms / 86400000));
  }

  function waterGlassMarkup({ variant = 'dark', id = '' }) {
    const outlineClass = variant === 'light' ? 'water-glass-outline water-glass-outline--light' : 'water-glass-outline';
    const gradId = id ? `waterFillGradient-${id}` : 'waterFillGradient';
    return `
      <div class="water-glass-wrap" data-water-glass${id ? ` id="${id}"` : ''} aria-hidden="true">
        <svg class="water-glass-svg" viewBox="0 0 100 140" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="${gradId}" x1="0%" y1="100%" x2="0%" y2="0%">
              <stop offset="0%" stop-color="#00a651"/>
              <stop offset="45%" stop-color="#1a9fd4"/>
              <stop offset="100%" stop-color="#5ec8ff"/>
            </linearGradient>
            <clipPath id="glassClip${id || 'Default'}">
              <path d="M28 42 L28 118 Q28 128 50 128 Q72 128 72 118 L72 42 Q50 36 28 42 Z"/>
            </clipPath>
          </defs>
          <path class="water-pour-stream" d="M46 4 L54 4 L52 42 L48 42 Z"/>
          <path class="${outlineClass}" d="M24 38 L26 120 Q26 132 50 132 Q74 132 76 120 L78 38 Q50 30 24 38 Z"/>
          <g clip-path="url(#glassClip${id || 'Default'})">
            <rect class="water-fill-rect" data-water-fill x="24" width="52" y="128" height="0"/>
            <ellipse class="water-surface-line" data-water-surface cx="50" cy="128" rx="22" ry="3" fill="rgba(94,200,255,0.5)" opacity="0"/>
          </g>
          <circle data-water-ripple cx="50" cy="128" r="2" fill="rgba(255,255,255,0.4)" opacity="0"/>
        </svg>
      </div>`;
  }

  function setGlassLevel(wrap, liters, animatePour) {
    if (!wrap) return;
    const fill = wrap.querySelector('[data-water-fill]');
    const surface = wrap.querySelector('[data-water-surface]');
    const pct = Math.min(liters / WATER_GOAL_L, 1);
    const glassBottom = 128;
    const glassTop = 42;
    const maxH = glassBottom - glassTop;
    const h = maxH * pct;
    const y = glassBottom - h;
    if (fill) {
      fill.setAttribute('y', String(y));
      fill.setAttribute('height', String(h));
    }
    if (surface) {
      surface.setAttribute('cy', String(y));
      surface.setAttribute('opacity', pct > 0.02 ? '1' : '0');
    }
    if (animatePour && !global.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      wrap.classList.add('is-pouring');
      const ripple = wrap.querySelector('[data-water-ripple]');
      if (ripple) {
        ripple.setAttribute('cy', String(y));
        ripple.classList.remove('water-ripple');
        void ripple.offsetWidth;
        ripple.classList.add('water-ripple');
      }
      window.setTimeout(() => wrap.classList.remove('is-pouring'), POUR_MS);
    }
  }

  function initWaterWidget(root, options) {
    const scope = root || document;
    const goal = options?.goalLiters ?? WATER_GOAL_L;
    let liters = options?.initialLiters ?? 1.3;

    const glassHost = scope.querySelector('[data-water-glass-host]');
    const glassId = options?.glassId || '';
    if (glassHost && !glassHost.querySelector('[data-water-glass]')) {
      glassHost.innerHTML = waterGlassMarkup({ variant: options?.variant || 'dark', id: glassId });
    }

    const wrap = scope.querySelector('[data-water-glass]');
    const label = scope.querySelector('[data-water-label]');
    const sublabel = scope.querySelector('[data-water-sublabel]');
    const pctEl = scope.querySelector('[data-water-pct]');
    const ring = scope.querySelector('[data-water-ring-progress]');
    const CIRC = options?.ringCircumference ?? 314.16;

    const update = (pour) => {
      setGlassLevel(wrap, liters, pour);
      if (label) label.textContent = `${liters.toFixed(1)} / ${goal.toFixed(1)} L`;
      if (sublabel) sublabel.textContent = formatLiters(liters);
      const pct = Math.min(liters / goal, 1);
      if (pctEl) pctEl.textContent = `${Math.round(pct * 100)}%`;
      if (ring) ring.setAttribute('stroke-dashoffset', String(CIRC * (1 - pct)));
    };

    update(false);

    scope.querySelectorAll('[data-water-add]').forEach((btn) => {
      btn.addEventListener('click', () => {
        if (liters >= goal) return;
        const add = Number(btn.getAttribute('data-ml') || 0) / 1000 || ADD_L;
        liters = Math.min(liters + add, goal);
        update(true);
        if (liters >= goal) {
          scope.querySelectorAll('[data-water-add]').forEach((b) => {
            b.disabled = true;
            b.classList.add('opacity-60', 'cursor-not-allowed');
          });
        }
      });
    });

    return { getLiters: () => liters, setLiters: (v) => { liters = v; update(false); } };
  }

  function initPrescriptionWidget(root) {
    const scope = root || document;
    const daysInput = scope.querySelector('[data-rx-days]');
    const startInput = scope.querySelector('[data-rx-start]');
    const endInput = scope.querySelector('[data-rx-end]');
    const dayLabel = scope.querySelector('[data-rx-day-label]');
    const remaining = scope.querySelector('[data-rx-remaining]');
    const progress = scope.querySelector('[data-rx-progress]');
    const endDisplay = scope.querySelector('[data-rx-end-display]');
    const startDisplay = scope.querySelector('[data-rx-start-display]');

    if (!daysInput || !startInput) return;

    const today = new Date();
    today.setHours(12, 0, 0, 0);
    if (!startInput.value) {
      const demoStart = new Date(2026, 4, 15);
      startInput.value = toInputDate(demoStart);
    }

    const recalc = () => {
      const days = Math.max(1, Math.min(365, Number(daysInput.value) || 30));
      daysInput.value = String(days);
      const start = parseDate(startInput.value);
      if (!start) return;
      const end = addDays(start, days - 1);
      if (endInput) endInput.value = toInputDate(end);
      if (endDisplay) endDisplay.textContent = end.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
      if (startDisplay) startDisplay.textContent = start.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });

      const elapsed = daysBetween(start, today) + 1;
      const currentDay = Math.min(Math.max(elapsed, 1), days);
      const left = Math.max(days - currentDay, 0);
      const pct = Math.min((currentDay / days) * 100, 100);

      if (dayLabel) dayLabel.textContent = `Day ${currentDay} of ${days}`;
      if (remaining) {
        remaining.textContent = left === 0 ? 'Course complete' : `${left} day${left === 1 ? '' : 's'} left in course`;
      }
      if (progress) progress.style.width = `${pct}%`;
    };

    const onRecalc = () => {
      recalc();
      syncHeroPrescriptionFrom(scope);
      const bar = scope.querySelector('[role="progressbar"]');
      const fill = scope.querySelector('[data-rx-progress]');
      if (bar && fill) bar.setAttribute('aria-valuenow', String(Math.round(parseFloat(fill.style.width) || 0)));
    };
    daysInput.addEventListener('input', onRecalc);
    daysInput.addEventListener('change', onRecalc);
    startInput.addEventListener('change', onRecalc);
    onRecalc();
  }

  function initMedCheckboxes(scope) {
    (scope || document).querySelectorAll('.med-checkbox').forEach((checkbox) => {
      checkbox.addEventListener('click', () => {
        const checked = checkbox.classList.toggle('is-checked');
        checkbox.setAttribute('aria-checked', String(checked));
        const row = checkbox.closest('[data-med-row]');
        const label = row?.querySelector('.med-row-label');
        if (label) {
          label.classList.toggle('line-through', checked);
          label.classList.toggle('text-on-surface-variant', checked);
          label.classList.toggle('text-on-surface', !checked);
        }
        if (checked) checkbox.innerHTML = '<span class="material-symbols-outlined text-sm" aria-hidden="true">check</span>';
        else checkbox.innerHTML = '';
      });
    });
  }

  function initHeroMed() {
    const btn = document.getElementById('hero-med-btn');
    const name = document.getElementById('hero-med-name');
    if (!btn || !name || btn.dataset.bound === '1') return;
    btn.dataset.bound = '1';
    btn.addEventListener('click', () => {
      const taken = btn.classList.toggle('is-taken');
      name.classList.toggle('line-through', taken);
      if (taken) {
        btn.textContent = '✓ Taken';
        btn.classList.remove('bg-tertiary-container');
        btn.style.backgroundColor = '#00a651';
      } else {
        btn.textContent = 'Mark as Taken';
        btn.classList.add('bg-tertiary-container');
        btn.style.backgroundColor = '';
      }
    });
  }

  function syncHeroPrescriptionFrom(mainRoot) {
    const main = mainRoot || document.getElementById('index-prescription');
    if (!main) return;
    const days = main.querySelector('[data-rx-days]')?.value;
    const start = main.querySelector('[data-rx-start]')?.value;
    const end = main.querySelector('[data-rx-end]')?.value;
    const dayLabel = main.querySelector('[data-rx-day-label]')?.textContent;
    const daysInline = document.querySelector('[data-hero-rx-days-inline]');
    const startD = document.querySelector('[data-hero-rx-start-display]');
    const endD = document.querySelector('[data-hero-rx-end-display]');
    const rxDay = document.getElementById('hero-rx-day');
    if (rxDay && dayLabel) rxDay.textContent = dayLabel;
    if (daysInline && days) daysInline.textContent = `${days} days`;
    if (startD && start) {
      const d = parseDate(start);
      if (d) startD.textContent = d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
    }
    if (endD && end) {
      const d = parseDate(end);
      if (d) endD.textContent = d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
    }
  }

  global.DailyDoseWellness = {
    initWaterWidget,
    initPrescriptionWidget,
    initMedCheckboxes,
    initHeroMed,
    syncHeroPrescriptionFrom,
    waterGlassMarkup,
  };
})(typeof window !== 'undefined' ? window : globalThis);
