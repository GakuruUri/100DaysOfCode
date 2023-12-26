prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "



while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd like to go to {city.title()}!")


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



