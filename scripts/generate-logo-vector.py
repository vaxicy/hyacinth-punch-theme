#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hyacinth Punch Theme — vector logo candidates (SVG rendered by headless Chromium).

Every mark carries a gradient fill, a soft drop shadow and highlights so it reads
as a designed icon rather than flat clip-art. The palette is pale, so the floral
shapes use slightly deepened orchid/periwinkle tones (same hues) plus the ink
colour for stems and details.

Playwright screenshots each SVG cell with omit_background=True (true
transparency); PIL only composes the contact sheets, the inline strip and the
official logo/logo.png exported from SELECTED.

Colours come from manifest.json. Change SELECTED and re-run; never hand-copy PNGs.
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
SELECTED = "01"
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

# deepened takes on the two signature hues, so the mark survives a pale page
DEEP_PINK = "#D96BB4"
DEEP_PERI = "#7E5FB5"

SHADOW = """
  <filter id="ds" x="-35%%" y="-35%%" width="170%%" height="170%%">
    <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="%s" flood-opacity=".18"/>
  </filter>""" % INK


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def petal(x, y, angle, length, width, fill, vein=None):
    """Pointed petal standing on (x, y), rotated by `angle`, tip at length."""
    d = ('M0 0 C %.1f %.1f %.1f %.1f 0 %.1f C %.1f %.1f %.1f %.1f 0 0 Z'
         % (width * 0.90, -length * 0.24, width * 0.72, -length * 0.74, -length,
            -width * 0.72, -length * 0.74, -width * 0.90, -length * 0.24))
    out = ('<g transform="translate(%.1f %.1f) rotate(%.1f)"><path d="%s" fill="%s"/>'
           % (x, y, angle, d, fill))
    if vein:
        out += ('<path d="M0 -%.1f V-%.1f" stroke="%s" stroke-opacity=".30" '
                'stroke-width="%.1f" stroke-linecap="round" fill="none"/>'
                % (length * 0.10, length * 0.82, vein, max(1.6, length * 0.05)))
    return out + '</g>'


def spike(base, count=9, fill="", dot=None):
    """Hyacinth floret cluster: beads along a gently curving stem."""
    bx, by = base
    out = []
    for i in range(count):
        t = i / (count - 1)
        cy = by - 22 - t * 118
        cx = bx + math.sin(t * 2.4) * 7
        r = 13.5 - t * 7.5
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (cx, cy, r, fill))
        if dot:
            out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" fill-opacity=".85"/>'
                       % (cx, cy, max(1.6, r * 0.26), dot))
    return "".join(out)


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <linearGradient id="sp1" x1="0" y1="1" x2="1" y2="0">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.55" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 200 V226" stroke="%s" stroke-width="7" stroke-linecap="round"/>
%s
%s
%s
<g filter="url(#ds)">%s</g>
%s
""" % (DEEP_PERI, ORCHID, DEEP_PINK, SHADOW, LINK,
       petal(128, 200, -44, 60, 21, PERI, LINK),
       petal(128, 200, 44, 60, 21, PERI, LINK),
       petal(128, 176, 0, 34, 13, ORCHID, LINK),
       spike((128, 200), count=9, fill="url(#sp1)", dot=None),
       '<circle cx="196" cy="86" r="7" fill="%s" fill-opacity=".45"/>' % DEEP_PERI))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="bd2" x1="0" y1="0" x2="0.8" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<circle cx="128" cy="128" r="102" fill="url(#bd2)"/>
<circle cx="128" cy="128" r="102" fill="none" stroke="%s" stroke-opacity=".22" stroke-width="4"/>
<g transform="translate(128 132) scale(0.70) translate(-128 -136)">
  %s
  %s
  %s
  %s
</g>
""" % (DEEP_PERI, DEEP_PINK, SHADOW, PALE,
       petal(128, 214, 148, 58, 19, PALE, None),
       petal(128, 214, 32, 58, 19, PALE, None),
       spike((128, 214), count=9, fill=PALE, dot=None),
       '<circle cx="128" cy="214" r="9" fill="%s"/>' % CREAM))

