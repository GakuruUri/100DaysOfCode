from pathlib import Path

print("\n==== Reading the file only ====")

path = Path('learning_python.txt')
contents = path.read_text()


print(contents)

print("\n==== Reading the file only and stripping whitespaces. ====")
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip().lstrip()
print(contents)


print("\n==== Reading the file only and looping through the lines. ====")
from pathlib import Path


path = Path('learning_python.txt')
contents = path.read_text()

# list_learning_python = []
lines = contents.splitlines()
for line in lines:
    print(line)
    # print(line.rstrip())
    # print(line.lstrip())
    # print(line.strip())
    # print(line.replace('Python', 'C'))
    # print(line.replace('Python', 'C').rstrip())
    # print(line.replace('Python', 'C').lstrip())
    # print(line.replace('Python', 'C').strip())
    # print(line.replace('Python', 'C').rstrip().lstrip())
    # print(line.replace('Python', 'C').rstrip().strip())
    # print(line.replace('Python', 'C').lstrip().strip())
    # print(line.replace('Python', 'C').strip().strip())
    # print(line.replace('Python', 'C').strip().lstrip())
    # print(line.replace('Python', 'C').strip().rstrip())
    # print(line.replace('Python', 'C').strip().rstrip().strip())
    # print(line.replace('Python', 'C').strip().rstrip().lstrip())

    # list_learning_python += line
    # list_learning_python.append(line)

# print(list_learning_python)
# print(contents)
# print(len(list_learning_python))
# print(len(contents))
