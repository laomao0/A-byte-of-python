# Sets are unordered collections of simple objects.
# There are used when the existence of an object in a collection is
# more important than the order or how many times it occurs
bri = set(['brazil', 'russia', 'india'])
print('india' in bri)

print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))

bri.remove('russia')

print(bri & bric)

