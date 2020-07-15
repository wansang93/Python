file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
    'How to use Python in Silicon Valley/08. File IO and System/test.txt')

s = """\
AaA
BbB
CcC
DdD 123
"""

# w+ 쓰고 보기, r+ 읽고 보기
with open(file_path, 'w+') as f:
    # f.read() !!!주의!!! -> 읽기 부터 하면 파일이 날라감 
    f.write(s)
    f.seek(0)  # 커서 위치 이동 0번째로
    print(f.read())  # 읽기 가능