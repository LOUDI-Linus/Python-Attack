"""
@file: 各种方法
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/21
@decs

"""
"""
方法
    实例普通方法
    静态方法   
            如果一个类中定义了一个方法，没有用到实例的数据和类的数据
    类方法
"""

# class Animal(object):
#     pass
#
# class Pig(Animal):
#     a="aaaaaaaaaaaaaa"
#     b="bbbbbbbbbbbbbb"
#
#     "静态发法-----装饰器 @开头后加英文"
#     @staticmethod
#     # 没有用到self
#     def xxx():
#         print("123")
#
#
#     @classmethod
#     def a_classmethod(cls):
#         print(cls)
#
#     def aaa(self):
#         print(self.a)
#
#
# p1 = Pig()
# Pig.xxx()   # 静态方法 => Pig.xxx()，不会把当前实例传递方法
# p1.a_classmethod()    # 静态方法 => Pig.p_staticmethod()，不会把当前实例传递方法
import platform

class BasePlugin(object):
    def os_platform(self):
        output = platform.system()
        return output

    def os_version_linux(self):
        return