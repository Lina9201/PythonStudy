#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/3/23 21:54
# @Author : zhuxuefei
def function(*args):
    print(args, type(args))


function(1)


def function(**kwargs):
    print(kwargs, type(kwargs))


function(a=2, b=3)
