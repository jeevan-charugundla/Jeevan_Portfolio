import re

with open('index.html', 'rb') as f:
    b = f.read()

original_size = len(b)

# The corruption pattern is: C3 A2 + [EF BF BD and/or 2C 22]+ + letter
# This came from: ' (U+2019, E2 80 99) read as latin-1 giving â€™
# then written as UTF-8 giving C3A2 E2 82 AC E2 84 A2
# After further corruption some bytes became EF BF BD (replacement char)
# The regex below catches all remaining instances before vowel+consonant combos

# Direct known-good substitutions
fixes = [
    # â€™  (E2 80 99 = ' double-encoded) — most common form
    (b'\xc3\xa2\xe2\x82\xac\xe2\x84\xa2', b'\xe2\x80\x99'),
    # â€™ another variant with broken middle byte
    (b'\xc3\xa2\xe2\x82\xac\x99', b'\xe2\x80\x99'),
    # â€œ  (E2 80 9C = " left quote)
    (b'\xc3\xa2\xe2\x82\xac\xc5\x93', b'\xe2\x80\x9c'),
    # â€   (E2 80 9D = " right quote)
    (b'\xc3\xa2\xe2\x82\xac\xc2\x9d', b'\xe2\x80\x9d'),
    # â€"  (E2 80 93 = en-dash)
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9c', b'\xe2\x80\x93'),
    # â€"  (E2 80 94 = em-dash)
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'\xe2\x80\x94'),
    # â†'  (E2 86 92 = rightwards arrow)
    (b'\xc3\xa2\xe2\x80\xa0\xe2\x80\x99', b'\xe2\x86\x92'),
    # â€¦  (E2 80 A6 = ellipsis)
    (b'\xc3\xa2\xe2\x82\xac\xc2\xa6', b'\xe2\x80\xa6'),
]

for bad, good in fixes:
    b = b.replace(bad, good)

# Remaining EF BF BD (replacement char U+FFFD) sequences near apostrophe context
# Pattern: C3 A2 [junk bytes] followed by ASCII letter
# Replace these with correct apostrophe + the letter
def replace_corrupt_apostrophe(m):
    letter = m.group(1)
    return b'\xe2\x80\x99' + letter

b = re.sub(b'\xc3\xa2[\xef\xbf\xbd\x2c\x22\x80-\xff]{1,8}([STstmrvnd])', replace_corrupt_apostrophe, b)

print(f'original={original_size}, fixed={len(b)}')

# Verify LET'S
idx = b.find(b'BUILD')
print('near BUILD:', b[max(0,idx-25):idx+5].hex())

with open('index.html', 'wb') as f:
    f.write(b)
print('done')
