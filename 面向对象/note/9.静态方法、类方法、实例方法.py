"""
@file:   9.静态方法、类方法、实例方法
@author: linuxzhen520@163.com
@date:   2020/05/21
@desc:
"""


class Animal(object):
    category = "animal"
    number = 0

    def breath(self):
        print(self.category)
        print("需要呼吸！")

    def __init__(self):
        Animal.number += 1


class Pig(Animal):
    category = "pig"
    number = 0

    # 定义静态方法 => @staticmethod => 装饰器
    # 如果在一个类中定义了一个方法，没有用到实例的数据和类的数据, 可以成静态方法 => pycharm会提示你！
    @staticmethod
    def p_staticmethod(tag):
        print("这是Pig的一个静态方法", tag)

    # 定义一个类方法 => @classmethod
    # 如果在一个方法中，想要用到类属性，而不硬编码(写死了)，可以将方法定义成类方法
    @classmethod
    def a_classmethod(cls, tag):
        print(cls, tag)
        cls.number += 1

    def __init__(self):
        self.a_classmethod("ghi")
        super().__init__()

p = Pig()
p.breath()           # 实例方法 => Pig.breath(p)
p.p_staticmethod("abc")   # 静态方法 => Pig.p_staticmethod()，不会把当前实例传递方法
Pig.p_staticmethod("def") # 静态方法 => Pig.p_staticmethod()，不会把当前实例传递方法
p2 = Pig()
print(Pig.number)

"""
Animal -> breath -> 实例方法 => self => 当前调用的实例 => 想使用实例的数据和方法
                    与实例绑定 => 调用的时候 pig.breath()
Animal -> breath -> 实例方法 => self => 当前调用的实例 => 想使用实例的数据和方法
                    与实例绑定 => 调用的时候 pig.breath()               
                    
三种的区别，使用场景




"""

import platform
import distro

# class BasePlugin():
#     @staticmethod
#     def os_platform():
#         output = platform.system()
#         return output.strip()
#
#     @staticmethod
#     def os_version_win():
#         return f"{platform.uname().system} {platform.uname().release}"
#
#     @staticmethod
#     def os_version_linux():
#         """xxxx"""
#         return " ".join(distro.linux_distribution())
#
#     def os_version(self):
#         try:
#             if self.os_platform() == "Linux":
#                 output = self.os_version_linux()
#             else:
#                 output = self.os_version_win()
#             result = output.strip()
#         except Exception as e:
#             result = "got os version failed"
#         return result

# p = BasePlugin()
# print(p.os_platform())
# print(p.os_version())

class BasePlugin():
    # xxxx
    os_platform = platform.system().strip()
    # xxxx
    os_version_win = f"{platform.uname().system} {platform.uname().release}"
    # xxxx
    os_version_linux = " ".join(distro.linux_distribution())

    def os_version(self):
        try:
            if self.os_platform == "Linux":
                output = self.os_version_linux
            else:
                output = self.os_version_win
            result = output.strip()
        except Exception as e:
            result = "got os version failed"
        return result

p = BasePlugin()
print(p.os_platform)
print(p.os_version())