
'''
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


# Simulate printing each model, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)


# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
'''
    

""" 
We can reorganize this code by writing two functions, each of which
does one specific job. Most of the code won’t change; we’re just structuring
it more carefully. The first function will handle printing the designs, and
the second will summarize the prints that have been made:
"""


'''

8-15. Printing Models: 
Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, 
and modify the file to use the imported functions.

import printing_functions


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)

printing_functions.show_completed_models(completed_models)

'''
 


''' 
8-16. Imports: 
Using a program you wrote that has one function in it, 
store that function in a separate file. Import the function into your main program file, 
and call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

'''
import pizza
pizza.make_pizza(16, 'pepperoni')


from pizza import make_pizza
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza import make_pizza as mp
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


import pizza as p
p.make_pizza(16, 'pepperoni')

from pizza import *
make_pizza(16, 'pepperoni')



