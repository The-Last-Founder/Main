# Intro video outputs

This folder contains rendered intro-video outputs based on `design/INTRO_VIDEO.md`.

## Files

| File | Duration | Description |
|------|----------|-------------|
| `build-intro-final.mp4` | ~1:51 | **Final cut** — Option 1 "Join the party", full production spec applied |
| `build-intro-option-1.mp4` | ~1:45 | Earlier draft of Option 1 (caption-only, pre-spec) |
| `build-intro-option-2.mp4` | ~2:30 | Earlier draft of Option 2 "Builder MMO" (caption-only, pre-spec) |

## Render

To regenerate `build-intro-final.mp4`:

```bash
pip install pillow
sudo apt install ffmpeg   # or: brew install ffmpeg
python3 design/render_video.py
```

## Notes

- All videos are caption-driven MP4s (no voice track yet).
- **Use `build-intro-final.mp4`** for homepage, social posts, and WhatsApp invite sharing.
- Voice narration can be added in post-production using ElevenLabs (voice: "Adam" or "Josh")
  or OpenAI TTS (`onyx` / `echo`) — see voice spec in `design/INTRO_VIDEO.md`.
- Music bed: royalty-free indie electronic, 95–110 BPM — see music spec in `design/INTRO_VIDEO.md`.
