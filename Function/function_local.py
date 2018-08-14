x = 50


def func(x):
    print('x is', x)
    x = 2  # local value change
    print('Changed local x to', x)


func(x)
print('x is still', x)

# 如果程序中的变量和函数中的形参名称一样，函数的形参是函数内部起作用的局部变量，不会影响程序的同名变量
