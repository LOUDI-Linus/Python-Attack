"""
@file:   7.自定义异常类
@author: linuxzhen520@163.com
@date:   2020/05/21
@desc:
    细分异常类 -> 出现问题更精确判断问题

"""
# 最简单的异常类
# class SimpleException(Exception):
#     pass
#
# raise SimpleException

class ValueTypeError(Exception):
    message = "应该给一个int或float类型的数据"

    def __str__(self):
        """打印ValueTyperror的时候输出的东西"""
        return self.message

# class ValueRangeError(Exception):
#     def __init__(self, message):
#         self.message = message

class ValueRangeError(Exception):
    message = "数据范围不对"
    def __str__(self):
        """打印ValueTyperror的时候输出的东西"""
        return self.message

def grade(score):
    """
        score => int，float
        [0~100]
        print/raise
    """
    if not isinstance(score, int) and not isinstance(score, float):
        raise ValueTypeError

    if score <0 or  score > 100:
        raise ValueRangeError
    print("计算出成绩的等级")


# grade(1)
grade('a')
# grade(11.1)
grade(1000)
# KeyError => 字典key不存在
# IndexError => list/tuple index越界

# ops_backend  error_code.py
# AuthorizedException -> APIException -> HTTPException -> Exception
# 好处通过异常名字基本上就能判断出错误的类型




