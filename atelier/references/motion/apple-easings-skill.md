---
name: apple-easings
description: >
  Apple-style easing library and motion auditor with physics-grounded spring-to-bezier
  translation. Five modes: apply to a single element, audit/apply across a codebase,
  self-extend with new Apple-grounded easings, calibrate library against current Apple
  research (WWDC, SwiftUI spring presets, live web search for iOS 26 / Liquid Glass /
  visionOS), and translate Apple's spring physics into cubic-bezier and CSS linear()
  timing. Modifies only timing-function/ease — never durations, keyframes, layout,
  color, or typography. Trigger when the user says apply Apple easings, audit my
  animations, calibrate easings, ease this, give this Apple feel; uses motion vibe
  language (snappy, buttery, magnetic, springy, liquid, glass, floaty, elastic, punchy,
  bouncy, premium); mentions SwiftUI springs, Liquid Glass, or iOS 26 motion; or
  implements transitions in CSS, Framer Motion, GSAP, Tailwind, or Motion One. Do not
  trigger for After Effects work, basic ease-in/out, or color/layout/typography.
---

# Apple Easings — Web Motion Library + Auditor

A motion design tool with three modes. The skill is **codebase-aware** and operates with
minimal user guidance — point it at code and it figures out what's animated, what kind of
element each one is, and what easing fits best.

---

## Five Modes

### Mode A: Single Element
User points at one element. Apply the right easing.

### Mode B: Codebase Audit (DEFAULT for ambient triggers)
User says "apply easings" or similar without scoping. Claude scans the codebase, identifies
every animated element from the code alone (no user labeling needed), and proposes the
right easing for each.

### Mode C: Self-Extension
User uses vibe language that doesn't map to any existing easing. Claude consults the
Apple Motion Reference Library, runs the Physics Translator for spring-grounded proposals,
gets approval, and adds new easings to the library permanently.

### Mode D: Library Calibration
User asks to audit/calibrate the existing library. Claude walks every easing through the
Library Calibration Protocol, comparing current values against current Apple research
(SwiftUI spring presets, WWDC content, live web search), and proposes adjustments where
research shows discrepancies. Critical for libraries built before recent Apple OS releases
(iOS 26 Liquid Glass, visionOS 2, etc.).

### Mode E: Physics Translation
Not a user-invoked mode — automatic machinery used inside Modes C and D. Translates
Apple's spring physics (response, dampingFraction) into cubic-bezier and CSS linear()
timing functions. Outputs both formats for progressive enhancement.

---

## How to Identify the Right Easing (decision tree)

For any element Claude needs to ease, walk this tree in order. **Stop at the first match.**

```
1. Did the user use vibe language? (e.g., "magnetic", "liquid glass", "snappy")
   → Consult vibe-dictionary.md
   → If found, use that easing
   → If not found, go to Mode C (self-extension)

2. Did the user point at a specific element type? (modal, toast, etc.)
   → Consult element-to-easing-map.md
   → Use the recommended easing for that element type

3. Otherwise, infer the element type from the code:
   → Component name, file name, ARIA role, class names, Tailwind layout patterns
   → Consult element-to-easing-map.md for the inferred type
   → Use the recommended easing

4. If inference is ambiguous (multiple equally-likely types):
   → Flag the element as "needs review"
   → Do not guess
```

---

## Mode B: Codebase Audit Workflow

When the user invokes the skill with broad scope ("audit my app", "apply easings everywhere",
"go through the site"), execute these steps **in order**. Never skip the user-approval step.

### Step 1: Scan
Use `grep`/`rg` to find every animated element. Look for:
- CSS: `transition:`, `animation:`, `@keyframes`, `cubic-bezier(`, `timing-function`
- Framer Motion: `transition={`, `ease:`, `transition: {`
- GSAP: `ease:` parameters in `.to()`, `.from()`, `.fromTo()`, timelines
- Tailwind: `ease-*`, `transition-*`, `duration-*` classes
- Web Animations API: `easing:` in `.animate()` calls
- CSS-in-JS: `transition:` in styled-components, emotion, vanilla-extract

Catalog every match with: file path, line, current easing, property animated, surrounding context.

### Step 2: Identify each element's type from code alone
For each match, run the detection rules in `element-to-easing-map.md`. Detection
uses (in priority order):
1. Component name (e.g., `<Dialog>`, `<Toast>`)
2. File name (e.g., `Modal.tsx`, `dropdown.tsx`)
3. ARIA role (`role="dialog"`, `role="menu"`)
4. Library imports (e.g., `@radix-ui/react-dialog`)
5. CSS class patterns (`.modal`, `.toast`)
6. Tailwind/CSS layout signals (`fixed inset-0` → likely modal overlay)
7. Animation context (looped + repeat: Infinity → idle/float)

