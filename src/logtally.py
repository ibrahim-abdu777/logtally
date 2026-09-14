"""Tally severity counts in newline-delimited application logs."""
import re
from collections import Counter

LEVELS = ("DEBUG", "INFO", "WARN", "ERROR", "FATAL")
_PATTERN = re.compile(r"\b(" + "|".join(LEVELS) + r")\b")


def summarize(lines):
    counts = Counter()
    for line in lines:
        for match in _PATTERN.findall(line):
            counts[match] += 1
    return {level: counts.get(level, 0) for level in LEVELS}


def summarize_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return summarize(handle)
