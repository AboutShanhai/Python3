#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import tool
import oss_server

# import path
self_path = os.path.dirname(os.path.abspath(__file__))
self_path = tool.path_replace(self_path)
self_out_path = os.path.abspath(os.path.join(self_path, ".."))
# self_out_path = tool.path_replace(self_out_path)

# 默认数据
g_upload_zip = '1'
kind_id = str(0)
ver = str(1)
local_root = "D:\\WorkSpace\\ZhanDouNiu\\SVNZhanDouNiu\\Client\\hotupdate"


if len(sys.argv) > 1:
    g_upload_zip = sys.argv[1]
    kind_id = sys.argv[2]
    ver = sys.argv[3]
    local_root = sys.argv[4]

local_root = tool.path_replace(local_root)

local_root = os.path.join(self_out_path, 'hotupdate')
local_root = tool.path_replace(local_root)

print("-------------------------------------------------------------------")
print("g_upload_zip = " + str(g_upload_zip))
print("self_path = " + self_path)
print("kind_id = " + kind_id)
print("ver = " + ver)
print("local_root = " + local_root)
print("-------------------------------------------------------------------")


def start_upload():
    # 简单校验路径，必须有发布目录存在，避免上传错误路径
    if local_root.find('hotupdate') == -1:
        print('请检查发布路径是否异常，上传路径必须在 hotupdate 路径下，执行完毕')
        os.system('pause')
        return

    # 简单校验路径，必须有发布目录存在，避免上传错误路径
    if not os.path.exists(local_root):
        print('上传路径不存在，请检查后重新执行')
        os.system('pause')
        return

    f = open(local_root + "/version.manifest")
    verCheck = True
    for line in f:
        if line.find("dev_ver") >= 0 and '1' == ver :
            print(line)
            verCheck = False

        if line.find("test_ver") >= 0 and '2' == ver :
            print(line)
            verCheck = False

        if line.find("official_ver") >= 0 and '3' == ver :
            print(line)
            verCheck = False

    f.close()
    if verCheck:
        print('上传路径资源版本和输入版本不匹配，请检查 version.manifest 配置中的OSS路径后重新执行')
        os.system('pause')
        return

    print("-------------------------------------------------------------------")
    print('请认真检查路径和和参数配置,参数上传将无法撤回...')
    os.system('pause')

    print('开始上传')
    ret = oss_server.startUploadFinder(g_upload_zip, local_root, kind_id, ver)
    if ret == 0:
        print('OSS资源上传完成!')
        os.system('pause')
    elif ret == 1:
        print("未找到 ver=" + str(ver) + "输入的Ver版本信息！")
        os.system('pause')
    elif ret == 2:
        print("未找到 kindid=" + str(kind_id) + "-的配置路径，请检查 oss_config.json 的配置！")
        os.system('pause')


start_upload()
