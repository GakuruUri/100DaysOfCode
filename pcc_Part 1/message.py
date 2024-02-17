def display_message():
    print("I'm learning about functions in this chapter.")
    
display_message()


'''
8-9. Messages: 
Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
'''

def show_message(messages):
    """Print text messages"""
    for message in messages:
        print(message)
        
messages = ['Hi', 'How are you?', 'Hello, there!']
show_message(messages)
        


'''
8-10. Sending Messages: 
Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message 
to a new list called sent_messages as it’s printed. After calling the function, 
print both of your lists to make sure the messages were moved correctly.
'''
def show_messages(messages):
    """Print text messages"""
    for message in messages:
        print(message)
        
# Show_messages(messages)

def send_messages(messages, sent_messages):
    """Print messages and move them to list"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ['Hi', 'How are you?', 'Hello, there!']
sent_messages = []

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)



""" 
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the 
riginal list has retained its messages.
"""
# You achieve this by addidng a slicer [:]


def show_messages(messages):
    """Print text messages"""
    for message in messages:
        print(message)
        
# Show_messages(messages)

def send_messages(messages, sent_messages):
    """Print messages and move them to list"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ['Hi', 'How are you?', 'Hello, there!']
sent_messages = []

send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)









