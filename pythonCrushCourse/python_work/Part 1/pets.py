pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Describe describe_pet in pets.py using keyword arguments
print("\n====Using keyword arguments =====   ")
def describe_pet(animal_type, pet_name):
    """Display infromation about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
describe_pet(pet_name='harry', animal_type='hamster')


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    

describe_pet('willie')
describe_pet(pet_name='poppy')
describe_pet(pet_name='kangaa', animal_type='mongoose').er.er.er.er.er.er.er

