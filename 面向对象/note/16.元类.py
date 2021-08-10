"""
@file:   16.元类
@author: linuxzhen520@163.com
@date:   2020/05/28
@desc:
    元类: 创建类的类
    所有的类型最终都是由type创建 => 默认的元类 => type
"""

class A(object):
    pass

a = A()

# 查看a由谁创建 => 查看a是什么类型 => A
print(type(a))
# 查看A由谁创建 => 查看A是什么类型 => type
print(type(type(a)))
# 查看type由谁创建 => 查看type是什么类型 => type
print(type(type(type(a))))
print(type(type))

print(type(1), type(type(1)))