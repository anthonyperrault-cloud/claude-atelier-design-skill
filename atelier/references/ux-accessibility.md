# UX & Accessibility — The Floor That Never Moves

Sources: the ui-ux-pro-max UX guideline set (priority-ordered), the bencium accessibility baseline,
and the web-design-guidelines skill (live-fetched Vercel rules). Distinctive design lives *on top*
of this floor, never by removing it. Accessibility enables creativity; it does not limit it.

---

## Priority order (fix earlier rows before later ones)

| # | Category | Level | Must have | Avoid |
|---|---|---|---|---|
| 1 | Accessibility | CRITICAL | Contrast ≥4.5:1 body, visible focus, alt text, ARIA labels, keyboard nav | Removing focus rings; icon-only buttons with no label |
| 2 | Touch & interaction | CRITICAL | ≥44×44pt targets, ≥8px spacing, loading feedback | Hover-only actions; 0ms instant state changes |
| 3 | Performance | HIGH | WebP/AVIF, lazy load, reserved space (CLS <0.1) | Layout thrash; cumulative layout shift |
| 4 | Style coherence | HIGH | Match the chosen direction; consistent SVG icon family | Mixing styles at random; emoji as structural icons |
| 5 | Layout & responsive | HIGH | Mobile-first, viewport meta, no horizontal scroll | Fixed-px widths; disabling zoom |
| 6 | Type & color | MEDIUM | Base ~16px, line-height ~1.5, semantic tokens | Body <12px; gray-on-gray; raw hex in components |
| 7 | Animation | MEDIUM | 150–300ms, motion conveys meaning, reduced-motion respected | Decorative-only motion; animating width/height |
| 8 | Forms & feedback | MEDIUM | Visible labels, inline errors near field, helper text | Placeholder-as-label; errors only at top |
| 9 | Navigation | HIGH | Predictable back, bottom nav ≤5, deep linking | Overloaded nav; broken back behavior |
| 10 | Charts & data | LOW | Legends, tooltips, accessible encodings | Color as the only signal |

---

## Accessibility (the non-negotiables)

- **Contrast:** ≥4.5:1 normal text, ≥3:1 large text and larger UI glyphs. Holds in light *and* dark.
- **Focus:** every interactive element has a visible focus state (2–4px ring). Never remove it.
- **Keyboard:** full operability; tab order matches visual order; logical traversal; offer keyboard
  alternatives to drag-and-drop; don't trap focus except intentionally in modals (and restore it on
  close).
- **Labels & semantics:** `label`/`for` on inputs; `aria-label` (or native accessibility label) on
  icon-only controls; sequential heading levels (no skips); semantic HTML first, ARIA only when HTML
  cannot express it; announce state (selected, disabled, expanded).
- **Color is never the only signal** — pair with icon, text, or pattern.
- **Reduced motion & dynamic type:** respect `prefers-reduced-motion`; support text scaling without
  truncation or layout breakage.
- **Alt text** for meaningful images; skip links for keyboard users; escape routes (cancel/back) in
  modals and multi-step flows.

---

## Touch & interaction

- Targets ≥44×44pt (iOS) / 48×48dp (Android); expand hit area beyond the visual bounds if the glyph
  is smaller. ≥8px between targets.
- Primary actions on click/tap, not hover. Add `cursor: pointer` to clickables on web;
  `touch-action: manipulation` to drop the 300ms delay.
- Visible press feedback within ~80–150ms (ripple/opacity/elevation) that does not shift layout.
- Don't override or block standard system gestures (back-swipe, pinch-zoom, Control Center).
- Disabled controls look disabled and do nothing; don't make dead controls look tappable.

---

## Forms & feedback

- Visible labels, not placeholder-only. Errors inline, next to the field, in plain language that
  says what went wrong and how to fix it.
- Helper text where useful. Progressive disclosure over overwhelming the user upfront.
- Disable submit during async work and show progress.

---

## Navigation

- Predictable back behavior. Bottom nav capped at ~5 items. Support deep links. Clear active states.

---

## Light / dark parity

- Surfaces separate clearly from background in both themes; primary text ≥4.5:1, secondary ≥3:1 in
  both. Borders, dividers, and interaction states stay distinguishable in both modes.
- Modal scrims strong enough to isolate foreground content (~40–60% black).
- Theme by semantic token, not per-screen hex. Test both modes before delivery, never infer one
  from the other.

---

## Icons & visual elements

- Vector only (SVG / platform vector), one consistent family, consistent stroke width and sizing
  (size as tokens: sm/md/lg). No emoji as structural icons. Filled vs outline: one style per
  hierarchy level. Align to text baseline. Meet contrast and touch-target minimums.

---

## Live web standards (fetch fresh each review)

For a current, authoritative web-interface review, fetch the latest Vercel Web Interface Guidelines
rather than relying on a cached copy (they evolve):

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use `web_fetch` to retrieve it, then check the target files against every rule and report findings
in terse `file:line` format. Fetch before each review so the rules are never stale.

---

## Pre-delivery accessibility checklist

- [ ] Body contrast ≥4.5:1, secondary ≥3:1, in light and dark
- [ ] Every interactive element has a visible focus state
- [ ] Keyboard operable; tab order matches visual order; modal focus trapped + restored
- [ ] Inputs have real labels, hints, inline errors
- [ ] Color is never the sole indicator
- [ ] Touch targets ≥44×44pt with adequate spacing
- [ ] `prefers-reduced-motion` respected; dynamic text size doesn't break layout
- [ ] Both themes tested, not inferred

Accessibility is the floor for every other room. A creative choice that breaks it is not a creative
choice — it's a defect (see `design-philosophy.md`, "when to break the rules").
