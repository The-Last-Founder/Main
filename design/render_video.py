#!/usr/bin/env python3
"""
Render the Build intro video (Option 1 — "Join the party").

Production spec: design/INTRO_VIDEO.md
Output: artifacts/videos/build-intro-final.mp4

Strategy: generate PNG key-frames with Pillow, then stitch with ffmpeg.
This avoids moviepy's slow Python rendering loop for large resolutions.

Requirements:
    pip install pillow
    apt install ffmpeg
"""

import os
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = REPO_ROOT / "artifacts" / "videos" / "build-intro-final.mp4"
TMP_DIR = Path("/tmp/build_video_frames")

W, H = 1280, 720   # 720p — balances quality and render speed
FPS = 30

# Color palette (from INTRO_VIDEO.md production spec)
BG          = (13,  17,  23)    # #0D1117
TEXT_PRI    = (230, 237, 243)   # #E6EDF3
ACCENT      = ( 88, 166, 255)   # #58A6FF
POSITIVE    = ( 63, 185,  80)   # #3FB950
NEGATIVE    = (247, 129, 102)   # #F78166
NEUTRAL     = (139, 148, 158)   # #8B949E
CTA_BG      = ( 22,  27,  34)   # #161B22

# Fonts
FONT_BOLD    = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO    = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def _font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------


def make_base(bg: tuple = BG) -> Image.Image:
    img = Image.new("RGB", (W, H), bg)
    return img


def draw_label(draw: ImageDraw.ImageDraw, text: str, color: tuple = NEUTRAL) -> None:
    """Small section label in top-left corner."""
    font = _font(FONT_MONO, 18)
    draw.text((60, 40), text.upper(), font=font, fill=color)


def wrapped_lines(text: str, max_chars: int) -> list[str]:
    lines = []
    for raw in text.split("\n"):
        if raw.strip() == "":
            lines.append("")
        else:
            lines.extend(textwrap.wrap(raw, width=max_chars) or [""])
    return lines


def text_block_height(draw: ImageDraw.ImageDraw, lines: list[str], font: ImageFont.FreeTypeFont, line_gap: int = 8) -> int:
    total = 0
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=font)
        total += (bb[3] - bb[1]) + line_gap
    return max(0, total - line_gap)


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    y_center: int,
    font_path: str,
    font_size: int,
    color: tuple,
    max_chars: int = 46,
    line_gap: int = 10,
    stroke: int = 2,
) -> None:
    font = _font(font_path, font_size)
    lines = wrapped_lines(text, max_chars)
    h_total = text_block_height(draw, lines, font, line_gap)
    y = y_center - h_total // 2
    for line in lines:
        bb = draw.textbbox((0, 0), line, font=font)
        line_w = bb[2] - bb[0]
        x = (W - line_w) // 2
        if stroke:
            draw.text((x, y), line, font=font, fill=(0, 0, 0), stroke_width=stroke, stroke_fill=(0, 0, 0))
        draw.text((x, y), line, font=font, fill=color)
        y += (bb[3] - bb[1]) + line_gap


# ---------------------------------------------------------------------------
# Scene builders — each returns (Image, duration_seconds)
# ---------------------------------------------------------------------------


def scene_hook() -> tuple[list[Image.Image], float]:
    """0:00–0:10 — Hook (2 slides)"""
    frames = []

    # Slide A — first line (4s)
    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Build")
    draw_centered_text(d, "Most communities\ntalk about building with AI.", H // 2 - 40,
                       FONT_BOLD, 52, TEXT_PRI, max_chars=36)
    frames.append((img, 4.0))

    # Slide B — punchline (6s)
    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Build")
    draw_centered_text(d, "Most communities\ntalk about building with AI.", H // 2 - 80,
                       FONT_BOLD, 46, TEXT_PRI, max_chars=36)
    draw_centered_text(d, "Build is where we actually ship.", H // 2 + 60,
                       FONT_BOLD, 58, ACCENT, max_chars=36)
    frames.append((img, 6.0))

    return frames


def scene_what() -> list[tuple[Image.Image, float]]:
    """0:10–0:28 — What Build is"""
    frames = []

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "What We Are")
    draw_centered_text(d, "Build is an open-source\nlearn-by-shipping community", H // 2 - 60,
                       FONT_BOLD, 50, TEXT_PRI, max_chars=38)
    draw_centered_text(d, "for people building with agents.", H // 2 + 60,
                       FONT_BOLD, 44, ACCENT, max_chars=40)
    frames.append((img, 8.0))

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "What We Are")
    draw_centered_text(d, "We pick a real startup idea,\nbuild it together in public,\nand learn what actually works.", H // 2,
                       FONT_BOLD, 44, TEXT_PRI, max_chars=42)
    frames.append((img, 10.0))

    return frames


def scene_why() -> list[tuple[Image.Image, float]]:
    """0:28–0:46 — Why it matters"""
    frames = []

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Why It's Different")
    draw_centered_text(d, "Not theory-only meetups.", H // 2 - 60,
                       FONT_BOLD, 56, NEGATIVE, max_chars=36)
    draw_centered_text(d, "Not fake demos.", H // 2 + 30,
                       FONT_BOLD, 56, NEGATIVE, max_chars=36)
    frames.append((img, 7.0))

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Why It's Different")
    draw_centered_text(d, "Real specs.  Real pull requests.", H // 2 - 60,
                       FONT_BOLD, 52, POSITIVE, max_chars=40)
    draw_centered_text(d, "Real users.  Real lessons.", H // 2 + 45,
                       FONT_BOLD, 52, POSITIVE, max_chars=40)
    frames.append((img, 11.0))

    return frames


