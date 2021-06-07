#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/6 20:22
# @Author : shanhai
# @File : JesusTraitor.py
# @Software: PyCharm


# 耶稣的叛徒
def JesusTraitor():
    people = list(range(1, 11))
    print(people)
    count = 1
    index = 0
    flag = 0
    while count < len(people):
        index = index % len(people)
        if people[index] != 0:
            flag = flag + 1

        if 3 == flag:
            people[index] = 0
            flag = 0
            count = count + 1

        index = index + 1

    print(people)


if __name__ == '__main__':
    JesusTraitor()
