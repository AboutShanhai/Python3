#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/5 22:58
# @Author : shanhai
# @File : BaseWhileAndFor.py
# @Software: PyCharm

import random


def HundredOddAndEvenSum():
    n = 1
    oddSum = 0
    evenSum = 0
    numberSum = 0
    while n <= 100:
        if n % 2 == 1:
            oddSum = oddSum + n
        else:
            evenSum = evenSum + n
        numberSum = numberSum + n
        n = n + 1

    print(f'1~100的奇数和：{oddSum}')
    print(f'1~100的偶数数和：{evenSum}')
    print(f'1~100的和：{numberSum}')


def WhileElse():
    number = random.randint(0, 100)
    guess = -1
    count = 0
    countSum = 5
    while guess != number:
        guess = int(input(f"总次数为{countSum}次,第{count + 1}次猜数,请输入你猜的数字："))
        if guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")

        count = count + 1
        if count >= countSum:
            print("机会已经用完，很遗憾你没有猜对了！")
            break
        else:
            print(f'剩余次数为：{countSum - count}')
    else:
        print("恭喜，你猜对了！")


def HundredOddAndEvenSumFor():
    oddSum = 0
    evenSum = 0
    numberSum = 0
    for i in range(1, 101):
        if i % 2 == 1:
            oddSum = oddSum + i
        else:
            evenSum = evenSum + i
        numberSum = numberSum + i

    print(f'1~100的奇数和：{oddSum}')
    print(f'1~100的偶数数和：{evenSum}')
    print(f'1~100的和：{numberSum}')


def HundredOddAndEvenSumRange():
    oddSum = 0
    evenSum = 0
    numberSum = 0
    for i in range(1, 100, 2):
        oddSum = oddSum + i

    for i in range(2, 101, 2):
        evenSum = evenSum + i

    for i in range(1, 101, 1):
        numberSum = numberSum + i

    print(f'1~100的奇数和：{oddSum}')
    print(f'1~100的偶数数和：{evenSum}')
    print(f'1~100的和：{numberSum}')


if __name__ == '__main__':
    print("--------------------While Strata--------------------")
    HundredOddAndEvenSum()
    print("--------------------While End--------------------")
    print()

    print("--------------------For Strata--------------------")
    HundredOddAndEvenSumFor()
    print("--------------------For End--------------------")
    print()

    print("--------------------Range Strata--------------------")
    HundredOddAndEvenSumRange()
    print("--------------------Range End--------------------")
    print()

    print("--------------------WhileElse Game Strata--------------------")
    WhileElse()
    print("--------------------WhileElse Game End--------------------")
