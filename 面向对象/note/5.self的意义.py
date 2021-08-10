"""
@file:   5.self的意义
@author: linuxzhen520@163.com
@date:   2020/05/21
@desc:
"""

# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         """查看实例的信息"""
#         print(self)
#         # print(f"我是{}")
#
# p1 = Person("Cali")
# p2 = Person("Feng")
# # p1.info() = p1 = self
# p1.info()
# print(p1)
#
# # p2.info() = p2 = self
# p2.info()
# print(p2)
#
# # 当调用实例方法的时候，self被赋值成当前调用的实例。


class Person(object):
    def __init__(self, name):
        self.name = name

    def info(self):
        """查看实例的信息"""
        print(self.name)
        print(self)

    def info2(this):
        """查看实例的信息"""
        print(this)


    def info3():
        """查看实例的信息"""
        print("haha")

p1 = Person("Cali")
# p1.info() = p1 = self
p1.info() # Person.info(p1)  # p1 => self
Person.info(p1)
Person.info3()

# 当调用实例方法的时候，self被赋值成当前调用的实例。
# self可以改成其他的任何名字。建议约定俗成的名字self
# 在实例中方法中，self是否可以省略 => 不行  p1.info() => Person.info(p1)

class A(object):
    def info(self):
        print(self)

class B(A):
    def info2(self):
        print(self)

b = B()
b.info() # B的实例 => b
a = A()
a.info() # A的实例 => a

