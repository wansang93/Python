# formating 과 f-string을 비슷하게 사용할 수 있어서 f-string으로 표현하였습니다.
t = (1, 2, 3)

# 1. 기본적인 사용법
print(f'{t[0]}, {t[2]}')
# 1, 3
print('{0} {2}'.format(*t))
# 1 3

# 2. 빈공간 만들기
center='center'; fill='*'; align='^'; width=30
left = 'left'; right = 'right'
print(f'{left:<30}')
print(f'{right:>30}')
print(f'{center:^30}')
print(f'{center:{fill}{align}{width}}')
# left
#                         right
#             center
# ************center************

# 3. 숫자에 소숫점 만들기
print(f'{123456789:,}')  # 123,456,789

# 4. 숫자에 + 적기
print(f'{3.14:+f} {3.14:+f}')  # +3.140000 +3.140000

# 5. % 표기법
nums = 19 / 22
print(f'{nums:.2%}')  # 86.36%

# 6. 숫자 문자로 표기하기
hdr = 100
print(f'{hdr:d} {hdr:#x} {hdr:#o} {hdr:#b}')  # 100 0x64 0o144 0b1100100

# 7. 이쁘게 2, 8, 10, 16진수 출력하기
for i in range(16):
    for base in 'bodX':
        # i값을 5자리로 {b} {o} {d} {X}형식으로 출력
        print(f'{i:5{base}}', end=' ')
    print()
#     0     0     0     0
#     1     1     1     1
#    10     2     2     2
#    11     3     3     3
#   100     4     4     4
#   101     5     5     5
#   110     6     6     6
#   111     7     7     7
#  1000    10     8     8
#  1001    11     9     9
#  1010    12    10     A
#  1011    13    11     B 
#  1100    14    12     C
#  1101    15    13     D
#  1110    16    14     E
#  1111    17    15     F