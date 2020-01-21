# 빈 메모리를 확보한 후에, 작업하기.
import random
SIZE = 10

# 1. 메모리 확보 개념 (타 언어 스타일)
aa = [] # 빈 리스트 준비
for i in range(SIZE):
    aa.append(0)

# 2. 메모리에 필요한 값 대입 --> 파일 읽기
for i in range(SIZE):  # range(0, 4, 1)
    num = random.randint(0, 99)
    aa[i] = num
print('원 영상 -->', aa)

# 3. 메모리 처리/조작/연산~~~~ --> 알고리즘(컴퓨터 비전, 영상처리)
sum = 0
for i in range(SIZE):
    aa[i] += 10
    if aa[i] > 99:
        aa[i] = 99

## 4. 출력
print('결과 영상 --> ', aa)
