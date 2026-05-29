# Physics Translator — Spring → Bezier & linear()

How to translate Apple's spring-based motion into web-compatible cubic-bezier and CSS
`linear()` timing functions. This file is used by Mode C (self-extension), Mode D
(library calibration), and any other workflow needing physics-grounded translation.

---

## Important: What Translation Can and Can't Do

### What's possible
- ✅ Match the **dominant feel** of a spring (acceleration profile, single overshoot, settle)
- ✅ Translate critically-damped or overdamped springs → cubic-bezier with high accuracy
- ✅ Sample any spring into a `linear()` timing function with arbitrarily-close fidelity
- ✅ Use Apple's published SwiftUI spring presets as authoritative anchor points

### What's not possible
- ❌ Replicate multi-bounce / heavily underdamped springs in cubic-bezier (cubic-bezier passes its target exactly once)
- ❌ Match Apple's motion 1:1 — even with research, we're approximating a continuous physics simulation
- ❌ Replace `@keyframes` animations that use complex 2D path manipulation

### When to NOT translate to cubic-bezier
If a spring oscillates more than once before settling (dampingFraction < ~0.5), flag it.
The translation should propose `linear()` syntax instead, or recommend `@keyframes`.

---

## Apple's Documented Spring Presets (Source of Truth)

These are explicitly published by Apple in WWDC 2023 Session 10158 *"Animate with springs"*
and the SwiftUI documentation. Use these as anchor points whenever possible — they're as
close to "Apple's actual values" as anything publicly available.

| SwiftUI preset | response | dampingFraction | Approx. duration | Visible overshoot |
|---|---|---|---|---|
| `.smooth` | 0.5 | 1.0 | ~0.75s | None (critically damped) |
| `.snappy` | 0.5 | 0.85 | ~0.5s | ~3% (subtle) |
| `.bouncy` | 0.5 | 0.7 | ~0.5s | ~12% (visible) |
| `.interactiveSpring` | 0.15 | 0.86 | ~0.2s | ~3% (very fast) |
| `.spring()` default | 0.5 | 0.825 | ~0.5s | ~5% |

These are the **named feels** SwiftUI engineers reach for. When researching an Apple
pattern, if you can identify which preset it uses (via WWDC content or developer docs),
translate directly from these values.

---

## Spring → Cubic-Bezier Translation Table

Use these approximations for the documented presets. Each is the closest cubic-bezier
that captures the dominant settle character.

| Spring | Approx. cubic-bezier | Notes |
|---|---|---|
| `.smooth` (0.5, 1.0) | `cubic-bezier(0.4, 0.0, 0.2, 1.0)` | Material-style smooth ease; no overshoot |
| `.snappy` (0.5, 0.85) | `cubic-bezier(0.45, 0.0, 0.2, 1.1)` | Slight overshoot; close to MD3 emphasized |
| `.bouncy` (0.5, 0.7) | `cubic-bezier(0.5, 0.0, 0.25, 1.25)` | Visible overshoot; one-pass bezier loses some bounce character |
| `.interactiveSpring` (0.15, 0.86) | `cubic-bezier(0.4, 0.0, 0.2, 1.1)` | Fast & snappy; use shorter duration (~200ms) |
| `.spring()` default | `cubic-bezier(0.45, 0.0, 0.2, 1.15)` | Apple's "standard" feel |

---

## Spring → linear() Translation (Higher Fidelity)

For springs with visible overshoot or oscillation, `linear()` is more accurate than
`cubic-bezier()` because it can represent multi-pass motion.

### Generation procedure

Sample the spring's position over time at ~10–15 evenly spaced points. The formula for
a damped harmonic oscillator at time t (where target = 1.0):

```
ω₀  = 2π / response                              (natural frequency)
ω_d = ω₀ · √(1 - ζ²)                             (damped frequency, for ζ < 1)
y(t) = 1 - e^(-ζω₀·t) · (cos(ω_d·t) + (ζω₀/ω_d)·sin(ω_d·t))
```

