"""
problem : 
@DATE: 2023-05-12 16:10:17
"""

"""
学生成绩列表：复合列表

复合列表排序：
和简单一样，我这里以临时为例

@list, 排序的列表
@key, 排序的关键字
@reverse, 是否倒序
sorted(list, key = , reverse = True/False)
"""

"""
lambda函数：
1. 匿名函数（lambda就是函数名），直接使用函数定义
2. 简单的函数定义，不会重复多次使用

lambda TODO

"""
stusGrade = [
    {'sno': 101 , 'sname': "张三", "sgrade": 88},
    {'sno': 102 , 'sname': "李四", "sgrade": 99},
    {'sno': 103 , 'sname': "王二", "sgrade": 66},
    {'sno': 104 , 'sname': "麻子", "sgrade": 77},
]

stusGrade_sort = sorted(stusGrade,
                        key = lambda x : x["sgrade"],
                        reverse = True)

print(f"origin list {stusGrade}")
print(f"dsc list {stusGrade_sort}")