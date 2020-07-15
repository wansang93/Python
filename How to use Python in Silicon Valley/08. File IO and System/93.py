file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
    'How to use Python in Silicon Valley/08. File IO and System/test.txt')

s = """\
AaA
BbB
CcC
DdD
"""

# 파일 쓰기
with open(file_path, 'w') as f:
    f.write(s)

# 한꺼번에 읽어오기
with open(file_path, 'r') as f:
    print(f.read())

# 한줄씩 읽어오기
with open(file_path, 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break

# chuck 단위로 읽어오기
# 네트워크 프로그래밍때도 chuck 단위로 읽어오기 가능
with open(file_path, 'r') as f:
    while True:
        chuck = 2
        line = f.readline(chuck)
        print(line)
        if not line:
            break