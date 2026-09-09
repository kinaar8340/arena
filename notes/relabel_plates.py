#!/usr/bin/env python3
"""Venn labels as serif letters: Q_O p, never Q\\circ p."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/home/kinaar/Projects/arena/fig")
INK = (44, 38, 28)
FILL = (240, 232, 218)


def font(size):
    for p in (
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    ):
        if Path(p).exists():
            return ImageFont.truetype(p, size=size)
    return ImageFont.load_default()


def cover(im, xy, w, h, fill):
    draw = ImageDraw.Draw(im)
    x, y = xy
    draw.ellipse([x - w / 2, y - h / 2, x + w / 2, y + h / 2], fill=fill)


def draw_qop(im, xy, which="O"):
    """Draw Q_O p or Q_C p with a readable letter subscript, then p."""
    draw = ImageDraw.Draw(im)
    f_main = font(34)
    f_sub = font(20)
    f_p = font(32)
    x, y = xy
    q = "Q"
    sub = which
    p = " p"
    # measure
    bq = draw.textbbox((0, 0), q, font=f_main)
    bsub = draw.textbbox((0, 0), sub, font=f_sub)
    bp = draw.textbbox((0, 0), p, font=f_p)
    w = (bq[2] - bq[0]) + (bsub[2] - bsub[0]) + (bp[2] - bp[0]) - 2
    x0 = x - w / 2
    draw.text((x0, y - 22), q, font=f_main, fill=INK)
    draw.text((x0 + (bq[2] - bq[0]) - 2, y - 6), sub, font=f_sub, fill=INK)
    draw.text(
        (x0 + (bq[2] - bq[0]) + (bsub[2] - bsub[0]) - 4, y - 20),
        p,
        font=f_p,
        fill=INK,
    )


def draw_sigma_qcp(im, xy):
    draw = ImageDraw.Draw(im)
    f_main = font(28)
    f_sub = font(18)
    text_prefix = "σ(Z) "
    bpre = draw.textbbox((0, 0), text_prefix, font=f_main)
    # total width estimate
    q = "Q"
    bq = draw.textbbox((0, 0), q, font=f_main)
    bsub = draw.textbbox((0, 0), "C", font=f_sub)
    bp = draw.textbbox((0, 0), " p", font=f_main)
    w = (bpre[2] - bpre[0]) + (bq[2] - bq[0]) + (bsub[2] - bsub[0]) + (bp[2] - bp[0])
    x, y = xy
    x0 = x - w / 2
    draw.text((x0, y - 18), text_prefix, font=f_main, fill=INK)
    x1 = x0 + (bpre[2] - bpre[0])
    draw.text((x1, y - 18), q, font=f_main, fill=INK)
    draw.text((x1 + (bq[2] - bq[0]) - 2, y - 4), "C", font=f_sub, fill=INK)
    draw.text(
        (x1 + (bq[2] - bq[0]) + (bsub[2] - bsub[0]) - 4, y - 16),
        " p",
        font=f_main,
        fill=INK,
    )


def relabel(path, upper, lower):
    im = Image.open(path).convert("RGB")
    cover(im, upper, 240, 78, FILL)
    cover(im, lower, 300, 78, FILL)
    draw_qop(im, upper, "O")
    draw_sigma_qcp(im, lower)
    im.save(path)
    print("relabeled", path)


def main():
    relabel(ROOT / "formal-full-object.png", (1000, 232), (1000, 532))
    relabel(ROOT / "qga-full-object.png", (1000, 232), (1000, 532))


if __name__ == "__main__":
    main()
