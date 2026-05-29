# Element → Easing Map

Maps every common UI pattern to its recommended Apple easing. Used by Mode B (codebase audit)
to decide what easing each element should get based on what it IS, detected from code.

---

## Detection Rules — How to Identify an Element from Code

Apply these signals **in priority order**. First strong match wins. If signals conflict or
none match, mark "ambiguous — needs review".

### Priority order
1. **Component name** (highest confidence)
2. **File name**
3. **ARIA role**
4. **Library imports** (Radix, shadcn, MUI, Chakra, Headless UI)
5. **CSS class patterns**
6. **Tailwind/CSS layout signals**
7. **Animation context** (looped vs terminal, entrance vs exit)

### Detection signals by pattern

| Pattern | Component names | File names | ARIA / role | Class patterns | Tailwind/CSS signals |
|---|---|---|---|---|---|
| **Modal / Dialog** | `<Modal>`, `<Dialog>`, `<AlertDialog>`, `<Sheet>` | `modal.tsx`, `dialog.tsx`, `alertdialog.tsx` | `role="dialog"`, `role="alertdialog"` | `.modal`, `.dialog` | `fixed inset-0`, `z-50` + backdrop |
| **Drawer / Sheet** | `<Drawer>`, `<Sheet>`, `<SideSheet>` | `drawer.tsx`, `sheet.tsx` | `role="dialog"` + side | `.drawer`, `.sheet` | `fixed left-0/right-0/top-0/bottom-0` + slide animation |
| **Toast / Snackbar** | `<Toast>`, `<Snackbar>`, `<Notification>` | `toast.tsx`, `snackbar.tsx` | `role="status"`, `role="alert"` | `.toast`, `.snackbar` | `fixed` + corner positioning, auto-dismiss |
| **Tooltip** | `<Tooltip>`, `<HoverCard>` | `tooltip.tsx` | `role="tooltip"` | `.tooltip` | small + arrow + hover-triggered |
| **Dropdown / Menu** | `<DropdownMenu>`, `<Menu>`, `<Popover>`, `<Select>` | `dropdown.tsx`, `menu.tsx`, `popover.tsx` | `role="menu"`, `role="listbox"` | `.dropdown`, `.menu` | absolute positioning, opens from trigger |
| **Accordion** | `<Accordion>`, `<Collapsible>`, `<Disclosure>` | `accordion.tsx`, `collapsible.tsx` | `aria-expanded` | `.accordion` | height transitions |
| **Tabs** | `<Tabs>`, `<TabList>`, `<TabPanel>` | `tabs.tsx` | `role="tab"`, `role="tabpanel"` | `.tabs` | content swap on click |
| **Card (entrance)** | `<Card>` in a list | `card.tsx` | – | `.card` | translateY + opacity entrance |
| **Card (hover)** | `<Card>` with hover state | – | – | `:hover` rules on `.card` | scale on hover |
| **Button (hover)** | `<Button>` | `button.tsx` | `role="button"` | `.btn`, `.button` | scale/transform on hover |
| **Button (press)** | `<Button>` active state | – | – | `:active` rules | scale shrink on press |
| **Icon / Badge** | `<Icon>`, `<Badge>`, `<Chip>` | `icon.tsx`, `badge.tsx` | – | `.icon`, `.badge` | small element with scale animation |
| **Hero / CTA** | `<Hero>`, `<HeroBanner>`, `<CallToAction>` | `hero.tsx`, `cta.tsx` | – | `.hero`, `.cta` | large element, page-top, prominent |
| **Page transition** | route components, `<Outlet>` wrappers | `Layout.tsx`, `_app.tsx` | – | – | applied at route level, framework hooks |
| **Title / Heading** | `<h1>`–`<h6>`, `<Heading>`, `<Title>` | – | – | `.title`, `.heading` | text element, opacity/translate entrance |
| **Body text** | `<p>`, `<Text>`, `<Paragraph>` | – | – | `.body-text`, `.lead` | text element, opacity entrance |
| **Loading / Skeleton** | `<Skeleton>`, `<Spinner>`, `<Loader>` | `skeleton.tsx`, `loader.tsx` | `role="status"` | `.skeleton`, `.loading` | shimmer or pulse, looped |
| **Form field (focus)** | `<Input>`, `<TextField>` focus state | – | – | `:focus`, `:focus-visible` | border/shadow transitions |
| **Floating / Idle accent** | – | – | – | `.float`, `.idle` | `repeat: Infinity`, looped y-axis motion |
| **Number count-up** | `<CountUp>`, `<AnimatedNumber>` | `countup.tsx` | – | `.counter` | numeric value animating |

