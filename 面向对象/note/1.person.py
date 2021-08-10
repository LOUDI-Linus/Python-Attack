"""
@file:   1.person
@author: linuxzhen520@163.com
@date:   2020/05/20
@desc:
表示一个人
信息：姓名，年龄，性别
行为：上网(url) => 返回网页的内容！requests.get
               => 不好意思，你太小了，不能上网！
通用性表示一个人呢？
"""

import requests
URL = "https://www.sanchuangedu.cn"


def browser(peopel_dic):
    if peopel_dic['age'] < 6:
        print('不好意思，你太小了，不能上网！')
    else:
        resp = requests.get(URL)
        print(resp)

peopel_dic = {'name':'cali', 'age':18, 'sex':'male'}


peopel2_dic = {'name':'feng', 'age':4, 'sex':'male'}
browser(peopel2_dic)
browser(peopel_dic)
# dog_dic = {"age":10}
# browser(dog_dic)
# browser(1)
#
# """
# 存在的问题：
# 1. 任何对象作为browser传递调用执行
# 2. 有以下两种调用方式，哪种会更适合当前场景：
#     browser(person)  => 上网 1         => 强调上网这件事
#     person.browser() => 上网 2 => 更好 => 强调人这个整体
#
# 主体：某个功能、某人
# 主体 => 人去做某事
# """
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
#         resp = requests.get(url)
#         return resp
#
#
#
#
