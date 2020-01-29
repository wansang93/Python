# 04일차 파이썬 기본문법 190610

## 복습

2주차 : 파이썬용 APP

3주차 : Numpy, Pandas, Matplotlib, OpenCU을 한다.

Numby는 행렬을 다루기 때문에 좋고 연산 속도가 빠르다.

OpenCU는 C++에서 지원이 잘되는데 파이썬에서도 호환이 잘 된다.

유명한 DBMS(DB Program): Oracle, SQL Server, MySQL, Maria, (SQLite)

## 파이썬

### 책 : 파이썬 for Beginner

#### 5장 - 조건문

1. 기본 if문

    ``` python
    if 조건:
        실행
    elif 조건2:
        실행2
    else:
        return None
    ```

2. 삼항 연산자를 사용한 if문

    ``` python
    실행 if 조건 elif 조건2 else 실행2
    a = 1 if a=b else 0
    ```

#### 6장 - 반복문

1. 중첩 for문, range와 enumerate

    ``` python
    for 변수 in range(시작값이상, 끝값미만, 증감값):
        for 변수 i, name in enumerate(순서가 있는 자료형):
            실행(실행 횟수는 range * 자료형 갯수)
    ```

    > range는 시작값이상에서 증감값만큼 증감하다 끝값미만까지 반환한다.
    >
    > enumerate는 순서가 있는 자료형의 첫번째 값이 자료형의 순서, 두번째값이 자료형의 값을 반환한다.

2. while 문, 무한 루프

    ``` python
    while 조건:
        실행(실행 후 다시 조건으로)
        
    while Ture:
        실행(계속 실행)
    ```

3. break문, continue문

    반복문에서 break를 만나면 무조건 반복문을 빠져나온다.

    반복문에서 continue를 만나면 남은 부분을 무조건 건너뛰고 반복문 위로 다시 돌아가 실행한다.

#### 7장 - 리스트, 튜플, 딕셔너리

