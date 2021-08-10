"""
@file:   13.常见魔术方法
@author: linuxzhen520@163.com
@date:   2020/05/27
@desc:
"""

class Tst(object):
    """这是一个测试类"""
    def __new__(cls, *args, **kwargs):
        """O 创建并返回一个实例，自动调用"""
        print("创建并返回一个实例")
        print(args, kwargs)
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        """OOOOO 初始化刚刚创建的实例，自动调用"""
        print("初始化刚刚创建的实例")
        self.name = name
        self.n = 1
        self.data = {}

    def __del__(self):
        """当删除实例时，自动执行"""
        print(f"{self.name}被销毁实例")
        del self

    def __call__(self, *args, **kwargs):
        """O 当实例需要被调用的时候：t2()"""
        print(args, kwargs)
        print("被调用了")

    def __str__(self):
        """OOO: 用友好的方式显示一个对象，返回一个字符串，当print输出对象的时候，会显示成这里的样子"""
        return f"str:{self.name}"

    def __repr__(self):
        """OOO: 用友好的方式显示一个对象, 返回一个字符串 """
        return f"repr:{self.name}"

    def __iter__(self):
        """O"""
        print("返回一个迭代器")
        return self

    def __next__(self):
        """O"""
        self.n += 1
        if self.n > 10:
            raise StopIteration
        return self.n

    def __getitem__(self, key):
        print("获取数据时被调用")
        print(key)
        if not isinstance(key, slice):
            return self.data.get(key)

    def __setitem__(self, key, value):
        print('设置数据:', key, value)
        self.data[key] =value

    def __delitem__(self, key):
        print('删除数据:', key)
        del(self.data[key])

    def __add__(self, other):
        # t1 + t22 => t1.__add__(t22)
        # self => t1
        # other => t22
        if isinstance(other, int):
            return self.n + other
        return self.n + other.n

class SubTst(Tst):
    pass

class Tst2(object):
    n = 10


t1 = Tst("t1")
# t1['key1'] = 'abc'   # t1.__setitem__('key1', 'abc')
# print(t1["key1"])    # t1.__getitem__('key1')
# del t1["key1"]       # t1.__delitem__('key1')

# Tst => t1 => 迭代器
# for i in t1:
#     # for循环，隐式地去调用next
#     print(i)


t2 = Tst("t2")
# t0 = SubTst(name="t0")
# # del t1
#
# # 调用t2 => 默认情况下t2是不可以被调用的
# # TypeError: 'Tst' object is not callable
# # 如果想要实例能被调用 => 定义__call__
# # t2(1, a=1)

print(dir(t1))
# TypeError: unsupported operand type(s) for +: 'Tst' and 'Tst'
# print(t1+t2)
# t22 = Tst2()
# # 可以 => t1.__add__(t22)
# print(t1+t22)
# # 不行 => t22.__add__(t1)
# print(t22+t1)
# # TypeError: unsupported operand type(s) for +: 'int' and 'Tst'
# # print(dir(1))
# # print(1+t2)

print(t1+100)  # t1.n+1


# # import time
# # time.sleep(10)
#
# # 多实例销毁顺序 => 先被创建的，先销毁
# #               => 同一个级别，分代回收 => 内存地址
#
#
# # __str__: 非正式场合 => print(object)
# # __repr__：正式场合  => li = [object, object] => print(li)
# li = [t0, t1, t2]
# print(t0, t1, t2)
# print(li)

print(Tst.__dict__)
print(Tst.__name__)
print(Tst.__module__)
print(Tst.__bases__)
print(dir(Tst))