---

## Pattern → Easing Recommendations

Use the **primary** easing by default. Use the **alternate** if context suggests it (noted in
"when alternate fits").

| Pattern | Primary Easing | Alternate | When alternate fits |
|---|---|---|---|
| Modal / Dialog (open) | `scaleSubtleBounce` | `whooshFloatSettle` | Large hero-style modal |
| Modal / Dialog (close) | `opacitySmooth` | `opacityFadeIn` | Quick dismissal |
| Drawer / Sheet | `whooshSnapIn` | `whooshEnergetic` | Aggressive entry needed |
| Toast / Snackbar | `whooshSnapIn` | `opacitySnap` | Toast fades rather than slides |
| Tooltip | `opacitySnap` | `scaleSubtleBounce` | Tooltip has scale animation |
| Dropdown / Menu | `whooshSnapIn` | `opacitySnap` | Menu fades instead of slides |
| Accordion | `opacityFadeIn` | – | (height should use CSS native ease-out, opacity gets this) |
| Tabs (content swap) | `opacitySnap` | `textSnapFade` | Content is primarily text |
| Card entrance (single) | `whooshFloatSettle` | `whooshSnapIn` | Quick reveal needed |
| Card entrance (grid, staggered) | `whooshSnapIn` | `scaleSubtleBounce` | Cards should bounce in |
| Card hover | `scaleSubtleBounce` | – | – |
| Button hover | `scaleSubtleBounce` | – | – |
| Button press | `opacitySnap` | – | (fast feedback, no overshoot) |
| Icon / Badge entrance | `scaleOvershoot01` | `scaleOvershoot02` | Playful, very noticeable |
| Hero element entrance | `whooshFloatSettle` | `scaleOvershoot01` | Energetic hero |
| Page transition (fade) | `opacityFadeIn` | `textElegantFadeIn` | Text-heavy page |
| Page transition (slide) | `whooshSnapIn` | – | – |
| Title / Heading entrance | `textElegantFadeIn` | `textSnapFade` | Matched to other quick motion |
| Body text entrance | `opacityFadeIn` | – | – |
| Loading / Skeleton fade | `opacitySmooth` | – | – |
| Form field focus | `opacitySmooth` | – | (very subtle, calm) |
| Floating / Idle accent | `floatLoose` | `floatSettleLoop` | Continuous loop animation |
| Number count-up | `textElegantFadeIn` | – | – |

---

## Rules

1. **Never apply overshoot to text.** If the element type is text-related, the recommended
   easing has no `y` values >1.0. Don't override this even if the user asks for "bouncy text"
   — propose a vertical translate with overshoot on a wrapper instead.

2. **Never apply overshoot to scale on elements with `overflow: hidden` ancestors.** Check
   the parent chain. If overflow clipping is detected, downgrade overshoot to a non-overshoot
   alternative.

3. **Preserve direction-aware easings.** Page transitions in some routers use different
   easings for forward vs back. Don't collapse these into a single easing without flagging.

4. **Loop animations get loop-safe easings.** Anything with `repeat: Infinity` or
   `animation-iteration-count: infinite` must use a Float-category easing — overshoot eases
   look like glitches on repeat.

5. **Cooperate with motion design tokens.** If the project already has a motion token system
   (CSS variables named `--motion-*`, `--ease-*`, etc.), map onto those existing tokens
   rather than creating a parallel set. Surface conflicts to the user.
