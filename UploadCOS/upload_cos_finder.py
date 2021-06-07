#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import tool
import cos_server

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

# import path
self_path = os.path.dirname(os.path.abspath(__file__))
self_path = tool.path_replace(self_path)
self_out_path = os.path.abspath(os.path.join(self_path, ".."))
# self_out_path = tool.path_replace(self_out_path)


# 默认数据
ver = str(1)
local_root = "D:\\WorkSpace\\ZhanDouNiu\\SVNZhanDouNiu\\Client\\hotupdate"


if len(sys.argv) > 1:
    ver = sys.argv[1]
    local_root = sys.argv[2]

local_root = tool.path_replace(local_root)

local_root = os.path.join(self_out_path, 'hotupdate')
local_root = tool.path_replace(local_root)

print("-------------------------------------------------------------------")
print("self_path = " + self_path)
print("ver = " + ver)
print("local_root = " + local_root)
print("-------------------------------------------------------------------")

# class CFileInfo:
#     def __init__(self, LocalFilePath, Key):
#         self.LocalFilePath = LocalFilePath
#         self.Key = Key
#         self.count = 0  # 0：无效状态 1：上传中
#         self.th_idx = 0


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

    ret = cos_server.startUploadFinder(local_root, ver)
    if ret == 0:
        print('腾讯云COS资源上传完成!')
        os.system('pause')
    elif ret == 1:
        print("未找到 ver=" + str(ver) + "输入的Ver版本信息！")
        os.system('pause')
    elif ret == 2:
        print("未找到 ver_bucket" + str(ver) + "-的配置路径，请检查 cos_config.json 的配置！")
        os.system('pause')


start_upload()

# secret_id = 'SecretId'      # 替换为用户的 secretId
# secret_key = 'SecretKey'      # 替换为用户的 secretKey
# region = 'ap-guangzhou'     # 替换为用户的 Region

# config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
# # 2. 获取客户端对象
# client = CosS3Client(config)

# upload_root = 'dev_ver\\hotupdate'
# upload_root = upload_root.replace('\\', '/')
# upload_local_path = 'D:\\WorkSpace\\ZhanDouNiu\\SVNZhanDouNiu\\Client\\hotupdate'
# upload_local_path = upload_local_path.replace('\\', '/')

# versions = tool.read_file_json(os.path.join(upload_local_path, 'version.manifest'))
# # 本地上传文件列表
# g_upload_list = []
# for maindir, subdir, file_list in os.walk(upload_local_path):
#     # 忽略非上传版本目录
#     hotver = str(maindir)
#     if hotver.find(versions['version']) == -1:
#         continue

#     for filename in file_list:
#         apath = os.path.join(maindir, filename)
#         apath = apath.replace('\\', '/')

#         file_path = apath.replace(upload_local_path, '')
#         cloud_name = upload_root + file_path
#         file_info = CFileInfo(apath, cloud_name)
#         g_upload_list.append(file_info)

# g_upload_count = len(g_upload_list)

# for files in g_upload_list:
#     # 文件上传
#     response = client.upload_file(
#         Bucket='fagka-1302952074',
#         LocalFilePath=files.LocalFilePath,   # 代指本地文件路径
#         Key=files.Key,   # 上传到桶之后的文件名
#         MAXThread=50,
#         EnableMD5=False
#     )
#     print(response['ETag'])

# g_upload_list = []
# LocalFile = os.path.join(upload_local_path, 'project.manifest')
# LocalFile = LocalFile.replace('\\', '/')
# WebKey = os.path.join(upload_root, 'project.manifest')
# WebKey = WebKey.replace('\\', '/')
# file_info = CFileInfo(LocalFile, WebKey)
# g_upload_list.append(file_info)

# LocalFile = os.path.join(upload_local_path, 'version.manifest')
# LocalFile = LocalFile.replace('\\', '/')
# WebKey = os.path.join(upload_root, 'version.manifest')
# WebKey = WebKey.replace('\\', '/')
# file_info = CFileInfo(LocalFile, WebKey)
# g_upload_list.append(file_info)

# for files in g_upload_list:
#     # 文件上传
#     response = client.upload_file(
#         Bucket='fagka-1302952074',
#         LocalFilePath=files.LocalFilePath,   # 代指本地文件路径
#         Key=files.Key,   # 上传到桶之后的文件名
#         MAXThread=50,
#         EnableMD5=False
#     )
#     print(response['ETag'])
