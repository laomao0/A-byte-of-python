def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


# keyword parameters: 1. ignore order of variable 2. specify variable assignment

func(3, 7)
func(25, c=24)
func(c=50, a=100)

