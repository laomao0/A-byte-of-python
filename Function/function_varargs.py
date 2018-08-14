def total(a=5, *numbers, **phonebook):
    print('a', a)

    # iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    # iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
# a = 10
# tuple number = { 0 1 2}
# dict phonebook = {Jack=1123, John=2231, Inge=1560}

# Declare a starred parameter such as *param - tuple
# Declare a double-starred parameters such as **param - dictionary
