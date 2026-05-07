#!/usr/bin/env python3
"""
Generate social media card for the repo.
1280x640, dark theme, Pillow.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def create_social_card(output_path):
    """Create a social card PNG."""
    width, height = 1280, 640
    bg_color = (26, 26, 46)  # Dark blue-gray
    text_color = (255, 255, 255)
    accent_color = (100, 200, 255)  # Light blue

    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        tagline_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        credit_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except (OSError, IOError):
        title_font = ImageFont.load_default()
        tagline_font = ImageFont.load_default()
        credit_font = ImageFont.load_default()

    title = "n8n-agentic-workflows"
    tagline = "61 lessons from production workflows"
    credit = "by @whodeanie"

    title_y = 120
    draw.text(
        (64, title_y),
        title,
        fill=accent_color,
        font=title_font,
    )

    tagline_y = 280
    draw.text(
        (64, tagline_y),
        tagline,
        fill=text_color,
        font=tagline_font,
    )

    credit_y = 540
    draw.text(
        (64, credit_y),
        credit,
        fill=(150, 150, 150),
        font=credit_font,
    )

    img.save(output_path)
    print(f"Created {output_path}")


if __name__ == "__main__":
    repo_root = Path(__file__).parent.parent
    output_path = repo_root / "assets" / "social.png"
    create_social_card(output_path)
