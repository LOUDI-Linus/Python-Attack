"""
@file: 类的继承
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/20
@decs

"""

class Animal(object):
    category = "animal"
    num = 0

    def __init__(self):
        Animal.num += 1

    def breath(self):
        print(f"{self.category}需要呼吸")


class Pig(Animal):
    category = "pig"
    num = 0

    def __init__(self):
        Pig.num += 1
        # 继承父类的init方法
        super().__init__()


    def breath(self):
        super().breath()
        print(f"{self.category}呼吸个屁")


pig1 = Pig()
pig2 = Pig()
pig3 = Animal()
# print(Pig.num)
pig1.breath()