"""
@file: 魔术方法和属性
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/27
@decs

"""
"""new,init---构造函数"""
class Tst(object):
    """123123123"""
    def __new__(cls, *args, **kwargs):
        """需要返回一个实例"""
        print("创建并且返回一个实例")
        instance = super().__new__(cls)
        return instance

    def __init__(self,name):
        self.name = name
        "初始化刚刚创建的实例，自动调用"
        print("初始化instacne")

    # def __del__(self):
    #     "当删除实例，自动执行"
    #     print("销毁实例")
    #     del self

    def __call__(self, *args, **kwargs):
        """调用方法
        不可被调用，需要定义call方法,实例化的对象当作函数来使用
        """
        print("被调用")

    def __str__(self):
        # 更友好的显示一个对象,返回一个字符串
        return f"str:{self.name}"

    def __repr__(self):
        # 更友好的显示一个对象,返回一个字符串
        return f"repr:{self.name}"

# # __str__: 非正式场合 => print(object)
# # __repr__：正式场合  => li = [object, object] => print(li)
p1 = Tst("zwc")
p2 = Tst("cmz")
print(p2)
list1 = [p1]
print(list1)
print(Tst.__doc__)