Where ζ is the dampingFraction.

### Pre-computed `linear()` for documented presets

| Spring | `linear()` value | Total duration |
|---|---|---|
| `.smooth` | `linear(0, 0.084, 0.302, 0.547, 0.769, 0.901, 0.967, 0.992, 1)` | 0.75s |
| `.snappy` | `linear(0, 0.144, 0.466, 0.764, 0.949, 1.029, 1.030, 1.008, 1)` | 0.5s |
| `.bouncy` | `linear(0, 0.187, 0.591, 0.917, 1.106, 1.140, 1.075, 1.011, 0.988, 0.995, 1)` | 0.5s |
| `.interactiveSpring` | `linear(0, 0.272, 0.681, 0.910, 1.000, 1.014, 1.008, 1)` | 0.2s |
| `.spring()` default | `linear(0, 0.151, 0.487, 0.797, 0.974, 1.040, 1.041, 1.020, 1)` | 0.5s |

### Usage

```css
.element {
  /* Both for progressive enhancement */
  transition: transform 0.5s cubic-bezier(0.5, 0, 0.25, 1.25); /* fallback */
  transition: transform 0.5s linear(0, 0.187, 0.591, 0.917, 1.106, 1.140, 1.075, 1.011, 0.988, 0.995, 1);
}
```

Browser support: `linear()` is supported in Safari 17.4+, Chrome 113+, Firefox 112+.
Always provide `cubic-bezier()` as a fallback in the same declaration (browser uses last
valid value).

---

## Reverse Engineering (Observation → Spring Estimate)

When researching an Apple motion pattern via observation only (no published values),
estimate spring parameters using this decision tree:

### Step 1: How does it settle?

| Observed settle behavior | Estimated dampingFraction |
|---|---|
| Reaches target and stops with no visible overshoot | 1.0 (critically damped) |
| Slight subtle nudge past target, then settles | 0.85–0.95 |
| Clearly visible single bounce past target | 0.65–0.8 |
| Two or more visible oscillations | 0.4–0.6 (use linear() not bezier) |
| Many bounces, jelly-like | < 0.4 (use linear() or @keyframes) |

### Step 2: How long does it take?

| Total motion duration | Estimated response |
|---|---|
| ~200ms | 0.15 |
| ~300ms | 0.3 |
| ~400ms | 0.4 |
| ~500ms | 0.5 |
| ~600–700ms | 0.6 |
| ~800ms+ | 0.7+ |

### Step 3: Translate

Use the Translation Table above (or interpolate between rows). Document the estimated
spring params alongside the bezier value so they can be re-translated later if needed.

---

## The Corrective Workflow

When the Physics Translator finds that a library easing doesn't match the spring values
Apple uses for a given pattern, follow this procedure.

### Step 1: Identify the discrepancy

For each library easing, compare its current bezier values against the bezier translation
of the matching Apple spring preset.

**Threshold:** If any single bezier parameter differs by more than **0.1** from the
research-derived value, flag for review. If multiple parameters differ, flag with higher
priority.

### Step 2: Determine the cause

A library easing can be "off" for legitimate reasons:
- It was built before the matching Apple pattern existed (e.g., iOS 26 / visionOS)
- It was tuned for a different specific use case (good — keep)
- It was inherited from an older Apple motion (e.g., pre-iOS 7) and the modern equivalent has shifted
- It was authored from imperfect references at the time

Note the cause in the proposal.

### Step 3: Propose adjustment

Show the user:

