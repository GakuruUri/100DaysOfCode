
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
9-1. Restaurant:
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually,
and then call both methods.
'''

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
        

restaurant = Restaurant('Kwa Mathe', 'Kibandaski foods')
print(f"Restaurant name: {restaurant.restaurant_name}.")
print(f"Restaurant cuisine: {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant






'''
9-2. Three Restaurants: Start with your class from Exercise 9-1.
Create three different instances from the class,
and call describe_restaurant() for each instance.
'''
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
        
'''
restaurant = Restaurant('Kwa Mathe', 'Kibandaski foods')
print(f"Restaurant name: {restaurant.restaurant_name}.")
print(f"Restaurant cuisine: {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant
'''

french_restaurant = Restaurant('Brasserie', 'French')
italian_restaurant = Restaurant('Luigis', 'Italian')
chinese_restaurant = Restaurant('Beijing Temple', 'Chinese')

french_restaurant.describe_restaurant()
print("_____")

italian_restaurant.describe_restaurant()
print("_____")

chinese_restaurant.describe_restaurant()
print("_____")



'''
9-3. Users:
Make a class called User.
Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
'''


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
        
        
user_1 = User('Bob', 'the builder', 'London', 42)
user_1.describe_user()
user_1.greet_user()

print("_____")


user_2= User('Uri', 'Gakuru', 'Ikinu', 37)
user_2.describe_user()
user_2.greet_user()

































