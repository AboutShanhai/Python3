#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/7 20:25
# @Author : shanhai
# @File : Function.py
# @Software: PyCharm


def AddFunction(a, b):
    return a + b


def MaxFunction(a, b):
    return b if a < b else a


def changeString(content):
    print('函数内取值:', content)
    content = 'python'
    print('函数内修改后，函数内取值:', content)


def changeList(content_list):
    print('函数内取值:', content_list)
    content_list.append([1, 2, 3, 4])
    print('函数内修改后，函数内取值:', content_list)


def printInfo(name, age):
    print("名字: ", name)
    print("年龄: ", age)


def printInfoDefault(name='shanhai', age=27):
    print("名字: ", name)
    print("年龄: ", age)


def functionName(arg1, *var_tuple):
    print('输出：')
    print(arg1)
    print(var_tuple)


def functionNameVer1(arg1, *var_tuple):
    print('输出：')
    print(arg1)
    for var in var_tuple:
        print(var)


def functionNameVer2(arg1, **var_tuple):
    print('输出：')
    print(arg1)
    print(var_tuple)


def functionNameVer3(*, age):
    print('输出：')
    print(age)


if __name__ == '__main__':
    print(f'Add:{AddFunction(2, 3)}')
    print(f'Max:{MaxFunction(2, 3)}')

    # 在python中，strings, tuples, 和numbers是不可更改的对象，而list, dict等则是可以修改的对象。
    str_content = 'shanhai'
    print('函数外取值:', str_content)
    changeString(str_content)
    print('函数内修改后，函数外取值:', str_content)
    print()

    list_content = list(range(1, 5))
    print('函数外取值:', list_content)
    changeList(list_content)
    print('函数内修改后，函数外取值:', list_content)
    print()

    # 关键字参数
    # 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为Python解释器能够用参数名匹配参数值。
    print('关键字参数:')
    printInfo(age=27, name='shanhai')
    print()

    # 默认参数
    print('默认参数:')
    printInfoDefault()
    printInfoDefault(age=1)
    printInfoDefault(name='python')
    printInfoDefault(age=1, name='python')
    print()

    # 不定长参数
    # 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
    print('不定长参数[*]:')
    functionName('shanhai', 'man', 27)
    functionNameVer1('shanhai', 'man', 27)

    # 加了两个星号 ** 的参数会以字典的形式导入
    print('不定长参数[**]:')
    functionNameVer2('shanhai', sex='man', age=27)
    print()

    # 强制位置参数
    # 声明函数时，参数中星号 * 可以单独出现。如果单独出现星号 * 后的参数必须用关键字传入
    print('强制位置参数 *:')
    functionNameVer3(age=27)
    print()

    # Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
    # 当前用的是Python3.7 所以没有示例

    # 匿名函数
    # python 使用 lambda 来创建匿名函数。所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    sum_add = lambda arg1, arg2: arg1 + arg2

    print("相加后的值为 : ", sum_add(10, 20))
