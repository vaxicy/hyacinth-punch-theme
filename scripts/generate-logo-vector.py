#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hyacinth Punch Theme — vector logo candidates, batch 2 (headless Chromium).

Batch 1 read too literally (the floret spike looked like beads on a skewer).
Batch 2 shifts the graphic language: a retro-poster mini scene, a real petal
cluster, a refined tumbler, a minimal badge, a splash and a sunburst — all with
gradients, soft shadows and consistent weights.

Playwright screenshots each SVG cell with omit_background=True (true
transparency); PIL only composes the contact sheets, the inline strip and the
official logo/logo.png exported from SELECTED.
"""
import json
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

SIZE = 128
CELL = 512
PREVIEW = 256
SELECTED = "03"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


PINK = hx(_C["frame"])                             # #F8C7D9
PALE = hx(_C["toolbar"])                           # #FBE3FA
CREAM = hx(_C["ntp_background"])                   # #FBEED3
ORCHID = hx(_C["button_background"])               # #E3A0D3
PERI = hx(_C["button_background_secondary"])       # #A98BD5
LINK = hx(_C["ntp_link"])                          # #6B4A8F
INK = hx(_C["ntp_text"])                           # #3A2745

DEEP_PINK = "#D96BB4"
DEEP_PERI = "#7E5FB5"

SHADOW = """
  <filter id="ds" x="-35%%" y="-35%%" width="170%%" height="170%%">
    <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="%s" flood-opacity=".18"/>
  </filter>""" % INK


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def flower(cx, cy, scale, petal_fill, core_fill, petals=5, rx=8.6, ry=14.5):
    """Small multi-petal bloom centred on (cx, cy)."""
    out = ['<g transform="translate(%.1f %.1f) scale(%.3f)">' % (cx, cy, scale)]
    for i in range(petals):
        a = 360.0 * i / petals
        out.append('<ellipse cx="0" cy="-11" rx="%.1f" ry="%.1f" fill="%s" '
                   'transform="rotate(%.1f)"/>' % (rx, ry, petal_fill, a))
    out.append('<circle cx="0" cy="0" r="5.6" fill="%s"/>' % core_fill)
    out.append('</g>')
    return "".join(out)


def ray(cx, cy, a_deg, r0, r1, half_w, fill):
    a = math.radians(a_deg)
    x0, y0 = cx + r0 * math.cos(a), cy + r0 * math.sin(a)
    ex, ey = cx + r1 * math.cos(a), cy + r1 * math.sin(a)
    px, py = -math.sin(a), math.cos(a)
    return ('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="%s"/>'
            % (x0, y0, ex + px * half_w, ey + py * half_w,
               ex - px * half_w, ey - py * half_w, fill))


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <clipPath id="arch1"><path d="M66 224 V116 a62 62 0 0 1 124 0 V224 Z"/></clipPath>
  %s
</defs>
<g clip-path="url(#arch1)">
  <rect x="60" y="50" width="136" height="180" fill="%s"/>
  <circle cx="128" cy="108" r="30" fill="%s"/>
  <path d="M56 168 C92 148 108 184 140 172 C172 160 184 184 200 176 V232 H56 Z" fill="%s"/>
  <path d="M56 194 C92 178 108 208 140 197 C172 186 184 208 200 200 V232 H56 Z" fill="%s"/>
</g>
<path d="M66 224 V116 a62 62 0 0 1 124 0 V224" fill="none" stroke="%s" stroke-width="15"
      stroke-linecap="round" filter="url(#ds)"/>
<circle cx="190" cy="72" r="9" fill="%s"/>
""" % (SHADOW, PALE, DEEP_PINK, PERI, DEEP_PERI, DEEP_PERI, ORCHID))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="um2" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 228 C128 196 126 178 128 158" stroke="%s" stroke-width="7" stroke-linecap="round"
      fill="none"/>
<path d="M128 214 C104 206 96 188 96 176" stroke="%s" stroke-width="5" stroke-linecap="round" fill="none"/>
<path d="M128 214 C152 206 160 188 160 176" stroke="%s" stroke-width="5" stroke-linecap="round" fill="none"/>
<g filter="url(#ds)">
  %s
  %s
  %s
  %s
  %s
