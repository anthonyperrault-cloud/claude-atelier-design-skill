# Layout & Spacing — Rhythm, Hierarchy, Composition

Sources: the rad-spacing method (hierarchical proximity), the ui-ux-pro-max layout standards, and
the composition rules salvaged from ckm design (banner/safe-zone logic). Works in Figma and in code
alike — the principle is the same whether you set `itemSpacing` or `gap`.

---

## Hierarchical spacing (the proximity method)

Spacing is how the eye parses structure without dividers. The Gestalt principle of proximity:
related things sit closer, separate groups sit farther apart. Outer containers get proportionally
more space than inner elements.

**The ~40% rule:** each parent level gets ≈ 1.4× the spacing of its child level (child ≈ parent ×
0.6). Snap each result to the nearest 8px step; if 0.6× lands closer to a 4px step, use that.

**Method:**
1. Map the nesting depth, outermost to innermost (page → section → card → card content → inline).
2. Use the file's or system's existing spacing scale if one exists; adapt to its naming.
3. If none exists, use a semantic scale:
   `xs 4 · sm 8 · md 12 · lg 16 · xl 24 · 2xl 32 · 3xl 48`.
4. Work outward from a base (commonly 8px for the tightest grouping), applying the 1.4× step per
   level and snapping to 8px (or 4px when closer).
5. Apply as **padding** for container-level spacing and **gap** for spacing between siblings. Bind
   to spacing tokens wherever possible.
6. Validate: outer groups feel clearly separated; inner items feel cohesive; every level's step is
   perceptible. If two adjacent levels look the same, increase the ratio or re-snap.

**Worked example** (base 8px, working outward):

| Level | Element | Spacing | Why |
|---|---|---|---|
| 4 (inner) | label ↔ input | 8px gap | base |
| 3 | fields in a section | 12px gap | 8 × 1.4 ≈ 11.2 → 12 (4px snap) |
| 2 | sections in content | 16px gap | 12 × 1.4 ≈ 16.8 → 16 |
| 1 | content padding | 24px | 16 × 1.4 ≈ 22.4 → 24 |
| 0 (outer) | page padding | 32px | 24 × 1.4 ≈ 33.6 → 32 |

**Edge cases:** cap the outermost at a sane max (48–64px) for deep trees and compress inner levels
to keep the progression. Floor the innermost at 4px. When sibling-vs-parent is ambiguous, treat
visually distinct groups as separate levels. A component reused at different depths takes the spacing
of its context, not its definition.

---

## The 8px rhythm

Use a consistent 4/8px spacing system across component, section, and page levels. Random increments
with no rhythm read as sloppy. Define vertical-rhythm tiers by hierarchy (e.g. 16 / 24 / 32 / 48) so
similar UI levels share spacing and different levels clearly differ.

---

## Layout standards (web and app)

- **Mobile-first.** Start small, layer up. Breakpoints follow content needs, not specific devices.
- **No horizontal scroll** on main content. No fixed-px container widths that break small screens.
  Never disable zoom; set the viewport meta correctly.
- **Reserve space for async content** to keep cumulative layout shift low (CLS < 0.1). Don't let
  things jump as images/data load.
- **Readable measure on large screens** — don't let long-form text run edge-to-edge on tablet/desktop
  (ties to the 45–90 character line length in `typography.md`).
- **Adaptive gutters** — wider horizontal insets at larger widths and in landscape.
- **Safe areas (app)** — respect notch, status bar, gesture home indicator, and Dynamic Island for
  fixed headers, tab bars, and CTA bars. Add content insets so lists are not hidden behind sticky
  bars.
- **Grids guide, they don't guarantee.** Simpler grids enforce more consistency. Aligning weak
  composition to a grid still leaves it weak. Print: 2–3 columns on letter, rarely 4. Web columns
  are awkward (indefinite bottom edge) — use with care.

---

## Composition rules (fixed-canvas / banner / hero)

For fixed-dimension visual pieces:
- Keep critical content in the central **70–80%** safe zone.
- **One primary CTA** per piece, typically bottom-right, minimum 44px tall.
- Max two type families; body ≥ 16px, headline ≥ 32px.
- For ad placements, keep text light (heavy text gets penalized on some platforms).
- Print output: 300 DPI, CMYK, 3–5mm bleed.

---

## Validation before delivery

- Spacing follows one rhythm and reads as intentional hierarchy.
- Nothing is off by 1–2px; elements align to the grid.
- Touch targets and tap spacing meet the minimums in `ux-accessibility.md`.
- Layout holds at small phone, large phone, tablet, and desktop, portrait and landscape.

(All changes stay surgical and token-bound; propose-then-apply on existing layouts — Law 3/4.)
