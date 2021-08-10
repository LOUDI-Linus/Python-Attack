"""
@file: 主机信息收集
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/16
@decs


CPU,网络，磁盘，等
"""
from ping3 import ping

def ping_ip(ip):
    second = ping(ip)
    if second:
        print(second)
    else:
        print(second)




ping_ip("192.168.142.172")

list2=["123","None"]
for i in list2:
    if i:
        print(i)
    else:
        print("xxx")