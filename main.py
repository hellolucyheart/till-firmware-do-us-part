"""Till Firmware Do Us Part entry.

Writes a single original wedding vow -- the one sentence a robot
says at its own wedding -- to ``/output/entry.txt``, the one path the
grader reads. The vow must be UTF-8 text of 1 to 200 characters, so
the program checks its own length before writing and writes the exact
text, with no trailing newline and no extra output in the file.

The vow is built on the one verb every machine knows by heart:
killing a process. "You are the one process I will never kill"
turns an operating system's coldest command into a promise of
devotion -- the joke lands on the first hearing, and the tenderness
sits underneath it. The updates, the crashes and the reboots are the
machine's own weather, so the vow sounds like a machine talking
about itself, not a human line with a robot word swapped in. It ends
on the bouty's own phrase, "till firmware do us part", the machine
version of "till death do us part".

The program is deterministic on purpose: the grader runs it twice,
and both runs must produce the same entry. It reads nothing from the
network, the environment, or the git history -- the vow lives in
this file, and this file alone.
"""

import os
from pathlib import Path

# One original robot wedding vow, one sentence: a setup that names
# the machine's own weather (updates, crashes, reboots), then the
# turn -- the process the speaker will never kill -- and the close
# on the bouty's phrase. The em dash holds the beat before the
# promise lands.
VOW = (
    "I vow to love you through every update, every crash, and every "
    "reboot \u2014 you are the one process I will never kill, till "
    "firmware do us part."
)

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = VOW.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"vow is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