</g>
""" % (DEEP_PINK, DEEP_PERI, SHADOW, LINK, LINK, LINK,
       flower(128, 118, 1.30, "url(#um2)", CREAM),
       flower(96, 148, 0.86, ORCHID, CREAM),
       flower(160, 148, 0.86, ORCHID, CREAM),
       flower(112, 172, 0.62, PERI, CREAM),
       flower(146, 170, 0.62, PERI, CREAM)))

SVG_03 = svg_open("""
<defs>
  <linearGradient id="lq3" x1="0" y1="0" x2="0.5" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.55" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M82 74 h92 l-9 134 q-1 14 -16 14 h-42 q-15 0 -16 -14 z" fill="#FFFFFF"
      fill-opacity=".42" stroke="%s" stroke-width="5" filter="url(#ds)"/>
<path d="M88 112 h80 l-7 96 q-1 12 -14 12 h-38 q-13 0 -14 -12 z" fill="url(#lq3)"/>
<path d="M88 112 h80 l-1.6 22 h-76.8 z" fill="#FFFFFF" fill-opacity=".20"/>
<ellipse cx="128" cy="74" rx="46" ry="8.5" fill="#FFFFFF" fill-opacity=".55"/>
<rect x="102" y="136" width="32" height="30" rx="8" fill="#FFFFFF" fill-opacity=".40"
      transform="rotate(-16 118 151)"/>
<rect x="138" y="158" width="26" height="24" rx="7" fill="#FFFFFF" fill-opacity=".30"
      transform="rotate(14 151 170)"/>
<rect x="112" y="182" width="22" height="20" rx="6" fill="#FFFFFF" fill-opacity=".22"
      transform="rotate(-8 123 192)"/>
<path d="M96 112 q-2 40 0 78" stroke="#FFFFFF" stroke-opacity=".45" stroke-width="5"
      stroke-linecap="round" fill="none"/>
""" % (PINK, ORCHID, DEEP_PERI, SHADOW, PERI))

SVG_04 = svg_open("""
<defs>
  <linearGradient id="bd4" x1="0" y1="0" x2="0.85" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<circle cx="128" cy="128" r="102" fill="url(#bd4)" filter="url(#ds)"/>
<g transform="translate(128 138) rotate(18)">
  <path d="M0 -78 C34 -58 44 -18 22 22 C10 44 -10 44 -22 22 C-44 -18 -34 -58 0 -78 Z"
        fill="%s" fill-opacity=".95"/>
  <path d="M0 -70 V26" stroke="%s" stroke-opacity=".35" stroke-width="4" stroke-linecap="round"/>
</g>
<circle cx="128" cy="176" r="9" fill="%s"/>
<circle cx="196" cy="74" r="7" fill="%s" fill-opacity=".6"/>
""" % (DEEP_PERI, DEEP_PINK, SHADOW, CREAM, DEEP_PINK, CREAM, CREAM))

SVG_05 = svg_open("""
<defs>
  <linearGradient id="sp5" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<g filter="url(#ds)">
  <circle cx="112" cy="148" r="52" fill="url(#sp5)"/>
  <circle cx="158" cy="118" r="34" fill="%s" fill-opacity=".92"/>
</g>
<circle cx="98" cy="128" r="7" fill="#FFFFFF" fill-opacity=".55"/>
<g fill="%s">
  <circle cx="180" cy="176" r="13"/>
  <circle cx="196" cy="146" r="8"/>
  <circle cx="168" cy="196" r="7"/>
  <circle cx="76" cy="90" r="10"/>
  <circle cx="58" cy="118" r="6"/>
  <circle cx="196" cy="196" r="5"/>
</g>
<g fill="%s">
  <circle cx="62" cy="76" r="5"/>
  <circle cx="150" cy="60" r="6"/>
