def print_max(a, b):  # parameter
    if a > b:
        print(a, 'is maximum')
        a[0] = 10
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# directly pass literal values

print_max(3, 4)  # arguments

x = [6]
y = [5]

# pass variables as arguments
print_max(x, y)
print("x = {}; y = {}".format(x,y))

# The names given in the function are called parameters
# The value you supply in the function call are called arguments
