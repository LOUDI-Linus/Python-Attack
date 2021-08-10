"""
@file: 类的定义
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/14
@decs

"""
"""
三种定义方法
class xxx
class xxx()
class xxx(object)推荐     基类obj

属性：静态/类属性（公用）
          实例属性（创建出来的实例，每个实例都独有的信息）
          
          
    实例属性和类(静态)属性的区别？（为什么要使用类/静态属性）
    1. 实例化的时候不需要额外传参
    2. 使用静态属性占用的在存储空间更少(国籍)
    
    a.属性   ---获取属性！！！
    
方法：实例方法 
      静态方法
      类方法
    a.方法()!!!
添加，删除，修改实例的属性
        可自由实现以上功能
        实例查找属性时，先查找本身，没有就去类上查找，没有在抛出异常
        
        
实例化
    __new__返回一个实例
    __init__初始化属性
"""
import requests

class Person(object):
    "建立模型"
    def __init__(self,name:str,age:int,sex:str):
        " 实例初始化属性，基本信息，init特殊方法，每创建新实例都会运行"
        self.name = name
        self.age = age
        self.sex = sex

    def brower(self):
        "行为"
        url = "https://www.baidu.com"
        if self.age <18:
            print("xxxx")
        else:
            data = requests.get(url)
            return data

class Bus(object):
    "静态属性（公共）"
    prod = "BYD"

    # # 创建并且返回一个实例,先执行new在执行init
    # def __new__(cls, *args, **kwargs):
    #     print(cls,args,kwargs)
    #     obj = super().__new__(cls)
    #     return obj

    "实例属性，创建实例，初始化提供的信息"
    "self表示当前创建的实例"
    def __init__(self,driver,num,color="red"):
        self.driver = driver
        self.num = num
        self.color = color

    "方法"
    def run(self):
        print(f"{self.driver}往返于长沙火车站")

# 实例化---参数由__init__方法决定
bus1 = Bus(driver="zwc",num=123)
Bus.prod="BMW"


# bus2 = Bus("cmz",123).run()

# # 查看信息
# print(bus1.driver,bus2.color)
# bus1.run()
#
# class Student(object):
#     sch_name = "SANCHUANG"
#
#     def __init__(self,stu_name:str,stu_age:int,stu_gra:dict):
#         # stu_name形式参数赋值给当前的实例
#         self.stu_name0 = stu_name
#         self.stu_age = stu_age
#         self.stu_gra = stu_gra
#
#     def total(self):
#         "总分"
#         gra_sum = 0
#         for i in self.stu_gra.values():
#             gra_sum+=int(i)
#         return gra_sum
#
#     def avg_gra(self):
#         "平均分"
#         a=int(sum(self.stu_gra.values())/len(self.stu_gra))
#         return  a
#
# msg ={"yw":100,"sx":100,"yy":250}
#
# cail = Student("zwc",10,msg)
# print(cail.total(),cail.avg_gra())







