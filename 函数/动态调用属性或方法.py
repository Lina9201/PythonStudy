#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/4/17 22:16
# @Author : zhuxuefei


class Person:
    age = 15
    def test(self):
        print("helloworld")

    def __setattr__(self, key, value):
        self.__dict__['key'] = self.value

    def __getattr__(self, item):
        print("___getattr__")


p1 = Person()
# print(p1.age)
# getattr(p1, 'height', 165)
getattr(p1, 'test')()
p1.test()

print(getattr(p1, 'age'))
print(p1.age)

