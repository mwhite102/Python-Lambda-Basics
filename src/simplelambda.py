# define a regular function
def add(x, y):
    return x + y

# define an equivalent lambda function
add_lambda = lambda x, y: x + y

# test the regular function and the lambda function
print(add(1, 2))
print(add_lambda(1, 2))

# output
3
3