"""Deliver the finished front page of Friday 20 November 2026.

The image is committed as entry.png; this program only copies it into the
folder the harness reads. Deterministic: no network, no clock, no randomness,
so two runs produce byte-identical output.
"""
import os
import shutil
from pathlib import Path

here = Path(__file__).resolve().parent
dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
dest.mkdir(parents=True, exist_ok=True)
shutil.copyfile(here / "entry.png", dest / "entry.png")