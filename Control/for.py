for i in range(1, 5):
    # in C++, similar to for(int i = 0; i < 5; i++)
    print(i)
else:
    # the else part is optional
    print('The for loop is over')

a = list(range(5))
print(a)


# range(a,b) built-in range function, start from number 'a', up to the second number 'b',
# i.e. it does not include the second number
# range(1,5) = [1,5) =[1 2 3 4]
# range(1,5,2) step-size = 2; equal to [1 3 ]

# range generate only one number at a time
# list() can get the full list of numbers
# list(range(5)) = [0 1 2 3 4]
