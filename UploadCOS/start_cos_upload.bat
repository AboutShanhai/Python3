@echo 请确认上传"腾讯云对象存储COS"功能，必须提前编译生成脚本与资源！！！
@echo 请确认上传"腾讯云对象存储COS"功能，必须提前编译生成脚本与资源！！！
@echo 请确认上传"腾讯云对象存储COS"功能，必须提前编译生成脚本与资源！！！

@echo 请输入上传的游戏版本(例:1-dev 2-test 3-official_ver):
set /p ver=
echo %ver%

::@echo 请输入上传根路径(例: D:\WorkSpace\ZhanDouNiu\SVNZhanDouNiuClient\hotupdate):
::set /p local_path=
::echo %local_path%

set local_path='D:\hotupdate'
py -3 upload_cos_finder.py %ver% %local_path%
pause