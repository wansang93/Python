### 1부터 100까지의 합계
hap = 0
#hap = 1 + 2 + 3 + .....

for  i  in  range(12345,100001,1) : # range(0,101), range(101)
    if i % 7878 == 0 :
        hap += i

print(hap)

"""
퀴즈4-1. 1부터 100까지 홀수의 합계
퀴즈4-2. 1부터 100까지 7의 배수의 합계
퀴즈4-3. 12345부터 100000까지  7878의 배수의 합계
"""

num = 0
for i in range(1, 101, 2):
    num += i

num2 = 0
for i in range(7, 101, 7):
    num2 += i

num3 = 0
for i in range(0, 100001, 7878):
    if i > 12345:
        num3 += i

print(num)
print(num2)
print(num3)