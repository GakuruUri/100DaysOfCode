# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_nae'] = last
#     return user_info


# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)


# """ 
# 8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

# """

# def build_profile(first, last, **user_info):
#     """Build a  dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_info = build_profile('robin', 'wagner', location='berlin', language='python', mood='great')
# print(user_info)


# '''
# 9-3. Users:
# Make a class called User.
# Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
# '''


# class User:
#     # A simple user class
    
#     def __init__(self, first_name, last_name, location, age):
#         #Initialize user calss and attributes
#         self.first_name = first_name
#         self.last_name = last_name
#         self.location = location
#         self.age = age
        
        
#     def describe_user(self):
#         # Describe a user
#         print(f"The user's name is {self.first_name} {self.last_name}.")
#         print(f"The user is {self.age} years old and lives in {self.location}.")
        
        
#     def greet_user(self):
#         # Greet a user
#         print(f"Hello, {self.first_name} {self.last_name}!")
        
        
# user_1 = User('Bob', 'the builder', 'London', 42)
# user_1.describe_user()
# user_1.greet_user()

# print("_____")


# user_2= User('Uri', 'Gakuru', 'Ikinu', 37)
# user_2.describe_user()
# user_2.greet_user()




'''
9-5. Login Attempts: 
Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
'''


class User:
    # A simple user class
    
    def __init__(self, first_name, last_name, location, age):
        #Initialize user calss and attributes
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0
        
        
    def describe_user(self):
        # Describe a user
        print(f"The user's name is {self.first_name} {self.last_name}.")
        print(f"The user is {self.age} years old and lives in {self.location}.")
        
        
    def greet_user(self):
        # Greet a user
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        #Increament number of login attempts by one.
        self.login_attempts += 1
        

    def reset_login_attempts(self):
        #reset login attempts to zero 0
        self.login_attempts = 0

user = User('John', 'Doe', 'Boston', 35)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")


user.reset_login_attempts()
print(f"Login attempts (after reset): {user.login_attempts}")


