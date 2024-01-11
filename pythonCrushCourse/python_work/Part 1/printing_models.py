'''
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


# Simulate printing each design until none is left
# Move each design to completed modelsafter printing

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model now...: {current_design}")
    completed_models.append(current_design)
   
    
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
    
    
'''    
    
    
# Extend the above using 2 functions for efficiency

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(commpleted_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)
    
    
    
# Preventing a function from modifying a list. you use a slice [:]
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until nonr are left.
    Move each design to completed_models after printing
    """    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    