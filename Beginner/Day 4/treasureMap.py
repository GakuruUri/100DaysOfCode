#Hide treasure in a 2D map

# This map contains a nested list.
# When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have used new lines (\n) to format the three rows into a square, like this

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to hide the treasure? ")

vertical = int(position[0])
horizontal = int(position[1])


spot = [map[vertical -1][horizontal - 1]] = "X"

print(f"{row1}\n{row2}\n{row3}")
# print(map[vertical -1])

