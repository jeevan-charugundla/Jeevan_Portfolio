# fix_encoding.ps1 — reverses the double-encoding damage
# The file is currently: UTF-8 bytes that were mis-read as Windows-1252 and re-written as UTF-8
# Fix: read as UTF-8 → re-encode to ISO-8859-1 (gets original bytes back) → decode those bytes as UTF-8

$file = 'index.html'

# Step 1: read the currently-broken file as UTF-8 (this gives us the mojibake string)
$broken = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

# Step 2: re-encode using iso-8859-1 to recover the original UTF-8 bytes
$originalBytes = [System.Text.Encoding]::GetEncoding('iso-8859-1').GetBytes($broken)

# Step 3: decode those bytes as proper UTF-8
$fixed = [System.Text.Encoding]::UTF8.GetString($originalBytes)

# Step 4: write back as clean UTF-8 (no BOM)
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($file, $fixed, $utf8NoBom)

Write-Host "Encoding fixed. File size: $((Get-Item $file).Length) bytes"
