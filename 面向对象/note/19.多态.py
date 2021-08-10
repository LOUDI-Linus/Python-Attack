"""
@file:   19.多态
@author: linuxzhen520@163.com
@date:   2020/05/28
@desc:
    python是动态语言
    不关心数据是什么类型。
    只关心数据实现的功能有什么
"""
# class A():pass
#
# def sum(a, b):
#     # a.__add__(other)
#     return a+b
#
# print(sum(1,2))
# print(sum('a','b'))
# print(sum([0,1],[2,3]))
# print(sum(A(),1))

class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(self.name, ' Can Speak')
    @staticmethod
    def talk_with(obj):
        obj.talk()
class Cat(Animal):
    def talk(self):
        print(self.name,' Says Meow!')
class Dog():
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(self.name,' Says Woof!')
# 正常用法
dog = Dog("狗狗")
# dog.talk()
cat = Cat("猫猫")
# cat.talk()
# # 封装统一接口用法2
Animal.talk_with(dog)
Animal.talk_with(cat)
