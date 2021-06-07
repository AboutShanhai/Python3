#!/usr/bin/env python
# coding:utf8
# ftp 上传服务
import os
import sys
import threading
import tool
import time
from AesEverywhere import aes256        # pip install aes-everywhere
from qcloud_cos import CosConfig        # pip install -U cos-python-sdk-v5
from qcloud_cos import CosS3Client


sys.setrecursionlimit(10000000)

# import path
self_path = os.path.dirname(os.path.abspath(__file__))
self_path = tool.path_replace(self_path)
print("self_path:" + self_path)

cos_client = None

g_root_path = ""
g_upload_count = 0    # 总上传数量
g_succee_count = 0    # 成功数量
g_upload_list = []    # 上传列表
g_thread_max = 50       # 最大上传线程
g_thread_lock = None    # 线程锁


class CFileInfo:
    def __init__(self, LocalFilePath, Key):
        self.LocalFilePath = LocalFilePath
        self.Key = Key
        self.count = 0  # 0：无效状态 1：上传中
        self.th_idx = 0


# 文件上传
def uploadThread(file_info):
    global g_succee_count
    global g_thread_lock
    global g_upload_count
    try:
        LocalFile_Path = file_info.LocalFilePath
        Web_Key = file_info.Key
        th_idx = file_info.th_idx
        response = cos_client.upload_file(
            Bucket=cos_bucket,
            LocalFilePath=LocalFile_Path,   # 代指本地文件路径
            Key=Web_Key,   # 上传到桶之后的文件名
            MAXThread=50,
            EnableMD5=False
        )
        # print(response['ETag'])

        g_thread_lock.acquire(True)
        print("成功: " + str(g_succee_count) + "/" + str(g_upload_count) + ",t:" + str(int(th_idx/10)) + str(int(th_idx % 10)) + ",Path=" + LocalFile_Path)
        g_succee_count += 1
        g_thread_lock.release()

        start_next_thread(th_idx)
        return True

    # catch 失败
    except Exception as error:
        print("异常进行重试处理 Path=" + file_info.LocalFilePath)
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
    print('重试:' + str(file_info.count) + '次: ' + file_info.LocalFilePath)
    g_thread_lock.release()
    uploadThread(file_info)


# 开始上传
def startUploadFinder(local_root, ver):
    global g_thread_lock
    global g_thread_max
    global g_root_path
    global g_upload_list
    global g_upload_count
    global g_succee_count

    global cos_bucket
    global cos_client

    g_root_path = local_root
    print('上传路径:' + g_root_path)

    versions = tool.read_file_json(os.path.join(g_root_path, 'version.manifest'))
    server_info = tool.get_server_info()

    ver_info = server_info['ver_info']
    if not (ver in ver_info):
        return 1
    ver_path = ver_info[ver]

    ver_bucket_name = server_info['ver_bucket_name']
    if not (ver in ver_bucket_name):
        return 2
    cos_bucket = ver_bucket_name[ver]

    cosinfo = server_info['cos_info']
    secret_id = cosinfo['SecretId']
    secret_key = cosinfo['SecretKey']
    region = cosinfo['Region']

    key = 'Ua^FkU=+l_TYgODQ'
    secret_id = aes256.decrypt(secret_id, key)
    secret_key = aes256.decrypt(secret_key, key)

    # secret_id = 'secretId'        # 替换为用户的 secretId
    # secret_key = 'secretKey'      # 替换为用户的 secretKey
    # region = 'ap-guangzhou'       # 替换为用户的 Region
    # 2. 获取客户端对象
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
    cos_client = CosS3Client(config)

    versions = tool.read_file_json(os.path.join(g_root_path, 'version.manifest'))
    # 本地上传文件列表
    g_upload_list = []
    for maindir, subdir, file_list in os.walk(g_root_path):
        # 忽略非上传版本目录
        hotver = str(maindir)
        if hotver.find(versions['version']) == -1:
            continue

        for filename in file_list:
            apath = os.path.join(maindir, filename)
            apath = apath.replace('\\', '/')

            file_path = apath.replace(g_root_path, '')
            cloud_name = ver_path + file_path
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
    print('上传耗时:', end_time - start_time)
    print('即将上传资源版本文件......')

    g_upload_list = []
    LocalFile = g_root_path + '/project.manifest'
    WebKey = ver_path + '/project.manifest'
    file_info = CFileInfo(LocalFile, WebKey)
    g_upload_list.append(file_info)

    LocalFile = g_root_path + '/version.manifest'
    WebKey = ver_path + '/version.manifest'
    file_info = CFileInfo(LocalFile, WebKey)
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
