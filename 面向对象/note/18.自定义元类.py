"""
@file:   18.自定义元类
@author: linuxzhen520@163.com
@date:   2020/05/28
@desc:
"""

# class MyType(type):
#     """MyType就是一个自定义元类"""
#     pass
#
# # 默认情况下,Animal是由type创建=>由于指定了metclass =>Animal类由MyType
# class Animal(metaclass=MyType):
#     pass
#
# a = Animal()
# print(a)                      # Animal object
# print(type(a))                # Animal
# print(type(type(a)))          # MyType
# print(type(type(type(a))))    # type
#

# class A(object):
#     foo = 1
#
# class B(object):
#     Foo = 1
#
# a = A()
# b = B()
# print(a, b)

# 定义类的时候，希望在类中一定要包含一个类属性foo，创建失败


# # 自定义元类
# class MyType(type):
#     # 创建类
#     # def __new__(cls, *args, **kwargs):
#     #     print(cls, args, kwargs)
#     # 参数1: 类名 => str
#     # 参数2：父类 => tuple
#     # 参数3：类中的属性和方法 => dict => 方法名：方法
#     def __new__(cls, name, bases, attrs):
#         """创建并返回一个类"""
#         # print(cls,  name, bases, attrs)
#         # 一定要返回一个对象(类)
#         # return type.__new__(cls, name, bases, attrs)
#         return super().__new__(cls, name, bases, attrs)
#
#     def __init__(self, name, bases, attrs):
#         """
#         对刚刚创建的类做一些初始化操作
#         如果没有重写__init__ => 自动找父类__init__
#         如果重写了__init__， 不会自动调用父类__init__, 手动调用父类的__init__
#         """
#         # print(self, name, bases, attrs)
#         super().__init__(name, bases, attrs)
#
#
# # 父类 => 初始化操作 self.name = name
# # 子类 => 初始化操作 pass
#
# # 使用class 定义类A的时候，实际上
# class A(metaclass=MyType):
#     def __init__(self, name):
#         self.name = name
#
# print(A)
#
# a = A(name="cali")
# print(a, type(a), type(type(a)))
#
# # B = MyType("B", (), {'__module__': '__main__', '__qualname__': 'A'})
# # print(B)


# class MyType(type):
#     """
#     限制创建的类中一定要包含foo类属性
#     """
#
#     # def __init__(self, name, bases, attrs):
#     #     """
#     #     对刚刚创建的类做一些初始化操作
#     #     如果没有重写__init__ => 自动找父类__init__
#     #     如果重写了__init__， 不会自动调用父类__init__, 手动调用父类的__init__
#     #     """
#     #     if 'foo' not in attrs:
#     #         raise ValueError("类中必须定义一个foo属性")
#     #     super().__init__(name, bases, attrs)
#
#     def __new__(cls, name, bases, attrs):
#         """创建并返回一个类"""
#         if 'foo' not in attrs:
#             raise ValueError("类中必须定义一个foo属性")
#         return super().__new__(cls, name, bases, attrs)


#
# class A(metaclass=MyType):
#     """成功"""
#     foo = 1
#     def Cat(self):
#         pass
# # A => foo, cat
#
# a = A()
# print(a, a.foo)
#
# class B(metaclass=MyType):
#     """失败"""
#     Foo = 1
# # B => foo


# class MyTpye(type):
#     def __new__(cls, name, bases, attrs):
#         # key:value
#         # attr = {i.lower():attrs[i] for i in attrs.keys()}
#         # attrs = attr
#         # return super().__new__(cls, name, bases, attrs)
#         attr = {i.lower(): attrs[i] for i in attrs.keys()}
#         return super().__new__(cls, name, bases, attr)
#


#
#
# class A(metaclass=MyTpye):
#     Soo = 1
#     def _A(self):
#         print("我是一个方法")
#
#
# print(A.soo)
# a = A()
# print(a.soo)
# a._a()




# from abc import ABCMeta
# from django.db import models
# class UserInfo(models.Model):
#     pass
#     class Meta:
#         app_label = "xxx"


# 为什么在这里不可以创建这个类呢？
# userInfo

# 元类是什么，有什么用
# 自定义元类如何定义

class MyTpye(type):
    def __init__(self, *args , **kwargs):
        print("初始化类")

class A(object, metaclass=MyTpye):
    def __init__(self):
        print("初始化实例")

a = A()
# object => __init__, __new__ => 创建A的实例用object
# MyType => __init__, __new__ => 创建类(A)的时候用Mytype
# 定义类的时候就会执行元类的初始化方法和new方法吗 => 对



