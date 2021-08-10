"""
@file: 抽象基类
@author: Cooper.wy_zou1103@163.com
@date: 2021/08/04
@decs

基类=父类
"""

from abc import  ABC,abstractmethod

# 定义成抽象基类,要继承至ABC
class Animal(ABC):
    "抽象基类：主要定义了基本类和最基本的抽象方法，可以为子类定义共有的API，不需要具体实现"
    #声明成抽象方法才是抽象方法,具体实现由子类来实现

    #抽象方法
    @abstractmethod
    def eat(self):
        """
        通过@abstractmethod装饰器，抽象方法
        在子类中一定要重写方法，所以父类不需要实现
        """
        pass
    def durink(self):
        print("我要喝水")

# 抽象基类不能被实例化
# a = Animal()

class Person1(Animal):
    def eat(self):
        print("Person1要喝水")
#必须重写父类的方法才能实例化调用
class Person2(Animal):
    def eat(self):
        print("Person2要喝水")
p1 = Person1()
p2 = Person2()
p1.eat()
p2.eat()