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

    리스트 생성과 값 채워넣기

    ``` python
    리스트이름 = [1,2,3,4]  # 리스트 선언
    리스트이름.append(값)  # 리스트의 순서대로 값을 앞에서 채워넣는다.
    ```

    > 리스트의 특징은 가장 앞에 번호가 0번이다. N개의 리스트를 만드려면 가장 마지막 번호는 N-1이다.

    리스트 접근하기

    ``` python
    a[0], a[1], a[-2]  # 앞에서 0+1번째값, 1+1번째 값, 뒤에서(-) 2번째 값
    a[3:6]  # 3+1부터 6+1전까지 출력
    a[(초깃값):(마지막값):(뛰어넘기))]  # 초깃값부터 마지막값 전까지 점프수
    a[1:5:2]  # a[1], a[3] 이렇게 인덱싱 된다.
    a[5:2:-2]  # a[5] a[3] 이렇게 인덱싱 된다.
    ```

    리스트 조작 함수

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

    튜플 생성

    ``` python
    mytuple = (1, 2, 3)  # 튜플을 생성한다.
    mytuple = tuple([1, 2, 3])  # 튜플을 생성한다.
    ```

3. 딕셔너리

    딕셔너리는 {}로 묶어서 구성한다. 순서가 없다.

    딕셔너리 생성

    ``` python
    mydic = {'키1': '값1', '키2': '값2', '키3': '값3'}
    ```

    딕셔너리 조작 함수

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
4. 세트(Set)

#### 8장- 문자열



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

- 04-01 중첩 for문
- 04-02 리스트1, 2, 3, 4
- 04-03 리스트 조작함수1, 2
- 04-04 2차리스트
- 04-05 딕셔너리 활용
- 04-06 함수
- 04-07 지역, 전역변수
- 04-08 내부함수
- 04-09 GUI 01
- 04-10 과제

## 과제

1. 16진수 정렬 -> 선택 정렬, 버블 정렬, 퀵 정렬(p.219)
2. 문자, 숫자 정렬 -> 선택 정렬, 버블 정렬, 퀵 정렬(p.283)

