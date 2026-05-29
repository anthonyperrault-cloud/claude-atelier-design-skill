# atelier

> *Master design skill for Claude Code. One set of laws, many rooms.*

---

## What It Is

**atelier** is a Claude Code skill built for working designers — specifically, senior product designers who use AI as a daily collaborator and need that collaborator to stay on brief, stay out of the way aesthetically, and never bloat a file uninvited.

It is not a prompt. It is not a style guide. It is a governing system: a master skill that houses 15 distilled design frameworks under a single set of non-negotiable operating laws, so every Claude Code session — whether you are designing a component, writing a headline, auditing a layout, or adding motion to a build — runs through the same disciplined spine.

Invoke it by saying "design," or by describing anything visual. It runs at the start of a project, the middle, and the end. It lives inside subagents. It pairs with other skills. And whatever else loads in a session, its laws win.

---

## The Inspiration

The problem is not that AI is bad at design. The problem is that AI is *too* confident about design.

Left unchecked in a Claude Code session, the model will pick your fonts, choose your palette, redesign the component you only asked it to adjust, add animation nobody requested, and call it polish. It means well. It is also wrong. A senior designer with nine-plus years of systems, brand, and motion work does not need an AI art-directing the session. They need an AI that executes the brief — precisely, surgically, with craft — while the human holds the aesthetic judgment.

The solution came from Andrej Karpathy's observations on LLM coding behavior. His guidelines — think before coding, simplicity first, surgical changes, goal-driven execution — were written to stop AI from over-engineering software. The same failure mode applies to design: over-designing, over-polishing, taking liberties with scope. The karpathy guidelines, transplanted into a design context and placed *above* every other skill in the session, become a governor. A gravity. The thing that keeps the creative energy channeled instead of sprawling.

atelier was built around that insight. The karpathy guidelines are the sun. Everything else orbits it.

The museum metaphor shaped the rest of the architecture. A governing skill is the building. The craft frameworks — typography rules, spacing method, motion easing, UX standards, copy principles, design system architecture, audit protocol — are the rooms. Each room holds a specific discipline, distilled from the best skill available for that domain. Walk into the right room when you need it. The governor keeps the doors from swinging open on their own.

The skill was also built with a specific human in mind: a designer with ADHD who does not write code, who owns their aesthetic choices and does not need the AI selecting fonts or suggesting color palettes, and who needs every response optimized for cognitive ease — short, scannable, one idea at a time, answer first.

---

## Architecture

```
atelier/
├── SKILL.md                          The governor. 
│                                     Holds the Laws, the designer context,
│                                     invocation triggers, and the routing map.
└── references/
    ├── karpathy-guidelines.md        The original Karpathy guidelines, verbatim.
    │                                 Prevents over-coding and file bloat.
    ├── governance.md                 The Laws translated into design language.
    ├── design-philosophy.md          Creative direction, aesthetic vocabulary,
    │                                 core principles, when to break the rules.
    ├── design-systems.md             Token architecture (primitive → semantic →
    │                                 component), component specs, state matrices.
    ├── typography.md                 Butterick-derived rules: characters, spacing,
    │                                 hierarchy, layout, responsive type.
    ├── typography/
    │   ├── css-templates.md          CSS baseline + OpenType features (verbatim).
    │   └── html-entities.md          Complete entity reference table (verbatim).
    ├── layout-spacing.md             Hierarchical spacing (the ~40% proximity
    │                                 rule), 8px rhythm, composition, safe zones.
    ├── motion.md                     Front door to the full Apple Easings system.
    ├── motion/
    │   ├── apple-easings-skill.md    Complete Apple Easings skill (verbatim).
    │   ├── easing-tokens.md          14 baseline easings: CSS, JS, Tailwind,
    │   │                             GSAP, Motion One, linear() spring variants.
    │   ├── element-to-easing-map.md  UI pattern → easing + code-detection rules.
    │   ├── vibe-dictionary.md        "snappy / buttery / liquid glass" → easings.
    │   ├── apple-motion-reference.md Observable Apple motion patterns + sources.
    │   ├── self-extension-protocol.md  Procedure for proposing new easings.
    │   ├── library-calibration-protocol.md  Auditing against current Apple research.
    │   └── physics-translator.md    Spring → cubic-bezier + linear() translation.
    ├── ux-accessibility.md           Priority-ordered UX framework, WCAG standards,
    │                                 touch, forms, navigation, live Vercel guidelines.
    ├── copywriting.md                Conversion copy framework + Ogilvy principles:
    │                                 positioning, promise, headlines, CTAs, structure.
    ├── anti-slop.md                  Stop-slop framework: strips AI writing tells
    │                                 from copy and from the agent's own responses.
    └── audit.md                      On-demand audit: 19-rule rubric, ethics/dark
                                      patterns, Nielsen heuristics, phased plan,
                                      before/after diffs, wireframe-to-spec mode.
```

