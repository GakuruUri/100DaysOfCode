"""
10 -11.  Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. 
Write a separate program that reads in this value and prints the message 
“I know your favorite number! It’s _____.
"""

from pathlib import Path
import json

fav_number = input("Enter your favorite number: ")

path = Path('fav_number.json')
contents = json.dumps(fav_number)
path.write_text(contents)

print("Thanks I'll remember that number.")