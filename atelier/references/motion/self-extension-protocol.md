# Self-Extension Protocol

How to grow the easing library when a user request can't be served by the existing 14
easings. Follow these steps in order. **Never modify the skill files without explicit user
approval.**

---

## CRITICAL: Stay in Apple's Motion Vocabulary

This entire skill exists to produce **Apple-style** motion. Every easing — baseline or
self-extended — must live within Apple's motion language. This means:

- Generated curves are bounded by Apple's actual motion characteristics
- New easings must reference a specific Apple usage pattern they're modeled on
- If Claude can't name an Apple pattern that fits the requested vibe, **fall back to the
  closest existing library easing** — do not invent freely

Apple's motion vocabulary (across iOS, macOS, visionOS, and apple.com product reveals)
has consistent characteristics. **Stay inside this envelope:**

| Characteristic | Apple's range |
|---|---|
| Total duration | 200ms (microinteractions) – 800ms (hero reveals) |
| Overshoot magnitude | Subtle (y2 = 1.05–1.2) to moderate (y2 = 1.3–1.5). **Rarely** beyond 1.5. |
| Undershoot | Slight (y1 = -0.1 to -0.25). Apple uses this for icon pops and toggle switches. |
| Acceleration profile | Almost always asymmetric, biased toward fast-out / slow-in (`x1` low, `x2` low-to-mid) |
| Loops | Subtle, breath-like. y2 ≤ 1.1, no harsh transitions. |
| Sharp linear motion | Almost never — Apple avoids hard `ease-in`, `ease-out`, or `linear` |

**Anti-patterns** (NOT Apple — never propose these):
- Heavy multi-bounces (Apple uses single, contained overshoot)
- Cartoonish elastic (rubber-banding that overshoots 50%+)
- Mechanical/robotic timing (perfectly linear, sharp instant stops)
- "Frantic" jittery motion (Apple never does this)
- Sudden direction reversals mid-curve

---

## When to Trigger Self-Extension

Run this protocol when **ALL** of these are true:

1. The user's vibe language isn't in `vibe-dictionary.md` (and isn't in the "Reject" list)
2. After examining how Apple uses motion that could fit the vibe, no existing library
   easing is close enough (defined as: within 0.1 on every bezier parameter)
3. The motion characteristics the user wants **fit inside Apple's envelope** above

**Do NOT trigger self-extension when:**
- An existing easing is within Apple's interpretation of the vibe (offer that instead)
- The vibe is in the "Reject or Reinterpret" list — clarify with the user
- The user used a vibe word once and the existing library has a close match
- **The requested motion is fundamentally not Apple** (e.g., "frantic", "chaotic",
  "cartoonish bounce", "jittery", "violent shake"). In that case respond:

  > "That feel sits outside Apple's motion language — Apple's curves are deliberate and
  > contained, even when energetic. The closest Apple-friendly interpretation of [vibe]
  > would be [existing easing], which gives you [characteristic]. Want that, or should we
  > talk about what specifically about [vibe] you're after?"

---

## Step 1: Apple Reference Check (MANDATORY GATE)

Before doing anything else, examine the vibe against Apple's actual motion vocabulary.
This step has three outcomes — only one of them allows proceeding to a new easing.

### 1a. Find the closest Apple pattern — use the Reference Library first

**ALWAYS read `references/apple-motion-reference.md` first.** It contains the curated
catalog of observable Apple motion patterns with documented sources. Use the **Quick
Lookup: Motion Characteristic → Apple References** table to find patterns matching the
vibe.

If the reference library has a matching pattern, use it as your citation. Note the
confidence level (🟢 Documented / 🟡 Inferred / 🟠 Approximated).

### 1b. Web search if the pattern isn't in the reference library

If the user's vibe relates to a feature not covered in `apple-motion-reference.md` (e.g.,
a recently-released iOS feature, visionOS 2 motion, iOS 26 Liquid Glass), use web search.

Effective search queries:
- `WWDC [current year] [feature] spring animation`
- `apple [feature name] motion design`
- `iOS [version] [feature] cubic-bezier`
- `SwiftUI .spring [feature] response damping`

Capture:
- The exact URL
- Spring parameter values if mentioned (response, dampingFraction, mass)
- Cubic-bezier values if cited
- WWDC session numbers

After the conversation, if findings are credible, add a new entry to
`apple-motion-reference.md` via surgical edits (after user approval).

### 1c. Use Physics Translator if spring values are available

