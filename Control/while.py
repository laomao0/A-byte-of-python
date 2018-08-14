number = 23
running = True

while running:
    guess = int(input('Enter an integer :'))
    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a littele lower than that.')
else:  # this else if optional
    # This final else is optional
    print('The while loop is over.')
    # Do anything else you want to do here

print('Done')

# Note for C/C++ Programmers: Remember that you can have an else clause for while loop