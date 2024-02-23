from pathlib import Path

path = Path('Guests.txt')
path.write_text(input("Please enter your name: "))


##########################################################

from pathlib import Path

path = Path('guests.txt')

name = input("Please enter your name: ")
path.write_text(name)