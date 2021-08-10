"""
@file:   6.类的继承
@author: linuxzhen520@163.com
@date:   2020/05/21
@desc:
"""

# class A(object):
#     pass
#
# a = A()
# # 这个类有__init__方法吗
# print(dir(A))
# # 这些方法继承自object
#
# class B(object):
#     def __int__(self):
#         print("i am B __init__")
#         pass
#
# # 如果父类定义了一个aaa方法，子类也定义了一个aaa方法。
# # 使用子类自己定义的aaa方法。

class Animal(object):
    category = "animal"
    number = 0

    def breath(self):
        print(f"{self.category}需要呼吸！")

    def eat(self):
        print(f"{self.category}需要吃东西！")


    def __init__(self):
        # self.number = self.number+1
        Animal.number += 1


# class Person(Animal):
#     category = "person"
#     number = 0
#     pass


class Pig(Animal):
    category = "pig"
    number = 0

    def __init__(self):
        # self.number = self.number+1
        Pig.number += 1
        super().__init__()
        # super => 类 => super实例
        # Animal.number += 1
        # Animal.__init__(self)

    def eat(self):
        # 执行父类的eat
        super().eat()
        # 执行自己额外定义的内容
        print("每天吃3顿，一顿吃5kg")

# 硬编码 Pig.number += 1 => 类属性
# 灵活度不够。Pig => Pig

# Pig.number => 0
pig1 = Pig()
# Pig.number => 1
pig2 = Pig()
# Pig.number => 2
# pig1.number => 2
print(Pig.number)

a1 = Animal()
print(Animal.number)

pig1.breath()
a1.breath()
pig1.eat()
a1.eat()

# category => 属性、方法
#             类属性、实例属性
