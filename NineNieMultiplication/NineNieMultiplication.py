#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/5 21:44
# @Author : shanhai
# @File : NineNieMultiplication.py
# @Software: PyCharm


def MultiplicationFunction(num=9):
    print("for循环实现：")
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(f'{i}x{j}={i*j}\t', end='')
            # print('{}x{}={}\t'.format(j, i, i * j), end='')
            # print(i, "*", j, "=", i * j, end="\t")
        print()


def MultiplicationFunctionList(num=9):
    print("列表解析实现：")
    nine_nine_table = []
    for i in range(1, num+1):
        nine_nine_table.append(
            [(str(i) + "*" + str(j) + "=" + str(i*j)) for j in range(1, i + 1)])

    for i in range(len(nine_nine_table)):
        print(nine_nine_table[i])


if __name__ == '__main__':
    MultiplicationFunction()
    MultiplicationFunctionList()
    pass
