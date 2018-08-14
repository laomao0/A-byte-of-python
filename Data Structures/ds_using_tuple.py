# tuple - immutable(you can not modify tuples) 元组就是不能修改数量的List
# tuples are used to hold together mmultiple objects
# tuple is similar to list, but without extensive functionality
# I would recommend always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.
zoo = ('python', 'elephant', 'penguin')  # zoo is tuple
print('Number of animals in the zoo is', len(zoo))


new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])  # index operator
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))