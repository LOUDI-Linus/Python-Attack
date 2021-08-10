"""
@file: 1.属性包装
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/26
@decs

"""

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self._age = self.check_age(age)

    # 属性包装
    @property
    def age(self):
        return self._age
    # 设置age的值
    @age.setter
    def age(self,value):
        self._age = self.check_age(value)

    @staticmethod
    def check_age(age):
        if 0 <=age <= 100:
            return age
        else:
            raise ValueError("xxxxx")

p1 = Person("zwc",100)
p1.age=1000
# 属性包装，这里age实质是一个方法
print(p1.age)


