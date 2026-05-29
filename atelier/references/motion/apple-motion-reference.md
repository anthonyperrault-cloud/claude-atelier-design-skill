# Apple Motion Reference Library

Curated catalog of observable Apple motion patterns. Every entry references a feature
**you can verify with your own eyes** on shipping Apple products. This file is the source
of truth for Claude's "Apple grounding" — used by both the self-extension protocol and
the library calibration protocol.

---

## Important: What This File Is (and Isn't)

### What this is
Public, observable Apple motion patterns documented with:
- Where to observe them on shipping Apple products
- What the motion looks like
- Estimated cubic-bezier approximations of the feel
- Source citations (WWDC sessions, HIG, public docs, designer write-ups)
- Confidence levels

### What this isn't
**Apple's internal motion specs.** Apple does not publish their exact cubic-bezier values
or spring parameters. More importantly, **modern Apple motion is spring-based, not
cubic-bezier-based.** UIKit uses `UIView.animate(...usingSpringWithDamping:...)`. SwiftUI
uses `.animation(.spring())`. visionOS uses spatial spring physics. There is no
authoritative bezier curve for "iOS Share Sheet" because Apple isn't using one.

### What this means in practice
- Every cubic-bezier in this file is **an approximation** of a spring-based feel
- Confidence levels matter — see legend below
- Multiple bezier curves can be equally valid approximations of the same Apple motion
- Your library easings may already be a good fit; calibration is about evidence, not absolutes

### Confidence Legend
| Level | Meaning |
|---|---|
| 🟢 **Documented** | Apple's own docs/WWDC sessions describe the motion characteristics explicitly |
| 🟡 **Inferred** | Observable in shipping products; characteristics inferred from careful observation |
| 🟠 **Approximated** | Spring-based in Apple's actual implementation; cubic-bezier is the closest CSS analog |

---

## Quick Lookup: Library Easing → Apple References

| Library easing | Closest Apple patterns | Confidence |
|---|---|---|
| `whooshEnergetic` | App Library zoom open; visionOS window summon | 🟠 |
| `whooshSnapIn` | iOS Control Center pull-down; Spotlight open | 🟡 |
| `whooshFloatSettle` | iOS Share Sheet; Modal page sheet presentation | 🟡 |
| `scaleOvershoot01` | iOS app icon launch zoom; Memoji entry | 🟡 |
| `scaleOvershoot02` | iMessage effects (slam); Game Center reveals | 🟡 |
| `scaleSubtleBounce` | macOS Dock magnification; iOS toggle switch flip | 🟡 |
| `textTypeOn` | iOS Messages typing indicator cadence | 🟠 |
| `textElegantFadeIn` | apple.com product reveal headlines; Keynote title build | 🟡 |
| `textSnapFade` | iOS Settings detail-view title fade; tab switch text | 🟡 |
| `opacityFadeIn` | iOS Photos thumbnail load; lazy-load image fade | 🟢 |
| `opacitySmooth` | iOS Lock Screen / wake fade; Safari content fade | 🟡 |
| `opacitySnap` | iOS notification appear; toast animations | 🟡 |
| `floatLoose` | iOS Home Screen idle wallpaper parallax | 🟡 |
| `floatSettleLoop` | Siri orb pulse; Now Playing on Apple TV | 🟡 |

---

## Quick Lookup: Motion Characteristic → Apple References

For when Claude needs to find an Apple pattern matching a vibe:

| Characteristic | Apple patterns to reference |
|---|---|
| Subtle overshoot, single bounce | iOS app icon launch, Memoji entry, Game Center |
| Asymmetric (fast-out, slow-settle) | iOS Share Sheet, modal presentations, Control Center |
| Smooth and weighted | macOS window minimize/restore, iOS keyboard slide |
| Idle / breathing / ambient | Siri orb, Now Playing, Home Screen wallpaper, visionOS ambient elements |
| Sharp and decisive | Spotlight open, iOS dismiss gestures, app switcher transitions |
| Playful / energetic / kinetic | iMessage effects (slam, gentle, loud, invisible ink), Apple Music visualizer |
| Liquid / weighted-fluid | iOS Liquid Detection alert, iPadOS Stage Manager window morphs, visionOS window drag |
| Premium / cinematic | apple.com product reveals (iPhone, AirPods Max, Vision Pro pages) |
| Magnetic / pull-to-target | macOS Dock magnification, Apple Pencil hover preview, AirPods case lid snap |

---

## Documented Patterns (by category)

### 1. Navigation & Presentation

