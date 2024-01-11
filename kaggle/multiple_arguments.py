"""
So far, you have learned how to define a function with just one argument. To define a function with multiple arguments, you only need to add more arguments inside the parentheses in the function head and separate them with a comma.

We do this with the get_pay_with_more_inputs() function below, which calculates a weekly paycheck based on three arguments:

num_hours - number of hours worked in one week
hourly_wage - the hourly wage (in $/hour)
tax_bracket - percentage of your salary that is removed for taxes

"""

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    #Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    #After-tax pay
    pay_aftertax = pay_pretax * ( 1 - tax_bracket)
    return pay_aftertax

"""
Then, to call the function, you need to provide one value for each input, again separated by a comma.

In the code cell below, we calculate the pay after taxes for someone who works 40 hours, makes $24/hour, and is in a 22% tax bracket.
"""

higher_pay_aftertax = get_pay_with_more_inputs(40, 24, 0.22)
print(higher_pay_aftertax)


same_pay_fulltime = get_pay_with_more_inputs(40, 15, .12)
print(same_pay_fulltime)