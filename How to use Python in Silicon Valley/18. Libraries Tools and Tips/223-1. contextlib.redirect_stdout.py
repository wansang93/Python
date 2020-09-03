import logging
import sys

# 1. input 대신에 sys.stdin 사용
# high level 에서 실행
x = input('Enter: ')
print(x)

# low level 에서 실행
for line in sys.stdin:
    print(line)
    break

# 2. print 대신에 sys.stdout.write 사용
print('hello')
sys.stdout.write('hello')

# 3. 콘솔에 나온 메시지 파일화 하기
import contextlib

file_path = (r'C:/Users/wansang/Desktop/Gitrep/Python/How '
    r'to use Python in Silicon Valley/18. Libraries Tools and Tips')

with open(file_path + '/stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        # print('hello')
        help(sys.stdout)