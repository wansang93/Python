# How to use Python in Silicon Valley

This is a lecture how to use Python in Silicon Valley

Link -> [https://www.udemy.com/share/102aRUCEIacV5QTHQ=/](https://www.udemy.com/share/102aRUCEIacV5QTHQ=/)

start at 09 June, 2020

expected period: 5days

## What I learned?

### Section 01: Start here

1. 첫인사

2. Udemy 미국 본사 가 봄

3. 강의 속도 변경

### Section 02: Setting up Python environment

4. install Python on Mac

5. install Pycharm on Mac

6. install Python on Windows

    아나콘다는 유용한 패치지를 다운로드 합니다.
    (Anaconda install a lot of useful python packages like skit-learn.)

7. install Pycharm on Windows

    아나콘다 다운로드 하고 IDE는 파이참을 쓰세요.
    (Download Anaconda instead of Download Python and Use Pycharm as an IDE.)

### Section 03: Basic Python

8. 변수 선언

    ``` python
    name: str = '1'  # 이렇게 파이썬에서도 변수명에 타입을 설정해 줄 수 있다.
    ```

9. print로 출력하기

    ``` python
    print('Hi', 'Mike', sep=', ', end='.\n')
    # sep는 두 문자 사이에 무엇을 넣을 수 있냐는 옵션이고
    # end는 프린트문이 끝나고 실행할 다음 문자라고 생각하면 된다.
    ```

10. 수치

    수치끼리는 잘 더하고 뺄 수 있다.

    ``` python
    import math
    print(help(math))  # math 패키지 사용법을 볼 수 있다.
    ```

11. 문자열

    엔터 처리가 되는 경우 r(raw data)를 사용하면 된다.
    ``` python
    'C:\name\name'  # \n을 줄바꿈으로 인식하기 때문에
    r'C:\name\name'  # 이렇게 표현하면 편하다.
    ```

    문자열이 긴경우
    
    1. \(back slash)를 사용하면 된다.
    ``` python
    # 이 경우 첫 줄과 마지막 줄이 항상 \n 이 들어가 있다.
    ''' 
    line1
    line2
    line3
    '''
    ```
    ``` python
    # 따라서 \를 써주면 \는 \n을 없에 줄 수 있다.
    '''\
    line1
    line2
    line3\
    '''
    ```
    2. 문자열 2개를 따로 적어 소괄호로 합치기도 한다.(unpacking의 원리)

    ``` python
    s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
         'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
    ```

12. 문자열 인덱스와 슬라이스

    문자도 인덱싱 슬라이싱 할 수 있다.

13. 문자 메소드

    startswith, find, rfind, count, capitalize, title, upper, lower, replace 등이 있다.

    ``` python
    s = 'My name is Mike. Hi Mike.'
    is_start = s.startswith('My')
    print(is_start)
    ```

14. 문자의 대입(.fromat())

    format 함수로 변수를 바로 문자열로 넣을 수 있다.

    {:} 에서 : 기준으로 앞쪽은 순번 뒷쪽은 옵션을 넣을 수 있다.

    ``` python
    'a is {}'.format('a')  # a is a
    print('{:08d}'.format(3344))  # 00003344
    print('{1:03d}, {0:05d}'.format(300, 400))
    ```

    format 의 단점

    변수명에 변수명을 또 넣어주기 때문에 느리다. 따라서 다음 장의 f-string을 추천한다.

    ``` python
    name = 'Mike'
    user_id = 'm0303'
    print('{name}, {id}'.format(name=name, id=user_id))
    ```
15. f-string

    3.6 Ver 이상에서 사용 가능

    빠르고 코드 이해도 쉽고 좋다.
    
    왜 더 좋은지 참고 링크 -> [https://realpython.com/python-f-strings/](https://realpython.com/python-f-strings/)

    ``` python
    name = 'Mike'
    user_id = 'm0303'
    print(f'{name} {user_id}')
    ```

### Section 04: Data Structure


16. 리스트형
17. 리스트 조작
18. 리스트 메소드
19. 리스트 복사
20. 리스트 사용 예

    ``` python
    s = [1, 2, 2, 3, 4]
    
    s[::-1]  # 거꾸로 하기
    
    s.remove(1)  # 없으면 오류
        
    k = s  # 참조 전달
    t = s.copy()  # 수치전달
    print(id(s))
    print(id(k))  # 복사한 k는 s와 같은 곳을 가르킴
    print(id(t))  # 복사한 t는 s와 다른 곳을 가르킴
    ```

    리스트는 변동이 있는 값이 있는 경우 사용하면 좋음

21. 튜플형
22. 튜플의 언패킹
23. 튜플 사용 예

    ``` python
    t = ([1, 2, 3], [100, 200, 300])
    t[0][0] = 100  # 바꾸기 가능(1-> 100)
    
    min, max = 100, 200
    # 사실 튜플의 언패킹 원리를 이용
    # 100, 200이 (100, 200)이 생성되면서 각각 자료값이 들어감
    
    # 언패킹의 대표적인 예
    a, b = b, a  
    ```
    
    실수로 추가할 수 없게 만들 때 좋음 즉, 자료가 정해저 있는 경우
    
    예) 가위 바위 보 중 하나 고르세요.
    
24. 사전형
25. 사전형 메소드
26. 사전형 복사
27. 사전형 사용 예

    ``` python
    # dict 정의하는 방법들
    dict0 = {}
    dict1 = dict(a=10, b=20)  # {'a': 10, 'b': 20}
    dict2 = dict([('a', 10), ('b', 20)])  # {'a': 10, 'b': 20}
    
    # dict 자료 검색
    dict1.keys()
    dict1.values()
    dict1.items()

    dict1.get('c')  # 해당 값이 없을 때 리턴값이 NoneType 이다.
    dict1.get('c', 30)  # 해당 값이 없을 때 리턴값이 30 이다. 있으면 그대로를 리턴한다.
    ```

    딕셔너리는 해쉬 테이블 구조로 구현되어서 값을 가져오는데 빠르다.

28. 집합형
29. 집합형 메소드
30. 집합형 사용 예

    ``` python
    s = {1, 1, 2, 3, 3}  # {1, 2, 3}
    s2 = {3, 4, 5, 3}  # {3, 4, 5}
    s & s2  # {3}
    s - s2  # {1, 2}
    s | s2  # {1, 2, 3, 4, 5}
    s ^ s2  # {1, 2, 4, 5}
    ```

    페이스북에 공통인 친구 찾기, 리스트에서 유니크 한 값만 빼올 때

### Section 05: Control Flow

31. 주석문
32. 한줄이 길어질 경우
33. if 문
34. 디버거를 써서 확인해보기
35. 논리연산자
36. In 과 Not의 쓰임
37. 값이 들어 있지 않다는 판정을 하는 테크닉
38. None 판정
39. while 문, continue 문, break 문
40. while else문
41. input 함수
42. for 문, break 문, continue 문
43. for else 문
44. range 함수
45. enumerate 함수
46. zip 함수
47. 사전을 for 문으로 처리하기
48. 함수 정의
49. 함수의 인수와 반환값의 선언
50. 위치 인수, 키워드 인수, 그리고 디폴트 인수
51. 디폴트 인수 쓸 때 주의할 점
52. 위치 인수의 튜플화
53. 키워드 인수의 사전화
54. Docstrings 란
55. 함수의 함수
56. 클로저
57. 데코레이터
58. 람다
59. 제너레이터
60. 리스트 내포 표기
61. 사전 내포 표기
62. 제너레이터 내포 표기
63. 집합 내포 표기
64. 이름 공간과 스코프
65. 예외 처리
66. 독자 예외의 작성

### Section 06: Modules and Packages

67. 커맨드라인 인수

    콘솔 창에서 ls: 파일명, pwd: 현재 폴더 위치 를 알려주고 python 파일명.py 는 파이썬을 실행한다.
    windows 는 dir: 파일명, cd: 현재 폴더 위치 를 알려준다.

    ``` python
    import sys
    print(sys.argv)
    ```

    콘솔창에서 python test.py option1 option2 를 입력하면 -> tset.py, option1, option2 가 출력된다.

    파이참에서 Run -> Edit Configurations -> Select Python -> Click '+' button -> Parameters 에 option1 option2 입력

68. Import 문 과 AS

    패키지를 만들 때 폴더안에 \_\_init\_\_.py 파일을 반드시 만들어 줘서 패키지 파일임을 알려야 한다.

    이 파일이 없을 경우 패키지로 인식되지 않는다.

    ``` python
    import lesson_package.utils
    from lesson_package import utils
    from lesson_package.utils import say_twice

    r = lesson_package.utils.say_twice('hello')
    r2 = utils.say_twice('hello')
    r3 = say_twice('hello')

    print(r)  # hello!hello!
    print(r2)  # hello!hello!
    print(r3)  # hello!hello!
    ```

    r3 같은 경우 함수명이 동일하면 충돌 발생 위험과 어디서 불러왔는지 출처가 불분명하기 때문에 비추천

    r1 이나 r2 처럼 불러오는 것이 바람직함

    회사에 따라 r1처럼 풀네임으로 불러오게 하는 규칙이 있기도 함

    ``` python
    # 모듈이름이 너무 길 경우 as로 줄여서 작성 가능
    from lesson_package import utils as ut
    print(ut.say_twice('hello'))
    ```

69. 절대 경로와 상대 경로의 Import

    ``` python
    from lesson_package.tools import utils
    from ..tools import utils
    ```
    
    같은 디렉토리를 가르키고 있지만 첫번째 방법을 추천, 명확성때문

70. 애스터리스크의 import 와 \_\_init\_\_.py, \_\_all\_\_의 의미
71. ImportError 의 쓰임
72. setup.py 로 패키지로 만들어 배부하기
73. 내장 함수
74. 표준 라이브러리
75. 서드파티의 라이브러리
76. import 적는 방법
77. \_\_name\_\_ 과 \_\_main\_\_

### Section 07: Objects and Classes

### Section 08: File I/O and System



### Section 23: Final Message

thanks! さかい じゅん! :sunglasses::+1:
