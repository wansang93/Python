import os

file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
             'How to use Python in Silicon Valley/08. File IO and System/')

# 환경 설정하기
# # 디렉토리 만들기(해당 이름의 디렉토리가 없을 때 가능)
# os.mkdir(file_path + 'test_dir')
#
# # 디렉토리 만들기(해당 이름의 디렉토리가 없을 때 가능)
# os.mkdir(file_path + 'test_dir/sub_dir')
#
# # 파일 만들기
# import pathlib  # python -v >= 3.0
# pathlib.Path(file_path + 'test_dir/empty.txt').touch()
# pathlib.Path(file_path + 'test_dir/sub_dir/sub_text.txt').touch()


import tarfile

# tarfile 로 압축하기
with tarfile.open(file_path + 'test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

# tarfile 로 압축풀기
with tarfile.open(file_path + 'test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='test_tar')
    with tr.extractfile('test_dir/sub_dir/sub_text.txt') as f:
        print(f.read())
