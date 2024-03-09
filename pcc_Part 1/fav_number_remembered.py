"""
10-12. Favorite Number Remembered: Combine the two programs you wrote in
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.

"""

'''
from pathlib import Path
import json

path = Path('fav_number.json')

if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"Your favorite number is {fav_number}")
    
else:
    fav_number = input("Please enter your favorite number")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print(fav_number)
'''


# try-except error handling
from pathlib import Path
import json

path = Path('fav_number.json')
try:
    contents = path.read_text()
    
except FileNotFoundError:
    fav_number = input("What's your favorite number: ")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
    
else:
    fav_number = json.loads(contents)
    print(f"I know your favorite number! It's {fav_number}. ")
