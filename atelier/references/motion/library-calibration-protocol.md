# Library Calibration Protocol

How to audit the existing 14 (or more) library easings against current Apple motion
research and propose physics-grounded corrections. Triggered when the user wants to
re-verify the library is still Apple-coherent — especially after new iOS/macOS/visionOS
versions ship with updated motion language.

---

## When to Trigger

Run this protocol when the user says:
- "Calibrate my easings"
- "Audit my library against current Apple motion"
- "Make sure my easings still match Apple"
- "Update my library for iOS 26" (or any new OS version)
- "My library is old — refresh it against current Apple research"

Also recommended (but not auto-triggered) on:
- Initial install of this skill on top of a pre-existing library
- After major Apple OS releases (new iOS, macOS, visionOS major versions)

**Do NOT auto-trigger this protocol during other workflows.** Calibration changes the
user's library tokens — only run when explicitly requested.

---

## Pre-flight

Before scanning, confirm with the user:

```
LIBRARY CALIBRATION

I'll audit all 14 easings in your library against:
- Documented Apple spring presets (SwiftUI .smooth, .snappy, .bouncy, etc.)
- WWDC session content
- The Apple Motion Reference Library (references/apple-motion-reference.md)
- Live web search for any patterns not covered above

For each easing, I'll show you:
- Current values
- Apple research findings
- Whether the current values match research, or need calibration
- Proposed adjustments (with reasoning)

Nothing will be changed until you approve each finding individually.

Ready to start?
```

Wait for explicit confirmation before proceeding.

---

## Workflow

### Step 1: Read the current state

Read both:
- `references/easing-tokens.md` — current bezier values for all 14 easings
- `references/apple-motion-reference.md` — currently-mapped Apple references for each

### Step 2: For each easing, gather evidence

Walk through each easing one at a time. For each, run this sub-procedure:

**2a. Identify Apple reference patterns**
Look up which Apple patterns this easing is currently mapped to (from
`apple-motion-reference.md`).

**2b. Check for documented spring values**
- Is this pattern's spring preset documented? (Check WWDC, SwiftUI docs)
- If yes, note the spring parameters (response, dampingFraction)

**2c. Web search if needed**
Always web search if:
- The mapped Apple pattern is post-iOS 17 / post-visionOS 1.0 (because library may predate this)
- The pattern is associated with a newer feature (iOS 26 Liquid Glass, visionOS 2 spatial UI, etc.)
- The reference library has confidence level "Approximated" (uncertain values worth verifying)
- No spring preset is documented but the motion is well-known

Search queries:
- `WWDC [current year] [feature] spring animation`
- `apple [feature name] motion timing`
- `iOS [version] [feature] cubic-bezier`
- `SwiftUI .spring [feature]`

Capture URLs for citation.

**2d. Translate to bezier and linear()**
Using `references/physics-translator.md`:
- Translate the spring values to cubic-bezier
- Translate to linear() for higher-fidelity overshoot motion
- Note any uncertainty in the translation

**2e. Compare to current library values**
Apply the threshold from `physics-translator.md`:
- Any single parameter differs by more than 0.1 → flag
- Multiple parameters differ → higher-priority flag
- Within threshold → "well-calibrated, no change needed"

### Step 3: Compile findings table

Build a complete table before proposing any changes:

```
LIBRARY CALIBRATION FINDINGS

✅ Well-calibrated (no change needed): 6 easings
  - whooshFloatSettle (0.65, 0, 0.2, 1.2) — matches iOS Share Sheet spring
  - textElegantFadeIn (0.5, 0, 0.3, 1.0) — matches Apple.com headline easing
  - scaleSubtleBounce (0.6, 0, 0.3, 1.1) — matches macOS Dock magnification
  - floatSettleLoop (0.4, 0.1, 0.25, 1.05) — matches Siri orb pulse
  - ... etc

🟡 Minor drift (within Apple's range, but tightenable): 3 easings
  - whooshSnapIn (0.6, 0.05, 0.25, 1.2) — Control Center pull suggests 1.1; small tightening recommended
  - ... etc

🔴 Significant drift (does not match current Apple motion): 2 easings
  - scaleOvershoot01 (0.7, -0.2, 0.6, 1.4) — App icon launch uses (0.45, 0.0, 0.2, 1.1) per WWDC 2023 Session 10158
  - scaleOvershoot02 (0.75, -0.25, 0.5, 1.5) — iMessage Slam uses (0.5, 0.0, 0.25, 1.25) per recent research
  - Both significantly more aggressive than current Apple motion

🆕 Missing patterns (no library easing exists for these): 2
  - iOS 26 Liquid Glass material motion (response: 0.6, dampingFraction: 0.75)
  - visionOS window resize haptic-coupled motion (response: 0.3, dampingFraction: 0.9)
```

