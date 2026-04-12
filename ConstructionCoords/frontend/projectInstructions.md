# ConstructionCoords — Implementation Brief

## Overview

Build a single-page mobile-first React application for submitting geographic coordinates. The app is used by construction field workers on-site (outdoor conditions, bright sunlight, phone in hand), so every design decision prioritizes **high contrast, large touch targets, and readability**.

The design direction is **"Industrial Grit"** — monospace typography, dark charcoal backgrounds, amber/orange accents, and an animated caution-stripe detail that evokes heavy equipment and construction site tools.

---

## Application States

The app has two views that cross-fade between each other:

1. **Form View** — Logo, subtitle, a single freeform text input, and a submit button.
2. **Success View** — A confirmation card showing the parsed latitude and longitude, with a button to return to the form.

There is also an inline **error state** on the form view when validation fails.

---

## Design Tokens

### Colors

| Token | Hex | Usage |
|---|---|---|
| `--bg-primary` | `#1A1A1A` | Page background |
| `--bg-surface` | `#2A2A2A` | Input background, success card background |
| `--accent` | `#F5A623` | Logo accent, button fill, borders, labels, caution stripe |
| `--accent-hover` | `#FFB83D` | Button hover state |
| `--text-primary` | `#E0E0E0` | Headings, coordinate values |
| `--text-secondary` | `#888888` | Subtitle, footer |
| `--text-footer` | `#444444` | Footer text, dividers |
| `--error` | `#FF4136` | Error text, error border |
| `--error-glow` | `rgba(255, 65, 54, 0.12)` | Error input box-shadow |
| `--accent-glow` | `rgba(245, 166, 35, 0.15)` | Input focus box-shadow |
| `--accent-glow-strong` | `rgba(245, 166, 35, 0.3)` | Button hover box-shadow |

### Typography

| Element | Font Family | Size | Weight | Extras |
|---|---|---|---|---|
| Logo | `'IBM Plex Mono', 'Courier New', monospace` | `28px` | `700` | Letter-spacing: `-0.5px` |
| Subtitle | Same family | `14px` | `400` | Letter-spacing: `0.5px` |
| Input text | Same family | `18px` | `400` | — |
| Button text | Same family | `16px` | `700` | Uppercase, letter-spacing: `0.5px` |
| Error text | Same family | `13px` | `400` | — |
| Coord labels (LAT/LON) | Same family | `11px` | `700` | Letter-spacing: `1.5px` |
| Coord values | Same family | `16px` | `400` | — |
| Success title | Same family | `20px` | `700` | — |
| Back button | Same family | `14px` | `700` | Uppercase, letter-spacing: `0.5px` |
| Footer | Same family | `11px` | `400` | Uppercase, letter-spacing: `1px` |

Import `IBM Plex Mono` from Google Fonts (weights 400 and 700).

### Spacing & Layout

- Page padding: `24px`
- Max content width: `400px`, centered
- Input padding: `18px 16px`
- Button padding: `18px` (full width)
- Success card padding: `48px 32px`
- Back button padding: `16px 32px`
- Gap between coord label/value groups: `12px`
- Coord display inner padding: `16px 20px`
- Coord divider: `1px` wide, `24px` tall, color `#444`

### Border Treatments

- Input: `2px solid #444`, border-radius `6px`
- Submit button: No border, border-radius `6px`
- Success card: `2px solid #F5A623`, border-radius `8px`
- Back button: `2px solid #F5A623`, border-radius `6px`
- Coord display box: border-radius `6px`, background `#1A1A1A`

---

## Component Behavior

### Caution Stripe (top of page)

A fixed bar at the very top of the viewport, `4px` tall. Uses a `repeating-linear-gradient` of amber (`#F5A623`) and background (`#1A1A1A`) in 20px/8px segments. Animates horizontally in a continuous loop (`background-position` from `0` to `48px` over `1.5s linear infinite`).

### Coordinate Input