SVG_03 = svg_open("""
<defs>
  <linearGradient id="pl3" x1="0" y1="0" x2="0.3" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  <linearGradient id="pc3" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M78 74 h100 l-12 132 q-2 16 -18 16 h-40 q-16 0 -18 -16 z" fill="url(#pl3)"
      fill-opacity=".55" stroke="%s" stroke-opacity=".35" stroke-width="4"/>
<path d="M78 74 h100" stroke="%s" stroke-opacity=".45" stroke-width="5" stroke-linecap="round"/>
<path d="M86 116 h84 l-8 90 q-2 12 -14 12 h-40 q-12 0 -14 -12 z" fill="url(#pc3)"/>
<rect x="104" y="132" width="34" height="30" rx="7" fill="#FFFFFF" fill-opacity=".38"
      transform="rotate(-12 121 147)"/>
<ellipse cx="100" cy="96" rx="16" ry="9" fill="#FFFFFF" opacity=".35" transform="rotate(-20 100 96)"/>
<g filter="url(#ds)">
  <path d="M170 92 q22 -18 30 -2 q-16 22 -30 2 Z" fill="%s"/>
  <path d="M172 96 q16 -2 26 6" stroke="%s" stroke-opacity=".35" stroke-width="3" fill="none"/>
</g>
""" % (PERI, LINK, DEEP_PINK, ORCHID, SHADOW, LINK, LINK, DEEP_PINK, LINK))

SVG_04 = svg_open("""
<defs>
  <linearGradient id="pf4" x1="0" y1="1" x2="1" y2="0">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.5" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 216 V150" stroke="%s" stroke-width="7" stroke-linecap="round"/>
<g filter="url(#ds)">
%s
%s
%s
%s
%s
</g>
""" % (DEEP_PERI, ORCHID, DEEP_PINK, SHADOW, LINK,
       petal(128, 152, -74, 104, 27, "url(#pf4)", LINK),
       petal(128, 152, -44, 112, 26, "url(#pf4)", LINK),
       petal(128, 152, -14, 96, 24, "url(#pf4)", LINK),
       petal(128, 152, 16, 112, 26, "url(#pf4)", LINK),
       petal(128, 152, 46, 104, 27, "url(#pf4)", LINK)))

SVG_05 = svg_open("""
<defs>%s</defs>
<g transform="translate(0 -10)">
<g filter="url(#ds)" fill="none" stroke-linecap="round">
  <path d="M64 224 V120 a64 64 0 0 1 128 0 V224" stroke="%s" stroke-width="18"/>
</g>
<circle cx="128" cy="136" r="22" fill="%s"/>
<g filter="url(#ds)">
  <path d="M52 196 C92 184 116 148 122 118" stroke="%s" stroke-width="8" fill="none" stroke-linecap="round"/>
%s
%s
%s
</g>
</g>
""" % (SHADOW, PERI, DEEP_PERI, LINK,
       petal(100, 176, -136, 46, 16, DEEP_PINK, LINK),
       petal(116, 148, -110, 42, 15, ORCHID, LINK),
       petal(120, 124, -88, 36, 13, DEEP_PINK, LINK)))

SVG_06 = svg_open("""
<defs>
  <linearGradient id="dp6" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.6" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 44 C168 96 192 126 192 156 C192 192 163 216 128 216 C93 216 64 192 64 156
         C64 126 88 96 128 44 Z" fill="url(#dp6)" filter="url(#ds)"/>
<ellipse cx="106" cy="152" rx="17" ry="26" fill="#FFFFFF" opacity=".28" transform="rotate(-16 106 152)"/>
%s
%s
%s
<circle cx="150" cy="176" r="6" fill="%s" fill-opacity=".8"/>
""" % (DEEP_PINK, ORCHID, DEEP_PERI, SHADOW,
       petal(128, 190, -20, 40, 13, "#FFFFFF", None),
       petal(128, 190, -90, 46, 14, "#FFFFFF", None),
       petal(128, 190, -160, 40, 13, "#FFFFFF", None),
       CREAM))

CANDIDATES = [
    ("01", "hyacinth-spike", "Hyacinth floret spike with two leaves — most literal", SVG_01),
    ("02", "hyacinth-badge", "Pale spike in an orchid badge — strongest at 32px", SVG_02),
    ("03", "punch-glass", "Punch tumbler with ice and a sprig — most product-like", SVG_03),
    ("04", "petal-fan", "Five-petal fan — abstract, echoes the poster leaf", SVG_04),
    ("05", "arch-bloom", "Leaf over an arch — mirrors the source artwork", SVG_05),
    ("06", "punch-drop", "Gradient drop with petals — softest silhouette", SVG_06),
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
                  CAND_DIR / "contact-light.png", "Hyacinth Punch — vector logo candidates (light)")
    contact_sheet(rendered, (38, 28, 46), (251, 238, 211), (196, 168, 196),
                  CAND_DIR / "contact-dark.png", "Hyacinth Punch — vector logo candidates (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
