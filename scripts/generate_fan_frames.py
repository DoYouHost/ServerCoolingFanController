#!/usr/bin/env python3
"""Generate rotated fan icon frames for LVGL animimg."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = Path(__file__).parent.parent / "fonts" / "materialdesignicons-webfont.ttf"
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "fan_anim"
FAN_CODEPOINT = "\U000F0210"
CANVAS = 30  # output image size (square)
NUM_FRAMES = 12  # 12 frames = 30° per step
BG_COLOR = (0, 0, 0, 0)  # transparent
FG_COLOR = (0, 170, 255, 255)  # color_accent #00AAFF
RENDER_SCALE = 8  # supersample for smooth rotation


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    render_size = CANVAS * RENDER_SCALE

    # Render glyph large, then crop tight and scale to fill canvas
    big_font = ImageFont.truetype(str(FONT_PATH), render_size * 2)
    tmp = Image.new("RGBA", (render_size * 4, render_size * 4), BG_COLOR)
    draw = ImageDraw.Draw(tmp)
    bbox = draw.textbbox((0, 0), FAN_CODEPOINT, font=big_font)
    draw.text((-bbox[0], -bbox[1]), FAN_CODEPOINT, font=big_font, fill=FG_COLOR)

    # Crop to actual pixel content (tight bounding box)
    content_bbox = tmp.getbbox()
    cropped = tmp.crop(content_bbox)

    # Make square (pad shorter side)
    w, h = cropped.size
    side = max(w, h)
    square = Image.new("RGBA", (side, side), BG_COLOR)
    square.paste(cropped, ((side - w) // 2, (side - h) // 2))

    # Scale to fill render canvas with ~5% margin for rotation clearance
    glyph_size = int(render_size * 0.92)
    glyph = square.resize((glyph_size, glyph_size), Image.LANCZOS)

    # Place centered on rotation canvas
    base = Image.new("RGBA", (render_size, render_size), BG_COLOR)
    offset = (render_size - glyph_size) // 2
    base.paste(glyph, (offset, offset))

    for i in range(NUM_FRAMES):
        angle = i * (360 / NUM_FRAMES)
        rotated = base.rotate(angle, resample=Image.BICUBIC, center=(render_size // 2, render_size // 2))
        frame = rotated.resize((CANVAS, CANVAS), Image.LANCZOS)
        frame.save(OUTPUT_DIR / f"fan_{i:02d}.png")

    print(f"Generated {NUM_FRAMES} frames in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
