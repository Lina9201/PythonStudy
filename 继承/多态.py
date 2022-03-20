#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/1/25 14:45
# @Author : zhuxuefei
class Man:
    def eat(self):
        print("人要吃饭")


class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")


class English(Man):
    def eat(self):
        print("英国人用勺子吃饭")


def manEat(m):
    if isinstance(m, Man):
        m.eat()
    else:
        print("不能吃饭")


manEat(Chinese())
manEat(English())
