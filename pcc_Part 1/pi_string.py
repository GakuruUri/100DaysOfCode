from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line


print(pi_string)
print(len(pi_string))


print("\n ====== Using lstrip =======")
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

print("\n ====== pi to the millionth digit =======")

from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:100]} that's pi for you to the {100} times")
print(len(pi_string))










