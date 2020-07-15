import os

file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
    'How to use Python in Silicon Valley/08. File IO and System/')

print(os.path.exists(file_path + 'test.csv'))
print(os.path.isdir(file_path))

# 파일 이름 바꾸기
# os.rename(file_path + 'test.txt', file_path + 'renamed.txt')

# 바로가기 만들기
# os.symlink(file_path + 'renamed.txt', file_path + 'symlink.txt')

# 디렉토리 만들기(해당 이름의 디렉토리가 없을 때 가능)
os.mkdir(file_path + 'test_dir')

# 디렉토리 삭제하기(디렉토리 안 아무것도 없을 때 가능)
os.rmdir(file_path + 'test_dir')

# 현재 실행되는 디렉토리를 반환
cwd = os.getcwd()  # current working directory

# 파일 만들기
import pathlib  # python -v >= 3.0
pathlib.Path(file_path + 'empty.txt').touch()

import glob

# 해당 디렉토리의 하위 목록을 리스트로 반환
print(glob.glob(cwd + '\\*'))

import shutil

# 파일 복사하기
shutil.copy('복사하고 싶은 파일', '복사한 파일 이름')

# 해당 디렉토리 모두 삭제
shutil.rmtree('삭제하고 싶은 디렉토리')
