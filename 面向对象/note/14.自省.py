"""
@file:   14.自省  =>  反射
@author: linuxzhen520@163.com
@date:   2020/05/27
@desc:
"""


class Tst(object):
    def __init__(self):
        self.name1 = "cali1"
        self.name2 = "cali2"
t1 = Tst()

# 检查name属性是否存在，如果存在，再打印
# if "name" in Tst.__dict__:
#     print(t1.name)
# else:
#     print("name不存在")

# if hasattr(t1, "name"):
#     print(t1.name)
# else:
#     print("name不存在")

name = input("请输入您要访问的属性")
if hasattr(t1, name):
    # name 是一个变量
    # t1.name => name 属性名
    print(getattr(t1, name))
else:
    print("name不存在")


###### 动态设置属性值
setattr(t1, "name2", "feng2")
print(getattr(t1, "name2"))

delattr(t1, "name2")   # del t1.name2
# del t1.name2
# print(getattr(t1, "name2"))
print(hasattr(t1, "name2"))
# print(dir(t1))

"""
类的自省方法：
hasattr => 判断对象是否有某个属性/方法
"""