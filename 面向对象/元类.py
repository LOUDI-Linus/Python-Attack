"""
@file: 元类
@author: Cooper.wy_zou1103@163.com
@date: 2021/08/06
@decs


type是python的内建元类，我们也可以创建自己的元类
"""
# 使用type元类创建
# type参数，str:类名， tuple：父类， dict：类中的属性与方法


Dog= type("Dog",(object,),{"name":"123"})

dog = Dog()
print(dog.name)

# 编写元类
class Mytype(type):
    "自定义元类,继承type就行"