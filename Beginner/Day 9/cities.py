travel_log = [                   #Create a list of Dictionaries that has nested lists
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited, times_visited, cities_visited):  #Create a new function 
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])  #The new function that was called
print(travel_log)