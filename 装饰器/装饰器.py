#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/1/25 10:55
# @Author : zhuxuefei
class Screen:
    def __init__(self, width, height, ch):
        self._width = width
        self._height = height
        self.__ch = ch

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


s = Screen(1024, 768, 56)
# s = Screen()
# s.width = 1024
# s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
s.width = 879
print(s.width)
s._width = 988
print(s._width)
s.__ch = 123
print(s.__ch)



