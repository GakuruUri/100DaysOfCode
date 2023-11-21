cars = ['bmw', 'audi', 'toyota', 'subaru']


print(sorted(cars))

# Sorting a list gives parmanet changes
cars.sort()
print(cars)

# This also results in parmanet changes.
cars.sort(reverse=True)
print(cars)