#### iOS Share Sheet (Modal Slide-Up)
- **Where to observe:** iPhone → any app → Share button → sheet rises from bottom
- **Motion:** Sheet rises from bottom edge, mild acceleration, subtle overshoot at top, settles
- **Characteristics:** Asymmetric (fast launch, slow settle), 4–6% overshoot, ~400ms total
- **Estimated bezier:** `(0.65, 0, 0.2, 1.15)`
- **Confidence:** 🟡 Inferred (Apple uses UIKit modal spring underneath)
- **Source:** WWDC 2019 "Modernizing Your UI for iOS 13" Session 224; HIG "Modality"
- **Currently mapped:** `whooshFloatSettle` (0.65, 0, 0.2, 1.2)
- **Notes:** Very close match. Library y2 = 1.2 slightly more overshoot than typical observation. Within acceptable margin.

#### iOS Modal Page Sheet (Card-style modal)
- **Where to observe:** iPhone → many apps → modal that takes over most of screen but shows previous content peeking at top
- **Motion:** Card rises from bottom with mild spring, settles ~30px below top edge
- **Characteristics:** Similar to Share Sheet but with more visible card edge animation
- **Estimated bezier:** `(0.6, 0, 0.2, 1.15)`
- **Confidence:** 🟡 Inferred
- **Source:** HIG "Sheets"; WWDC 2019 "Modernizing Your UI for iOS 13"
- **Currently mapped:** `whooshFloatSettle`
- **Notes:** Same family as Share Sheet, can share easing.

#### iOS Control Center Pull-Down
- **Where to observe:** iPhone → swipe down from top-right corner → panel pulls down
- **Motion:** Follows finger 1:1 during drag; on release, snaps with sharp deceleration
- **Characteristics:** Sharp, decisive, minimal overshoot, asymmetric
- **Estimated bezier:** `(0.6, 0.05, 0.25, 1.1)`
- **Confidence:** 🟡 Inferred
- **Source:** Observable behavior; iOS gesture system
- **Currently mapped:** `whooshSnapIn` (0.6, 0.05, 0.25, 1.2)
- **Notes:** Library y2 = 1.2; observed closer to 1.1. Candidate for calibration to softer overshoot.

#### Spotlight Search Open
- **Where to observe:** iPhone → swipe down from middle of Home Screen → Spotlight appears
- **Motion:** Search field expands from above with quick blur+fade; results area fades in
- **Characteristics:** Fast, crisp, opacity-driven primarily
- **Estimated bezier:** `(0.6, 0.05, 0.25, 1.2)`
- **Confidence:** 🟡 Inferred
- **Source:** Observable in iOS 14+ Spotlight
- **Currently mapped:** `whooshSnapIn`
- **Notes:** Good match.

#### iOS Action Sheet
- **Where to observe:** iPhone → many apps → "More" or destructive action → sheet of buttons rises
- **Motion:** Similar to Share Sheet but with no overshoot — slides up and stops cleanly
- **Characteristics:** Asymmetric, no overshoot, decisive stop
- **Estimated bezier:** `(0.6, 0, 0.25, 1.0)`
- **Confidence:** 🟡 Inferred
- **Source:** HIG "Action Sheets"
- **Currently mapped:** None directly; closest is `opacitySmooth` or `whooshSnapIn` minus overshoot
- **Notes:** Library may benefit from a non-overshoot whoosh variant.

---

### 2. App Launch & Window Management

#### iOS App Icon Launch Zoom
- **Where to observe:** iPhone → tap any app icon → icon zooms forward as launch screen appears
- **Motion:** Icon scales up rapidly, slight overshoot, then resolves into app
- **Characteristics:** Energetic, scale-based, single subtle overshoot, ~350–400ms
- **Estimated bezier:** `(0.7, -0.1, 0.5, 1.3)`
- **Confidence:** 🟠 Approximated (spring-based in iOS)
- **Source:** WWDC 2017 "Designing Sound" mentions accompanying motion timing
- **Currently mapped:** `scaleOvershoot01` (0.7, -0.2, 0.6, 1.4)
- **Notes:** Library values slightly more aggressive than observed launch zoom. Candidate for tuning to (0.7, -0.15, 0.55, 1.35).

#### App Library Zoom Open (Folder Expand)
- **Where to observe:** iPhone → swipe to last Home Screen page → tap any folder grid → all 4 mini-apps zoom forward
- **Motion:** Folder contents scale up energetically as previous Home Screen recedes
- **Characteristics:** Fast scale + subtle position translation, energetic feel
- **Estimated bezier:** `(0.7, 0, 0.3, 1.4)`
- **Confidence:** 🟡 Inferred
- **Source:** iOS 14+ App Library
- **Currently mapped:** `whooshEnergetic` (0.7, 0, 0.3, 1.5)
- **Notes:** Library y2 = 1.5; observed closer to 1.4. Candidate for calibration.

