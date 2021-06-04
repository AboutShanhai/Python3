#!user/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    print('斐波纳契数列', end=":")
    a, b, c = 0, 1, 1
    while c <= 10:
        print(b, end=',')
        a, b = b, a + b
        c = c + 1
