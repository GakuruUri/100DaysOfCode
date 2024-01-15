
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


def build_profile(first, last, **user_info):
    #Build a dictionary containing everything we know about a user.
    user_info['first_name'] = first
    user_info['last_name'] = last    
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


