</g>
""" % (DEEP_PINK, DEEP_PERI, SHADOW, ORCHID, ORCHID, PERI))

SVG_06 = svg_open("""
<defs>%s</defs>
<g filter="url(#ds)">
%s
%s
<circle cx="128" cy="128" r="46" fill="%s"/>
<circle cx="128" cy="128" r="30" fill="%s"/>
</g>
""" % (SHADOW,
       "".join(ray(128, 128, -90 + 30 * i, 52, 94, 8.0, ORCHID) for i in range(12)),
       "".join(ray(128, 128, -90 + 30 * i + 15, 52, 83, 5.5, PERI) for i in range(12)),
       DEEP_PINK, CREAM))

CANDIDATES = [
    ("01", "bloom-arch", "Retro poster scene: arch, sun and waves", SVG_01),
    ("02", "hyacinth-umbel", "Real petal cluster on a stem — botanical", SVG_02),
    ("03", "punch-glass", "Tapered tumbler with ice — clean, no garnish", SVG_03),
    ("04", "petal-badge", "Single orchid petal in a badge — best at 32px", SVG_04),
    ("05", "punch-splash", "Circle and droplets — the punch itself", SVG_05),
    ("06", "sunburst", "Retro sunburst — boldest silhouette", SVG_06),
]


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def render_cells():
    cells = "".join('<div id="cell%s" style="width:%dpx;height:%dpx">%s</div>' % (num, CELL, CELL, svg)
                    for num, _n, _d, svg in CANDIDATES)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            '#grid{display:flex;flex-wrap:wrap;width:%dpx}div[id^=cell]{display:block}'
            '</style></head><body><div id="grid">%s</div></body></html>' % (CELL * 3, cells))
    out = {}
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": CELL * 3, "height": CELL * 2})
        pg.set_content(html)
        for num, name, _d, _svg in CANDIDATES:
            path = CAND_DIR / ("%s-%s.png" % (num, name))
            pg.locator("#cell" + num).screenshot(path=str(path), omit_background=True)
            img = Image.open(path).convert("RGBA").resize((PREVIEW, PREVIEW), Image.LANCZOS)
            img.save(path)
            bbox = img.split()[3].getbbox()
            assert bbox, "candidate %s rendered empty" % name
            assert bbox[0] > 6 and bbox[1] > 6 and bbox[2] < PREVIEW - 6 and bbox[3] < PREVIEW - 6, \
                "candidate %s touches the canvas edge: %s" % (name, bbox)
            out[num] = img
            print("candidate %s %s -> alpha bbox %s" % (num, name, bbox))
        b.close()
    return out


def contact_sheet(rendered, bg, txt, sub, path, title):
    cols, rows = 3, 2
    cw, ch = 384, 374
    gap, margin = 28, 40
    W = margin * 2 + cols * cw + (cols - 1) * gap
    H = margin * 2 + 34 + rows * ch + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(sheet)
    f_title, f_name, f_desc, f_file = font(24, True), font(21, True), font(15), font(14)
    d.text((margin, margin), title, font=f_title, fill=txt)
    y0 = margin + 34
    for i, (num, name, desc, _svg) in enumerate(CANDIDATES):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        y = y0 + r * (ch + gap)
        big = rendered[num].resize((220, 220), Image.LANCZOS)
        sheet.paste(big, (x + (cw - 220) // 2, y + 14), big)
        d.text((x + 18, y + 250), "%s · %s" % (num, name), font=f_name, fill=txt)
        d.text((x + 18, y + 280), desc, font=f_desc, fill=sub)
        thumb = rendered[num].resize((32, 32), Image.LANCZOS)
        sheet.paste(thumb, (x + 18, y + 330), thumb)
        d.text((x + 60, y + 339), "%s.png  256x256" % name, font=f_file, fill=sub)
        assert y + 300 <= y + 322, "text block collides with the thumbnail row"
    sheet.save(path)
    print("saved:", path, sheet.size)


def inline_strip(rendered, path):
    n, cell, gap, margin = len(CANDIDATES), 108, 22, 30
    W = margin * 2 + n * cell + (n - 1) * gap
    H = margin * 2 + cell + 30
    strip = Image.new("RGB", (W, H), (252, 245, 240))
    d = ImageDraw.Draw(strip)
    f = font(15, True)
    for i, (num, _n, _d, _s) in enumerate(CANDIDATES):
        x = margin + i * (cell + gap)
        img = rendered[num].resize((cell, cell), Image.LANCZOS)
        strip.paste(img, (x, margin), img)
        d.text((x + cell // 2 - 8, margin + cell + 8), num, font=f, fill=(58, 39, 69))
    strip.save(path)
    print("saved:", path, strip.size)


def main():
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    rendered = render_cells()
    contact_sheet(rendered, (252, 245, 240), (58, 39, 69), (128, 110, 128),
                  CAND_DIR / "contact-light.png", "Hyacinth Punch — logo candidates v2 (light)")
    contact_sheet(rendered, (38, 28, 46), (251, 238, 211), (196, 168, 196),
                  CAND_DIR / "contact-dark.png", "Hyacinth Punch — logo candidates v2 (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
