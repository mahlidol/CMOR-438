"""
Structure and predictability features.

These features capture repetition, return, and linguistic
constraint without claiming to measure poetic quality.
"""

import re
import math
from collections import Counter
from typing import Dict, List


# ----------------------------
# Helpers
# ----------------------------

TOKEN_PATTERN = re.compile(r"\b\w+'?\w*\b")


def _get_lines(text: str) -> List[str]:
    """Split lyrics into non-empty lines."""
    lines = [line.strip().lower() for line in text.splitlines()]
    return [line for line in lines if line]


def _tokenize(text: str) -> List[str]:
    """Tokenize text into lowercase word tokens."""
    return TOKEN_PATTERN.findall(text.lower())


# ----------------------------
# Feature functions
# ----------------------------

def repetition_rate(lines: List[str]) -> float:
    """
    Compute the proportion of repeated lines.

    A higher value suggests stronger structural return
    (e.g., choruses).
    """
    if not lines:
        return

