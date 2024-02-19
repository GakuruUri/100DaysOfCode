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


print("\nApplying rstrip() after we call read_text()")
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

print(contents)

print("\n===Reading a line at a time===")

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
