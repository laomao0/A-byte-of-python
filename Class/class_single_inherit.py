class people(object):
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
class student(people):
    grade = ''

    def __init__(self, name, age, weight, grade):
        super(student, self).__init__(name, age, weight)
    # 方法2 使用名称
        people.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("Name:{} Age:{} Grade:{} ".format(self.name, self.age, self.grade))
        # 同样的， __weight是类people的私有成员，所以在student中也是不能访问的


s = student('ken', 10, 60, 100)
s.speak()
