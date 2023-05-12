"""
数据类型转换：
@DATE: 2023-05-12 19:32:59

python中的数据类型：
1. 数字型
    - int （整型，或二进制整型（0b））
    - float（浮点型，没有double！！！！）
    - bool （布尔型）
    - complex（复数）

2. 字符串（str）
3. 列表（list）
4. 元组（tuple）
5. 字典（dict）
6. 集合（set）

python中类型转换：
1. 自动转换（数字型）
精度等级：布尔 < 整型 < 浮点型 < 复数

2. 强制类型转换
    - str( )：可以把其他类型数据转化为字符串类型
    - int( )：可以把其他类型数据转化为整型
    - float( )：可以把其他类型数据转化为浮点型
    - bool( )：可以把其他类型数据转化为布尔类型
    - list( )：可以把其他类型数据转化为列表类型
    - tuple( )：可以把其他类型数据转化为元组类型
    - dict( )：可以把其他类型数据转化为字典类型
    - set( )：可以把其他类型数据转化为集合类型

3. 注意点
    - python 是不支持复数转换为整数或浮点数

"""

# 自动转换
boolvar = True
intvar = 10
floatvar = 10.5
complexvar = complex(10,9)
print("自动转换：")
print(f"boolvar: {boolvar}, intvar: {intvar}, bool -> int : ", boolvar + intvar)
print(f"intvar: {intvar}, floatvar: {floatvar}, int -> float: ", intvar + floatvar)
print(f"floatvar: {floatvar}, complexvar: {complexvar}, float -> complex: ", floatvar + complexvar)

# 强制转换
# 数字型中，精度高往精度低换
print("强制转换，数字型中，精度高往精度低换：")
print(f"intvar: {intvar}, int -> bool : ", bool(intvar))
print(f"floatvar: {floatvar}, float -> int : ", int(floatvar))
print("python 是不支持复数转换为整数或浮点数!!")

# 字符串和数字型互转，需要字符型里的字符都为数字才可以