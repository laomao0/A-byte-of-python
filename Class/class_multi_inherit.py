class People(object):
    # public attributes
    name = ''
    age = 0
    # private attributes
    __weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("Name:{} Age:{} ".format(self.name, self.age))


# 单继承
class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        super(Student, self).__init__(name, age, weight)
    # 方法2 使用名称
        People.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("Name:{} Age:{} Grade:{} ".format(self.name, self.age, self.grade))
        # 同样的， __weight是类people的私有成员，所以在student中也是不能访问的


# 另外一个类，多重继承之前的准备
class Speaker(object):
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("Name:{} Topic:{}".format(self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("Tim", 25, 80, 4, "Python")
test.speak()