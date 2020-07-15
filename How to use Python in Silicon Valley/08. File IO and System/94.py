file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
    'How to use Python in Silicon Valley/08. File IO and System/test.txt')

s = """\
AaA  #  0  1  2  3
BbB  #  5  6  7  8
CcC  # 10 11 12 13
DdD  # 15 16 17 18
"""

with open(file_path, 'r') as f:
    for i in range(20):
        print(i, f.tell(), ':', f.read(1))
    f.seek(5)
    print(f.read(5))

    # print(f.tell())  # 커서 어디?
    # print(f.read(2))  # 커서로 부터 2개 읽기
    # print(f.tell())
    # f.seek(3)
    # print(f.read(1))
    # f.seek(4)  # 커서 5번째로 이동
    # print(f.read(2))  # 커서 5번째 다음거 1개 읽기
    # f.seek(15)
    # print(f.read(1))
