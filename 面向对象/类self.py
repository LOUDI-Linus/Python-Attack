"""
@file: 类self
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/20
@decs

"""
# self代表类的实例，谁在调用就是谁
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