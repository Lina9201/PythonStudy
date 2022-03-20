#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/3/20 16:57
# @Author : zhuxuefei
def try_to_change(obj):
    obj += obj
    print("形参值为:", obj)


a = 'python学习'
print("a的值为:", a)
# 实参字符串类型
try_to_change(a)
print("实参值为:", a)

a = (7, 8, 9)
print("a的值为:", a)
# 实参元组类型
try_to_change(a)
print("实参值为:", a)

a = 6
print("a的值为:", a)
# 实参数字类型
try_to_change(a)
print("实参值为:", a)

a = [1, 2, 3]
print("a的值为:", a)
# 实参列表类型
try_to_change(a)
print("实参值为:", a)
# 复制整个列表的切片，则不会影响原始的列表
try_to_change(a[:])
print("实参值为:", a)

