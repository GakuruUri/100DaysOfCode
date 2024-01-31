
'''
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



'''
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.



def make_car(manufucturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufucturer'] = manufucturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

'''


'''
class Car:
    # A simple attempt to represent a car

    def __init__(self, make, model, year):
        # Initialize attributes to describe the car
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        # Return a neatly formatted descripive name.
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
'''

'''
# Modify the attribute's Value directly.
class Car:
    # A simple attempt to represent a car.

    def __init__(self, make, model, year):
        #Initialize attributes to describe the car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        # Return a neatly formatted name
        long_name = f"{self.year} {self.model} {self.year}"
        return long_name
    
    def read_odometer(self):
        #Print a statement showing the car's mileage
        print(f"This car has {self.odometer_reading} mile on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Modify the attribute's Value directly.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
'''


'''
# Modify an attribute value through a method.

class Car:
    # A simple attempt to represent a car.

    def __init__(self, make, model, year):
        #Initialize attributes to describe the car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        # Return a neatly formatted name
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name
    
    def read_odometer(self):
        #Print a statement showing the car's mileage
        print(f"This car has {self.odometer_reading} mile on it.")

    
    # Modify an attribute value through a method.
    def update_odometer(self, mileage):
        # Set the odometer reading to a given value
        # Reject the change if it attempts to roll the odometer back.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(21)
my_new_car.read_odometer()
'''



# Incrementing an Attribute's Value through a method.

class Car:
    # A simple attempt to represent a car.

    def __init__(self, make, model, year):
        #Initialize attributes to describe the car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        # Return a neatly formatted name
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name
    
    def read_odometer(self):
        #Print a statement showing the car's mileage
        print(f"This car has {self.odometer_reading} mile on it.")

    
    # Modify an attribute value through a method.
    def update_odometer(self, mileage):
        # Set the odometer reading to a given value
        # Reject the change if it attempts to roll the odometer back.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    
    def increment_odometer(self, miles):
        # Add the given amaount to the odometer reading
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())


# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(21)
# my_new_car.read_odometer()










