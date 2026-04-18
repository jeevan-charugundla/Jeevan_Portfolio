import os
import base64

files = [
    ".gitignore",
    "README.md",
    "apply_all.py",
    "fix_bytes.py",
    "fix_encoding.ps1",
    "fix_encoding.py",
    "fix_mojibake.ps1",
    "remove_old_section.ps1",
    "stream_replace.ps1"
]

for f in files:
    if os.path.exists(f):
        print(f"--- FILE: {f} ---")
        try:
            with open(f, "r", encoding="utf-8") as file:
                print(file.read())
        except:
            with open(f, "rb") as file:
                print(base64.b64encode(file.read()).decode())
        print(f"--- END: {f} ---")
