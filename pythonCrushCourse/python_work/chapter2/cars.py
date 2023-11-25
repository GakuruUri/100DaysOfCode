cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nThe first three lines in the list are: ")
print(cars[:3])

print("\nThree items from the middle of the list are: ")
print(cars[1:4])

print("\nThe last three items in the list are: ")
print(cars[-3:])



print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

cars.reverse()
print(cars)

print("\nHere is the original list again:")
print(cars)

# Sorting a list gives parmanet changes
cars.sort()
print(cars)

# This also results in parmanet changes.
cars.sort(reverse=True)
print(cars)

