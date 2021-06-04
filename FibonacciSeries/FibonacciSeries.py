#!user/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/6/4 22:57
# @Author : shanhai
# @File : FibonacciSeries.py
# @Software: PyCharm


def FibonacciFunction(num=5):
    print('斐波纳契数列', end=":")
    a, b, c = 0, 1, 1
    while c <= 10:
        print(b, end=',')
        a, b = b, a + b
        c = c + 1


if __name__ == '__main__':
    FibonacciFunction(10)
