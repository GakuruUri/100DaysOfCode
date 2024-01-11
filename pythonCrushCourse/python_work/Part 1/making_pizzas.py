import pizza


pizza.make_pizza(16, 'pepperoni',)
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese,')

# You can import specific functions [Importing Specific Functions]
print("=== You can import specific functions [Importing Specific Functions] ==")
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias
print("=== Using as to Give a Function an Alias ==")
from pizza import make_pizza  as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print(" ===  Importing All Functions in a Module ===")

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

