'''
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
'''


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


def make_pizza(*toppings):
    # Summarize the pizza we are about to make.
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Position and Arbitrary Arguments
def make_pizza(size, *toppings):
    # Summarize the pizza we are about to make.
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"-{toppings}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')








