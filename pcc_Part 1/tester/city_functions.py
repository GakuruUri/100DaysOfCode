"""
11-1.  City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form 
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py, and save this file in a new folder so pytest won’t try to run the
tests we’ve already written.
Create a file called test_cities.py that tests the function you just wrote.
Write a function called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run the
test, and make sure test_city_country() passes.

"""
# def city_country(city, country):
#     """Return a string like 'Santiao, Chile'."""
#     return f"{city.title()}, {country.title()}"

# A collection of functions for working with cities.

"""
11-2 .  Population: Modify your function so it requires a third parameter, population.
It should now return a single string of the form City, Country – population xxx,
such as Santiago, Chile – population 5000000. Run the test again, and make sure 
test_city_country() fails this time.
Modify the function so the population parameter is optional. Run the test, 
and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies 
you can call your function with the values 'santiago', 'chile', and 'population
=5000000'. Run the tests one more time, and make sure this new test passes
"""

# def city_country(city, country, population):
#     """Return a string like 'Santiago, Chile - population 5000000'."""
#     output_string = f"{city.title()}, {country.title()}"
#     output_string += f" -population {population}"
#     return output_string
# # The above produces an error:


"""A collection of functions for working with cities."""

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population: {population}"
    return output_string