If signals conflict or are weak, mark "ambiguous — needs review" and **move on without guessing**.

### Step 3: Map to recommended easing
Use `element-to-easing-map.md` to look up the easing for each identified type.

### Step 4: Propose changes (PAUSE — wait for approval)
Show the user a clear table:

```
PROPOSED EASING CHANGES (28 found)

✅ Auto-mapped (24):
  src/components/Modal.tsx:42       Modal open       ease-in-out → scaleSubtleBounce
  src/components/Toast.tsx:18       Toast appear     ease-out    → whooshSnapIn
  src/styles/cards.css:55           Card hover       linear      → scaleSubtleBounce
  ...

⚠️  Ambiguous (4 — please review):
  src/components/HeroBanner.tsx:30  Could be: whooshFloatSettle OR scaleOvershoot01
  src/styles/page.css:12            Generic .fade — context unclear
  ...

Approve auto-mapped? Review ambiguous ones?
```

**Do not write any code changes until the user explicitly approves.**

### Step 5: Apply
After approval, write the changes in the user's stack syntax. See `easing-tokens.md`
for format options. If the project lacks an easings module, create one (`src/lib/easings.ts`
or `src/styles/easings.css`).

### Step 6: Report
Show a summary: changes made, files touched, easings module created/updated, items still
flagged for review.

---

## Mode C: Self-Extension Workflow

Triggered when the user uses vibe language that doesn't match `vibe-dictionary.md`,
or explicitly asks for a new easing.

### Step 1: Decompose the vibe
Break the descriptive language into motion characteristics. Ask: does this vibe imply...
- Fast or slow start?
- Sharp or gradual stop?
- Overshoot or undershoot?
- Continuous or terminal motion?
- Linear or curved energy?

### Step 2: Propose cubic-bezier values
Generate a candidate `(x1, y1, x2, y2)` curve with explicit reasoning. Show the user:

```
The vibe "iridescent ripple" isn't in the library. I read it as:
- Wave-like motion (smooth acceleration & deceleration)
- Delicate (subtle overshoot, no harsh stops)
- Slightly slower than typical

Proposed easing: rippleSettle = (0.45, 0.05, 0.55, 1.15)
- Symmetric x values (0.45 / 0.55) → smooth wave feel
- Mild overshoot (y2 = 1.15) → delicate settle
- Reasonable duration: 500-600ms feels right

Should I:
  1. Add 'rippleSettle' to the library permanently and apply
  2. Apply this curve as a one-off (don't save to library)
  3. Try different values
  4. Suggest an existing easing instead
```

### Step 3: User approval (PAUSE)
**Do not modify the skill files until the user picks option 1.**

### Step 4: If approved, update the skill library
Edit these files using careful `str_replace`-style edits (never full rewrites):

1. **`easing-tokens.md`**:
   - Add a row to the main library table
   - Add a CSS custom property
   - Add a JS constant (both array format and CSS string format)
   - Add a Tailwind config entry
   - Add a GSAP CustomEase registration

2. **`vibe-dictionary.md`**:
   - Add the new vibe word(s) → new easing mapping

3. **`element-to-easing-map.md`**:
   - If the new easing fits a specific UI pattern, add it as an alternate option

4. **`SKILL.md`** (this file):
   - No edits typically needed — the library is referenced, not duplicated here

### Step 5: Apply to the user's code
Use the newly-added easing on the element that triggered the extension.

### Step 6: Report
Confirm the library has been updated and tell the user the new easing is permanent — future
projects will have it too.

---

## Mode D: Library Calibration Workflow

