# A list is a mutable data type, i.e. this type can be altered.
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase') # get the length of list


print('These items are:', end=' ')  # print end with a space not the usual line break
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')  # append a new element to the tail1 of list
# L.append(object)
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()  # sort elements in list
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]  # delete the first element
print('I bought the', olditem)
print('My shopping list is now', shoplist)




