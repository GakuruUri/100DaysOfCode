for value in range(1, 5):
    print(value)
    
    
numbers = list(range(1, 6))
print(numbers)


even_numbers = list(range(2, 11, 2))
print(even_numbers)



squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
print(squares)

# Counting to 20 and all odds upto 20
twentys = []
for value in range(1, 21, 2):
    twentys.append(value)
print(twentys)

# Counting 1 to a million
num_milli = list(range(1000001))
print(sum(num_milli))
print(min(num_milli))
print(max(num_milli))
print(num_milli)

# Multiples of 3 from 0 to 31
threes = list(range(3, 31, 3))
print(threes)



cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
    
print(cubes)