```
LIBRARY CALIBRATION FINDING

Easing: scaleOvershoot01
Current values: (0.7, -0.2, 0.6, 1.4)
Mapped Apple reference: iOS app icon launch zoom

Research finding:
- Apple pattern uses spring(.snappy) per WWDC 2023 Session 10158
- Spring values: response: 0.4, dampingFraction: 0.85
- Translated bezier: (0.45, 0.0, 0.2, 1.1)
- Translated linear(): linear(0, 0.144, 0.466, 0.764, 0.949, 1.029, 1.030, 1.008, 1)

Discrepancy:
- Current y1 = -0.2; research suggests 0.0 (no undershoot in modern iOS app launch)
- Current y2 = 1.4; research suggests 1.1 (less aggressive overshoot)
- Current asymmetry is more dramatic than current iOS uses

Recommendation: Calibrate to (0.45, 0.0, 0.2, 1.1) and add linear() variant

Options:
  1. Apply the recommended adjustment (replaces current values)
  2. Keep current values as 'scaleOvershoot01Legacy', add new values as 'scaleOvershoot01'
  3. Keep current values unchanged (you have a reason for them)
  4. Adjust to different values
```

### Step 4: After user approval, apply

Use surgical str_replace edits to update:
- `easing-tokens.md` (5 sections, plus add linear() if requested)
- `apple-motion-reference.md` (update the "Currently mapped" notes, add Translation Log entry)

### Step 5: Log the calibration

Append to the Calibration History section of `apple-motion-reference.md`:

```
YYYY-MM-DD: Calibrated scaleOvershoot01 from (0.7, -0.2, 0.6, 1.4) to (0.45, 0.0, 0.2, 1.1) based on WWDC 2023 Session 10158 spring values. Reason: original library predates SwiftUI spring preset publication.
```

---

## Web Search Integration

When researching an Apple pattern not covered by `apple-motion-reference.md` or by
documented SwiftUI presets, use web search.

### When to search
- New iOS / macOS / visionOS / watchOS version released after library was built
- User mentions a feature not in the reference library
- A pattern's behavior changed in a recent OS update
- Need to verify a claim about a specific motion

### What to search for
Effective queries:
- `WWDC 2024 spring animation iOS` (or current year)
- `apple [feature name] motion design`
- `iOS 26 liquid glass animation timing` (or current OS / feature)
- `SwiftUI .spring response damping documentation`
- `apple.com inspect cubic-bezier motion`
- `[feature name] iOS reverse engineered easing`

### What to extract
- Spring parameter values (response, dampingFraction, mass, initial velocity)
- Cubic-bezier values cited
- WWDC session numbers and URLs
- Apple Developer documentation URLs
- Specific feature versions (iOS 26.x, etc.)

### What to cite
Every new entry added to `apple-motion-reference.md` from a web search must include:
- The exact URL
- The confidence level (Documented / Inferred / Approximated)
- Whether the source is Apple-official or third-party

### What NOT to trust
- Random Stack Overflow answers without sources
- AI-generated content cited as Apple documentation
- Old (pre-iOS 14) bezier values being claimed to represent current iOS
- Vague "Apple uses this curve" claims with no source

When in doubt, mark confidence as Approximated and document the uncertainty.

---

## Specific Note: iOS 26 / Liquid Glass

If working with a library built before iOS 26, the existing easings may not reflect:
- Liquid Glass material motion (new in iOS 26)
- Updated visionOS 2 spatial spring tuning
- Refreshed Control Center spring parameters

When triggered for calibration, **always web search for current iOS / visionOS motion
guidance** before comparing to existing library values. Document any findings in
`apple-motion-reference.md`.

---

## How Other Protocols Use This File

### `self-extension-protocol.md`
At Step 2 (Decompose the Vibe), the protocol checks if the requested feel matches a
documented SwiftUI spring preset. If yes, use the translation table directly. If no,
estimate spring params via reverse engineering, then translate.

### `library-calibration-protocol.md`
Walks every existing library easing through the Corrective Workflow above. Web searches
for current Apple values when reference library is silent or stale.

### `apple-motion-reference.md`
Updated continuously as web search reveals new spring values. The Translation Log section
records every spring → bezier conversion for traceability.
