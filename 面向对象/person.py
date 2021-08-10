"""
@file: person
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/14
@decs

"""
import requests
URL = "https://www.baidu.com"
name_1 = {"name":"zwc","age":12}
name_2 = {"name":"cmz","age":18}

def msg_id(p_name):
    "年龄检测"
    if p_name["age"] >= 18:
        data = requests.get(URL)
        return data
    else:
        return "age to low"



print(msg_id(name_1), msg_id(name_2))


def msg_num(b_num:int,e_num:int):
    for i in range(b_num,e_num+1):
        msg_str = f"id: {str(i)}"
        print(msg_str)


msg_num(192,194)