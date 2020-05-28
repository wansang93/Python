# 1. 파일 열기
in_fp = open('C:/Windows/win.ini', 'r')
out_fp = open('C:/images/new_win.ini', 'w')

# 2. 파일 읽기, 또는 쓰기
while True:
    in_str = in_fp.readline()
    if not in_str:
        break
    out_fp.writelines(in_str)

# # 라인수가 적을 경우
# in_str_list = in_fp.readlines()
# print(in_str_list)
# for line in in_str_list:
#     print(line, end='')

# 3. 파일 닫기
in_fp.close()
out_fp.close()
print('ok')

# # 파일 열고 수정하기
# new_fp = open('C:/images/new_win.ini', 'r')

# while True:
#     in_str = new_fp.readline()
#     if not in_str:
#         break
#     print(in_str, end='')

# new_fp.close()
