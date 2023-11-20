#review
#Create a function called greet()
# Simple Function
def greet():

    #Write 3 print statements inside the function
    print("Hello",)
    print("How do you do?")
    print("Isn't the weather nice today?")

#Call the greet() fuction and run the code
greet()

#Function that allows for input
def greet_with_name(name): #Name == parameter
    print(f"Hello {name} ",)
    print(f"How do you do {name} ?")
    print(f"Isn't the weather nice today {name} ?")

greet_with_name("Uri Gakuru")  #The double quotes to call the function Argument for intergers no quotes
#"Uri Gakuru" is an argument in this case


#Functions with more than one input

def greet_with(name, location):
    print(f"Hello {name} from {location} ",)
    print(f"How do you do {name} ?")
    print(f"Isn't the weather nice today in {location} ?")

greet_with(location="Ikinu", name="Uri Gakuru")