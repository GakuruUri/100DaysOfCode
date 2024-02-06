
"""
def show_message(messages):
    for message in messages:
        print(message)      

messages = ['Hi', 'There you', 'Okay!']
show_message(messages)

"""
'''

def show_messages(messages):
    # Print Text messages
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    # Print messages and move them to a list.
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
        
        

messages = ['Hi', 'There you', 'Okay!']
sent_messages = []


send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
'''


'''
# Slicing

def show_messages(messages):
    # Print text messages
    for message in messages:
        print(message)
        
        
def send_messages(message, sent_messages):
    # Print messages and move them to list
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
        
messages = ['Hi', 'There you', 'Okay!']
sent_messages = []


send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

'''

'''
def make_pizza(*toppings):
    #Print the list of toppings that have been requested.
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''

'''
def make_pizza(*toppings):
    # Summarize the pizza we are about to make.
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''

'''
def build_profile(first, last, **user_info):
    #Build a dictionary containing everything we know about a user.
    user_info['first_name'] = first
    user_info['last_name'] = last    
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
'''

'''
def sandwich_ingredients(*args):
    #Print a summary of the sandwich being ordered.
    print("\nThese are the sandwich ingredients:")
    for arg in args:
        print(f"-{arg}")
        
        
sandwich_ingredients("=====")
sandwich_ingredients('salad', 'cucumber', 'chicken')
sandwich_ingredients('salad', 'cucumber', 'chicken', 'tuna')
'''

'''
def build_profile(first, last, **user_info):
    #Build a dictionary containing everything about a user:
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_info = build_profile('Uri', 'Gakuru', location='Ikinu', language = 'Python', mood='Shaky', drive='Future')
print(user_info)
'''

'''
def make_car(manufucturer, model, **car_info):
    #Build a dictionary containing everything we know about a car.
    car_info['manufucturer'] = manufucturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
'''

'''
class Dog:
    # A simple attempt to model a dog.
    
    def __init__(self, name, age):
        #Initialize name and age attributes
        self.name = name
        self.age = age
        
    def sit(self):
        #Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        #Simulate a dog rolling over in response to a command.
        print(f"{self.name} rolled over")
        
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)



print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()


print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
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
my_new_car = Car(2024, 'audi', 'a4')
print(my_new_car.get_descriptive_name())
'''




'''
9-1. Restaurant:
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually,
and then call both methods.



9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.


class Restaurant:
    # A simple class describing a restaurant
    
    def __init__(self, restaurant_name, cuisine_type):
        # Describe the restaurants name and cuisune type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
        
    def describe_restaurant(self):
        # Describe our reaturant/print a summary of our restaurant.
        #print(f"Kwa {self.restaurant_name} serves mostly {self.cuisine_type} dishes.")
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
        
        
    def open_restaurant(self):
        #Print a message indicating that we are open
        #print(f"{self.restaurant_name} is open for business.")
        print(F" The restaurant {self.restaurant_name} is open.")
        
        
class IceCreamStand(Restaurant):
    # A simple ice cream stand(Inheriting from the restaurant class)
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        # Initialize icecream stand
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def display_flavor(self):
        # Display icecream flavors
        print(f"The flavors are")
        for flavor in self.flavors:
            print(f"-{flavor}")
        
ice_cream = IceCreamStand('ice cream parlor', 'ice cream', ['chocolate', 'banana'])
ice_cream.display_flavor()

'''



'''
9-3. Users:
Make a class called User.
Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.


9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.


9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.




class User:
    # A simple user class
    
    def __init__(self, first_name, last_name, location, age):
        #Initialize user calss and attributes
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        
        
    def describe_user(self):
        # Describe a user
        print(f"The user's name is {self.first_name} {self.last_name}.")
        print(f"The user is {self.age} years old and lives in {self.location}.")
        
        
    def greet_user(self):
        # Greet a user
        print(f"Hello, {self.first_name} {self.last_name}!")

class Privileges:
    # A simple privileges class
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        # Display privileges
        print("Privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(User):
    # A simple admin class
    
    def __init__(self, first_name, last_name, location, age, privileges):
        # Initialize admin class and attributes
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.privileges = Privileges(privileges)
        
admin_1 = Admin('Adam', 'Admin', 'NYC', 28, ['can add post', 'can delete post', 'can ban user'])
admin_1.privileges.show_privileges()
'''




'''
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 65 if it isn’t already. Make
an electric car with a default battery size, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase in the car’s range.
'''




class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add a given amount of miles to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        distance = 0
        if self.battery_size == 75:
            distance = 260
        elif self.battery_size == 150:
            distance = 315

        print(f"This car can go about {distance} miles on a full charge.")

    def upgrade_battery(self):
        """Check battery and set capacity to 150."""
        if self.battery_size != 100:
            self.battery_size = 150


class ElectricCar(Car):
    """Represent every aspect of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

my_tesla = ElectricCar("tesla", "Model S", 2019)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()