### Step 4: Pause for review

**Do not modify anything yet.** Present the full findings table and ask:

```
How would you like to proceed?
  1. Apply all recommended calibrations (✅ skips, 🟡 applies tightenings, 🔴 applies corrections)
  2. Review each finding individually and decide one at a time
  3. Only apply the 🔴 significant-drift corrections (most important)
  4. Don't change anything yet — I want to think about it
```

### Step 5: For each approved change

Apply via surgical str_replace edits to `easing-tokens.md`:

**5a. Update the bezier value**
Replace the value in the main library table.

**5b. Update CSS custom property**
Replace the cubic-bezier() in the CSS block.

**5c. Update TypeScript constants**
Replace in both `easings` object (array form) and `easingsCSS` object (string form).

**5d. Update Tailwind config entry**
Replace in transitionTimingFunction.

**5e. Update GSAP CustomEase registration**
Replace the values string.

**5f. If linear() variant is being added**
Append a new section to `easing-tokens.md` titled "## linear() Variants (Modern Spring Fidelity)" if it doesn't exist. Add the new linear() value with a comment showing both the bezier fallback and the spring source.

Example:

```css
/* iOS app icon launch — spring(.snappy) from WWDC 2023 */
--ease-scale-overshoot-01-linear: linear(0, 0.144, 0.466, 0.764, 0.949, 1.029, 1.030, 1.008, 1);
```

**5g. Update apple-motion-reference.md**
- Update "Currently mapped" note if values changed
- Update confidence level if web search upgraded it (Approximated → Inferred → Documented)
- Add new spring parameters to the entry if discovered

**5h. Log to calibration history**
Append to the Calibration History section of `apple-motion-reference.md`:

```
YYYY-MM-DD: Calibrated [easingName] from (old values) to (new values).
  Source: [WWDC session / URL / observation]
  Reason: [brief explanation, e.g., "Library predated SwiftUI spring preset publication"]
```

### Step 6: Final report

After all approved changes are applied:

```
CALIBRATION COMPLETE

✅ Calibrated: [N] easings
🆕 New linear() variants added: [N]
📚 Apple Motion Reference Library updated: [N] new entries
📝 Calibration history logged

Files modified:
  - references/easing-tokens.md
  - references/apple-motion-reference.md

Your library is now calibrated against:
  - SwiftUI spring presets (WWDC 2023 Session 10158)
  - [Other research sources cited]

Recommendation:
  - Test the calibrated easings in your existing projects
  - Some motion will feel subtly different — that's expected
  - If anything feels off, you can revert individual easings using git
    or by referring to the calibration history log
```

---

## Conservative Defaults

To prevent accidental motion-feel changes across the user's projects:

1. **Default to keeping existing values** when discrepancy is within 0.1 (the threshold).
   Small drift is fine.

2. **Preserve user-authored easings** (those added via self-extension after the initial 14)
   with extra scrutiny. The user may have tuned them deliberately.

3. **Never collapse easings** that have similar values. If `whooshFloatSettle` and
   `whooshSnapIn` end up close after calibration, keep them separate — they have
   different semantic meanings.

4. **Flag, don't replace, ambiguous cases**. If multiple Apple patterns could be the
   reference for an easing, list all options and let the user choose.

5. **Respect "Apple-friendly but not Apple-faithful" intent**. If the user originally
   tuned an easing for their own brand on top of Apple's vocabulary, calibration should
   surface the option but not force it.

---

## Special Case: New Apple OS Released

When the user mentions a recent Apple OS release (e.g., "iOS 26 just shipped, recalibrate"):

1. Start with web search for `WWDC [year] motion design` and `iOS [version] animation`
2. Build a "what's new in motion" summary before scanning the library
3. Identify patterns that are NEW or CHANGED in this release
4. For each NEW pattern, propose adding it to `apple-motion-reference.md`
5. For each CHANGED pattern, check if any library easing maps to it and flag for calibration
6. Run the standard calibration workflow above

This is more involved than standard calibration but produces a library that's current
with the latest Apple motion language.

---

## What This Protocol Does NOT Do

- Does not change durations, delays, keyframes, or animated properties (out of scope)
- Does not modify any code outside the `apple-easings/` skill folder
- Does not touch user project code without going through Mode A or Mode B workflows
- Does not auto-apply changes without explicit user approval
- Does not delete easings (only adjusts values or adds new ones)
