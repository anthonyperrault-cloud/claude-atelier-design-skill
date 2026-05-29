# Motion — Apple Easings System (Authoritative)

Motion in atelier is governed **entirely** by the Apple Easings system, preserved here in full and
unaltered (only internal file paths were adjusted to resolve inside this folder). It is the source
of truth for all easing and timing. This room is just the front door; the complete specification
lives in the files below.

**Read first for any motion work:** `motion/apple-easings-skill.md` (the complete skill, verbatim).

**The full library and protocols (all verbatim):**
| File | What it holds |
|---|---|
| `motion/apple-easings-skill.md` | The complete system: five modes, decision tree, workflows, critical rules, best practices |
| `motion/easing-tokens.md` | All 14 baseline easings in CSS, JS/TS, Tailwind, GSAP, Motion One, plus `linear()` spring variants |
| `motion/element-to-easing-map.md` | UI pattern → easing mapping, plus rules to detect element type from code |
| `motion/vibe-dictionary.md` | Natural-language motion words ("snappy", "liquid glass", "magnetic") → easings |
| `motion/apple-motion-reference.md` | Catalog of observable Apple motion patterns, sources, confidence, calibration history |
| `motion/self-extension-protocol.md` | Procedure for proposing new, Apple-grounded easings |
| `motion/library-calibration-protocol.md` | Auditing the library against current Apple research (iOS 26 / Liquid Glass / visionOS) |
| `motion/physics-translator.md` | Spring (response, dampingFraction) → cubic-bezier and `linear()` translation |

---

## What to do (quick orientation)

The system is codebase-aware and works from the code alone. Five modes:

- **A · Single element** — point at one thing, apply the right easing.
- **B · Codebase audit (default for broad asks)** — scan everything animated, identify each
  element's type from code, propose the right easing per element, **pause for approval, then apply.**
- **C · Self-extension** — a motion "vibe" not in the dictionary triggers an Apple-grounded proposal
  for a new easing; on approval, it is added to the library permanently.
- **D · Library calibration** — audit existing easings against current Apple research.
- **E · Physics translation** — internal machinery converting Apple spring presets to web timing.

**Decision tree for any element** (stop at first match): vibe word → `vibe-dictionary.md`; stated
element type → `element-to-easing-map.md`; otherwise infer type from code → map it; if genuinely
ambiguous → flag "needs review", do not guess.

---

## Non-negotiable motion rules (from the system, reinforced by the Laws)

1. **Stay in scope.** Modify only easing / timing-function. Never touch durations, keyframes,
   animated properties, layout, color, type, or accessibility properties.
2. **Never auto-apply.** Show proposed changes; wait for explicit approval. (Mirrors Law 4.)
3. **Flag ambiguity, don't guess.** List uncertain cases for review.
4. **Preserve intentional custom easings.** Surface an existing `cubic-bezier(...)` and ask before
   replacing it.
5. **Respect reduced motion.** Preserve existing `prefers-reduced-motion` handling; if missing,
   suggest it, do not add silently.
6. **No overshoot on text.** Downgrade any overshoot easing proposed for text to a non-overshoot one.
7. **Update the library surgically.** When self-extending, use precise edits, never full rewrites.

## Best practices

- Use semantic names in code (`var(--ease-modal-enter)`), not raw bezier inline.
- Match easing to duration — overshoot easings need ~350–500ms to land cleanly.
- One easing across related components reads as intentional; mixed reads as random.
- Check parent `overflow: hidden` before overshoot-scale (it will clip).
- Test motion in the browser; what reads in code may need tuning in practice.

This room coordinates with the rest of atelier without overlap: other rooms (typography, UX,
systems, audit) can run before or after motion work without conflict, and motion stays out of their
lanes. When code is the deliverable, it is final and complete (the designer does not finish code).
