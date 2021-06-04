#!usr/bin/python3
# -*- coding: UTF-8 -*-

import re

if __name__ == '__main__':
    pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
    string_ip = u'当前 IP：35.241.80.59  来自于：中国 香港   cloud.google.com'
    print(string_ip)
    result_pattern = pattern.search(string_ip)
    print(pattern.search(string_ip))

    result = re.findall(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", string_ip)
    print(result)
