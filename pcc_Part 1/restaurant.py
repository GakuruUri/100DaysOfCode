'''
# 9-1. Restaurant:
# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually,
# and then call both methods.


# class Restaurant:
#     # A simple class describing a restaurant
    
#     def __init__(self, restaurant_name, cuisine_type):
#         # Describe the restaurants name and cuisune type
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
        
        
#     def describe_restaurant(self):
#         # Describe our reaturant/print a summary of our restaurant.
#         #print(f"Kwa {self.restaurant_name} serves mostly {self.cuisine_type} dishes.")
#         print(f"The restaurant is called {self.restaurant_name}.")
#         print(f"The cuisine type is {self.cuisine_type}.")
        
        
#     def open_restaurant(self):
#         #Print a message indicating that we are open
#         #print(f"{self.restaurant_name} is open for business.")
#         print(F" The restaurant {self.restaurant_name} is open.")
        

# restaurant = Restaurant('Kwa Mathe', 'Kibandaski foods')
# print(f"Restaurant name: {restaurant.restaurant_name}.")
# print(f"Restaurant cuisine: {restaurant.cuisine_type}.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant
'''




# '''
# 9-2. Three Restaurants: Start with your class from Exercise 9-1.
# Create three different instances from the class,
# and call describe_restaurant() for each instance.
# '''

# class Restaurant:
#     # A simple class describing a restaurant
    
#     def __init__(self, restaurant_name, cuisine_type):
#         # Describe the restaurants name and cuisune type
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
        
        
#     def describe_restaurant(self):
#         # Describe our reaturant/print a summary of our restaurant.
#         #print(f"Kwa {self.restaurant_name} serves mostly {self.cuisine_type} dishes.")
#         print(f"The restaurant is called {self.restaurant_name}.")
#         print(f"The cuisine type is {self.cuisine_type}.")
        
        
#     def open_restaurant(self):
#         #Print a message indicating that we are open
#         #print(f"{self.restaurant_name} is open for business.")
#         print(F" The restaurant {self.restaurant_name} is open.")
        

# restaurant = Restaurant('Kwa Mathe', 'Kibandaski foods')
# print(f"Restaurant name: {restaurant.restaurant_name}.")
# print(f"Restaurant cuisine: {restaurant.cuisine_type}.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant


# french_restaurant = Restaurant('Brasserie', 'French')
# italian_restaurant = Restaurant('Luigis', 'Italian')
# chinese_restaurant = Restaurant('Beijing Temple', 'Chinese')

# french_restaurant.describe_restaurant()
# print("_____")

# italian_restaurant.describe_restaurant()
# print("_____")

# chinese_restaurant.describe_restaurant()
# print("_____")




'''
9-4. Number Served: 
Start with your program from Exercise 9-1 (page 162). 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, 
and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.



class Restaurant:
    # A simple class describing a restaurant
    
    def __init__(self, restaurant_name, cuisine_type):
        # Describe the restaurants name and cuisune type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
        
    def describe_restaurant(self):
        # Describe our reaturant/print a summary of our restaurant.
        #print(f"Kwa {self.restaurant_name} serves mostly {self.cuisine_type} dishes.")
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
        
        
    def open_restaurant(self):
        #Print a message indicating that we are open
        #print(f"{self.restaurant_name} is open for business.")
        print(f" The restaurant {self.restaurant_name} is open.")
        

# restaurant = Restaurant('Kwa Mathe', 'Kibandaski foods')
# print(f"Restaurant name: {restaurant.restaurant_name}.")
# print(f"Restaurant cuisine: {restaurant.cuisine_type}.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant
        
    def set_number_served(self, guests):
        # Stet the number of customers to a given value.
        self.number_served = guests

    def increment_number_served(self, increment):
        # Add a give number to the number of guestes served.
        self.number_served += increment


restaurant = Restaurant('Brasserie', 'French')
print(f"Number served: {restaurant.number_served}")

restaurant.number_served = 200
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(300)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(110)
print(f"Number served: {restaurant.number_served}")
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
        print(f" The restaurant {self.restaurant_name} is open.")
        
        
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
        
ice_cream = IceCreamStand('ice cream parlor', 'ice cream', [' chocolate', ' banana', ' funky monkey', ' blueberry'])
ice_cream.display_flavor()
'''


'''
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.
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
        print(f" The restaurant {self.restaurant_name} is open.")









