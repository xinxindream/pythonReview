"""
problem 10 : 简单列表排序 
@DATE: 2023-05-12 15:41:29
"""

"""
简单列表：元素类型不是复合类型（列表/元组/字典）
即：
形式1 : [10,20,30,40,50]
形式2 : ["abc","cd","ee"]
"""

"""
列表排序函数：
1. 列表永久排序 list.sort()
2. 列表临时排序 tempList = sorted(list)
两者默认升序排序

3. 列表倒序函数 list.reverse()

结合reverse可以实现sort降序排序
list.sort(reverse=True)
sorted(list,reverse=True)
"""

orgin_list = [50,10,15,2,70]

# 临时排序，不改变原列表
temp_list = sorted(orgin_list)

# 永久排序，改变原列表
orgin_list.sort(reverse=True)

print(f"orgin_list is {orgin_list}")
print(f"asc is {temp_list}")
print(f"dsc is {orgin_list}")
