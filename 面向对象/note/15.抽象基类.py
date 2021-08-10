"""
@file:   15.抽象基类
@author: linuxzhen520@163.com
@date:   2020/05/27
@desc:

抽象 =>
基类 => 类的继承

把一个类定义成基类(父类) -> 对子类有某些限制
"""
#
# # 定义成抽象基类
# class Person(object):
#     # 声明成抽象方法，该方法中不需要写具体实现
#     # 具体实现由子类来实现
#     def a(self):
#         pass
#
#     def b(self):
#         pass
#
# class SubPerson1(Person):
#     def a(self):
#         #xxxxx
#         pass
#
# class SubPerson2(Person):
#     def a(self):
#         # xxx
#         pass

from abc import ABC, abstractmethod

class Animal(ABC):
    """继承自ABC => Animal抽象基类"""

    @abstractmethod
    def eat(self):
        """
            通过@abstractmethod装饰器，抽象方法
            在子类一定要重写该方法
        """
        pass

    def drink(self):
        print("我要喝水~~")

# # 抽象基类能否被直接实例化 => 否
# a = Animal()

# 正确的用法
class Person1(Animal):
    def eat(self):
        print("Person1要喝水")
p1 = Person1()
p1.eat()


# # 可以定义类，但是没法实例化
# class Person2(Animal):
#     pass
# p2 = Person2()
# p2.eat()
