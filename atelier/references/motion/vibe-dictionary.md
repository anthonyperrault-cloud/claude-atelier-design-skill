# Vibe Dictionary — Descriptor Language → Easing

When the user uses vibe words instead of specifying an element type, consult this dictionary
first. If a vibe maps to multiple options, use the **primary**. If a vibe isn't found, run
the self-extension protocol.

---

## Direct Mappings

| Vibe word(s) | Primary Easing | Alternates | Reasoning |
|---|---|---|---|
| snappy, crisp, tight | `whooshSnapIn` | `opacitySnap` | Fast, clean stop |
| buttery, smooth, silky | `opacitySmooth` | `whooshFloatSettle` | Gentle, no sharp transitions |
| subtle, gentle, soft, mild | `scaleSubtleBounce` | `opacityFadeIn` | Refined, minimal energy |
| bouncy, playful, springy | `scaleOvershoot01` | `scaleOvershoot02` | Visible overshoot |
| elastic, rubber-band, stretchy, taffy | `scaleOvershoot02` | – | Strong overshoot |
| magnetic, snap-to, attracted, pulled | `scaleOvershoot01` | `whooshEnergetic` | Strong pull-to-target, slight overshoot on arrival |
| punchy, impactful, energetic, kinetic | `whooshEnergetic` | `scaleOvershoot01` | Fast, dramatic, hits hard |
| whip, flick, lash | `whooshEnergetic` | – | Strong initial acceleration |
| liquid, fluid, flowing, watery | `whooshFloatSettle` | `opacitySmooth` | No sharp edges, has weight |
| liquid glass, weighty fluid | `whooshFloatSettle` | – | Smooth flow + slight terminal settle |
| glass, crystalline, rigid, mechanical | `whooshSnapIn` | – | Quick, decisive |
| floaty, drifty, weightless, airy, ethereal | `floatLoose` | `floatSettleLoop` | Slow, light, ambient |
| premium, polished, refined, high-end | `textElegantFadeIn` | `whooshFloatSettle` | Apple's signature feel — calm, intentional |
| iOS-feel, Apple, native | `scaleSubtleBounce` | `whooshFloatSettle` | Default Apple system motion |
| elegant, graceful, dignified | `textElegantFadeIn` | – | Slow-ish, no overshoot, calm |
| smooth slide, glide | `opacitySmooth` | `whooshSnapIn` | Slow, no hops |
| cinematic, dramatic, hero | `whooshFloatSettle` | `whooshEnergetic` | Weighty, builds tension, lands intentionally |
| energetic entry, hype | `whooshEnergetic` | `scaleOvershoot01` | Dramatic, alive |
| calm, quiet, zen, meditative | `opacitySmooth` | `floatLoose` | Slow, ambient |
| precision, surgical, deliberate | `whooshSnapIn` | – | Sharp, no waste |
| ambient, breathing, alive | `floatSettleLoop` | `floatLoose` | Idle loops |

---

## Compound / Combination Vibes

Some vibes describe motion that uses **multiple easings on different properties** of the
same element. These are paired recommendations.

| Vibe | Property A | Property B | Notes |
|---|---|---|---|
| magnetic hover | `scale`: `scaleOvershoot01` | `translate`: `whooshSnapIn` | Element snaps toward cursor with slight overshoot |
| liquid glass card | `opacity`: `opacitySmooth` | `transform`: `whooshFloatSettle` | Card fades in while gliding into place |
| premium product reveal | `scale`: `whooshFloatSettle` | `opacity`: `textElegantFadeIn` | Hero-style entrance |
| toast snap-up | `translate`: `whooshSnapIn` | `opacity`: `opacitySnap` | Slide + fade together |
| modal hero open | `scale`: `scaleSubtleBounce` | `opacity`: `opacityFadeIn` | Standard Apple modal |
| floating ambient | `translate`: `floatSettleLoop` | (none) | Apply to translate only, loop |

---

## Vibes That May Need Self-Extension (no direct match — but check Apple first)

If the user uses any of these words **and the request is for a specific motion**, FIRST
examine Apple's motion patterns for inspiration before proposing anything new. Per the
self-extension protocol, you MUST cite a specific Apple usage pattern (iOS, macOS,
visionOS, apple.com) before proposing a new easing. If you can't find a clear Apple
reference, fall back to the closest existing easing.

- iridescent, shimmer, prismatic — check Apple Watch dynamic faces, Vision Pro UI shimmer
- morphic, shapeshifting — check iOS app icon transitions, Stage Manager window morphs
- gravity, falling, dropping — check iOS Control Center pull-down, multitasking dismiss
- breathes, alive, ambient pulse — check Siri orb, Now Playing animations, Home Screen idle

## Vibes That Are NOT Apple — Reject and Reframe

These vibes describe motion that sits **outside** Apple's motion vocabulary entirely. Do
not propose new easings for these. Instead, redirect the user toward the closest
Apple-compatible interpretation:

- frantic, chaotic, jittery, violent, manic — Apple motion is always deliberate and contained
- bounce-house, trampoline, ricochet, ping-pong — Apple uses single contained overshoot, not multi-bounce
- cartoonish, exaggerated elastic — Apple's overshoot is subtle (y2 ≤ 1.5), never theatrical
- glitch, broken, error-jitter — Apple uses subtle shake (CSS keyframes), not easings

When the user uses one of these, respond:
> "[vibe] sits outside Apple's motion language — Apple's curves are deliberate and contained, even when energetic. The closest Apple-friendly interpretation would be [closest easing], which gives you [characteristic]. Want that, or want to describe what you're after differently?"

---

## Vibes to Reject or Reinterpret

Some vibe words are about **non-motion** qualities. Don't propose easings for these without
clarification:

- glowing, luminous → about color/lighting, not motion
- transparent, ghostly → about opacity value, not opacity timing
- vibrant, saturated → about color
- minimalist, clean → about visual design
- modern, contemporary → too vague; ask for specifics

When the user uses one of these, respond:
> "That sounds like a [color/typography/visual] concern more than a motion concern. Did you mean to ease the motion of this element, or are you asking about its appearance?"

---

## How to Use This Dictionary

1. User uses a vibe word
2. Search the **Direct Mappings** table — case-insensitive, partial match OK
3. If found → use the primary easing (or alternate if context suggests it)
4. If multiple properties animate → check **Compound Vibes** for paired recommendations
5. If listed in **Self-Extension Needed** → propose a new easing
6. If listed in **Reject or Reinterpret** → ask the user to clarify

---

## Self-Extension Updates

When the self-extension protocol adds a new vibe word + easing pairing, append the row to the
**Direct Mappings** table. Use surgical `str_replace` edits — never rewrite this file.
