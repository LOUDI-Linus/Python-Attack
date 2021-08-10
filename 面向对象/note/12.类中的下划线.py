"""
@file:   12.类中的下划线
@author: linuxzhen520@163.com
@date:   2020/05/27
@desc:
    _foo => 保护变量 => 约定俗成 -> 私有
    __foo => 私有 => 不能直接访问
    __foo__ => python内部专有命名方式 => 用户自定义的东西，不要这样命名
"""

class Parent():
    _min = 1
    __max = 100

    # 魔术方法
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.__sex = sex

    def __make(self):
        print('我是私有方法')
        print(self.__sex, self._age)


class Child(Parent):
    def __init__(self, name, age, sex, score1, score2):
        super().__init__(name, age, sex)
        self._score1 = score1
        self.__score2 = score2


class Child2(Child):
    pass


p = Parent('cali', 18, '男')
print(p._min, p._age)
# 直接访问是不行的
# print(p.__max, p.__sex)
# 强行访问
print(p._Parent__max, p._Parent__sex)
print(dir(Parent))



c = Child('lucy', 19, '女', 100, 99)
c2 = Child2('lucy2', 19, '女', 100, 99)