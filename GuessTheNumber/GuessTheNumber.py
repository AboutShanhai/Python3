#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/5 22:35
# @Author : shanhai
# @File : GuessTheNumber.py
# @Software: PyCharm

import random


def GuessTheNumber():
    number = random.randint(0, 100)
    guess = -1
    while guess != number:
        guess = int(input("请输入你猜的数字："))

        if guess == number:
            print("恭喜，你猜对了！")
        elif guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")


if __name__ == '__main__':
    GuessTheNumber()
    pass
