#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hyacinth Punch Theme — promo tiles (440x280 + 1400x560), all English.

Two presentation styles, one per size:

  1400x560 · full-bleed stripes — the palette itself becomes the background.
  440x280  · dot palette      — centred stack with six colour dots.

Colours are read from manifest.json. Every layout ends with bounds assertions so
overflow fails loudly at generation time.
"""
import json
import os
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

OUT_DIR = "store-assets/promo"
INK = (34, 48, 58)
WHITE = (255, 255, 255)
SHELL = (255, 253, 246)

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def save_png(img, path, tries=5):
    """PIL intermittently raises OSError [Errno 22] on this non-ASCII path."""
    last = None
    for i in range(tries):
        try:
            img.save(path)
            return
        except OSError as exc:            # pragma: no cover - environment specific
            last = exc
            time.sleep(0.35 * (i + 1))
    raise last


def rgb(vals):
    return (vals[0], vals[1], vals[2])


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def font(size, bold=False):
    win = os.environ.get("WINDIR", r"C:\Windows")
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(win, "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def text_w(d, s, f):
    return d.textbbox((0, 0), s, font=f)[2]


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def draw_chip(d, x, y, h, label, f, fill, txt, pad=16):
    w = text_w(d, label, f) + pad * 2
    # a hairline keeps the pill readable when it lands on a same-tone stripe
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill,
                        outline=lerp(INK, WHITE, 0.84), width=1)
    d.text((x + pad, y + (h - f.size) // 2 - 3), label, font=f, fill=txt)
    return w


# ------------------------------------------------------- 1400x560: stripes
def compose_bands(size=(1400, 560)):
    W, H = size
    M = 70
    RIGHT = W - M

    stripe_colors = [
        rgb(_C["button_background"]),             # sky
        rgb(_C["button_background_secondary"]),   # mint
        SHELL,                                    # shell
        rgb(_C["ntp_background"]),                # cream
        rgb(_C["frame"]),                         # blush
        rgb(_C["toolbar"]),                       # lilac
    ]
    img = Image.new("RGB", (W, H), stripe_colors[0])
    d = ImageDraw.Draw(img)
    n = len(stripe_colors)
    sw = W / n
    lean = W * 0.05
    for i, col in enumerate(stripe_colors):
        # stripes overlap so the lean never exposes the base fill at the edges
        x0 = i * sw - sw * 0.14
        x1 = x0 + sw * 1.30
        d.polygon([(x0 + lean, -2), (x1 + lean, -2), (x1 - lean, H + 2), (x0 - lean, H + 2)],
                  fill=col)

    # logo sits on a white tile so it never melts into a same-hue stripe
    tile = 140
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([M, 60, M + tile, 60 + tile], radius=34, fill=INK + (38,))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    img = Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([M, 56, M + tile, 56 + tile], radius=34, fill=WHITE)
    logo = Image.open("logo/logo.png").convert("RGBA").resize((100, 100), Image.LANCZOS)
    img.paste(logo, (M + 20, 76), logo)
    d = ImageDraw.Draw(img)

    f_title, f_sub = font(60, True), font(21)
    tx = M + tile + 34
    ty = 74
    d.text((tx, ty), "Hyacinth Punch", font=f_title, fill=INK)
    d.text((tx, ty + 76), "A retro pastel Chrome theme", font=f_sub,
           fill=lerp(INK, WHITE, 0.18))
    assert tx + text_w(d, "Hyacinth Punch", f_title) <= RIGHT - 20, "title overflows"

    f_chip = font(15)
    cx, cy = tx, ty + 116
    for label in ("Solid colors", "Retro pastel", "Easy on the eyes"):
        cx += draw_chip(d, cx, cy, 34, label, f_chip, WHITE, INK) + 12
    assert cx - 12 <= RIGHT, "chip row overflows"

    f_cta = font(20, True)
    cw, ch = 210, 54
    bx, by = RIGHT - cw, H - M - ch
    d.rounded_rectangle([bx, by, bx + cw, by + ch], radius=ch // 2, fill=INK)
    label = "Try It Now"
    d.text((bx + (cw - text_w(d, label, f_cta)) // 2, by + (ch - f_cta.size) // 2 - 3),
           label, font=f_cta, fill=SHELL)
    assert by > cy + 34 + 8, "CTA collides with the chip row"
    return img, {"cta": (bx, by, cw, ch), "logo_tile": (M, 56, tile, tile)}


# ------------------------------------------------------- 440x280: dot palette
def compose_dots(size=(440, 280)):
    W, H = size
    M = 28
    bg = rgb(_C["ntp_background"])
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    lsize = 60
    logo = Image.open("logo/logo.png").convert("RGBA").resize((lsize, lsize), Image.LANCZOS)
    img.paste(logo, ((W - lsize) // 2, 22), logo)
    d = ImageDraw.Draw(img)

    f_title, f_sub = font(27, True), font(12)
    title = "Hyacinth Punch"
    d.text(((W - text_w(d, title, f_title)) // 2, 92), title, font=f_title, fill=INK)
    sub = "A retro pastel Chrome theme"
    d.text(((W - text_w(d, sub, f_sub)) // 2, 126), sub, font=f_sub, fill=lerp(INK, bg, 0.32))

    # six dots; a soft shadow keeps the palest ones readable on the cream page
    dots = [
        rgb(_C["button_background"]), rgb(_C["button_background_secondary"]),
        hex2rgb("#FFFDF6"), bg, rgb(_C["frame"]), rgb(_C["toolbar"]),
    ]
    r, gap = 11, 12
    total = len(dots) * 2 * r + (len(dots) - 1) * gap
    x0 = (W - total) // 2
    y0 = 158
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for i in range(len(dots)):
        cx = x0 + i * (2 * r + gap) + r
        sd.ellipse([cx - r, y0 - r + 3, cx + r, y0 + r + 3], fill=INK + (34,))
    shadow = shadow.filter(ImageFilter.GaussianBlur(4))
    img = Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB")
    d = ImageDraw.Draw(img)
    for i, col in enumerate(dots):
        cx = x0 + i * (2 * r + gap) + r
        d.ellipse([cx - r, y0 - r, cx + r, y0 + r], fill=col)
    assert x0 >= M and x0 + total <= W - M, "dot row overflows"

    f_cta = font(13, True)
    cw, ch = 128, 34
    bx, by = (W - cw) // 2, 196
    d.rounded_rectangle([bx, by, bx + cw, by + ch], radius=ch // 2, fill=INK)
    label = "Try It Now"
    d.text((bx + (cw - text_w(d, label, f_cta)) // 2, by + (ch - f_cta.size) // 2 - 3),
           label, font=f_cta, fill=SHELL)
    assert by + ch <= H - M, "CTA too close to the bottom"
    return img, {"cta": (bx, by, cw, ch), "dots": (x0, y0 - r, total, 2 * r)}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for compose, name in ((compose_bands, "1400x560.png"), (compose_dots, "440x280.png")):
        img, boxes = compose()
        out = "%s/%s" % (OUT_DIR, name)
        save_png(img, out)
        print("saved:", out, img.size, img.mode, boxes)


if __name__ == "__main__":
    main()
