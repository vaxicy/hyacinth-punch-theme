<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/hyacinth-punch-theme/main/logo/logo.png" width="128" alt="Hyacinth Punch Theme logo">
</p>

<h1 align="center">Hyacinth Punch Theme</h1>

<p align="center">
  A retro pastel Chrome theme in orchid pink, periwinkle and cream — soft, floral, and easy on the eyes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/manifest-v3-f8c7d9" alt="Manifest V3">
  <img src="https://img.shields.io/badge/version-1.0.0-e3a0d3" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/chrome-light-fbe3fa" alt="Light chrome">
  <img src="https://img.shields.io/badge/license-non--commercial-3a2745" alt="Non-commercial license">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/hyacinth-punch-theme/main/store-assets/promo/1400x560.png?v=5\" alt="Hyacinth Punch Theme promo" width="700">
</p>

## Overview

Hyacinth Punch pairs a blush-pink frame with a pale orchid toolbar, then opens onto a soft pink New Tab Page with a coral Google logo that matches the mood. Deep plum ink keeps every tab, bookmark and toolbar icon readable on the light chrome, links take a deeper violet, and a single-row shortcut layout keeps the New Tab Page clean.

The palette leans retro: orchid pink, periwinkle and cream, all kept pale so the browser feels like printed poster stock rather than a candy screen.

## Design Concept

The source palette is a 70s-style pastel set — pale floss pink, orchid, periwinkle, blush and cream. Because every tone is light, the theme assigns them by role: blush and orchid build the chrome, floss carries the toolbar, and the page sits on the pinkest cream in the set. A single deep plum ink does all the reading work, so the pastel never has to compromise.

| Color | Hex | RGB | Role |
|---|---|---|---|
| Floss | `#FBE3FA` | 251, 227, 250 | Toolbar / New Tab header |
| Orchid | `#E3A0D3` | 227, 160, 211 | Buttons |
| Periwinkle | `#A98BD5` | 169, 139, 213 | Secondary buttons |
| Blush | `#F8C7D9` | 248, 199, 217 | Frame |
| Cream | `#FBEED3` | 251, 238, 211 | Palette cream |
| Page | `#F9EAEE` | 249, 234, 238 | New Tab background |
| Deep Plum Ink | `#3A2745` | 58, 39, 69 | Tab, bookmark and New Tab text |
| Violet Link | `#6B4A8F` | 107, 74, 143 | New Tab links |

## Features

- Pure color, no wallpaper — fast and distraction-free
- Retro pastel palette: orchid, periwinkle, blush and cream
- Light chrome with deep plum ink — readable without a dark frame
- Tab text, bookmark text and toolbar icons all share the same ink
- Single-row shortcut row and a color-matched Google logo for a clean New Tab Page
- No configuration needed — install and enjoy

## Screenshots

| Browser | Palette |
|:-:|:-:|
| <img src="https://raw.githubusercontent.com/vaxicy/hyacinth-punch-theme/main/store-assets/screenshots/en/screenshot-1-browser.png?v=2" width="420" alt="Hyacinth Punch New Tab"> | <img src="https://raw.githubusercontent.com/vaxicy/hyacinth-punch-theme/main/store-assets/screenshots/en/screenshot-2-palette.png" width="420" alt="Hyacinth Punch palette"> |

## Installation

### Load unpacked (development)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode** in the top right.
4. Click **Load unpacked** and select this folder (`hyacinth-punch-theme`).
5. The theme is active immediately.

### Package for the Chrome Web Store

```
chrome://extensions → Pack extension → select this folder → hyacinth-punch-theme.zip
```

Upload the resulting `.zip` to the [Chrome Web Store developer dashboard](https://chrome.google.com/webstore/devconsole).

## Store listing copy

Ready to paste into the store listing (also kept in `store-assets/store-description.txt`):

> Hyacinth Punch is a retro pastel Chrome theme: blush-pink chrome, a pale orchid toolbar, and a soft pink New Tab Page with a rose-pink Google logo. Deep plum ink keeps every tab, bookmark and toolbar icon readable. Solid colors only, no wallpaper.

## Project structure

| File | Purpose |
|---|---|
| `manifest.json` | Theme definition (single-file, inlined `theme` field) |
| `logo/logo.png` | 128×128 store icon (transparent background) |
| `store-assets/promo/440x280.png` | Small promo tile |
| `store-assets/promo/1400x560.png` | Marquee promo tile |
| `store-assets/screenshots/en/screenshot-1-browser.png` | Browser mockup screenshot (1280×800) |
| `store-assets/screenshots/en/screenshot-2-palette.png` | Palette introduction screenshot (1280×800) |
| `store-assets/store-description.txt` | Store listing description |
| `scripts/generate-logo-vector.py` | Render all SVG logo candidates with headless Chromium, build contact sheets, export `logo/logo.png` from `SELECTED` |
| `scripts/generate-screenshot-headless.py` | Regenerate the browser mockup via Playwright |
| `scripts/generate-screenshot-2-palette.py` | Regenerate the palette screenshot |
| `scripts/generate-promo.py` | Regenerate both promo tiles (1400×560 window hero, 440×280 dot palette) |
| `logo/candidates/` | Candidate previews and light/dark contact sheets |
| `LICENSE` | Non-Commercial License (English / 中文) |

## Regenerating assets

Every asset is code-generated, so nothing here is hand-drawn or hand-copied:

```bash
py -3 scripts/generate-logo-vector.py         # candidates + contact sheets + logo/logo.png
py -3 scripts/generate-screenshot-headless.py # store screenshot 1 (browser mockup)
py -3 scripts/generate-screenshot-2-palette.py # store screenshot 2 (palette)
py -3 scripts/generate-promo.py               # promo 440x280 + 1400x560
```

To ship a different icon candidate, change `SELECTED` at the top of `generate-logo-vector.py` and re-run, then re-run the three asset scripts so the promo and screenshots pick up the new logo.

## License

Hyacinth Punch Theme is released under the Non-Commercial License. See `LICENSE` for full text (English / 中文).