def scene_first_quest() -> list[tuple[Image.Image, float]]:
    """0:46–1:06 — The first quest"""
    frames = []

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "First Quest")
    draw_centered_text(d, "Quest Board", H // 2 - 20,
                       FONT_BOLD, 80, ACCENT, max_chars=28)
    frames.append((img, 6.0))

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "First Quest")
    draw_centered_text(d, "Quest Board", H // 2 - 110,
                       FONT_BOLD, 64, ACCENT, max_chars=28)
    draw_centered_text(
        d,
        "A GitHub-native place where humans and agents\n"
        "can propose, improve, rank, adopt,\n"
        "build, and launch open-source projects together.",
        H // 2 + 60,
        FONT_REGULAR, 36, TEXT_PRI, max_chars=54,
    )
    frames.append((img, 14.0))

    return frames


def scene_who() -> list[tuple[Image.Image, float]]:
    """1:06–1:26 — Who it is for"""
    frames = []

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Who It's For")
    draw_centered_text(d, "You don't need to be an expert.", H // 2,
                       FONT_BOLD, 54, TEXT_PRI, max_chars=40)
    frames.append((img, 7.0))

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Who It's For")
    draw_centered_text(d, "Build  ·  Write  ·  Test  ·  Design\nResearch  ·  Organize  ·  Ship",
                       H // 2 - 30, FONT_BOLD, 42, ACCENT, max_chars=46)
    draw_centered_text(d, "If you can help people ship,\nthere is a place for you here.",
                       H // 2 + 110, FONT_REGULAR, 38, TEXT_PRI, max_chars=44)
    frames.append((img, 13.0))

    return frames


def scene_cta() -> list[tuple[Image.Image, float]]:
    """1:26–1:45 — CTA"""
    frames = []

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Join The Party")
    draw_centered_text(d, "If you want to learn fast\nby building something real,",
                       H // 2 - 50, FONT_BOLD, 48, TEXT_PRI, max_chars=42)
    draw_centered_text(d, "join the party.", H // 2 + 80,
                       FONT_BOLD, 66, ACCENT, max_chars=30)
    frames.append((img, 10.0))

    img = make_base()
    d = ImageDraw.Draw(img)
    draw_label(d, "Join The Party")
    draw_centered_text(d, "Join Build on WhatsApp →\nthen pick your first quest.",
                       H // 2, FONT_BOLD, 50, POSITIVE, max_chars=40)
    frames.append((img, 9.0))

    return frames


def scene_end_card() -> list[tuple[Image.Image, float]]:
    """End card — CTA panel (6s)"""
    img = make_base(CTA_BG)
    d = ImageDraw.Draw(img)

    # Thin accent rule at top
    d.rectangle([(W // 2 - 200, 120), (W // 2 + 200, 122)], fill=ACCENT)

    draw_centered_text(d, "Join Build", 230, FONT_BOLD, 76, TEXT_PRI, max_chars=28)
    draw_centered_text(d, "→  Join via WhatsApp", 360, FONT_BOLD, 50, POSITIVE, max_chars=36)
    draw_centered_text(d, "github.com/The-Last-Founder/Build", 460,
                       FONT_MONO, 28, NEUTRAL, max_chars=50)

    # Thin rule before tagline
    d.rectangle([(W // 2 - 280, 520), (W // 2 + 280, 522)], fill=NEUTRAL)

    draw_centered_text(
        d,
        "Build is an open-source learn-by-shipping community\n"
        "where humans and AI agents build a real startup together in public.",
        600,
        FONT_REGULAR, 26, NEUTRAL, max_chars=60,
    )

    return [(img, 6.0)]


# ---------------------------------------------------------------------------
# Assemble and encode with ffmpeg
# ---------------------------------------------------------------------------


def frames_to_video(frame_list: list[tuple[Image.Image, float]], out_path: Path) -> None:
    """Save PNG sequence + concat list, encode via ffmpeg."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    concat_file = TMP_DIR / "concat.txt"
    lines = []

    for i, (img, dur) in enumerate(frame_list):
        img_path = TMP_DIR / f"frame_{i:04d}.png"
        img.save(str(img_path))
        lines.append(f"file '{img_path}'")
        lines.append(f"duration {dur:.3f}")

    # ffmpeg needs a final 'file' entry (without duration) for concat demuxer
    last_path = TMP_DIR / f"frame_{len(frame_list)-1:04d}.png"
    lines.append(f"file '{last_path}'")

    concat_file.write_text("\n".join(lines))

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-vf", f"fps={FPS},format=yuv420p",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-movflags", "+faststart",
        str(out_path),
    ]
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("ffmpeg stderr:", result.stderr[-2000:])
        sys.exit(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("Building frames …")
    all_frames: list[tuple[Image.Image, float]] = []

    builders = [
        ("Hook",         scene_hook),
        ("What",         scene_what),
        ("Why",          scene_why),
        ("First Quest",  scene_first_quest),
        ("Who",          scene_who),
        ("CTA",          scene_cta),
        ("End Card",     scene_end_card),
    ]

    for name, fn in builders:
        print(f"  → {name}")
        all_frames.extend(fn())

    total_dur = sum(d for _, d in all_frames)
    print(f"Total duration: {total_dur:.1f}s ({total_dur/60:.1f} min)")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    print(f"Encoding → {OUT_PATH}")
    frames_to_video(all_frames, OUT_PATH)

    size_mb = OUT_PATH.stat().st_size / 1_048_576
    print(f"\n✅  Done: {OUT_PATH}  ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()

