from pathlib import Path

print("--- Reading the entire file.")
path = Path('learning_python2.txt')
contents = path.read_text()
print(contents)


print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'Assembly')
    print(line)