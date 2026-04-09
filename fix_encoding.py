#!/usr/bin/env python3
"""
fix_encoding.py
Fixes double-encoded UTF-8 (mojibake) in index.html.

Root cause: PowerShell read UTF-8 file using Windows-1252 (default),
then wrote the mis-interpreted string back as UTF-8.
This means each UTF-8 byte sequence B was decoded as Windows-1252 codepoints,
then re-encoded as UTF-8. We reverse this by:
  1. Reading the current file as UTF-8  (gets mojibake string)
  2. Encoding that string back to bytes using latin-1 (recovers original UTF-8 bytes)
  3. Decoding those bytes as UTF-8  (gets correct characters)
  4. Writing back as UTF-8 without BOM
"""
import sys

path = 'index.html'

with open(path, 'r', encoding='utf-8') as f:
    broken = f.read()

# Try to recover original UTF-8 bytes
try:
    original_bytes = broken.encode('latin-1')
    fixed = original_bytes.decode('utf-8')
    print("Single-pass fix succeeded")
except (UnicodeDecodeError, UnicodeEncodeError) as e:
    print(f"Single-pass failed ({e}), trying char-by-char recovery...")
    # Some chars may be mix — fix known sequences manually
    fixed = broken
    replacements = {
        '\u00e2\u20ac\u2122': '\u2019',  # â€™ -> '
        '\u00e2\u20ac\u0153': '\u201c',  # â€œ -> "
        '\u00e2\u20ac\uFFFD': '\u201d',  # â€ -> "
        '\u00e2\u20ac\u201c': '\u2013',  # â€" -> –
        '\u00e2\u20ac\u201d': '\u2014',  # â€" -> —
        '\u00e2\u20ac\xa6':   '\u2026',  # â€¦ -> …
        '\u00e2\u2020\u2019': '\u2192',  # â†' -> →
        '\u00c3\u00a2\u00e2\u20ac\u201d': '\u2192',  # triple-encoded →
        '\u00c2\u00a0': '\u00a0',        # Â  -> NBSP
        'LET\u00e2\u20ac\u2122S': "LET\u2019S",
        "don\u00e2\u20ac\u2122t": "don\u2019t",
        "it\u00e2\u20ac\u2122s": "it\u2019s",
        "I\u00e2\u20ac\u2122m": "I\u2019m",
        "doesn\u00e2\u20ac\u2122t": "doesn\u2019t",
        "isn\u00e2\u20ac\u2122t": "isn\u2019t",
        "won\u00e2\u20ac\u2122t": "won\u2019t",
        "can\u00e2\u20ac\u2122t": "can\u2019t",
    }
    for bad, good in replacements.items():
        fixed = fixed.replace(bad, good)

with open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(fixed)

print(f"Fixed. File size: {len(fixed)} chars")
