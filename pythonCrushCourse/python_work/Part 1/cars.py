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


'''
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.

'''
def make_car(manufucturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufucturer'] = manufucturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)






