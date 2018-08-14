x = 50


def func():
    global x  # declare x is global variable

    print('x is', x)
    x = 2  # change global x to 2
    print('Changed global x to', x)


func()
print('Value of x is', x)
