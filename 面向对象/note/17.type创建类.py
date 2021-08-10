"""
@file:   17.type创建类
@author: linuxzhen520@163.com
@date:   2020/05/28
@desc:
"""

# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         pass
#
#     def talk(self):
#         pass
#
# class Dog(Animal):
#     def talk(self):
#         print('Woff.')
#
# dog = Dog('Dog1')
# print(type(dog))   # Dog
# print(type(Dog))   # type
# print(type(type))  # type

print('#'*50)

# 类的中三个方法
def init(self, name):
    self.name = name

def eat(self):
    pass

def talk(self):
    pass

# 使用type来创建类
# 参数1: 类名 => str
# 参数2：父类 => tuple
# 参数3：类中的属性和方法 => dict => 方法名：方法
Animal = type('Animal',(object,), {'__init__':init, 'eat': eat, 'talk': talk, 'category':'Dog'})

a = Animal("动物1号")
print(a)
print(type(a))
print(type(Animal))

# 用type创建Dog类
# type元类，type是默认的创建类的类

def dog_talk(self):
    print('Woff.')

Dog = type("Dog", (Animal,), {"talk": dog_talk})
dog = Dog('Dog1')
print(type(dog))   # Dog
print(type(Dog))   # type
print(type(type))  # type