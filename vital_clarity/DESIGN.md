---
name: Vital Clarity
colors:
  surface: '#f3faff'
  surface-dim: '#c7dde9'
  surface-bright: '#f3faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e6f6ff'
  surface-container: '#dbf1fe'
  surface-container-high: '#d5ecf8'
  surface-container-highest: '#cfe6f2'
  on-surface: '#071e27'
  on-surface-variant: '#414754'
  inverse-surface: '#1e333c'
  inverse-on-surface: '#dff4ff'
  outline: '#727785'
  outline-variant: '#c1c6d6'
  surface-tint: '#005bc0'
  primary: '#005bbf'
  on-primary: '#ffffff'
  primary-container: '#1a73e8'
  on-primary-container: '#ffffff'
  inverse-primary: '#adc7ff'
  secondary: '#546067'
  on-secondary: '#ffffff'
  secondary-container: '#d8e4ed'
  on-secondary-container: '#5a666e'
  tertiary: '#ad2f34'
  on-tertiary: '#ffffff'
  tertiary-container: '#cf484a'
  on-tertiary-container: '#140001'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#d8e4ed'
  secondary-fixed-dim: '#bcc8d1'
  on-secondary-fixed: '#121d23'
  on-secondary-fixed-variant: '#3d484f'
  tertiary-fixed: '#ffdad8'
  tertiary-fixed-dim: '#ffb3b0'
  on-tertiary-fixed: '#410006'
  on-tertiary-fixed-variant: '#8c1520'
  background: '#f3faff'
  on-background: '#071e27'
  surface-variant: '#cfe6f2'
typography:
  display:
    fontFamily: Lexend
    fontSize: 34px
    fontWeight: '600'
    lineHeight: 42px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: '0'
  headline-md:
    fontFamily: Lexend
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
    letterSpacing: '0'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  stack-gap: 16px
  inline-gap: 12px
  section-margin: 32px
---

## Brand & Style
The design system is centered on the concept of "Guided Vitality." It aims to reduce the cognitive load associated with health management through a **Modern Corporate** aesthetic infused with **Soft Health-Tech** elements. The interface prioritizes clarity and reassurance, creating an environment that feels more like a wellness concierge than a medical utility.

The target audience includes both active adults and elderly users, necessitating high legibility and large, forgiving tap targets. By utilizing soft color transitions and generous whitespace, the UI evokes a sense of calm and competence. The visual language avoids "hospital coldness" by using organic shapes and a warm accent palette to encourage daily engagement.

## Colors
The palette is anchored by **Deep Blue**, representing trust and clinical precision. This is balanced by **Soft Aqua**, which serves as the primary surface color to reduce eye strain and provide a soothing backdrop.

Functional accents are strictly categorized to aid rapid recognition:
- **Medicine Accent (Coral):** Used for urgent reminders, pill schedules, and health alerts. The warm tone ensures high visibility without inducing panic.
- **Water Goal Accent (Green):** Used for hydration tracking and positive progress indicators, reinforcing a sense of growth and health.
- **Neutrals:** A slate-toned neutral is used for secondary text to ensure high contrast for elderly users while avoiding the harshness of pure black.

## Typography
This design system utilizes **Lexend** exclusively. Lexend was specifically designed to reduce visual stress and improve reading throughput, making it ideal for health applications. 

The type scale is intentionally enlarged to support accessibility. Large display styles are used for daily summaries, while body-lg is the standard for instruction text to accommodate users with varying visual acuities. Tracking is slightly increased on smaller labels to maintain legibility against colored backgrounds.

## Layout & Spacing
The design system employs a **fluid grid** with a strong 8px baseline rhythm. For mobile interfaces, a standard 4-column grid is used with 24px side margins to ensure content is centered and easy to tap.

The layout philosophy emphasizes "Breathable Containers." Cards and sections should never feel cramped; vertical spacing is prioritized to create a clear hierarchy of information. Elements are grouped using a logical stack-gap of 16px, ensuring that related items (like a pill name and its dosage) feel connected but distinct.

## Elevation & Depth
Depth is communicated through **Tonal Layers** and **Ambient Shadows**. This design system avoids high-contrast shadows in favor of soft, diffused blurs that suggest a gentle lift from the Soft Aqua background.

- **Level 0 (Background):** Soft Aqua (#E8F4FD) canvas.
- **Level 1 (Cards):** White (#FFFFFF) surfaces with a 10% opacity Deep Blue shadow, 20px blur, and 4px vertical offset.
- **Level 2 (Active/Floating):** Used for primary action buttons or active modals, featuring a slightly more pronounced shadow to indicate interactability.

The use of semi-transparent overlays is encouraged for modal backgrounds to maintain the user's context within the app.

## Shapes
The shape language of the design system is defined by "Friendly Geometry." Sharp corners are eliminated to foster a sense of safety and approachability.

- **Standard Components:** 0.5rem (8px) radius for buttons and small inputs.
- **Cards & Containers:** 1rem (16px) radius to create the "rounded card" aesthetic requested.
- **Feature Elements:** 1.5rem (24px) or pill-shapes for progress bars and "Add" buttons to make them feel tactile and inviting to the touch.

## Components
Consistent component behavior is vital for the elderly user base:

- **Buttons:** Primary buttons use Deep Blue with white Lexend text (Medium weight). Minimum height is 56px to ensure a large hit area.
- **Cards:** White background, 16px rounded corners, and 24px internal padding. Medicine cards use a Coral left-border accent (4px width) for quick identification.
- **Checkboxes & Radios:** Scaled to 24x24px minimum. Use the Water Goal Green for "completed" states to provide a rewarding visual "pop."
- **Input Fields:** Soft Aqua stroke (2px) when inactive, Deep Blue when focused. Labels always remain visible above the field to assist with cognitive recall.
- **Chips:** Small, pill-shaped tags used for "Dosage" or "Time of Day," utilizing a light tint of the primary color to keep the UI clean.
- **Progress Rings:** Used for Water Goals and Daily Completion. Use a thick stroke (8px-12px) with rounded caps for a modern, tactile feel.