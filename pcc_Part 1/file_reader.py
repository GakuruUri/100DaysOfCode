from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

print(contents)


print("\nStrip/remove whitespace from the contents")

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()

print(contents)


print("\n..Applying rstrip() after we call read_text()")
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

print(contents)