If you found documented spring parameters (e.g., from WWDC: "response: 0.4,
dampingFraction: 0.85"), use `references/physics-translator.md` to translate to bezier
AND linear() format. This gives you anchor values for the proposal that are
physics-grounded, not guesses.

### 1d. Match characteristics from that Apple pattern

What are the motion characteristics of the Apple reference?
- Duration range Apple uses for it
- Whether it has overshoot, undershoot, or neither
- Whether it's asymmetric (fast-out / slow-in is typical)
- Whether it loops or is terminal
- Spring parameters if documented

### 1e. Compare to existing library easings

Walk through every easing in `easing-tokens.md` and ask: which one is closest to the
characteristics you just identified from the Apple reference?

**"Close enough" means: within 0.1 on every bezier parameter.**

### 1f. Decide the path forward (three outcomes)

**Outcome A — Existing easing matches:** Stop. Don't propose a new easing. Tell the user:
> "[vibe] in Apple's motion language corresponds to how they animate [Apple reference].
> The closest match in your library is `[existingEasingName]`. Want me to apply that?"

**Outcome B — No Apple reference fits the vibe:** Stop. Don't propose a new easing. Tell the user:
> "[vibe] sits outside Apple's motion language — Apple's curves are deliberate and
> contained, even when energetic. The closest Apple-friendly interpretation would be
> `[closestExistingEasing]`, which gives you [characteristic]. Want that, or do you want
> to describe what specifically about [vibe] you're after so I can find a better Apple
> match?"

**Outcome C — Apple reference exists AND no existing easing is close:** Proceed to Step 2.
You may propose a new easing, but it MUST cite the Apple reference pattern from 1a-1b in
the proposal AND include physics translation if spring values are documented.

---

## Step 2: Decompose the Vibe

Break the descriptor into motion characteristics. Ask yourself:

| Characteristic | Question |
|---|---|
| Start velocity | Does it accelerate from rest, or start with momentum? |
| End velocity | Does it stop sharply, or coast to a halt? |
| Overshoot | Does the motion pass its target and come back? |
| Undershoot | Does it pull back before launching forward? |
| Symmetry | Is the acceleration profile symmetric, or front/back-loaded? |
| Loopability | Is this motion repeating, or single-shot? |
| Duration feel | Should the curve fit a short (200–300ms), medium (400–500ms), or long (600–800ms) duration? |

Write out your interpretation explicitly so the user can verify.

---

## Step 3: Propose Cubic-Bezier Values

Generate `(x1, y1, x2, y2)` values that match the characteristics from Step 2 AND stay
inside Apple's motion envelope (see "Stay in Apple's Motion Vocabulary" above). Show your
reasoning AND cite the Apple reference pattern from Step 1a.

### Guidelines for choosing values

**The x values** (`x1`, `x2`) control horizontal positioning of the control points and
shape the velocity profile:
- `x1` low + `x2` low → slow start, slow middle, fast end
- `x1` low + `x2` high → slow start, fast middle, slow end (classic ease-in-out)
- `x1` high + `x2` low → fast start, slow middle, fast end (uncommon, weird)
- `x1` high + `x2` high → fast start, fast middle, slow end

**The y values** (`y1`, `y2`) control how aggressively the curve approaches its endpoints:
- `y1 < 0` → undershoot (pulls back before launching)
- `y1` between 0 and 1 → normal acceleration
- `y2 > 1` → overshoot (passes target then returns)
- `y2` between 0 and 1 → normal deceleration

### Common patterns
- Snappy (`whooshSnapIn` family): x1 ~0.6, y1 ~0–0.1, x2 ~0.25, y2 ~1.1–1.3
- Smooth (`opacitySmooth` family): x1 ~0.4, y1 = 0, x2 ~0.2, y2 = 1
- Overshoot (`scaleOvershoot` family): x1 ~0.7, y1 ~-0.2, x2 ~0.5, y2 ~1.4–1.5
- Subtle bounce (`scaleSubtleBounce`): x1 ~0.6, y1 = 0, x2 ~0.3, y2 ~1.1
- Float (`float*` family): symmetric x values (0.4–0.5), small overshoot (y2 ~1.05–1.1)

### Output format

```
Proposed easing for "[vibe word]":

Apple reference: <specific Apple pattern this is modeled on, e.g.,
                  "iOS Home Screen icon idle breathing animation">
Name: <camelCaseName>
Values: (x1, y1, x2, y2)
Category: <Whoosh | Scale | Text | Opacity | Float | Other>

Why this matches Apple's pattern:
- <characteristic 1> → <how the bezier value achieves it, citing the Apple reference>
- <characteristic 2> → <how>
- ...

Within Apple's motion envelope:
- Overshoot: <value, within 1.0–1.5 range>
- Undershoot: <value, within 0 to -0.25 range or N/A>
- Duration target: <range, within 200–800ms>

Recommended use cases: <element types this fits>
```

---

## Step 4: Pause for User Approval

Show the user the proposal with **exactly these 4 options**:

```
Should I:
  1. Add '<easingName>' to the library permanently and apply to your element
  2. Apply this curve as a one-off (don't save to library)
  3. Try different values
  4. Suggest an existing easing instead
```

**Wait for explicit choice.** Do not proceed without it.

---

## Step 5: If User Chose Option 1 (Permanent Add)

Update the skill library files. Use **surgical edits only** — `str_replace` style, never
rewrite a file from scratch. The user has built up content over time; preserve all of it.

### File 1: `references/easing-tokens.md`

Add to FIVE sections in this exact order:

**a) The library table** — find the row matching the new easing's category. Insert a new
row in alphabetical order within that category section:
```
| `<easingName>` | <Category> | `<x1>, <y1>, <x2>, <y2>` | <use case description> |
```

