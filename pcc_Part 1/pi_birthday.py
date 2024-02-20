from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()


birthday = input("Enter yyour birthday in the format ddmmyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


print("\n==== Simpler Birthday =====")

from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()


pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday in the format ddmmyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")