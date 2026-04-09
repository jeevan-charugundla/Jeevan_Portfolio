# fix_mojibake.ps1 — targeted replacement of all known garbled sequences
$file = 'index.html'
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

$content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

# Map of mojibake -> correct character
# (these are UTF-8 bytes read as Windows-1252 then re-encoded as UTF-8 one or more times)
$fixes = [ordered]@{
    # RIGHT SINGLE QUOTATION MARK  '  (U+2019)   →  â€™  or  â�,��"™
    'â€™'       = [char]0x2019   # '
    'Ã¢â‚¬â„¢' = [char]0x2019   # '   (triple-encoded)
    "â\x00,\x00\x00`"\x00™" = [char]0x2019  # viewer artifact — skip
    # LEFT DOUBLE QUOTATION MARK  "  (U+201C)
    'â€œ'       = [char]0x201C   # "
    # RIGHT DOUBLE QUOTATION MARK  "  (U+201D)
    'â€'        = [char]0x201D   # "
    # RIGHTWARDS ARROW  →  (U+2192)
    'â†''       = [char]0x2192   # →   (NOTE: this pattern conflicts, handle carefully)
    'Ã¢â€ â€™'  = [char]0x2192   # →
    # EN DASH  –  (U+2013)
    'â€"'       = [char]0x2013   # –
    # EM DASH  —  (U+2014)
    'â€"'       = [char]0x2014   # —   (same bytes as en-dash in some encodings, use context)
    # ELLIPSIS  …  (U+2026)
    'â€¦'       = [char]0x2026   # …
    # NON-BREAKING SPACE (U+00A0) rendered as Â
    'Â '        = ' '
    # Ã variants
    'Ã©'        = [char]0x00E9   # é
    'Ã¨'        = [char]0x00E8   # è
    'Ãª'        = [char]0x00EA   # ê
    'Ã '        = [char]0x00E0   # à
    'Ã¢'        = [char]0x00E2   # â
    'Ã®'        = [char]0x00EE   # î
    'Ã´'        = [char]0x00F4   # ô
    'Ã»'        = [char]0x00FB   # û
    'Ã¹'        = [char]0x00F9   # ù
    'Ã§'        = [char]0x00E7   # ç
}

foreach ($key in $fixes.Keys) {
    $content = $content.Replace($key, [string]$fixes[$key])
}

# Also handle the viewer-artifact pattern seen in view_file output for apostrophes
# The actual bytes in file for ' after double-encoding: C3 A2 C2 80 C2 99
# Read as UTF-8 this gives: â€™  — already covered above

# Additional pass for arrow  →  which may appear as  â†'  (U+2192 double-encoded)
# UTF-8 for → is E2 86 92; read as 1252: â†' ; then written as UTF-8: C3 A2 E2 80  ...
# Direct byte approach safer:

$content = $content.Replace('â†'', [string][char]0x2192)
$content = $content.Replace('Ã¢â€ â€™', [string][char]0x2192)

# Catch LET'S pattern specifically
$content = $content.Replace("LETâ€™S", "LET'S")
$content = $content.Replace("don't", "don't").Replace("donâ€™t", "don't")
$content = $content.Replace("it's", "it's").Replace("itâ€™s", "it's")
$content = $content.Replace("I'm", "I'm").Replace("Iâ€™m", "I'm")
$content = $content.Replace("doesn't", "doesn't").Replace("doesnâ€™t", "doesn't")

[System.IO.File]::WriteAllText($file, $content, $utf8NoBom)
Write-Host "Done. Bytes: $((Get-Item $file).Length)"
