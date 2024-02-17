# Try it yourself 6.5
major_rivers = {
    'nile': 'uganda',
    'nyando': 'kenya',
    'athi': 'kenya'
}

for rivers in major_rivers:
    print(f"The {rivers.title()} is found in Africa")
    
    
for river in major_rivers.keys():
    print(river.title())

for river in major_rivers.values():
    print(river.title())
