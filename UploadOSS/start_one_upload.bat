@echo ��ȷ���ϴ�"�����ƶ���洢OSS"���ܣ�������ǰ�������ɽű�����Դ������
@echo ��ȷ���ϴ�"�����ƶ���洢OSS"���ܣ�������ǰ�������ɽű�����Դ������
@echo ��ȷ���ϴ�"�����ƶ���洢OSS"���ܣ�������ǰ�������ɽű�����Դ������

@echo �������ϴ�����Ϸ�汾(��:1-dev 2-test 3-official_ver):
set /p ver=
echo %ver%

::@echo �������ϴ���·��(��: D:\WorkSpace\ZhanDouNiu\SVNZhanDouNiuClient\hotupdate):
::set /p local_path=
::echo %local_path%

set up_load_zip=1
set kindid=0
set local_path='D:\hotupdate'
py -3 upload_kind_finder.py %up_load_zip% %kindid% %ver% %local_path%
pause