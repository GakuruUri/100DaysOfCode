# Create a variable.
full_name = " erick kantona  "
""" 
Use the .upper(), .lower(), .rstrip(), lstrip() and .strip() methods in your code
"""
print(f"Hello, {full_name.upper()} would you like to learn python today?")
print(f"Hello, {full_name.lower()} would you like to learn python today?")
print(f"Hello, {full_name.strip().title()} would you like to learn python today?")

famous_name = "albert eInstein"
print(f'\n\t{famous_name.title()} once said, "Gooooooal"')

file_name = 'python_notes.txt'
new_file_name = file_name.removesuffix('txt')
print(file_name, new_file_name)