print("\nWrite a single line.\n")
from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming")


print("\nWrite multiple lines.\n")
from pathlib import Path

contents = "I love programming. \n"
contents += "I love creating new games. \n"
contents += "I also love finding meaning in large datasets. \n"


path = Path("programming.txt")
path.write_text(contents)




