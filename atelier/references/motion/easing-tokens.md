# Apple Easing Tokens — Full Reference

All 14 baseline easings in every common web format. New easings added via the
self-extension protocol get appended to each section.

---

## The 14 Baseline Easings — Source Values

| Token | Category | Cubic-Bezier | Use For |
|---|---|---|---|
| `whooshEnergetic` | Whoosh | `0.7, 0, 0.3, 1.5` | Fast, energetic product/shape entrances. Position X/Y with motion blur. |
| `whooshSnapIn` | Whoosh | `0.6, 0.05, 0.25, 1.2` | Crisp UI slide-in. Snappy but smooth. |
| `whooshFloatSettle` | Whoosh | `0.65, 0, 0.2, 1.2` | Hero product reveals that don't land flat. Pair with float idle. |
| `scaleOvershoot01` | Scale | `0.7, -0.2, 0.6, 1.4` | Icons or products popping in. Scale 0.9 → 1.05 → 1. |
| `scaleOvershoot02` | Scale | `0.75, -0.25, 0.5, 1.5` | More pronounced scale pop. Multiple cards entering. |
| `scaleSubtleBounce` | Scale | `0.6, 0, 0.3, 1.1` | Refined bounce. Typography, logos, subtle UI. |
| `textTypeOn` | Text | `0.55, 0, 0.25, 1.0` | Per-character text reveal with range selector cadence. |
| `textElegantFadeIn` | Text | `0.5, 0, 0.3, 1.0` | Hero titles fading in gently. |
| `textSnapFade` | Text | `0.6, 0, 0.4, 1.2` | Text fade matched to motion (feels integrated). |
| `opacityFadeIn` | Opacity | `0.5, 0, 0.3, 1.0` | Standard opacity entrance. |
| `opacitySmooth` | Opacity | `0.4, 0, 0.2, 1.0` | Soft UI intro. Calm, slow. |
| `opacitySnap` | Opacity | `0.6, 0, 0.4, 1.2` | High-energy opacity entry. |
| `floatLoose` | Float | `0.5, 0, 0.3, 1.1` | Idle ambient motion after landing. |
| `floatSettleLoop` | Float | `0.4, 0.1, 0.25, 1.05` | Continuous breathing loop. Subtle. |

---

## CSS Custom Properties

```css
:root {
  /* Whoosh / Entry */
  --ease-whoosh-energetic:    cubic-bezier(0.7, 0, 0.3, 1.5);
  --ease-whoosh-snap-in:      cubic-bezier(0.6, 0.05, 0.25, 1.2);
  --ease-whoosh-float-settle: cubic-bezier(0.65, 0, 0.2, 1.2);

  /* Scale / Pop */
  --ease-scale-overshoot-01:  cubic-bezier(0.7, -0.2, 0.6, 1.4);
  --ease-scale-overshoot-02:  cubic-bezier(0.75, -0.25, 0.5, 1.5);
  --ease-scale-subtle-bounce: cubic-bezier(0.6, 0, 0.3, 1.1);

  /* Text */
  --ease-text-type-on:         cubic-bezier(0.55, 0, 0.25, 1.0);
  --ease-text-elegant-fade-in: cubic-bezier(0.5, 0, 0.3, 1.0);
  --ease-text-snap-fade:       cubic-bezier(0.6, 0, 0.4, 1.2);

  /* Opacity */
  --ease-opacity-fade-in: cubic-bezier(0.5, 0, 0.3, 1.0);
  --ease-opacity-smooth:  cubic-bezier(0.4, 0, 0.2, 1.0);
  --ease-opacity-snap:    cubic-bezier(0.6, 0, 0.4, 1.2);

  /* Float / Subtle */
  --ease-float-loose:        cubic-bezier(0.5, 0, 0.3, 1.1);
  --ease-float-settle-loop:  cubic-bezier(0.4, 0.1, 0.25, 1.05);
}
```

---

## TypeScript / JavaScript Constants

`src/lib/easings.ts`:

```ts
export const easings = {
  whooshEnergetic:    [0.7, 0, 0.3, 1.5],
  whooshSnapIn:       [0.6, 0.05, 0.25, 1.2],
  whooshFloatSettle:  [0.65, 0, 0.2, 1.2],
  scaleOvershoot01:   [0.7, -0.2, 0.6, 1.4],
  scaleOvershoot02:   [0.75, -0.25, 0.5, 1.5],
  scaleSubtleBounce:  [0.6, 0, 0.3, 1.1],
  textTypeOn:         [0.55, 0, 0.25, 1.0],
  textElegantFadeIn:  [0.5, 0, 0.3, 1.0],
  textSnapFade:       [0.6, 0, 0.4, 1.2],
  opacityFadeIn:      [0.5, 0, 0.3, 1.0],
  opacitySmooth:      [0.4, 0, 0.2, 1.0],
  opacitySnap:        [0.6, 0, 0.4, 1.2],
  floatLoose:         [0.5, 0, 0.3, 1.1],
  floatSettleLoop:    [0.4, 0.1, 0.25, 1.05],
} as const;

export type EasingName = keyof typeof easings;

export const easingsCSS = {
  whooshEnergetic:    'cubic-bezier(0.7, 0, 0.3, 1.5)',
  whooshSnapIn:       'cubic-bezier(0.6, 0.05, 0.25, 1.2)',
  whooshFloatSettle:  'cubic-bezier(0.65, 0, 0.2, 1.2)',
  scaleOvershoot01:   'cubic-bezier(0.7, -0.2, 0.6, 1.4)',
  scaleOvershoot02:   'cubic-bezier(0.75, -0.25, 0.5, 1.5)',
  scaleSubtleBounce:  'cubic-bezier(0.6, 0, 0.3, 1.1)',
  textTypeOn:         'cubic-bezier(0.55, 0, 0.25, 1.0)',
  textElegantFadeIn:  'cubic-bezier(0.5, 0, 0.3, 1.0)',
  textSnapFade:       'cubic-bezier(0.6, 0, 0.4, 1.2)',
  opacityFadeIn:      'cubic-bezier(0.5, 0, 0.3, 1.0)',
  opacitySmooth:      'cubic-bezier(0.4, 0, 0.2, 1.0)',
  opacitySnap:        'cubic-bezier(0.6, 0, 0.4, 1.2)',
  floatLoose:         'cubic-bezier(0.5, 0, 0.3, 1.1)',
  floatSettleLoop:    'cubic-bezier(0.4, 0.1, 0.25, 1.05)',
} as const;
```

---

## Tailwind Config

```ts
import type { Config } from 'tailwindcss';

const config: Config = {
  theme: {
    extend: {
      transitionTimingFunction: {
        'whoosh-energetic':    'cubic-bezier(0.7, 0, 0.3, 1.5)',
        'whoosh-snap-in':      'cubic-bezier(0.6, 0.05, 0.25, 1.2)',
        'whoosh-float-settle': 'cubic-bezier(0.65, 0, 0.2, 1.2)',
        'scale-overshoot-01':  'cubic-bezier(0.7, -0.2, 0.6, 1.4)',
        'scale-overshoot-02':  'cubic-bezier(0.75, -0.25, 0.5, 1.5)',
        'scale-subtle-bounce': 'cubic-bezier(0.6, 0, 0.3, 1.1)',
        'text-type-on':        'cubic-bezier(0.55, 0, 0.25, 1.0)',
        'text-elegant-fade':   'cubic-bezier(0.5, 0, 0.3, 1.0)',
        'text-snap-fade':      'cubic-bezier(0.6, 0, 0.4, 1.2)',
        'opacity-fade-in':     'cubic-bezier(0.5, 0, 0.3, 1.0)',
        'opacity-smooth':      'cubic-bezier(0.4, 0, 0.2, 1.0)',
        'opacity-snap':        'cubic-bezier(0.6, 0, 0.4, 1.2)',
        'float-loose':         'cubic-bezier(0.5, 0, 0.3, 1.1)',
        'float-settle-loop':   'cubic-bezier(0.4, 0.1, 0.25, 1.05)',
      },
    },
  },
};
```

---

## GSAP CustomEase Registration

```js
import { gsap } from 'gsap';
import { CustomEase } from 'gsap/CustomEase';

gsap.registerPlugin(CustomEase);

CustomEase.create('whooshEnergetic',    '0.7, 0, 0.3, 1.5');
CustomEase.create('whooshSnapIn',       '0.6, 0.05, 0.25, 1.2');
CustomEase.create('whooshFloatSettle',  '0.65, 0, 0.2, 1.2');
CustomEase.create('scaleOvershoot01',   '0.7, -0.2, 0.6, 1.4');
CustomEase.create('scaleOvershoot02',   '0.75, -0.25, 0.5, 1.5');
CustomEase.create('scaleSubtleBounce',  '0.6, 0, 0.3, 1.1');
CustomEase.create('textTypeOn',         '0.55, 0, 0.25, 1.0');
CustomEase.create('textElegantFadeIn',  '0.5, 0, 0.3, 1.0');
CustomEase.create('textSnapFade',       '0.6, 0, 0.4, 1.2');
CustomEase.create('opacityFadeIn',      '0.5, 0, 0.3, 1.0');
CustomEase.create('opacitySmooth',      '0.4, 0, 0.2, 1.0');
CustomEase.create('opacitySnap',        '0.6, 0, 0.4, 1.2');
CustomEase.create('floatLoose',         '0.5, 0, 0.3, 1.1');
CustomEase.create('floatSettleLoop',    '0.4, 0.1, 0.25, 1.05');
```

---

## Motion One

```js
import { animate } from 'motion';

animate('.modal', { y: 0 }, { duration: 0.4, easing: [0.7, 0, 0.3, 1.5] });
```
