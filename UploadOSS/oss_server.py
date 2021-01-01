#!/usr/bin/env python
# coding:utf8
# ftp 上传服务
import os
import sys
import threading
import tool
# import datetime
# import string
# import random
import time
import oss2
from AesEverywhere import aes256        # pip install aes-everywhere

sys.setrecursionlimit(10000000)

# import path
self_path = os.path.dirname(os.path.abspath(__file__))
self_path = tool.path_replace(self_path)
print("self_path:" + self_path)

oss2_auth = None
oss2_bucket = None

g_root_path = ""
g_upload_count = 0    # 总上传数量
g_succee_count = 0    # 成功数量
g_upload_list = []    # 上传列表
g_thread_max = 50       # 最大上传线程
g_thread_lock = None    # 线程锁


class CFileInfo:
    def __init__(self, local_file, cloud_name):
        self.local_file = local_file
        self.cloud_name = cloud_name
        self.count = 0  # 0：无效状态 1：上传中
        self.th_idx = 0


# 文件上传
def uploadThread(file_info):
    global oss2_bucket
    global g_succee_count
    global g_thread_lock
    global g_upload_count
    try:
        local_file = file_info.local_file
        cloud_name = file_info.cloud_name
        th_idx = file_info.th_idx
        result = oss2_bucket.put_object_from_file(cloud_name, local_file)
        if result.status == 200:
            g_thread_lock.acquire(True)
            print("成功: " + str(g_succee_count) + "/" + str(g_upload_count) + ",t:" + str(int(th_idx/10)) + str(int(th_idx % 10)) + "=" + local_file)
            g_succee_count += 1
            g_thread_lock.release()

            start_next_thread(th_idx)
            return True

        # 上传失败
        start_retry_thread(file_info)
        return False

    # catch 失败
    except Exception as error:
        start_retry_thread(file_info)
        return False

    # 默认失败
    start_retry_thread(file_info)
    return False


# 开启上传线程
def start_next_thread(th_idx):
    global g_thread_lock
    global g_upload_list

    g_thread_lock.acquire(True)
    count = len(g_upload_list)
    file_info = None
    if count > 0:
        file_info = g_upload_list.pop()
        file_info.th_idx = th_idx
        # print("开始上传:",file_info.local_file)
    g_thread_lock.release()

    if file_info:
        uploadThread(file_info)


# 创建进程
def start_new_thread(th_idx):
    global g_thread_lock
    global g_upload_list

    g_thread_lock.acquire(True)
    count = len(g_upload_list)
    file_info = None
    if count > 0:
        file_info = g_upload_list.pop()
        file_info.th_idx = th_idx
        # print("开始上传:",file_info.local_file)
    g_thread_lock.release()

    if file_info:
        # 创建
        t = threading.Thread(target=uploadThread, args=[file_info])
        # 不阻塞
        t.setDaemon(True)
        # 启动
        t.start()
        return t
    return None


# 失败线程，重新上传，成功为止
def start_retry_thread(file_info):
    # 1秒后重试
    time.sleep(1)
    g_thread_lock.acquire(True)
    file_info.count += 1
    print('重试:' + str(file_info.count) + '次: ' + file_info.local_file)
    g_thread_lock.release()
    uploadThread(file_info)


# 开始上传
def startUploadFinder(uploadZip, local_root, kind_id, ver):
    global g_thread_lock
    global g_thread_max
    global g_root_path
    global g_upload_list
    global g_upload_count
    global oss2_bucket
    global oss2_auth
    global g_succee_count

    g_root_path = local_root
    print('上传路径:' + g_root_path)

    versions = tool.read_file_json(os.path.join(g_root_path, 'version.manifest'))

    server_info = tool.get_server_info()
    ossinfo = server_info['oss_info']
    ver_bucket_name = server_info['ver_bucket_name']

    ver_info = server_info['ver_info']
    if not (ver in ver_info):
        return 1
    ver_path = ver_info[ver]

    upload_path = server_info['upload_path']
    root_path = upload_path['root']
    if not (kind_id in upload_path):
        return 2
    kind_path = upload_path[kind_id]
    upload_root = ver_path + root_path + kind_path

    key = 'Ua^FkU=+l_TYgODQ'
    accessKey = ossinfo['accessKey']
    accessKeySecret = ossinfo['accessKeySecret']

    accessKey = aes256.decrypt(accessKey, key)
    accessKeySecret = aes256.decrypt(accessKeySecret, key)
    # bytes转str
    accessKey = bytes.decode(accessKey)
    accessKeySecret = bytes.decode(accessKeySecret)

    endPoint = ossinfo['endpoint']
    # bucket_name = ossinfo['bucket_name']
    bucket_name = ver_bucket_name[ver]

    oss2_auth = oss2.Auth(accessKey, accessKeySecret)
    oss2_bucket = oss2.Bucket(oss2_auth, endPoint, bucket_name)
    # ret = oss2_bucket.delete_object(upload_root)

    upload_local_path = local_root
    if '1' != kind_id:
        upload_local_path = local_root + "/" + kind_path

    # 本地上传文件列表
    g_upload_list = []
    for maindir, subdir, file_list in os.walk(upload_local_path):
        # 忽略非上传版本目录
        hotver = str(maindir)
        if hotver.find(versions['version']) == -1:
            continue

        for filename in file_list:
            apath = os.path.join(maindir, filename)
            apath = apath.replace('\\', '/')

            file_path = apath.replace(upload_local_path, '')
            cloud_name = upload_root + file_path
            file_info = CFileInfo(apath, cloud_name)
            g_upload_list.append(file_info)

    g_upload_count = len(g_upload_list)

    # 多线程上传===========================================
    print('开始上传: 文件数量=' + str(g_upload_count))
    g_succee_count = 0
    start_time = time.time()

    # 最大上传线程
    g_thread_lock = threading.Lock()
    thread_list = []
    for i in range(g_thread_max):
        t = start_new_thread(i)
        if t:
            thread_list.append(t)

    for t in thread_list:
        t.join()

    # 上传完成
    end_time = time.time()
    print('资源文件上传完成')
    print('上传路径:', g_root_path)
    print('上传数量:', g_upload_count)
    print('成功数量:', g_succee_count)
    print('上传耗时:', end_time-start_time)
    print('即将上传资源版本文件......')

    file_info = CFileInfo(os.path.join(g_root_path, 'project.manifest'), os.path.join(upload_root, 'project.manifest'))
    g_upload_list.append(file_info)

    file_info = CFileInfo(os.path.join(g_root_path, 'version.manifest'), os.path.join(upload_root, 'version.manifest'))
    g_upload_list.append(file_info)

    g_upload_count = len(g_upload_list)

    # 多线程上传===========================================
    print('开始上传: 文件数量=' + str(g_upload_count))
    g_succee_count = 0

    # 最大上传线程
    g_thread_lock = threading.Lock()
    thread_list = []
    for i in range(g_thread_max):
        t = start_new_thread(i)
        if t:
            thread_list.append(t)

    for t in thread_list:
        t.join()

    # 上传完成
    all_end_time = time.time()
    print('上传完成:')
    print('上传路径:', g_root_path)
    print('上传数量:', g_upload_count)
    print('成功数量:', g_succee_count)
    print('上传耗时:', all_end_time - end_time)

    print('所有资源上传总耗时:', all_end_time - start_time)
    return 0
