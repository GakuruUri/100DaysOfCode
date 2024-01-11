def add_three(input_var):
    output_var = input_var + 3
    return output_var


## HEADER - the function header defines the name of the function and its arguments
# Every function is composed of a header and body
# Every function header begins with def.
# The function name is add_three
# The argument is input_var - The argument is the name of the variable that will be used as input to the function.
# The function can have no arguments or it can have multiple arguments.
# for every function, the parentheses enclosing the function argument(s) nust be followed by A COLON :


## BODY
# The function body specifies the work that the function does.
# Every line of code must be indented
# The function does its work by running all the indented lines from top to bottom.

# It takes the argument as input in this example input_var
# the function creates a new variable output_var with the calculation output_var = input_var + 3
# Then the final code, the return statement, just returns the value output_var as the function's output.

# Run the function with 10 as input
new_number = add_three(10)

print(new_number)
