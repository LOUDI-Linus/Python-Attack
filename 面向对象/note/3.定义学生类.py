"""
@file:   3.定义学生类
@author: linuxzhen520@163.com
@date:   2020/05/20
@desc:
"""


class Student():
    country = '中国'
    def __init__(self,name,age,school,grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade

    def total_grade(self):
        # 实例方法: self => 当前调用的实例
        # return int(self.grade['China'])+int(self.grade['Math'])+int(self.grade['English'])
        return sum(self.grade.values())

    def avg_grade(self):
        return self.total_grade()/len(self.grade)

curry_grade = {'China':100,'Math':100,'English':100}
curry = Student('curry',18,'幼儿园',curry_grade)
print(curry.total_grade(), curry.avg_grade())
# print(curry.avg_grade())

cali_grade = {'China':'90','Math':'90','English':'90'}
cali = Student("cali", 18, "幼儿园",cali_grade)
print(cali.total_grade(), cali.avg_grade())
# cali.total_grade() => Student.total_grade(cali)
# print(Student.total_grade(cali))


BrokenPipeError
