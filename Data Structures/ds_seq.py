# Sequence
# list, tuple, strings are examples of sequences
# membership tests( in and not in expression) and indexing operations, slicing operation

shoplist = ['apple', 'mango', 'carrot', 'banana']  # list
name = 'swaroop'  # string

# Indexing or 'Subscription' operation #
print("Item 0 is", shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])  # calculated from the end of the sequency
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# Provide step size for slicing( the default step size is 1)
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])  # inverse order


