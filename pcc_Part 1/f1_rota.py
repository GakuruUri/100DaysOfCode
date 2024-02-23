from pathlib import Path

path = Path('f1_rota.txt')


prompt = "\nHi, 2024 F1 driver rota. "
prompt += "\nEnter 'quit' if you have entered all the drivers. "

driver_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break
    
    print(f"{name.title()} added to rota.")
    driver_names.append(name)
    
    
# Build a string where "\n" is added after each name.
file_string = ''
for name in driver_names:
    file_string += f"{name}\n"
    
    
path.write_text(file_string)