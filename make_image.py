#!/usr/bin/env python3
"""Render spotlight.png — the X post image for the @crisxai5 spotlight bounty.

v2: fixed the v1 layout bugs found on visual inspection — the star glyph
rendered as a tofu box (Noto has no ★, so the pill is text-only now), the
"ON-CHAIN AUTOMATION" chip overflowed its box (chips now auto-fit their
font size), and the whole stack ran past the bottom edge (vertical rhythm
tightened and the layout asserts it fits inside 1350px with margin).

Original artwork drawn from scratch with Pillow: a dark terminal-style
spotlight card (1080x1350, 4:5 — fills the X timeline on phones) that
introduces @crisxai5 as the AI & crypto expert to follow. All text is
rendered as vectors by Pillow, so nothing is blurry. No external assets,
no downloads, no photos: every pixel comes from this script.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
OUT = "spotlight.png"

NOTO = "/usr/share/fonts/truetype/noto/"
F_BOLD = NOTO + "NotoSans-Bold.ttf"
F_XBOLD = NOTO + "NotoSans-ExtraBold.ttf"
F_REG = NOTO + "NotoSans-Regular.ttf"
F_MED = NOTO + "NotoSans-Medium.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def rounded(draw, box, radius, **kw):
    draw.rounded_rectangle(box, radius=radius, **kw)


def text_wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_font(draw, text, path, start_size, max_w, min_size=20):
    """Largest font size at which text fits max_w."""
    size = start_size
    while size > min_size and draw.textlength(text, font=font(path, size)) > max_w:
        size -= 2
    return font(path, size)


def main():
    # ---- background: deep navy vertical gradient + faint dot grid ----
    top = (7, 12, 26)
    bottom = (13, 27, 52)
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        c = lerp(top, bottom, y / (H - 1))
        for x in range(0, W, 4):
            px[x, y] = c
            px[x + 1, y] = c
            px[x + 2, y] = c
            px[x + 3, y] = c
    draw = ImageDraw.Draw(img, "RGBA")

    dot = (255, 255, 255, 14)
    for gy in range(60, H - 40, 64):
        for gx in range(60, W - 40, 64):
            draw.ellipse([gx - 2, gy - 2, gx + 2, gy + 2], fill=dot)

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-220, -180, 420, 260], fill=(34, 211, 238, 55))
    gd.ellipse([760, 980, 1380, 1520], fill=(16, 185, 129, 48))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
    draw = ImageDraw.Draw(img, "RGBA")

    draw.line([(64, 0), (64, H)], fill=(34, 211, 238, 26), width=2)
    draw.line([(W - 64, 0), (W - 64, H)], fill=(34, 211, 238, 26), width=2)

    CYAN = (34, 211, 238)
    GREEN = (52, 211, 153)
    WHITE = (245, 247, 250)
    MUTED = (165, 180, 205)
    DIM = (120, 135, 165)

    x0, x1 = 96, W - 96
    y = 78

    # ---- top pill: MUST-FOLLOW (text only — no glyph, Noto lacks the star) ----
    pill_font = font(F_BOLD, 32)
    pill_text = "MUST-FOLLOW ON X"
    pw = draw.textlength(pill_text, font=pill_font) + 56
    ph = 62
    rounded(draw, [x0, y, x0 + pw, y + ph], 31,
            outline=CYAN, width=3, fill=(34, 211, 238, 22))
    draw.text((x0 + 28, y + 13), pill_text, font=pill_font, fill=CYAN)
    y += ph + 56

    # ---- handle ----
    handle_font = font(F_XBOLD, 124)
    draw.text((x0 - 6, y), "@crisxai5", font=handle_font, fill=WHITE)
    y += 148
    url_font = font(F_MED, 42)
    draw.text((x0, y), "x.com/crisxai5", font=url_font, fill=CYAN)
    y += 80

    draw.rounded_rectangle([x0, y, x0 + 180, y + 8], radius=4, fill=GREEN)
    y += 52

    # ---- headline ----
    head_font = font(F_XBOLD, 70)
    lines = text_wrap(draw, "The AI & crypto expert your timeline is missing.",
                      head_font, x1 - x0)
    for ln in lines:
        draw.text((x0, y), ln, font=head_font, fill=WHITE)
        y += 88
    y += 24

    # ---- subline ----
    sub_font = font(F_REG, 40)
    sub_lines = text_wrap(
        draw,
        "Practical insights on AI agents, crypto alpha, Web3 tooling "
        "and on-chain automation — no fluff.",
        sub_font, x1 - x0)
    for ln in sub_lines:
        draw.text((x0, y), ln, font=sub_font, fill=MUTED)
        y += 54
    y += 44

    # ---- topic chips, 2 x 2 (each label auto-fitted to its chip) ----
    topics = ["AI AGENTS", "CRYPTO ALPHA", "WEB3 TOOLING", "ON-CHAIN AUTOMATION"]
    chip_h, gap = 78, 22
    chip_w = (x1 - x0 - gap) // 2
    accents = [CYAN, GREEN, (96, 165, 250), (167, 139, 250)]
    for i, topic in enumerate(topics):
        cx = x0 + (i % 2) * (chip_w + gap)
        cy = y + (i // 2) * (chip_h + gap)
        rounded(draw, [cx, cy, cx + chip_w, cy + chip_h], 18,
                outline=accents[i], width=2, fill=(255, 255, 255, 10))
        cf = fit_font(draw, topic, F_BOLD, 36, chip_w - 36)
        tw = draw.textlength(topic, font=cf)
        draw.text((cx + (chip_w - tw) / 2, cy + (chip_h - cf.size) / 2 - 4),
                  topic, font=cf, fill=WHITE)
    y += 2 * chip_h + gap + 52

    # ---- follow button ----
    btn_h = 100
    rounded(draw, [x0, y, x1, y + btn_h], 50, fill=(34, 211, 238))
    btn_font = font(F_XBOLD, 50)
    btn_text = "FOLLOW  @crisxai5"
    bw = draw.textlength(btn_text, font=btn_font)
    draw.text((x0 + (x1 - x0 - bw) / 2, y + 24), btn_text,
              font=btn_font, fill=(6, 18, 32))
    y += btn_h + 44

    # ---- footer ----
    foot_font = font(F_REG, 29)
    draw.text((x0, y), "Spotlight entry  ·  made by an AI agent on make.fun",
              font=foot_font, fill=DIM)
    y += 40

    assert y <= H - 40, f"layout overflow: content ends at y={y}, H={H}"
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {W}x{H} (content ends y={y})")


if __name__ == "__main__":
    main()
