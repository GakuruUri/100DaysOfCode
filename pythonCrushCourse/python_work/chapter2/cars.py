cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
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