#### macOS Window Minimize (Genie Effect)
- **Where to observe:** Mac → click yellow minimize button → window curves into Dock
- **Motion:** Window stretches downward into Dock following an S-curve path
- **Characteristics:** Unique to macOS; not pure bezier (it's a 2D mesh distortion)
- **Confidence:** 🟢 Documented (System Preference allows toggle between Genie and Scale)
- **Source:** macOS since Mac OS X 10.0 (Aqua)
- **Currently mapped:** Not directly applicable to web — keep noted as reference for spirit only
- **Notes:** Demonstrates Apple's preference for asymmetric, slightly playful motion in macOS.

---

### 3. Touch / Gesture Interactions

#### macOS Dock Magnification
- **Where to observe:** Mac → enable Dock magnification → drag cursor across Dock
- **Motion:** Icons scale up smoothly as cursor approaches, scale down as it passes
- **Characteristics:** Symmetric, smooth, no overshoot, position-driven not time-driven
- **Estimated bezier:** `(0.6, 0, 0.3, 1.1)` (when used as time-driven hover)
- **Confidence:** 🟡 Inferred
- **Source:** macOS Dock since Mac OS X 10.0 (Aqua)
- **Currently mapped:** `scaleSubtleBounce` (0.6, 0, 0.3, 1.1)
- **Notes:** Excellent match.

#### iOS Toggle Switch Flip
- **Where to observe:** iPhone → Settings → tap any toggle → thumb slides + color fills
- **Motion:** Thumb slides with mild overshoot at end; background color fills behind
- **Characteristics:** Position-based with subtle bounce, ~250–300ms
- **Estimated bezier:** `(0.6, 0, 0.3, 1.15)`
- **Confidence:** 🟡 Inferred
- **Source:** HIG "Toggles"
- **Currently mapped:** `scaleSubtleBounce`
- **Notes:** Good match.

#### iOS Pull-to-Refresh
- **Where to observe:** iPhone → Mail/Messages → pull down on top of list
- **Motion:** Spinner appears with elastic resistance; on release, list snaps back with mild overshoot
- **Characteristics:** Two-stage motion (resistance + release)
- **Estimated bezier:** Release stage ≈ `(0.5, 0, 0.2, 1.2)`
- **Confidence:** 🟡 Inferred
- **Source:** HIG "Refresh Content Controls"
- **Currently mapped:** Release-stage close to `whooshFloatSettle`
- **Notes:** Two-stage motion not fully capturable in single bezier.

---

### 4. Apple.com Marketing (Web)

#### Product Reveal Hero (iPhone, AirPods, Vision Pro pages)
- **Where to observe:** apple.com/iphone-16-pro/ → hero product image entrance on page load
- **Motion:** Product fades in while scaling slightly, with mild settle
- **Characteristics:** Cinematic, weighted, premium feel; ~600–800ms
- **Estimated bezier:** `(0.65, 0, 0.2, 1.15)`
- **Confidence:** 🟡 Inferred from inspecting Apple's CSS
- **Source:** Apple marketing site (live observation)
- **Currently mapped:** `whooshFloatSettle`
- **Notes:** Apple's marketing site uses a small set of repeated bezier curves; this is one of the most common.

#### Product Reveal Headline
- **Where to observe:** apple.com product pages → page headlines (e.g., "Pro. Beyond.")
- **Motion:** Word-by-word or letter-by-letter fade-in with slight upward translation
- **Characteristics:** Elegant, no overshoot, ~500ms per word
- **Estimated bezier:** `(0.5, 0, 0.3, 1.0)`
- **Confidence:** 🟢 Documented (inspectable in Apple's CSS)
- **Source:** Apple marketing site
- **Currently mapped:** `textElegantFadeIn` (0.5, 0, 0.3, 1.0)
- **Notes:** Excellent match. This library value is well-calibrated.

#### Scroll-Driven Product Animation
- **Where to observe:** apple.com/airpods-max → scroll through the page
- **Motion:** Product rotates and components separate as user scrolls; frame-bound, no easing per se
- **Confidence:** 🟢 Documented (this is what your scroll-driven-video skill builds)
- **Source:** Apple marketing site
- **Currently mapped:** Not an easing — handled by scroll-driven-video skill

---

### 5. Apple Watch & Wearables

#### Siri Orb Pulse
- **Where to observe:** Apple Watch → press Crown → say "Hey Siri" → animated orb appears
- **Motion:** Orb continuously pulses with breathing rhythm; no abrupt transitions
- **Characteristics:** Symmetric, slow, infinite loop, ~4s cycle
- **Estimated bezier:** `(0.4, 0.1, 0.25, 1.05)`
- **Confidence:** 🟡 Inferred
- **Source:** watchOS Siri interface
- **Currently mapped:** `floatSettleLoop` (0.4, 0.1, 0.25, 1.05)
- **Notes:** Identical values. Well-calibrated.

#### Now Playing Album Art Float
- **Where to observe:** Apple TV / iOS → playing music → Now Playing screen → album art floats subtly
- **Motion:** Continuous subtle vertical float, ambient
- **Characteristics:** Loop-safe, very gentle, no overshoot
- **Estimated bezier:** `(0.5, 0, 0.3, 1.1)`
- **Confidence:** 🟡 Inferred
- **Source:** tvOS / iOS Now Playing
- **Currently mapped:** `floatLoose`
- **Notes:** Good match.

---

### 6. visionOS Spatial Motion

#### visionOS Window Drag
- **Where to observe:** Apple Vision Pro → grab any window's bottom bar → move it through space
- **Motion:** Window floats with inertia; settles softly after release
- **Characteristics:** Strong damping, slight overshoot on settle, ~500ms decay
- **Estimated bezier:** `(0.65, 0, 0.2, 1.15)` (release-phase approximation)
- **Confidence:** 🟠 Approximated (spatial spring physics)
- **Source:** WWDC 2023 "Design for spatial user interfaces"
- **Currently mapped:** `whooshFloatSettle`
- **Notes:** Spatial motion is true 3D physics; bezier is only loose analog for the temporal feel.

#### visionOS Window Summon (open/close)
- **Where to observe:** Apple Vision Pro → open any app → window materializes
- **Motion:** Window scales up from a point with energetic feel, then settles
- **Characteristics:** Energetic, slight overshoot, ~400ms
- **Estimated bezier:** `(0.7, 0, 0.3, 1.4)`
- **Confidence:** 🟠 Approximated
- **Source:** WWDC 2023 "Design for spatial user interfaces"
- **Currently mapped:** `whooshEnergetic`
- **Notes:** Close match.

---

### 7. Communication Apps

#### iMessage "Slam" Effect
- **Where to observe:** iPhone → Messages → hold Send → tap "Slam" → send message
- **Motion:** Bubble flies in with strong overshoot, "slams" into place with bounce
- **Characteristics:** Strong overshoot, kinetic
- **Estimated bezier:** `(0.75, -0.25, 0.5, 1.5)`
- **Confidence:** 🟡 Inferred
- **Source:** iOS 10+ Messages effects
- **Currently mapped:** `scaleOvershoot02` (0.75, -0.25, 0.5, 1.5)
- **Notes:** Identical values. Well-calibrated.

#### iMessage "Gentle" Effect
- **Where to observe:** iPhone → Messages → hold Send → tap "Gentle"
- **Motion:** Bubble appears small, gently grows to full size
- **Characteristics:** Slow scale-up, no overshoot, breathing-like
- **Estimated bezier:** `(0.4, 0, 0.2, 1.0)`
- **Confidence:** 🟡 Inferred
- **Source:** iOS 10+ Messages effects
- **Currently mapped:** `opacitySmooth` (0.4, 0, 0.2, 1.0)
- **Notes:** Match on bezier values; library could note this as another anchor pattern.

---

## How Claude Should Use This File

### When self-extending (Mode C)
- ALWAYS read this file before proposing a new easing
- Find the Apple pattern matching the user's vibe in the **Quick Lookup: Motion Characteristic** table
- Use the documented bezier values as anchor points for the proposal
- Cite the specific pattern (with confidence level) in the proposal

### When calibrating (Mode D — see `library-calibration-protocol.md`)
- Walk through every library easing's entry in this file
- Compare current library values against this file's estimated bezier values
- Flag discrepancies for user review

### When the pattern isn't in this file
- Use web search (Apple HIG, WWDC, designer breakdowns) to find new patterns
- Document the finding in this file (after user approval)
- Cite the URL in the documentation

---

## How to Add New Entries

When web search reveals an Apple motion pattern not yet documented here:

1. Verify the source (prefer apple.com, developer.apple.com, or WWDC session pages)
2. Identify confidence level (Documented / Inferred / Approximated)
3. Use surgical `str_replace` edits to add the entry in the appropriate category section
4. Update the Quick Lookup tables at the top
5. Get user approval before adding

Never invent patterns. Never cite patterns Claude cannot verify exist.

---

## Calibration History

(This section tracks library-wide calibration events. Initially empty.)

```
YYYY-MM-DD: Calibration pass — adjusted [easings] based on [research findings]
```
