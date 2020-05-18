import os
from collections import Counter
counts = Counter()
for currentdir, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension] += 1
for extension, count in counts.items():
    print(f"{extension:8}{count}")
