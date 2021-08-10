"""
@file:   10.属性包装
@author: linuxzhen520@163.com
@date:   2020/05/27
@desc:
"""

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         if 0 <= age <= 150:
#             self.age = age
#         else:
#             raise ValueError("年龄范围不正确")
#
#
# p1 = Person("cali", 10)
# print(p1.name, p1.age)
# # 需求：200 不行，代码
# p1.age = 200
# print(p1.age)


# # 1. 代码冗余
# # 2. age 应该是一个属性 => 设置方法来设置的
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         if 0 <= age <= 150:
#             self.age = age
#         else:
#             raise ValueError("年龄范围不正确")
#
#     def set_age(self, age):
#         if 0 <= age <= 150:
#             self.age = age
#         else:
#             raise ValueError("年龄范围不正确")
#
#     def get_age(self):
#         return self.age
#
# p1 = Person("cali", 10)
# print(p1.name, p1.age)
# # 需求：200 不行，代码
# p1.set_age(200)
# print(p1.age)


# # 1. 代码冗余
# # 2. age 应该是一个属性 => 设置方法来设置的
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.check_age(age)
#
#     def set_age(self, age):
#         self.check_age(age)
#
#     def get_age(self):
#         return self.age
#
#     def check_age(self, age):
#         """检查age是否合法"""
#         if 0 <= age <= 150:
#             self.age = age
#         else:
#             raise ValueError("年龄范围不正确")
#
# p1 = Person("cali", 100)
# print(p1.name, p1.age)
# # # 需求：200 不行，代码
# p1.set_age(100)
# print(p1.age)

# # 1. 代码冗余
# # 2. age 应该是一个属性 => 设置方法来设置的
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = self.check_age(age)
#
#     def set_age(self, age):
#         self.age = self.check_age(age)
#
#     def get_age(self):
#         return self.age
#
#     @staticmethod
#     def check_age(age):
#         """检查age是否合法"""
#         if 0 <= age <= 150:
#             return age
#         else:
#             raise ValueError("年龄范围不正确")
#
# p1 = Person("cali", 100)
# print(p1.name, p1.age)
# # # 需求：200 不行，代码
# p1.set_age(100)
# print(p1.age)


# 属性包装 => 有一个方法 => 包装 => 用起来就像一个属性一样
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = self.check_age(age)

    # 当包装age之后，自动生成几个装饰器。age.setter, age.deleter...
    # age方法一定要返回一个结果 print(p1.age) =>
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = self.check_age(value)

    # @age.deleter
    # def age(self):
    #     del self._age

    @staticmethod
    def check_age(age):
        """检查age是否合法"""
        if 0 <= age <= 150:
            return age
        else:
            raise ValueError("年龄范围不正确")

# age应该是一个属性。
# 为什么要做属性包装 =>
p1 = Person("cali", 100)
print(p1.name, p1.age)
# 将age方法包装成一个属性
p1.age = 10   # 提示年龄范围不正确
print(p1.age)
p1.__age = 1000
print(p1.age)  # 10
print(dir(p1))
