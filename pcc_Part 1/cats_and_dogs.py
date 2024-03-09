"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block executes properly.
"""
from pathlib import Path

filenames = ['cats.txt', 'dogs.txt', 'cattle.txt']

for filename in filenames:
    print(f"\nReading file:{filename}")
    
    path = Path(filename)
    try:
        contents = path.read_text()
        
    except FileNotFoundError:
        print("Sorry i can't find that file.")
        # pass
        
    else:
        print(contents)
        
        
        
"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail
silently if either file is missing.
"""

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt', 'cattle.txt']

for filename in filenames:
    print(f"\nReading file:{filename}")
    
    path = Path(filename)
    try:
        contents = path.read_text()
        
    except FileNotFoundError:
        # print("Sorry i can't find that file.")
        pass
        
    else:
        print(contents)
     