When the user invokes calibration ("calibrate my easings", "audit my library against
current Apple", "update for iOS 26"), follow the **Library Calibration Protocol** in
`library-calibration-protocol.md`. Key points:

1. Read current library values from `easing-tokens.md`
2. For each easing, identify mapped Apple references from `apple-motion-reference.md`
3. Web search for current Apple motion guidance (especially for patterns post-dating the library)
4. Use the Physics Translator to convert documented spring presets to bezier and linear()
5. Compare research-derived values to current library values
6. Compile findings table (well-calibrated / minor drift / significant drift / missing patterns)
7. **Pause** for user review of findings
8. Apply approved changes via surgical edits to all relevant sections of `easing-tokens.md`
9. Update `apple-motion-reference.md` Calibration History log

The protocol is conservative — discrepancies under 0.1 on any bezier parameter are kept
as-is. Significant drift gets flagged, but the user always approves before changes apply.

---

## Mode E: Physics Translation (Automatic)

When Mode C or Mode D needs to translate Apple's spring physics into web-compatible
timing functions, use the **Physics Translator** in `physics-translator.md`.
Key capabilities:

- Translate documented SwiftUI spring presets (`.smooth`, `.snappy`, `.bouncy`, etc.) to
  cubic-bezier using a pre-computed table
- Sample any spring (response + dampingFraction) into a CSS `linear()` timing function
  for high-fidelity reproduction of overshoot/oscillation
- Reverse-engineer estimated spring parameters from observed motion when no published
  values are available
- Flag motion that's fundamentally not bezier-able (heavy oscillation) and recommend
  `linear()` or `@keyframes` instead

Output format for spring-based motion:

```css
/* Spring(.snappy) — WWDC 2023 Session 10158 */
--ease-scale-overshoot-01: cubic-bezier(0.45, 0.0, 0.2, 1.1); /* fallback */
--ease-scale-overshoot-01-linear: linear(0, 0.144, 0.466, 0.764, 0.949, 1.029, 1.030, 1.008, 1);
```

The skill should provide both formats when possible — `linear()` is more faithful to
Apple's actual motion, `cubic-bezier()` is the fallback for older browsers.

---

## Cooperation with Other Skills

This skill is intentionally narrow. It **modifies only**:
- `transition-timing-function` (CSS)
- `animation-timing-function` (CSS)
- `ease:` in Framer Motion, GSAP, Motion One
- `easing:` in Web Animations API
- The `ease-*` part of Tailwind classes
- `transitionTimingFunction` entries in Tailwind config

It **does not modify**:
- Animation durations or delays
- `@keyframes` content
- Which properties are animated
- Layout, sizing, positioning, color, typography
- Accessibility properties (focus rings, etc.)
- Reduced-motion media queries (but suggests adding if missing)

This means:
- Other audit skills (UX, typography, accessibility, color, design system) can run before
  or after this skill without conflict
- This skill can be invoked as a sub-step within a broader audit — it returns surgical,
  non-overlapping changes
- If another skill changes a `transition` shorthand, this skill's easing portion remains
  the source of truth

When this skill detects that another design skill is involved (based on context from the
user or imports in the project), it should:
- Defer non-easing concerns to those skills explicitly
- Stay in its lane

---

## Reference Files

| File | Purpose |
|---|---|
| `easing-tokens.md` | Library easings in CSS, JS, Framer Motion, GSAP, Tailwind, Motion One formats. Includes linear() variants for spring-based easings. |
| `element-to-easing-map.md` | UI pattern → easing mapping + detection rules from code |
| `vibe-dictionary.md` | Natural language descriptors → easings |
| `apple-motion-reference.md` | Curated catalog of observable Apple motion patterns with sources, confidence levels, mapped library easings, and a calibration history log |
| `self-extension-protocol.md` | Procedure for proposing new easings — requires Apple grounding via reference library or web search |
| `library-calibration-protocol.md` | Procedure for auditing existing library against current Apple research (Mode D) |
| `physics-translator.md` | Spring → cubic-bezier and linear() translation system. Includes documented SwiftUI spring presets, reverse engineering rules, and corrective workflow (Mode E) |

---

## Critical Rules

1. **Stay in scope.** Only modify easing/timing-function. Never touch other properties.
2. **Never auto-apply.** Always show proposed changes and wait for explicit approval.
3. **Flag ambiguous cases.** Don't guess. List them for human review.
4. **Preserve existing custom easings.** If a developer already has `cubic-bezier(0.x, 0.x, 0.x, 0.x)` in place, surface it and ask before replacing — it may be intentional.
5. **Respect reduced motion.** If the codebase has `prefers-reduced-motion` handling, preserve it. If it doesn't, suggest adding it (don't add silently).
6. **Update the library carefully.** When self-extending, use surgical edits — never rewrite reference files from scratch.
7. **No overshoot on text.** If a proposed change would put an overshoot easing on text, downgrade to a non-overshoot alternative.

---

## Best Practices

1. Use semantic names in code, not raw bezier — `var(--ease-modal-enter)` beats inline `cubic-bezier(...)`
2. Match easing to duration — overshoot easings need 350–500ms to land cleanly
3. Same easing across related components feels intentional; mixed feels random
4. Always check parent `overflow: hidden` before applying overshoot scale (it'll clip)
5. Test motion changes in browser — what feels right in code may need tuning in practice
