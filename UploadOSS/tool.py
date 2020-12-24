#!/usr/bin/env python
# coding:utf8
from colorama import  init, Fore, Back, Style
import os
import json
import codecs
# import hashlib
# import subprocess
# import shutil
# import time
# import zipfile

import platform
platform_name = platform.platform()
IsIos = platform_name.find("Darwin") == 0
IsWds = platform_name.find("Windows") == 0

self_path = os.path.dirname(os.path.abspath(__file__))
oss_config = self_path + "\\oss_config.json"


def run_script(py_script):
    if IsIos:
       return os.system('python3 ' + py_script)
    else:
       return os.system(py_script)


init(autoreset=True)


def path_replace(path):
    return path.replace('\\', '/')


def path_replace2(path):
    return path.replace('/', '\\')


# 获取json文件内容
def read_file_json(file_path):
    fp = codecs.open(file_path, 'r+', 'utf-8')
    load_data = fp.read()
    fp.close()
    tp_connect = json.loads(load_data)
    return tp_connect


# 获取文件内容
def read_file_string(file_path):
    fp = codecs.open(file_path, 'r+', 'utf-8')
    load_data = fp.read()
    fp.close()
    return load_data


# 保存内容
def save_file_string(file_path, buf):
    buf = buf.replace(' ', '')
    fp = codecs.open(file_path, 'w+', 'utf-8')
    fp.write(buf)
    fp.flush()
    fp.close()


# 获得ftp文件信息
def get_server_info():
    server_conf = read_file_json(oss_config)
    return server_conf


# 获得目录下的指定类型文件
def get_dir_file2(srcPath, file_array):
    apk_list = []
    for maindir, subdir, file_name_list in os.walk(srcPath):
        for filename in file_name_list:
            # 绝对路径
            apath = os.path.join(maindir, filename)
            apath = path_replace(apath)

            # 后缀
            ext = os.path.splitext(apath)[1]

            # 查找类型
            for find_type in file_array:
                if ext == find_type:
                    apk_list.append(apath)
                    break
    return apk_list


def get_meta_json_ct_ignore_piexl():
    return 2 * 2


def get_file_ext(path):
    return os.path.splitext(path)[1]


def get_file_name(path):
    filename = os.path.basename(path)
    return filename.split('.')[0]


# 写入json文件 str_data
def write_file_content(file_path, str_data):
    save_file_string(file_path, str_data)


# 写入json文件 json_obj
def write_file_json(file_path, json_obj, isDebug=False):
    if isDebug == True:
        save_file_string(file_path, json.dumps(json_obj, indent=4))
    else:
        save_file_string(file_path, json.dumps(json_obj))


# 写入json文件 json_obj
def write_file_json_indent4(file_path, json_obj):
    save_file_string(file_path, json.dumps(json_obj, indent=4))