[리스트, 튜플, 딕셔너리 다루는 함수들 링크](http://www.hanul93.com/kicomav-python-2)

1. 리스트의 기본과 2차원 리스트

    - 리스트 생성과 값 채워넣기

        ``` python
        리스트이름 = [1,2,3,4]  # 리스트 선언
        리스트이름.append(값)  # 리스트의 순서대로 값을 앞에서 채워넣는다.
        ```

        > 리스트의 특징은 가장 앞에 번호가 0번이다. N개의 리스트를 만드려면 가장 마지막 번호는 N-1이다.

    - 리스트 접근하기

        ``` python
        a[0], a[1], a[-2]  # 앞에서 0+1번째값, 1+1번째 값, 뒤에서(-) 2번째 값
        a[3:6]  # 3+1부터 6+1전까지 출력
        a[(초깃값):(마지막값):(뛰어넘기))]  # 초깃값부터 마지막값 전까지 점프수
        a[1:5:2]  # a[1], a[3] 이렇게 인덱싱 된다.
        a[5:2:-2]  # a[5] a[3] 이렇게 인덱싱 된다.
        ```

    - 리스트 조작 함수

        ``` python
        len(mylist)  # mylist의 길이를 반환해 준다.
        # 값 추가
        mylist.aapend(값)  # 값을 mylist 가장 뒤에 채워 넣는다.
        mylist.extend([list2])  # mylist에 list2의 값을 넣는다. mylist+list2와 같다.
        mylist.insert(위치, 값)  # mylist의 위치번째에 값을 삽입한다.
        # 값 삭제
        mylist.pop()  # 마지막 값을 mylist에서 뺀다.
        mylist.pop(0)  # 0번째 값을 mylist에서 뺀다.
        mylist.remove(지울값)  # 지울값을 지운다.단 값이 많은 경우 최초를 지운다.
        # 리스트 삭제
        mylist.clear()  # mylist를 내용을 모두 지운다.
        del(mylist[0])  # mylist 자체를 지운다.
        # 리스트 조회
        mylist.index(찾을 값)  # 찾을 값의 위치를 찾는다. 단 값이 많은 경우 최초의 위치를 알려준다.
        mylist.count(찾을 값)  # 찾을 값을 카운트해 결과를 반환한다. 
        # 리스트 수정
        mylist.reverse()  # mylist를 뒤집는다. 앞뒤 순서가 바뀐다.
        newlist = mylist  # newlist에 mylist를 얕은 복사(shallow Copy)한다.
        newlist = mylist.copy()  # newlist에 mylist를 깊은 복사(Deep Copy)한다.
        newlist = mylist.sort()  # newlist에 mylist를 정렬하여 한다.
        sorted(mylist)  # mylist를 정렬한다.
        ```

2. 튜플(tuple)

    튜플은 리스트에서 값을 수정할 수 없게 하여 읽기 전용 자료를 저장할 때 사용한다.

    생성은 리스트와 비슷하게 생성하는데 []대신 ()를 사용한다.

    - 튜플 생성

        ``` python
        mytuple = (1, 2, 3)  # 튜플을 생성한다.
        mytuple = tuple([1, 2, 3])  # 튜플을 생성한다.
        ```

3. 딕셔너리

    딕셔너리는 {}로 묶어서 구성한다. 순서가 없다.

    - 딕셔너리 생성

        ``` python
        mydic = {'키1': '값1', '키2': '값2', '키3': '값3'}
        ```

    - 딕셔너리 조작 함수

        ``` python
        mydic
        items()
        keys()
        values()
        update()
        pop()
        reverse()
        sort()
        ```

    - 딕셔너리 정렬

        딕셔너리는 순서가 없는 자료형이기 때문에 정렬하는 방법이 리스트나 튜플과는 다르다.

        ``` python
        import operator

        trainDic, trainList = {}, []
        trainDic = {'Thomas': '토마스', 'Edward': '에드워드', 'Henry': '헨리', 'Gothen': '고든', 'James': '제임스'}
        trainList = sorted(trainDic.items(), key=operator.itemgetter(0))
        # 0으로 설정하면 킷값으로, 1은 자료값을 바탕으로 정렬한다.        
        ```

4. 세트(Set)

    세트는 키만 모아 놓은 딕셔너리의 특수한 형태이다. 딕셔너리의 키는 중복되면 안 되므로 세트에 들어있는 값은 항상 유일하다.

    중복성을 제거하거나 합칠 때 유용하게 쓰이는 자료형이다. 역시 딕셔너리와 마찬가지로 순서가 없다.

    ``` python
    mylist = ['김밥', '김밥', '도넛', '도시락', '삼각김밥', '도시락', '김밥']
    mylist = set(mylist)
    print(mylist)  # {'삼각김밥', '도시락', '도넛', '김밥'}
    ```

    두 세트 사이의 교집합, 합집합, 차집합, 대칭 차집합을 구할 수도 있다.

    ``` python
    myset1 = {1, 2, 3, 4, 5}
    myset2 = {4, 5, 6, 7}
    myset1 & myset2  # myset1.intersection(myset2)
    # {4, 5}
    myset1 | myset2  # myset1.union(myset2)
    # {1, 2, 3, 4, 5, 6, 7}
    myset1 - myset2  # myset1.difference(myset2)
    # {1, 2, 3}
    myset1 ^ myset2  # myset1.symmetric_difference(myset2)
    # {1, 2, 3, 6, 7}
    ```

#### 8장- 문자열

문자열은 리스트와 비슷한 부분이 많다. 예들들어 다음과 같은 코드를 보자.

``` python
a = [10, 20, 30, 40, 50]
b = 'python is fun'

print(a[2:4])  # 30, 40
print(b[2:4])  # tho
```
> \[참고\] 함수와 메서드

``` python
# 함수는 함수이름(매개변수)로 구성되어있다.
len(ss)
# 메서드는 클래스에서 만든 함수라고 생각하면된다.
ss = 'abcd'  # ss라는 객체 생성(문자열 클래스로 부터)
ss.upper()  # 문자열 클래스의 upper 이라는 매소드 호출
```

문자열도 리스트처럼 인덱싱이 가능하다는 것이다.

1. 문자열 함수

    ``` python
    ss = 'Python is Easy.'
    ss.upper()  # 모든 문자를 대문자로
    ss.lower()  # 모든 문자를 소문자로
    ss.swapcase()  # 대소문자 swap 하기
    ss.title()  # 띄어쓰기 기준으로 앞글자만 대문자로 변환

    ss.count(' ')  # 2, ' '(공백)의 갯수 새기
    ss.find('y')   # 1, y가 제일 처음 나오는 곳 찾기 
    ss.rfind('y')  # 13, y가 제일 처음 뒷쪽에서부터 나오는 곳 찾기
    ss.find('y', 4)  # 13, 문자열이 4번째부터 나오는 곳부터 y찾기
    ss.find('nothing')  # -1, 문자열이 없을경우 -1 리턴

    ss.index('y')  # find 함수와 동일하게 사용가능, 없을 경우 에러 발생

    ss.startswith('Python')  # True, 처음 글자가 일치하면 True
    ss.startswith('Python', 2)  # False, 2번째부터 글자가 일치하면 True
    ss.endswith('y.')  # True, 끝 글자가 일치하면 True

    s2 = '     Py tho n  '
    s2.strip()
    s2.rstrip()
    s2.lstrip()
    ```


#### 9장- 함수와 모듈

모듈 불러오는 법

```python
import random  # random 이라는 폴더를 임포트하여 폴더 안 모듈들과 함수를 사용할 수 있다.
import random as rd  # random 대신에 rd 를 붙일 수 있다.
from random import randrange, randint  # random에 있는 특정 함수들만 임포드하여 쓴다.
from random import *  # random 폴더에 모든 함수들을 임포트한다.
# random 을 안붙일 수 있다. 하지만 이 방법은 추천하지 않는다. 충돌 발생 우려, 코드해석 어려움
```

## 코드

> 책에있는 내용은 스스로 복습한 것이고 선생님께서는 코드위주로 진도를 나갔습니다. 코드를 참고해주세요.

- 04-01 중첩 for문
    ```python
    i, k = 0, 0

    for i in range(2, 10, 1):
        print('## %d 단 ##' % (i))
        for k in range(1, 10, 1):
            print(i, '*', k, '=', i*k)

    ## 10 x 10 크기의 숫자를 예쁘게 출력해라 ##
    import random
    import random as rd
    from random import randrange, randint
    # from random import *

    #count = 0
    for _ in range(10):
        for _ in range(10):
            num = randint(0,99)  # randint(0,99)
            print("%2d" % (num), end=' ')
            #count += 1
        print()
    
    ```
- 04-02 리스트1, 2, 3, 4
    ```python
    ## 4개의 랜덤한 숫자를 리스트에 저장한 후, 합계를 계산하자.
    import random

    aa = [] # 빈 리스트 준비

    for i in range(4):  # range(0, 4, 1)
        num = random.randint(0, 99)
        aa.append(num)

    print(aa)

    ```
- 04-03 리스트 조작함수1, 2
    ```python
    # 특정값의 모든 위치를 출력하는 프로그램
    import random
    myList = [random.randint(1, 5) for _ in range(10)]
    print(myList)

    NUMBER = 5

    index = 0
    findList = []
    print('찾을 숫자:', NUMBER, '처음 있는 위치:', myList.index(NUMBER, index))
    # myList.index(값, 몇번째)를 사용할 때 주의점
    # myList에 값이 없으면 오류를 발생시킨다.

    while True:
        try:
            index = myList.index(NUMBER, index)
            findList.append(index)
            index += 1
        except:
            break

    print(NUMBER, '가 있는 위치들', findList)

    ```
- 04-04 2차리스트
    ```python
        # 3x4 크기의 리스트 조작하기
    # (1) 2차원 빈 리스트 생성

    # image =[
    #     [0 ,0 ,0, 0],
    #     [0 ,0 ,0, 0],
    #     [0 ,0 ,0, 0]]
    ROW, COL = 10, 10
    image = []
    temp = []
    for i in range(ROW):
        temp=[]
        for k in range(COL):
            temp.append(0)
        image.append(temp)

    print(image[0])
    print(image[1])

    # (2) 대입 --> 파일에서 로딩....
    import random
    for i in range(ROW):
        for k in range(COL):
            image[i][k] = random.randint(0, 255)

    # (3) 데이터 처리/변환/분석... --> 영상 밝게 하기(100)
    for i in range(ROW):
        for k in range(COL):
            image[i][k] += 100
            
    # (4) 데이터 출력
    for i in range(ROW):
        for k in range(COL):
            print("%3d" % (image[i][k]), end=' ')
        print()
    ```
- 04-05 딕셔너리 활용
    ```python
    import operator

    ttL = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('토마스', 12),
        ('에드워드', 1)]

    tD = {}
    for tmpTup in ttL:
        tName = tmpTup[0]
        tWeight = tmpTup[1]
        if tName in tD:
            tD[tName] += tWeight
        else:
            tD[tName] = tWeight

    print(list(tD.items()))

    tL = []
    tL = sorted(tD.items(), key=operator.itemgetter(1), reverse=True)
    print(tL)

    ```
- 04-06 함수
    ```python
    # 두 수를 받아서 더한 값을 반환하는 함수
    def calc(v1, v2, v3 = 10):
        result1 = v1 + v2 + v3
        result2 = v1 - v2 - v3
        return result1, result2

    def calc2(*para):
        res = 0
        for num in para:
            res += num
        return res

    # 메인 코드부
    hap1, hap2 = calc(100, 200, 300)
    print(hap1, hap2)
    hap1, hap2 = calc(10, 20)
    print(hap1, hap2)
    hap = calc2(12, 3, 3, 4, 5, 6, 7)
    print(hap)

    ```
- 04-07 지역, 전역변수
    ```python
    def func1():
        a = 10
        print('func1() --> ', a)

    def func2():
        global a
        print('func2() --> ', a)

    # 변수 선언부
    a = 1234

    # 메인 코드부
    func1()
    print(a)  # a가 10으로 변경되어 있기를 기대함.
    func2()
    print(a)

    ```
- 04-08 내부함수
    ```python
    # 내부함수
    def outFunc(v1, v2):
        def inFunc(n1, n2):
            return n1 + n2
        return inFunc(v1, v2)

    print(outFunc(100, 200))

    # (1) 함수에서 lambda 표현식으로
    def hap (v1, v2):
        res = v1 + v2
        return res

    hap2 = lambda v1, v2 : v1+v2

    print(hap(100,200))
    print(hap2(100,200))

    # (2) 함수에서 lambda 표현식으로
    def add10(num):
        return num + 10

    lambda_add10 = lambda num: num+10

    # 리스트에 10을 더하는 방법 3가지
    myList = [1, 2, 3, 4, 5]

    for i in range(len(myList)):
        myList[i] = add10(myList[i])
    print(myList)

    myList = list(map(lambda_add10, myList))
    print(myList)

    myList = list(map(lambda num: num+10, myList))
    print(myList)

    ```
- 04-09 GUI 01
    ```python
    from tkinter import Tk

    window = Tk()
    window.title('요기가 타이틀')
    window.geometry("400x100")
    window.resizable(width=False, height=True)

    window.mainloop()

    ```
- 04-10 과제1
    ```python

    ```

- 04-10 과제2
    ```python

    ```
## 과제

1. 16진수 정렬 -> 선택 정렬, 버블 정렬, 퀵 정렬(p.219)
2. 문자, 숫자 정렬 -> 선택 정렬, 버블 정렬, 퀵 정렬(p.283)

