#!usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    # 变量[头下标:尾下标:步长]
    str = '123456789'

    print(str)  # 输出字符串
    print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(str[0])  # 输出字符串第一个字符
    print(str[2:5])  # 输出从第三个开始到第五个的字符
    print(str[2:])  # 输出从第三个开始后的所有字符
    print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
    print(str * 2)  # 输出字符串两次
    print(str + '你好')  # 连接字符串

    print('------------------------------')

    print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

    print('------------------------------')

    # print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end = ""
    print('Hello World!')
    print('Hello', end="")
    print('World!')
