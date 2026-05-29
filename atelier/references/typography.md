# Typography — Timeless Rules for Screen Text

Source: the ui-typography skill, distilled from Matthew Butterick's *Practical Typography*. These
are permanent rules, not trends. They come from how the eye reads and do not go out of style.

**Mode:** when generating any UI with visible text, apply these automatically and silently. When
reviewing, flag violations with before/after fixes.

**Verbatim reference tables in this room** (read when writing code or looking up a character):
- `typography/css-templates.md` — full CSS baseline, responsive patterns, OpenType features
- `typography/html-entities.md` — complete entity table with codes

---

## Characters

**Quotes & apostrophes — always curly.** Straight quotes are typewriter relics. `&ldquo;`/`&rdquo;`,
`&lsquo;`/`&rsquo;`. The apostrophe is always the closing single quote `&rsquo;`, even before decade
abbreviations (`&rsquo;70s`) and word-initial contractions.

> **JSX/React trap:** `\u2019` and similar escapes render literally in JSX text between tags. Either
> paste the real UTF-8 character into the source, or wrap the escape in an expression: `Don{'\u2019'}t`.
> HTML entities (`&rsquo;`) work in `.html` only, not JSX text. In JS string/data arrays, `\u2019`
> works fine — the bug is only JSX text content.

**Dashes — three distinct characters:**
- hyphen `-` for compound words and line breaks
- en dash `&ndash;` for ranges (1–10) and connections (Sarbanes–Oxley)
- em dash `&mdash;` for sentence breaks
Never fake them with `--`/`---`. (Note: the anti-slop room bans em dashes in *prose copy* you write;
this rule is about rendering them correctly when they do appear.)

**Ellipsis** — one character `&hellip;`, not three periods.

**Foot/inch marks** are the one exception to curly quotes: they must be straight (`&#39;` foot,
`&quot;` inch), with `&nbsp;` between values: `6&#39;&nbsp;10&quot;`. Use `&times;` for dimensions
(8.5″ × 14″) and multiplication, `&minus;` for subtraction.

**Real symbols** for `&copy;` `&trade;` `&reg;`, never (c)/(TM)/(R). © is inline + `&nbsp;` + year;
"Copyright ©" is redundant.

**Accents are mandatory in proper names** (François Truffaut). One exclamation point per long
document, never stacked. Ampersands only in proper names; write "and" in body. No emoji in formal or
professional UI copy.

---

## Spacing

- **One space after punctuation. Always.** Two spaces create rivers.
- **Nonbreaking space `&nbsp;`** before numeric refs (`Fig.&nbsp;3`), after © and honorifics
  (`Dr.&nbsp;Smith`), between foot/inch values.
- Never hold the spacebar, never double `<br>` for spacing, never tabs for indentation in output.

---

## Text formatting

- **Bold OR italic, never both. Use as little as possible** — if everything is emphasized, nothing
  is. Sans serif: prefer bold (italic sans barely reads). Never bold whole paragraphs. Never use
  quotation marks for emphasis.
- **Never underline** in a document or UI (typewriter workaround). For links, style subtly:
  `text-decoration-thickness: 1px; text-underline-offset: 2px`.
- **All caps:** less than one line only, always letterspaced 5–12% (`letter-spacing: 0.06em`),
  kerning on. Never set whole paragraphs in caps.
- **Small caps:** real only (`font-variant-caps: small-caps` with OpenType `smcp`), never scaled
  caps. Add letterspacing.
- **Kerning always on:** `font-feature-settings: "kern" 1; text-rendering: optimizeLegibility;`
- **Figures:** tabular (`tnum`) for data columns, oldstyle (`onum`) for body where available.
- **Mixing fonts:** max two, each with a consistent role. Lower contrast often reads better than
  high contrast.

---

## Page layout

- **Set body text first.** Four decisions drive everything else: font, size, line spacing, line
  length. Everything calibrates to these.
- **Line length 45–90 characters.** The #1 readability factor designers get wrong, and the #1 flaw
  in responsive layouts. `max-width: 65ch` on text containers.
- **Line spacing 120–145%** of size (`line-height: 1.2`–`1.45`). Single is too tight, double too
  loose.
- **Generous margins** look professional. Don't fear white space.
- **Left-align for web** by default. Justify only with `hyphens: auto`. Center only short titles
  (under one line), never blocks.
- **Paragraph separation: indent OR space, never both.** `text-indent: 1.5em` or `margin-bottom:
  0.75em`. Never double `<br>`.
- **Headings: max ~3 levels.** Don't all-caps (unless short + letterspaced), don't underline, rarely
  center. Emphasize with space above and below (more above than below). Use bold over italic.
  Smallest size increment that reads as a level. `hyphens: none` on headings; keep with the
  following paragraph.
- **Lists:** semantic `<ul>`/`<ol>`, never manual bullets. Don't over-indent.
- **Tables:** remove borders, add padding (`0.5em 1em`). Keep at most a thin rule under the header.
  Tabular figures and right-aligned numbers in numeric columns.
- **Block quotes:** slightly smaller, indented 2–5em, no quote marks. Use sparingly.
- **Flow control (print):** `orphans: 2; widows: 2`. `&shy;` for words that confuse hyphenation.

---

## Responsive type

The rules do not change with screen size — same line length, spacing, hierarchy.
- Scale `font-size` and container `width` together; always `max-width` on text (never edge-to-edge).
- `clamp()` for fluid sizing: `font-size: clamp(16px, 2.5vw, 20px)`.
- Mobile minimum: `padding: 0 1rem` on text containers.
- Common failure: images and nav scale carefully while body text is ignored. Don't.

Modern screens render type as well as print; serif on screen is fine. In dark mode, reduce weight
slightly. Body text minimum ~15–16px on web.

---

## Maxims

1. Body text first — its four properties determine everything.
2. Don't let chrome upstage body text.
3. Smallest visible increments — half-points matter.
4. When in doubt, make samples; don't theorize.
5. Consistency — same things look the same.
6. Relate each new element to existing ones.
7. Keep it simple.
8. Emulate good typography you admire (don't copy a specific work).
