"""Normalize static bilingual profile heroes. No API calls or counters."""
from pathlib import Path
from PIL import Image

OUTPUTS = [
    Path("assets/eva/common/hero-signal-es.png"),
    Path("assets/eva/common/hero-signal-en.png"),
]

def main():
    for output in OUTPUTS:
        if not output.exists():
            raise SystemExit(f"missing hero asset: {output}")
        img = Image.open(output).convert("RGB")
        img.save(output, format="PNG", optimize=True)
        print(f"hero ready: {output} ({img.width}x{img.height})")

if __name__ == "__main__":
    main()
