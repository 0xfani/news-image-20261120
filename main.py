"""Deliver the finished front page of Friday 20 November 2026.

The page (entry.png, 1024 x 1024) sums up the whole day's world news: 35 stories
from 6 regions, 13 of them on cards drawn as small infographics. It is committed in
the repository; this program only copies it into the folder the harness reads.
"""
import os
import shutil
from pathlib import Path

here = Path(__file__).resolve().parent
src = here / "entry.png"
if not src.is_file():
    raise SystemExit("entry.png is missing next to main.py")
dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
dest.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dest / "entry.png")   # byte-for-byte copy: no network, no clock, same bytes every run
print("wrote", dest / "entry.png", src.stat().st_size, "bytes")
