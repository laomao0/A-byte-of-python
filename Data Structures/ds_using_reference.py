# use reference bind the name to the object
# simple assignment = refer
# full slicing = copy

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist is just another name pointing to the sane object!
# mylist is reference of shoplist
mylist = shoplist

# I purchased the first item, so I remove it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object

print('Copy by making a full slice')

# Make a copy by doing a full slice
# Copy will create two object which are independent
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different