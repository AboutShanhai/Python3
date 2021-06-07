#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/7 14:49
# @Author : shanhai
# @File : IterAndYield.py
# @Software: PyCharm


import sys


def iterFunction(num=10):
    number_list = list(range(1, num + 1))
    print(number_list)
    print("iter实现列表元素输出：")
    it = iter(number_list)
    for index in it:
        print(index, end=" ")


def nextFunction(num=10):
    print()
    number_list = list(range(1, num + 1))
    print(number_list)
    print("next实现列表元素输出：")
    it = iter(number_list)
    while True:
        try:
            print(next(it), end=" ")
        except StopIteration:
            # sys.exit()
            print("\nnext 标识迭代的完成!")
            break


def IterAndYieldFunction(num=10):
    result = 1
    index = 1
    while index <= num:
        result = result * index
        index = index + 1
        yield result


f = IterAndYieldFunction(10)


def factorial():
    count = 1
    print("\n生成器实现阶乘：")
    while True:
        try:
            print('%d!=' % count, next(f))
            count = count + 1
        except StopIteration:
            sys.exit()


if __name__ == '__main__':
    iterFunction()
    nextFunction()
    factorial()
    pass
