"""
@file: 自省
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/30
@decs

"""
class Tst(object):
    "类属性"
    name = "zwc"
    def __init__(self):
        "实例属性"
        self.name2 = "zwc2"

t1 = Tst()
#自省，动态访问属性bn
user_input = str(input("请输入: "))

# hasattr 根据字符串  判断对象是否有对应的属性和方法，返回布尔
#getattr 获取方法
if hasattr(t1,user_input):
    print(getattr(t1,user_input))
else:
    print(f"unexist {user_input}")

# 设置成员
setattr(t1,"name3","zwc3")
print(getattr(t1,"name3"))
# 删除成员   删除实例属性非
delattr(t1,"name")
print(hasattr(t1,"name"))