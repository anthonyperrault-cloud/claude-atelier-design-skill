# Design Systems — Tokens, Specs, States

Sources: the ckm design-system skill (token architecture, component specs) and the ckm ui-styling
skill (composition and theming principles). Slide generators, asset pipelines, and library install
commands are intentionally left out. This room is the systems-architecture method.

---

## Three-layer token architecture

Never reference raw values in components. Flow through three layers so the system can re-theme,
re-brand, and stay consistent without touching component code.

```
Primitive (raw values)        --color-blue-600: #2563EB;
        ↓
Semantic (purpose aliases)    --color-primary: var(--color-blue-600);
        ↓
Component (component-scoped)  --button-bg: var(--color-primary);
```

- **Primitive** — the raw scale. Colors, sizes, radii, durations. No meaning, just values.
- **Semantic** — purpose. `--color-primary`, `--color-danger`, `--surface`, `--text-muted`,
  `--space-section`. This layer is where theming and light/dark live.
- **Component** — component-specific aliases that point at semantic tokens. Enables per-component
  customization without leaking primitives into markup.

**Why it matters:** the semantic layer makes light/dark and re-brand a token swap, not a rewrite.
Component tokens let one component change without disturbing the rest. Document every token's
purpose. Prefer HSL where opacity control matters.

---

## Token compliance (the rule that keeps a system a system)

```css
/* CORRECT — references tokens */
background: var(--surface);
color: var(--color-primary);
font-family: var(--font-heading);

/* WRONG — hardcoded one-offs that fracture the system */
background: #0D0D0D;
color: #FF6B6B;
font-family: 'Some Font';
```

If a needed value has no token, **propose the token; do not invent a silent one-off.** Hardcoded
values are how a design system quietly dies.

---

## Component spec pattern

Specify every component as a state matrix before building it. This is the contract a build follows.

| Property | Default | Hover | Active | Focus | Disabled |
|----------|---------|-------|--------|-------|----------|
| Background | primary | primary-dark | primary-darker | primary | muted |
| Text | on-primary | on-primary | on-primary | on-primary | muted-fg |
| Border | none | none | none | focus-ring | muted-border |
| Elevation | sm | md | none | sm | none |

Rules:
- **Every interactive element needs every state** designed, not just default: hover, focus, active,
  disabled, and where relevant loading, error, selected, expanded.
- Press/active feedback should not shift layout bounds (no jitter). Change color, opacity, or
  elevation, not size that reflows neighbors.
- Focus states are mandatory and visible (see `ux-accessibility.md`). Never remove the focus ring.

---

## Composition and styling principles

From the ui-styling craft, kept as method (not as a setup tutorial):

1. **Compose from primitives.** Build complex UI from small, accessible, composable parts. Extract a
   component only for true repetition.
2. **Accessibility-first.** Prefer accessible primitives (e.g. Radix-style headless components) and
   semantic HTML; add focus states and roles. Accessibility is structural, not a finishing pass.
3. **Utility-first, token-bound.** Style with utilities where it keeps things fast and consistent,
   but bind to the token scale rather than scattering arbitrary values.
4. **Mobile-first responsive.** Start at the smallest viewport, layer up. See `layout-spacing.md`
   and `ux-accessibility.md`.
5. **Dark mode is designed, not inverted.** Every themed element gets a dark variant; check contrast
   and elevation in both modes, not just light.
6. **Visual hierarchy by composition.** Let spacing, scale, and color guide attention intentionally.
7. **Craft.** Every detail matters. Treat the interface as a crafted object.

---

## Where this connects

- Brand input (colors, type, voice) feeds the **primitive** layer.
- Tokens feed the build's theme configuration.
- The token scale for spacing is the same one `layout-spacing.md` uses for rhythm.
- Type tokens follow the rules in `typography.md`. Motion tokens follow `motion.md`.

When delivering tokens or specs as code, deliver the complete, correct file (the designer does not
finish code). When changing an existing system, change surgically and propose-then-apply (Law 3/4).
