"""
@file:   10.方法的选择
@author: linuxzhen520@163.com
@date:   2020/05/27
@desc:
"""

class Person():
    school = "hnnd"
    student = True

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @staticmethod
    def a():
        print("这是一个静态方法")

    @classmethod
    def b(cls):
        print("这是一个类方法")
        cls.school = "gongda"

    def c(self):
        print(self.name)

    def d(self):
        """
        即用到实例数据，又用到类数据（封装成一个类方法，然后调用）
        """
        print(self.name)
        self.b()

    def age(self):
        return self.__age

p1 = Person("cali", 18)
p1.d()
print(p1.school)



class Time(object):
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def hours(self):
        return  self.__hours

    @classmethod
    def c(cls, obj):
        # hours() missing 1 required positional argument: 'self'
        return cls.hours(obj)



t = Time(11, 7, 20)
t2 = Time(12, 7, 20)
print(t.c(t2))

# 邓济洲： 
#     类 -> 方法
#     a. 如果这个方法中，没有到实例的数据(属性和方法) self.name，也没有用到类数据(属性和方法) => 静态方法
#     b. 如果在方法中，用到了Person.school => 类属性，为了避免硬编码， => 类方法
#     c. 如果在方法中，用到了实例相关的信息 => 实例方法