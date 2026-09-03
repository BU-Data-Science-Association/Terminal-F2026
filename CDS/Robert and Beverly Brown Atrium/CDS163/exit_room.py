#!/usr/bin/env python3
"""Validate the CDS 163 scavenger-hunt answer and unlock the room."""

from __future__ import annotations

import hashlib
import hmac
import sys
from pathlib import Path


EXPECTED_DIGEST = "fdda6dc75e92d2ab46ad365a74ae99e5d1ba62207cc701eced2067147fa09e87"
UNLOCK_FILE = Path(__file__).with_name(".exit_permission")


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: python3 {Path(__file__).name} <20-character-hash>")
        return 2

    answer = sys.argv[1]
    digest = hashlib.sha256(answer.encode("ascii", errors="ignore")).hexdigest()
    if len(answer) != 20 or not hmac.compare_digest(digest, EXPECTED_DIGEST):
        print("The door stays locked.")
        return 1

    UNLOCK_FILE.write_text("CDS 163 exit unlocked\n", encoding="utf-8")
    print("Correct. Your permission to exit CDS 163 has been restored.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
