@echo ��ȷ���ϴ�"��Ѷ�ƶ���洢COS"���ܣ�������ǰ�������ɽű�����Դ������
@echo ��ȷ���ϴ�"��Ѷ�ƶ���洢COS"���ܣ�������ǰ�������ɽű�����Դ������
@echo ��ȷ���ϴ�"��Ѷ�ƶ���洢COS"���ܣ�������ǰ�������ɽű�����Դ������

@echo �������ϴ�����Ϸ�汾(��:1-dev 2-test 3-official_ver):
set /p ver=
echo %ver%

::@echo �������ϴ���·��(��: D:\WorkSpace\ZhanDouNiu\SVNZhanDouNiuClient\hotupdate):
::set /p local_path=
::echo %local_path%

set local_path='D:\hotupdate'
py -3 upload_cos_finder.py %ver% %local_path%
pause