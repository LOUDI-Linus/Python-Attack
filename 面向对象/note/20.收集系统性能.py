"""
@file:   20.收集系统性能
@author: linuxzhen520@163.com
@date:   2020/05/28
@desc:
    实现一个类：收集系统性能信息
    * cpu基本信息
    * cpu使用率
    * mem使用率
    * nic使用率
    * disk使用率（io、利用率）

    类名：SystemPerformance
    实现数据收集的两种方法：psutil


    如何着手编写一个类：
    1. 类名，实现功能 => 打如下框架
    class SystemPerformance(object):
        def cpu(self):
            pass

        def memory(self):
            pass
        ....
    2. 获取各种性能数据，确定是否需要统一的方法返回值的数据格式
        不要print，通过return返回

    3. 实现功能

    4. 优化(减少代码重复......)

    5. 如果一个类中方法全部都是静态方法。那么完全可以把它定义成一个模块（）
"""

import psutil

class SystemPerformance(object):
    """这是一个xxxx功能类"""
    @staticmethod
    def cpu():
        """参数，返回值"""
        result = dict()
        result["count"] = psutil.cpu_count()
        result["usage"] = psutil.cpu_percent(percpu=True)
        return result

    @staticmethod
    def memory():
        """参数，返回值"""
        result = psutil.swap_memory()
        return result

    def all(self):
        result = dict()
        result["cpu"] = self.cpu()
        result["memory"] = self.memory()
        return result

# s = SystemPerformance()
print(SystemPerformance.memory())
print(SystemPerformance.cpu())

###### json
# 类中方法 => 接口
# web中提供数据的一些url => 接口 => json
# json => 一种指定的格式 => json字符串（对象）
#      => 一种轻量级的数据交换格式
#      => 不同程序之间

"""
json字符串(对象) => 符合json格式的对象 https://www.bejson.com/
json => python中的对象的区别

python中的对象（由str, int, float, bool, None, dict, list 组成的数据） => json 
    1. key => 字符串
    2. 所有的字符串 => 双引号
    3. json对象中，不能包含类

json有什么用呢？(好处)
    不同程序之间的数据交换
        python <= json => mysql 
        python/json json mysql/json
    
    mysql => jdoc JSON =>
        表：天气（日期、天气信息）
            日期     => DATE
            天气信息 => CHAR/VARCHAR/JSON
            2020/5/28    20度、阴、pm2.5、穿衣、防晒...
                        CHAR/VARCHAR/ => "20度,阴,20,建议一件长袖,50"
                        JSON => {
                                    "temperature":20,
                                    "weather":"阴",
                                }
                             => ["20", "阴",20,"建议一件长袖",50]

    python => 会把python中的对象通过json.dumps转化为 => json
    
    192.168.0.23 / liu / Sanchuang123# 

创建一个表 
    weather (update_date, char_info, json_info)
    
    create table weather(update_date date,char_info varchar(20),json_info json);


插入记录
    2020/5/28 "20度,阴,20,建议一件长袖,50" '{"temperature":20,"weather":"阴"}'
    
    insert into weather(update_date,char_info,json_info) values(
            now(),
            "20度,阴,20,建议一件长袖,50",
            '{"temperature":20,"weather":"阴"}');

# 如果json字符串 => 字符串一定要符合json格式 => https://www.bejson.com/




"""

# obj = [1, 2, 3]
# obj = {"1":1, "2":object}

# 安装模块
# pip install pymysql

# 使用和连接数据库
import pymysql

# 连接数据库
conn = pymysql.connect('192.168.0.187', user="liu", passwd="Sanchuang123#", db="sc")
print(conn)

# 获取操作游标
cur = conn.cursor()

# 执行sql语句
cur.execute("select * from weather;")
result = cur.fetchall()
print(result)
# (
# (datetime.date(2020, 5, 28), '20度,阴,20,建议一件长袖,50', '{"weather": "阴", "temperature": 20}'),
# )

import json
print(type(result[0][1]), result[0][1].split(','))
# str , json.loads
print(type(result[0][2]), json.loads(result[0][2]))
cur.close()
conn.close()



# print(cur.fetchone())
# 命令没找到
# Can't connect to MySQL server on '192.168.0.187' (timed out)
# 1. 服务器是否连通(网络)
#    ping
# 2. 服务是否正常

"""
关于使用char和json的区别

json => 在不同程序之间通信

vachar => '20度,阴,20,建议一件长袖,50'                    => 取值不方便
          '20度,阴,20,建议一件长袖,有小雨。,50'            => 取值不方便
          '{"weather": "阴", "temperature": 20}'  => json.loads(data) => dict     
          "{'weather': '阴', 'temperature': 20}"  => json.loads(data) => dict 失败
                                                 
json => 对存进去的字符串格式进行检查 => 保存不进去。 
     => json字符串 => python/java对象 => 程序对象 => 取值方便 => 标准化输出
     
1. json是什么
2. 使用场景 => 在不同程序之间通信，数据处理比较方便
3. python => json.loads, json.dumps, json.load, json.dump
===========================================================
知乎 => 
微信 => 
搜索引擎(bing, sogou, baidu)
菜鸟教程
看书 
"""



