"""
@file:   4.自定义迭代器
@author: linuxzhen520@163.com
@date:   2020/05/21
@desc:
    如何判断一个对象是不是迭代器： __next__, __iter__
    __next__ => 返回下一个数据
    __iter__ => 返回一个迭代器(可迭代对象=>返回一个迭代器，迭代器=>返回自己)

    Fib

"""
# a = (i**2 for i in range(10))
# print(a.__next__())
# print(a.__next__())
# print(a.__iter__())
# print(a)
class Fib(object):
    def __init__(self):
        """定义当前值和下一个值，执行一次"""
        self.current = 0
        self.next = 1

    def __next__(self):
        """每次进行next调用的时候，计算出下一个current和next的值，并且返回current"""
        self.current, self.next = self.next, self.next+self.current
        # tmp = self.current
        # self.current = self.next
        # self.next = self.current+tmp
        return self.current

    def __iter__(self):
        print("这是斐波拉契数列")
        return self

# f => 迭代器
#    cur next
# 0, 1， 1， 2， 3， 5， 8， 13 。。。。。
f = Fib()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


class Fib(object):
    def __init__(self, n):
        """定义当前值和下一个值，执行一次"""
        self.current = 0
        self.next = 1
        self.n = n

    def __next__(self):
        """每次进行next调用的时候，计算出下一个current和next的值，并且返回current"""
        self.current, self.next = self.next, self.next+self.current
        # tmp = self.current
        # self.current = self.next
        # self.next = self.current+tmp
        if self.current > self.n:
            raise StopIteration
        return self.current

    def __iter__(self):
        print("这是斐波拉契数列")
        # return self

# f => 迭代器
#    cur next
# 0, 1， 1， 2， 3， 5， 8， 13 。。。。。
f0 = Fib(10)  # 计算10以内的fib数列, StopIteration
f1 = Fib(100)  # 计算100以内的fib数列


print("#"*40)
for item in f0:
    print(item)

print("#"*40)
for item in f1:
    print(item)
# # for item in iter(f1):
# # item = next(f1)
# # 当遇到StopItration停止
#
