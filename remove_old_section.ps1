$lines = Get-Content 'index.html'
$keep = $lines[0..1536] + $lines[1742..($lines.Length-1)]
Set-Content 'index.html' -Value $keep -Encoding UTF8
Write-Host "Done. Lines remaining: $($keep.Length)"
