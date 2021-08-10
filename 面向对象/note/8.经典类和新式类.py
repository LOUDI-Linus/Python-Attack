# coding:utf-8
"""
@file:   8.经典类和新式类
@author: linuxzhen520@163.com
@date:   2020/05/21
@desc:
    经典类和新式类最大区别 => MRO => 方法解析顺序
"""

class A:
    # def test(self):
    #     print("A.test")
    pass

class B(A):
    # def test(self):
    #     print("B.test")
    pass


class C(A):
    # def test(self):
    #     print("C.test")
    pass

class D(B):
    # def test(self):
    #     print("D.test")
    pass

class E(C):
    # def test(self):
    #     print("E.test")
    pass

class F(D,E):
    # def test(self):
    #     print("F.test")
    pass

# 经典类=> 深度优先 => F -> D -> B -> A ->  E-> C -> object
f = F()
# f.test()
# 查看类的方法解析顺序
# F -> D -> B -> E -> C -> A -> object
print(F.mro())