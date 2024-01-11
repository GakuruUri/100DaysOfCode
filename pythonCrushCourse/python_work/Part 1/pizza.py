
pizzas = ["margarita", "chicken", "beef"]
for pizza in pizzas:
    # print(pizza)
    print("\n================================")
    print(f"I really like {pizza.title()} pizza")
    
    
print("\n================================")
print("Gah damn it, i really really love pizza!\n")


jungle_cats = ["lion", "tiger", "leopard"]
for cat in jungle_cats:
    print(f" A {cat.title()}, would be a bloody great pet\n")
    
    
print("All these cats would also turn and fuckin' eat you")

friend_pizzas = pizzas[:]

pizzas.append('hawaian')
friend_pizzas.append('marcon')


print("My favorite pizzas: ")
for pizza in pizzas[:]:
    print(pizza)
    
    
print("My friend’s favorite pizzas are: ")
for pizza in friend_pizzas[:]:
    print(pizza)




# List in a Dictionary Day 17
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "WIth the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")



def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inche pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

