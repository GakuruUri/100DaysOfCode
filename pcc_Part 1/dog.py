'''
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dogs's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
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


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a summary of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")






















