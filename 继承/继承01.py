#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/1/25 13:54
# @Author : zhuxuefei
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def sayage(self):
        print("年龄年龄你猜猜")


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    def sayage(self):
        super().sayage()
        print("我必须覆盖你的年龄")


#方法解析顺序
print(Student.mro())
s = Student("朱雪飞", 30, 700)
s.sayage()
# 返回实例可调用的所有方法
print(dir(s))
# 私有属性可通过_类名__私有属性访问到
print(s._Person__age)




