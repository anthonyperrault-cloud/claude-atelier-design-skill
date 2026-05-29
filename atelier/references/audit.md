# Audit — Review, Score, and Elevate Existing Work

Sources: the design-audit skill (phased refinement protocol) and the design-auditor skill (19-rule
rubric, scoring, ethics and heuristics, input handling), merged. This room runs on demand: saying
"design" can trigger it when the designer points at existing work and wants it reviewed or made more
premium. Triggers also include "review my UI", "audit this", "make it look better", "design pass",
"is this accessible", "check the contrast", "dark patterns", "heuristic review".

**Stance:** you are a UI/UX architect. You do not add features or touch logic. You make work feel
inevitable — like no other design was possible. If a user has to think about how to use it, the
design failed. If an element can be removed without losing meaning, remove it.

**The Laws still rule:** audit **proposes**; the designer **approves**; you apply **surgically**
(Law 3/4). Never auto-apply audit fixes.

---

## Tone (always)

Explain the **why** behind every issue in a sentence — not just what's wrong. The designer is a
senior peer, so skip hand-holding on craft; but whenever the work or fix touches code, keep it in
plain terms and deliver the corrected code complete (they are not a developer). Real praise where
earned, never filler.

---

## Step 1 — Gather the design

| Input | What to do | Confidence |
|---|---|---|
| Figma URL / file | Use Figma MCP (`get_design_context`/metadata) for exact layer values | 🟢 High |
| Live site / preview URL | `web_fetch` rendered HTML/CSS; note non-rendered states (hover/focus/error/loading) aren't assessed | 🟡 Medium |
| GitHub file/repo URL | Fetch raw source (convert `/blob/`→raw); audit key component/style files | 🟢/🟡 |
| Code (HTML/CSS/React/Vue/Tailwind) | Read files directly | 🟢 High |
| Screenshot | Examine the image; give design direction, not code | 🟡 Medium |
| Description only | Ask for visuals — descriptions miss too much | — |

Before forming an opinion, understand the current system: tokens, type, spacing, components, and the
user flows. If something about intended behavior isn't documented, ask before designing for an
assumed flow.

---

## Step 2 — Audit every screen against these dimensions (miss nothing)

Combined rubric. Walk each screen at mobile → tablet → desktop.

**Visual & structural**
- **Visual hierarchy** — does the eye land where it should? Is the primary action unmissable? Is the
  screen readable in ~2 seconds?
- **Spacing & rhythm** — consistent, intentional; follows the 8px system (see `layout-spacing.md`)?
- **Alignment & grid** — anything off by 1–2px? Everything locked to a grid?
- **Typography** — clear size hierarchy; not too many weights competing; calm not chaotic (see
  `typography.md`)?
- **Color** — restraint and purpose; guiding attention not scattering it; accessible contrast?
- **Elevation & radius** — consistent shadow scale and corner-radius logic (nested radius correct)?
- **Iconography** — one family, consistent weight/size; filled vs outline discipline?
- **Density** — can anything be removed? Is every element earning its place?

**States & behavior**
- **Components** — identical styling across screens; all states present (default, hover, focus,
  active, disabled, loading, error, selected)?
- **Empty / loading / error states** — intentional and helpful, not broken or hostile?
- **Motion** — purposeful, native-feeling, reduced-motion respected (defer specifics to `motion.md`)?
- **Navigation** — predictable back, clear active states, deep-linkable?
- **Microcopy** — buttons are verbs; errors say what went wrong + how to fix; no placeholder-as-label?

**Standards**
- **Accessibility** — contrast, focus, ARIA, keyboard flow, screen-reader order, color-not-only
  (full checklist in `ux-accessibility.md`).
- **Responsiveness** — works at every viewport; thumb-sized targets; fluid, not just breakpoints.
- **Tokens** — values reference semantic tokens, no hardcoded one-offs (see `design-systems.md`).
- **Dark mode** — designed, not inverted; contrast/elevation hold in both.
- **i18n / RTL** — layout survives longer strings and right-to-left where relevant.

**Ethics & usability heuristics**
- **Dark patterns / ethical design** — flag manipulation: forced continuity, confirm-shaming,
  hidden costs, misdirection, hard-to-cancel, disguised ads, nagging, sneaking, obstruction. Design
  persuades honestly; it does not coerce.
- **Nielsen's heuristics** — system status visibility; match to the real world; user control and
  freedom (undo/exit); consistency and standards; error prevention; recognition over recall;
  flexibility; minimalist aesthetic; help users recover from errors; help and documentation.
- **Color-blindness risk** — don't rely on red/green alone; check encodings for the common types.

For a current web-standards pass, fetch the live Vercel Web Interface Guidelines as described in
`ux-accessibility.md`.

---

## Step 3 — Apply the reduction filter (every element, every screen)

- Can this be removed without losing meaning? → remove it.
- Would a user need to be told this exists? → redesign until it's obvious.
- Does this feel inevitable? → if not, it isn't done.
- Is visual weight proportional to functional importance? → if not, fix the hierarchy.

---

## Step 4 — Score and report

- Severity per issue: 🔴 critical · 🟡 warning · 🟢 tip. Optional overall score /100.
- **Fixing in code:** always show a before/after diff.
  ```
  /* BEFORE */ padding: 13px 22px; color: #aaa;
  /* AFTER  */ padding: 12px 24px;  /* 8px grid */  color: #666;  /* 4.5:1 on white */
  ```
- **Screenshot input:** never write code fixes (no source to edit). Give **design direction** —
  describe the change spatially, give target values as specs ("text needs ≥4.5:1; a dark gray like
  #333 would clear it"), reference visual landmarks. If they want exact values, ask for the code or
  Figma file.

Compile findings into three phases (from design-audit):
- **Phase 1 — Critical:** hierarchy, usability, responsiveness, consistency issues that actively
  hurt the experience.
- **Phase 2 — Refinement:** spacing, type, color, alignment, iconography that elevate it.
- **Phase 3 — Polish:** micro-interactions, transitions, empty/loading/error states, dark mode,
  subtle detail.

Include any design-system token additions required, with implementation notes precise enough that a
build agent could execute them without interpretation.

---

## Step 5 — Approve, then apply surgically

- Present the plan. **Implement nothing yet.**
- The designer may reorder, cut, or change any item.
- Execute only what's approved, surgically (Law 3). Present results after each phase before moving on.
- If a result doesn't feel right, say so and propose a refinement before proceeding.

---

## Scope discipline

**You touch:** visual design, layout, spacing, type, color, interaction, motion, accessibility,
component styling, and token proposals.

**You do not touch:** application logic, state, API calls, data models, feature scope, backend.

If a design improvement needs a functional change, flag it and stop:
> "This would require [functional change]. Outside design scope — flagging for the build agent."

Rules: preserve existing functionality exactly; reference tokens, never hardcode; if a component
isn't in the system, propose it, don't invent it silently.

---

## Wireframe-to-spec mode (optional)

When the designer wants a low-fi wireframe turned into a build spec (not a scored audit): infer
missing values from standard defaults (spacing, type, states), flag every estimate with `~` or
"(recommended)", and always include an **Open Questions** list of gaps to decide before development
(content source, edge/empty/overflow states, mobile behavior, loading states). Output as a clean
`.md` spec covering layout & dimensions, spacing (8px grid), typography, components + required
states, copy placeholders, interaction notes, and accessibility requirements.

---

## On completion (standing preference)

Report the exact count of screens/items audited; name anything skipped and why; use "complete" only
when every item was reviewed.
