"""
# Working with multiple files at once.

from pathlib import Path

def count_words(path):
    #Count the approximate number of words in a file.
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
        
# path = Path('alice.txt')
# count_words(path)


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

"""

from pathlib import Path

def count_words(path):
    """ Count the approximate number of words in files """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    
    else:
        # Count the approximate number of words ina  a file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words. ")
        
        
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
