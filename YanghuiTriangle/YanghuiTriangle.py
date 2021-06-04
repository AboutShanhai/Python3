#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/4 16:57
# @Author : shanhai
# @File : YanghuiTriangle.py
# @Software: PyCharm

# 列表解析(三目运算符)
def YangHui(num=2):
    LL = [[1]]
    for i in range(1, num):
        LL.append(
            [(0 if j == 0 else LL[i - 1][j - 1]) + (0 if j == len(LL[i - 1]) else LL[i - 1][j]) for j in range(i + 1)])

    print(LL)
    for j in range(len(LL)):
        print(LL[j])


# 采用列表实现
def YangHuiList(n=10):
    print("\n采用列表实现:")
    triangle = [[1], [1, 1]]
    for i in range(2, n):  # 已经给出前两行，所以求剩余行
        cur = [1]  # 定义每行第一个元素
        pre = triangle[i - 1]  # 上一行
        for j in range(i - 1):  # 算几次
            cur.append(pre[j] + pre[j + 1])
        cur.append(1)
        triangle.append(cur)
    print(triangle)
    for j in range(len(triangle)):
        print(triangle[j])


# 采用列表 补0法实现
def YangHuiListNewRow(n=10):
    print("\n采用列表 补0法实现:")
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        newrow = triangle[i - 1]
        newrow.append(0)
        row = [None] * (i + 1)  # 开辟空间
        for j in range(i + 1):
            row[j] = newrow[j - 1] + newrow[j]
        triangle.append(row)

    print(triangle)
    # 去掉尾部位补0
    for j in range(1, len(triangle) - 1):
        triangle[j].pop()

    for j in range(len(triangle)):
        print(triangle[j])


if __name__ == '__main__':
    YangHui()

    YangHuiList(5)

    YangHuiListNewRow(5)