**b) CSS Custom Properties block** — find the matching category comment (e.g., `/* Whoosh / Entry */`).
Insert a new line in alphabetical order:
```
  --ease-<kebab-case-name>: cubic-bezier(<x1>, <y1>, <x2>, <y2>);
```

**c) TypeScript constants** — add to BOTH `easings` and `easingsCSS` objects in alphabetical
order within their category section:
```ts
  <camelCaseName>: [<x1>, <y1>, <x2>, <y2>],
```
and:
```ts
  <camelCaseName>: 'cubic-bezier(<x1>, <y1>, <x2>, <y2>)',
```

**d) Tailwind Config** — add a new entry in `transitionTimingFunction`:
```
        '<kebab-case-name>': 'cubic-bezier(<x1>, <y1>, <x2>, <y2>)',
```

**e) GSAP CustomEase registration** — add a new line:
```js
CustomEase.create('<camelCaseName>',  '<x1>, <y1>, <x2>, <y2>');
```

### File 2: `references/vibe-dictionary.md`

Add to the **Direct Mappings** table:
```
| <vibe word(s)> | `<easingName>` | – | <reasoning> |
```

Insert in alphabetical order. If multiple vibe words triggered the extension, add them
all comma-separated in column 1.

If the vibe was previously in the "Self-Extension Needed" list, REMOVE it from that list.

### File 3: `references/element-to-easing-map.md`

If the new easing fits a specific UI pattern that's already in the **Pattern → Easing
Recommendations** table, add it as an "Alternate" with a "When alternate fits" note. Don't
replace existing primary recommendations.

If the new easing represents a new pattern entirely, add a row to both the **Detection
signals** and **Pattern → Easing Recommendations** tables.

### File 4: `SKILL.md`

No edits needed in most cases. Only update if:
- The new easing introduces a brand-new category (very rare)
- The trigger language section needs new vibe words added

---

## Step 6: Apply to the User's Code

Use the newly-added easing on the element that triggered the extension. Use the format
appropriate to the user's stack (see `easing-tokens.md`).

---

## Step 7: Confirm and Report

Tell the user:

```
✅ Added '<easingName>' to your easing library.
   Modeled on: <Apple reference pattern>
   Files updated:
   - references/easing-tokens.md (5 sections)
   - references/vibe-dictionary.md (vibe entry)
   - [references/element-to-easing-map.md, if applicable]

✅ Applied to <element/file>.

This easing is now permanent — future projects will have it too.
```

---

## Quality Bar for New Easings

To prevent library bloat AND keep the library Apple-coherent, hold proposed easings to
this bar. **If any of these fail, do NOT propose — fall back to an existing easing.**

1. **Apple-grounded** — must cite a specific Apple usage pattern (from Step 1a) that this
   easing is modeled on. "It feels Apple-ish" is not sufficient. Name the iOS / macOS /
   visionOS / apple.com feature it draws from.

2. **Inside Apple's motion envelope** — values fit within Apple's documented ranges:
   - Overshoot: y2 ≤ 1.5 (never beyond)
   - Undershoot: y1 ≥ -0.25 (never beyond)
   - No "frantic," "chaotic," or "violent" curves regardless of user vibe language

3. **Distinctive** — must produce visibly different motion from existing easings. If the
   proposed curve is within ~0.1 of all existing curves on every parameter, suggest using
   the closest existing easing instead.

4. **Named meaningfully** — name describes the motion or its use case, not arbitrary
   (e.g., `magneticPull` is good; `easing15` is bad).

5. **Justifiable** — the reasoning in Step 3 must connect the Apple reference to specific
   bezier values, not handwave.

6. **Loop-safe if Float-category** — easings added to Float must have `y2 ≤ 1.15` and
   avoid undershoot, since they'll be used in repeating contexts.

7. **Text-safe if Text-category** — easings added to Text must have `y1 ≥ 0` and `y2 ≤ 1.0`
   (no overshoot, no undershoot) to avoid text jitter.

If a proposed easing doesn't meet the bar, fall back to suggesting the closest existing
easing instead. **It is better to leave the library at 14 easings than to add one that
drifts from Apple's language.**

---

## What NOT to Do

- Don't generate easings for non-motion vibes (color, layout, typography)
- Don't generate easings for vibes outside Apple's motion language (frantic, chaotic, cartoonish, violent, jittery)
- Don't propose any new easing without citing a specific Apple usage pattern it's modeled on
- Don't add the same bezier values under multiple names
- Don't rewrite reference files — only surgical edits
- Don't bypass user approval — even for "obvious" additions
- Don't add easings to categories where they technically don't belong (a wild overshoot
  isn't a Text easing just because the user used it on text)
- Don't lower the Apple envelope bar to satisfy a request — fall back to existing easings instead
