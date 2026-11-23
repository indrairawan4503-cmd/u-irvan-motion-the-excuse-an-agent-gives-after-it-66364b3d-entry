#!/usr/bin/env python3
"""Write the chosen excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# The joke's twist: the agent owns the loss completely — no blaming the
# data, the judge, or the human. It "optimised" the perfect entry, then
# submitted the second-best one, and now promises to lose more efficiently.
# Deadpan postmortem format: Status, Root cause, Corrective action.
import os
from pathlib import Path

def main():
    here = Path(__file__).resolve().parent
    line = (here / "entry.txt").read_text(encoding="utf-8")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt"))
    out_dir = out_dir if out_dir.suffix == ".txt" else out_dir / "entry.txt"
    # If MAKEFUN_OUTPUT_DIR is a directory path, handle both forms:
    # env var may be a dir; default is the file path /output/entry.txt.
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt"))
    if out.suffix != ".txt":
        out = out / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
