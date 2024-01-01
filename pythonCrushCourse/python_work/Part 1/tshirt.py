"""
T-Shirt: 
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""


def make_shirt(size, message):
    """Print size and message on your shirt"""
    print(f"\nWhat is your t-shirt size? {size.title()}.")
    print(f"Your t-shirt size is {size.title()} and you picked the message {message.capitalize()}.")
   
    
make_shirt('medium', 'Reggae man...')
make_shirt(message="hello world", size='large')    

# Option 2 for tshirt Learning python
print("================================================")
def make_shirt(size, message):
    """Print size and message"""
    print(f"The shirt is size {size} and shows the message {message}")
    
make_shirt(5, 'Hello, there!')
make_shirt(message='Hello, there!', size=5)


"""
Large Shirts: 
Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""

def make_shirt(message, size = 'large'):
    print(f"\nWhat is your t-shirt size? {size.title()}.")
    print(f"Your t-shirt size is {size.title()} and you picked the message {message.capitalize()}.")
    
make_shirt('medium','Reggae man')
make_shirt(message="Don't give up.")


# Option 2 for tshirt Learning python
print("================================================")
def make_shirt(size='L', message='I love Python.'):
    """Print size and message"""
    print(f"The shirt is size {size} and shows the message {message}")
    
make_shirt(5, 'Hello, there!')
make_shirt(message='Hello, there!', size=5)
make_shirt()




"""
Cities: 
Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""

def describe_city(city, country = 'Kenya'):
    print(f"{city.title()}, is in {country.title()}.")
    
describe_city('Nairobi')
describe_city(city='Mombasa')
describe_city(city='Tanganyika', country='Tanzania')