- Single freeform text field accepting formats like `40.7128, -74.0060` or `(40.7128, -74.0060)`.
- **Parsing logic:** Strip parentheses, split on commas/whitespace, parse two floats. Validate latitude is within `[-90, 90]` and longitude within `[-180, 180]`.
- **Focus state:** Border transitions to `#F5A623`, box-shadow `0 0 0 3px rgba(245,166,35,0.15)`. Transition: `0.25s ease`.
- **Error state:** Border transitions to `#FF4136`, box-shadow `0 0 0 3px rgba(255,65,54,0.12)`.

### Error Display

- Text appears below the input with a slide-down animation (from `translateY(-6px), opacity 0` to `translateY(0), opacity 1` over `0.3s ease`).
- The entire input wrapper plays a horizontal shake animation on error (`0.45s`, ±6px diminishing).
- Error clears as soon as the user types.

### Submit Button

- Default: `background #F5A623`, `color #1A1A1A`.
- Hover: `background #FFB83D`, lifts `translateY(-1px)`, gains `box-shadow 0 4px 16px rgba(245,166,35,0.3)`. Transition: `0.2s ease`.
- Active: Snaps back to `translateY(0)`, shadow removed.
- Also triggers on `Enter` key inside the input.

### View Transitions (Form ↔ Success)

Both directions use a cross-fade with vertical slide:

1. Current view fades out: `opacity 0`, `translateY(10px)` over `300ms ease`.
2. After fade-out completes, swap content.
3. New view fades in: `opacity 1`, `translateY(0)` over `300ms ease`.

No hard cuts — the transition should feel seamless.

### Success View — Entry Choreography

Elements stagger in after the fade-in transition:

1. **Check circle** — Scales in from `scale(0.7)` with a spring curve (`cubic-bezier(0.34, 1.56, 0.64, 1)`) over `0.4s`. Followed by a pulse ring (`box-shadow` expanding from `0` to `16px` at `rgba(245,166,35,0.4)` then fading, over `1s ease` with `0.3s` delay).
2. **Checkmark SVG inside the circle** — A `stroke-dashoffset` animation drawing the check path from `30` to `0` over `0.5s ease` with `0.3s` delay. The path is: `M9 17l5 5 9-11`, stroke `#1A1A1A`, width `3`, round caps/joins, `dasharray 30`.
3. **"Coordinate Submitted" title** — Fades and slides up over `0.4s ease`, delay `0.15s`.
4. **Coordinate display box** — Same animation, delay `0.25s`.
5. **"Submit Another" button** — Same animation, delay `0.4s`.

### "Submit Another" Button

- Ghost style: transparent background, `2px solid #F5A623`, text `#F5A623`.
- Hover: background fills to `rgba(245,166,35,0.08)`, lifts `translateY(-1px)`. Transition: `0.2s ease`.
- Clicking triggers the reverse view transition back to the form. Input auto-focuses after the transition completes.

### Footer

Fixed to the bottom of the viewport, centered. Text: `"ConstructionCoords — Field Tool"`. Color `#444`, `11px`, uppercase, letter-spacing `1px`.

---

## Page Load Animation

On initial load, form elements stagger in:

1. Logo — slides down from above (`translateY(-12px)`) over `0.5s ease`.
2. Subtitle — same animation, `0.08s` delay.
3. Input wrapper — slides up from below (`translateY(20px)`) over `0.5s ease`, `0.15s` delay.
4. Submit button — same as input, `0.22s` delay.

---

## Responsive Considerations

- The layout is already mobile-first at `max-width: 400px`. On wider screens, content remains centered with generous whitespace.
- Touch targets (input, buttons) are all at least `54px` tall — well above the 44px minimum.
- Font sizes are deliberately large (`18px` input, `16px` button) for outdoor readability.
- High color contrast ratios: white text on dark backgrounds exceeds WCAG AA.

---

## Accessibility Notes

- Input should have an accessible label (visible or `aria-label="Coordinate input"`).
- Error messages should use `role="alert"` or `aria-live="polite"` so screen readers announce them.
- The success state should announce via `aria-live="polite"` region.
- All interactive elements must be keyboard accessible (the Enter-to-submit behavior is already specified).
- Focus should be managed: auto-focus the input on load and when returning from success view.



when subbmitting:
POST  on http://127.0.0.1:8000/api/api/construction-location
request
{
    latitude: double,
    longitude: double
}
response
{
    "id": "string",
    "latitude": 0,
    "longitude": 0
}