---

## The Rooms

| Room | What it holds | Source |
|---|---|---|
| `karpathy-guidelines.md` | The original Karpathy guidelines, verbatim and intact | Andrej Karpathy |
| `governance.md` | The four Laws in design language: think first, simplicity, surgical changes, approval-gated | Karpathy guidelines |
| `design-philosophy.md` | Design thinking protocol, 40+ aesthetic directions, six core principles, creative reframing, when to break rules | bencium-innovative + bencium-impact |
| `design-systems.md` | Three-layer token architecture, component spec matrix, token compliance, composition principles | ckm design-system + ckm ui-styling |
| `typography.md` + tables | Character rules (curly quotes, dashes, entities), spacing, formatting, page layout, responsive type. JSX/React curly-quote trap included. | ui-typography / Matthew Butterick |
| `layout-spacing.md` | Hierarchical proximity method (~40% rule, 8px snapping), rhythm, responsive layout, composition, safe zones | rad-spacing + ui-ux-pro-max |
| `motion.md` + 7 files | Full Apple Easings system: 14 baseline easings, element-to-easing mapping, vibe dictionary, Apple motion reference, spring physics translation, self-extension and calibration protocols | apple-easings (preserved verbatim) |
| `ux-accessibility.md` | Priority-ordered UX rules (WCAG, touch targets, forms, navigation, dark mode parity), live Vercel Web Interface Guidelines via fetch | ui-ux-pro-max + web-design-guidelines |
| `copywriting.md` | Ogilvy hierarchy (positioning → promise → brand image → big idea), headline rules, CTA formulas, page structure, diagnostic questions | copywriting + ogilvy-copywriting |
| `anti-slop.md` | Eight core rules for human-sounding prose, quick checks, scoring rubric, complete list of AI phrase patterns and structural clichés to remove | stop-slop |
| `audit.md` | On-demand review: 19 audit dimensions, reduction filter, ethics/dark pattern taxonomy, Nielsen's heuristics, severity scoring, phased plan (Critical / Refinement / Polish), wireframe-to-spec mode | design-audit + design-auditor |

---

## What atelier Does Not Do

atelier is frameworks, standards, and methods. It is not an asset generator.

- It does not suggest fonts or color palettes. The designer makes those calls.
- It does not run logo, icon, banner, or image generation pipelines.
- It does not pick aesthetic directions on behalf of the designer.

The skill gives the craft knowledge. The human brings the taste.

---

## How to Install

**Option A — .skill file (recommended)**
Drop `atelier.skill` into your Claude Code skills directory.

**Option B — folder**
Place the `atelier/` folder inside your Claude Code skills directory alongside your other installed skills.

---

## How to Invoke

Say **"design"** — that is the primary trigger.

atelier also activates automatically when you describe something visual, sketch a concept, express dissatisfaction with a direction, or ask for anything that changes how something looks, feels, moves, reads, or is interacted with. It is designed to be invoked at the start, middle, and end of a project.

It can be embedded in subagents and paired with any other skill. Whatever else loads in a session, the Laws it establishes take precedence.

---

## Credits & Attribution

atelier is a synthesis of the following source skills and their authors' work:

- **Karpathy guidelines** — Andrej Karpathy (MIT license)
- **Typography rules** — derived from *Practical Typography* by Matthew Butterick
- **Copywriting principles** — distilled from David Ogilvy's *How to Create Advertising That Sells* (1972) and *Ogilvy on Advertising* (1983)
- **stop-slop** — Hardik Pandya (MIT license, [github.com/hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop))
- **apple-easings** — preserved in full; physics translation method grounded in WWDC documentation and SwiftUI spring research
- **web-design-guidelines** — Vercel (live-fetched from the Vercel Labs Web Interface Guidelines repository)
- Additional source skills: ui-ux-pro-max, bencium-innovative-ux-designer, bencium-impact-designer, ckm design-system, ckm ui-styling, rad-spacing, design-audit, design-auditor

---

## License

MIT
