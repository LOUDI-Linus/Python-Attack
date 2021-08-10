"""
@file:   2.类的定义
@author: linuxzhen520@163.com
@date:   2020/05/20
@desc:
    描述一个人


    代码风格 => 类名一般使用大驼峰UserName
"""
# import requests
#
#
# class Person():
#     """创建一个用户模型"""
#     def __init__(self, name, age, sex):
#         """创建一个人的时候，需要提供的基本信息"""
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def browser(self):
#         """人的上网的行为"""
#         url = "https://www.sanchuangedu.cn"
#         if self.age < 6:
#             print('不好意思，你太小了，不能上网！')
#         else:
#             resp = requests.get(url)
#             print(resp)
#
# person1 = Person("cali", 1, "male")
# person1.browser()
# print(person1.name)
# print(person1.age)
# print(person1.sex)
#
#
#
# # list => 工厂函数 => 类
# print(dir(list))

"""
python => 写python代码一定要遵守python的代码风格规范。
javascript => 


python2 => 经典类、新式类
python3 => 新式类
"""

class Bus01():
    pass

class Bus02:
    pass

# () => 父类 => object => python3默认是定义类的父类
# 推荐！
class Bus03(object):
    pass


"""
定义一个类：
Bus317
属性：品牌prod, 司机driver, 车牌号no
方法: run

思考: 
    实例化5台317车。哪些信息是公用的？哪些信息是每台车独有的
    公用：BYD
    独有：driver, plate_number
    
    属性：静态/类属性（公用）
          实例属性（创建出来的实例，每个实例都独有的信息）
          
          
    实例属性和类属性的区别？（为什么要使用类/静态属性）
    1. 实例化的时候不需要额外传参
    2. 使用静态属性占用的在存储空间更少(国籍)
    
    
"""
class Bus317(object):
    # 静态属性
    prod = "BYD"

    def __new__(cls, *args, **kwargs):
        # __new__ => 创建并返回一个实例
        # 如果在__new__方法中没有返回自身类的实例,那么不会自动调用__init__
        print(cls, args, kwargs)
        obj = super().__new__(cls)
        return obj


    # 实例属性，创建实例，初始化提供的信息
    # self => 当前创建的实例
    def __init__(self, driver, plate_number, color="green"):
        print("生产出一台车啦!")
        # 把driver形式参数，赋值给当前的实例
        self.driver0 = driver
        self.plate_number0 = plate_number
        self.color=color

    # 实例方法：与普通函数的定义，有且必须有一个self参数
    def run(self, flag):
        # self.prod => 查找当前实例是否有prod => 查找类的prod => 报错
        print(f"{self.driver0}开的{self.prod}：{self.plate_number0}往返于湖南农业大学与长华小区")
        # 不能直接这样调用类（静态）属性
        # print(prod)

# 实例化 => 给的参数由__init__方法决定的。
# 创建实例时，会执行__init__方法
bus1 = Bus317("王晨", "湘A0001")
bus2 = Bus317("黄韬", "湘A0002")

# # 查看信息
# print(bus1.driver0, bus1.prod, bus1.plate_number0)
# print(bus2.driver0, bus2.prod, bus2.plate_number0)
#
# # # 多个私有属性如何赋值
# bus1.run(1)
# bus2.run(2)

# 动态性
# 修改类(静态)属性
print(bus1.prod)
print(bus2.prod)
Bus317.prod = "BMW"
print(bus1.prod)
print(bus2.prod)

# 检查bus1是否有prod这个实例属性,如果没有给bus1添加一个实例属性prod => BMW001
bus1.prod = "BMW001"
# 检查bus1是否有prod这个实例属性,如果有修改bus1的实例属性prod => BMW002
bus1.prod = "BMW002"
print(bus1.prod) # BMW001 => 刚刚修改完之后的值

print(bus2.prod) # BMW => 类属性
bus3 = Bus317("易YQ", "湘A0003")
print(bus3.prod) # BMW

# print('#'*100)
# del Bus317.prod
# print(bus1.prod) # zh ok BMW002
# """
# bus1 => 实例属性prod BMW002
# """
# print(bus2.prod) # zh error

print('#'*100)
del bus1.prod
print(bus1.prod) # 输出最新类属性的值
print(bus2.prod) # 输出最新类属性的值

"""
class Bus317(): prod = BMW
bus1.prod = "BMW001" 
bus1 => 实例属性prod BMW001
        类属性 prod BMW 
        print(bus1.prod) => 属性/方法查找顺序 => 查找是否存在该实例属性（父类） => 查找是否类属性（父类） => 报错    
"""
# 动态地给类添加静态属性 => weight => 所有的实例都能使用
Bus317.weight = "10t"
print(bus1.weight)
print(bus2.weight)


