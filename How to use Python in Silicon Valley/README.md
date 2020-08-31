# How to use Python in Silicon Valley

This is a lecture how to use Python in Silicon Valley

Lecture Link -> [https://www.udemy.com/share/102aRUCEIacV5QTHQ=/](https://www.udemy.com/share/102aRUCEIacV5QTHQ=/)

start at 09 June, 2020

## Introduction

### Section 01: Start here

1. 첫인사

2. Udemy 미국 본사 가 봄

3. 강의 속도 변경

### Section 02: Setting up Python environment

4. install Python on Mac

5. install Pycharm on Mac

6. install Python on Windows

    아나콘다는 유용한 패치지를 다운로드 합니다.
    (Anaconda installs a lot of useful python packages like skit-learn.)

7. install Pycharm on Windows

    아나콘다 다운로드 하고 IDE는 파이참을 쓰세요.
    (Download Anaconda instead of Download Python and Use Pycharm as an IDE.)

### Section 03: Basic Python

8. 변수 선언

    ``` python
    name: str = '1'  # 이렇게 파이썬에서도 변수명에 타입을 설정해 줄 수 있음
    ```

9. print로 출력하기

    ``` python
    print('Hi', 'Mike', sep=', ', end='.\n')
    # sep는 두 문자 사이에 무엇을 넣을 수 있냐는 옵션이고
    # end는 프린트문이 끝나고 실행할 다음 문자라고 생각하면 됨
    ```

10. 수치

    ``` python
    import math
    print(help(math))  # math 패키지 사용법을 볼 수 있음
    ```

11. 문자열

    엔터 처리가 되는 경우 r(raw data)를 사용하면 됨

    ``` python
    'C:\name\name'  # \n을 줄바꿈으로 인식하기 때문에
    r'C:\name\name'  # 이렇게 표현하면 편함
    ```

    문자열이 긴경우
    
    1. \(back slash)를 사용
        ``` python
        # 이 경우 첫 줄과 마지막 줄이 항상 \n 이 들어감
        ''' 
        line1
        line2
        line3
        '''
        ```
        ``` python
        # 따라서 \를 써주면 \는 \n을 없에 줄 수 있음
        '''\
        line1
        line2
        line3\
        '''
        ```
    2. 문자열 2개를 따로 적어 소괄호로 합치기도 함(unpacking의 원리)

        ``` python
        # 한줄로 처리됨
        s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        ```

12. 문자열 인덱스와 슬라이스

13. 문자 메소드

    startswith, find, rfind, count, capitalize, title, upper, lower, replace 등이 있음

    ``` python
    s = 'My name is Mike. Hi Mike.'
    is_start = s.startswith('My')
    print(is_start)
    ```

14. 문자의 대입(.fromat())

    format 함수로 변수를 바로 문자열로 넣을 수 있음

    {:} 에서 : 기준으로 앞쪽은 순번 뒷쪽은 옵션을 넣을 수 있음

    ``` python
    'a is {}'.format('a')  # a is a
    print('{:08d}'.format(3344))  # 00003344
    print('{1:03d}, {0:05d}'.format(300, 400))
    ```

    format 의 단점

    변수명에 변수명을 또 넣어주기 때문에 느림 따라서 다음 장의 f-string을 추천함

    ``` python
    name = 'Mike'
    user_id = 'm0303'
    print('{name}, {id}'.format(name=name, id=user_id))
    ```

15. f-string

    3.6 Ver 이상에서 사용 가능

    빠르고 코드 이해도 쉽고 좋음
    
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

    dict1.get('c')  # 해당 값이 없을 때 리턴값이 NoneType
    dict1.get('c', 30)  # 해당 값이 없을 때 리턴값이 30 임. 있으면 그대로를 리턴함
    ```

    딕셔너리는 해쉬 테이블 구조로 구현되어서 값을 가져오는데 빠름

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

    ``` python
    # 긴 주석은 """ """ 로 처리
    """
    long
    long
    comments
    """
    # 변수명 주석은 위에 써줌
    apple = 1000
    ```

32. 한줄이 길어질 경우

    \\(back slash) 사용, 소괄호로 묶어주기
    ``` python
    a = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + \
        1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

    a = (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 +
        1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) 
    ```

33. if 문
34. 디버거를 써서 확인해보기
35. 논리연산자
36. In 과 Not의 쓰임

    ``` python
    mylist = ['b', 'c']
    if 'a' not in mylist:
        print('a is not in mylist')

    is_ok = True
    if is_ok:
        print('This is True')
    if not is_ok:
        print('This is False')
    ```

37. 값이 들어 있지 않다는 판정을 하는 테크닉

    ``` python
    # False
    False, 0, 0.0, '', [], (), {}, set(), ...
    # True는 나머지
    True
    ```

38. None 판정

    ``` python
    is_empty = None

    # is_empty == None: 이건 추천하지 않음
    if is_empty is None:
        print('None')
    elif is_empty is not None:
        print('Not None')
    ```

39. while 문, continue 문, break 문
40. while else문

    while문을 완전히 종료할 때만 else문을 실행함  
    while문안에 break가 걸리면 else문은 실행하지 않음

    ``` python
    count = 0
    while count < 5:
        if count == 2:
            print(count)
            break
        print('while')
        count += 1
    else:
        print('done')
    ```

41. input 함수

    ``` python
    while True:
        word = input('Enter(if word is 100 then break): ')
        if word == 100:
            break
        print(word)
    ```

42. for 문, break 문, continue 문
43. for else 문

    for문을 완전히 종료할 때만 else문을 실행함  
    for문안에 break가 걸리면 else문은 실행하지 않음

    ``` python
    for fruit in ['apple', 'banana', 'orange']:
        if fruit == 'banana':
            print('stop eating')
            break
        print(fruit)
    else:
        print('I ate all')
    ```

44. range 함수
45. enumerate 함수
46. zip 함수
47. 사전을 for 문으로 처리하기
48. 함수 정의
49. 함수의 인수와 반환값의 선언

    ``` python    
    # 자료형을 미리 넣어줄 수 있음(자주 쓰이는 방법은 아님)
    def add(a: int, b:int) -> int:
        return a + b

    # 형을 정해줬어도 다른 형을 넣어도 실행은 됨
    add('a', 'b')
    ```

50. 위치 인수, 키워드 인수, 그리고 디폴트 인수    
51. 디폴트 인수 쓸 때 주의할 점

    인수로 빈 리스트나 빈 딕셔너리를 넣으면 참조변환을 하기 때문에 에러가 발생할 가능성이 있음  
    아래 코드 참고

    ``` python
    def test_func(x, l=[]):
        l.append(x)
        return l

    r = test_func(100)
    print(r)  # [100]
    r = test_func(100)
    print(r)  # [100, 100]
    ```

    따라서 리스트나 빈 딕셔너리를 인수로 사용하고 싶으면 다음과 같이 코딩  
    ex) l = None 타입으로 설정 
    
    ``` python
    def test_func(x, l=None):
        if l is None:
            l = []
        l.append(x)
        return l    
    ```

52. 위치 인수의 튜플화

    ``` python
    def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print('args =', arg)

    say_something('Hi', 'Mike', 'Nance', 'Chris')
    ```

53. 키워드 인수의 사전화

    ``` python
    def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

    c = {
        'entree': 'stake',
        'drink': 'coke',
    }
    menu('banana', 'apple', 'orange', entree='beef', drink='coffee')
    """
    banana
    ('apple', 'orange')
    {'entree': 'beef', 'drink': 'coffee'}
    """

    menu('eggs', 'tomato', **c)
    """
    eggs
    ('tomato',)
    {'entree': 'stake', 'drink': 'coke'} 
    """
    ```

54. Docstrings 란

    함수 내부에 """ """ 를 이용하여 함수를 설명해주는 것

    ``` python
    def exam_func(parm1, parm2):
        """Example Function with types documented in the docstring.

        Args:
            parm1(int): The first parameter.
            parm2(str): The second parameter.

        Returns:
            bool: The return value. True for success, False otherwise.
        """
        print(parm1)
        print(parm2)
        return True
    ```
    
    Docstrings을 보는 방법들

    ``` python
    print(exam_func.__doc__)
    help(exam_func)
    ```

55. 함수의 함수

    함수 내에서만 함수를 사용할 경우

    ``` python
    def outer(a, b):
        def plus(c, d):
            return c + d

        r1 = plus(a, b)
        r2 = plus(b, a)
        return r1 + r2

    print(outer(1, 2))  # 6
    ```

56. 클로저

    함수를 둘러싼 환경을 유지했다가 나중에 다시 활용하는 기술
    
    장점
    
    프로그램 흐름을 변수에 저장하여 사용 할 수 있음  
    클로저의 지역 변수와 코드를 묶어서 사용할 수 있음  
    클로저의 지역 변수는 바깥에서 접근이 불가해 데이터를 숨기고 싶을 때 활용함  


    ``` python
    # 순서는 주석처리
    def circle_area_func(pi):  # 2, 5
        def circle_area(radius):  # 8, 12
            return pi * radius * radius  # 9, 13
        
        return circle_area  # 3, 6

    cal1 = circle_area_func(3.14)  # 1
    cal2 = circle_area_func(3.141592)  # 4

    print(cal1(10))  # 7  # 10 결과(314.0)
    print(cal2(10))  # 11  # 14 결과(314.1592)
    ```
    
57. 데코레이터

    Decorator: 감싸준다 포괄한다는 의미로 알아두기 바람, 함수의 재사용이 용이함

    데코레이터를 잘 설명한 링크 -> [https://bluese05.tistory.com/30](https://bluese05.tistory.com/30)

    실습

    ``` python
    def add_num(a, b):
        return a + b
    
    # print('start')
    # r = add_num(10, 20)
    # print('end')

    def print_info(func):  # 2
        def wrapper(*args, **kwargs):  # 3  # 7
            print('start')  # 8
            result = func(*args, **kwargs)  # 9
            print('end')
            return print(result)
        return wrapper  # 4

    def print_more(func):
        def wrapper(*args, **kwargs):
            print('func:', func.__name__)
            print('args:', args)
            print('kwargs:', kwargs)
            result = func(*args, **kwargs)
            print('result:', result)
            return result
        return wrapper

    # # f = print_info(add_num)  # 1  # 5 wrapper()함수가 들어가있음
    # # r = f(10, 20)  # 6 wrapper 실행 -> print_info(add_num) wrapper(10, 20)

    # # 더 간단히?
    # # @print_info를 붙임
    # @print_info
    # def add2_num(a, b):
    #     return a + b

    # r = add2_num(10, 4)

    @print_info
    @print_more  # 데코레이터는 순서도 중요함
    def add2_num(a, b):
        return a + b

    r2 = add2_num(10, 5)
    ```

58. 람다

    Lambda: 간단하게 만드는 함수, 가독성, 편의성을 위해 사용

    `lambda 매개변수: 결괏값`

    ``` python
    def change_words(words, func):
        for word in words:
            print(func(word))
        
    l = ['Mon', 'Tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    change_words(l, lambda word: word.capitalize())
    change_words(l, lambda word: word.lower())
    ```

59. 제너레이터

    Generator: 반복처리 시 한 요소들을 생성해서 사용

    ``` python
    def greeting():
        yield 'Good morning'
        yield 'Good afternoon'
        yield 'Good evening'
        for i in range(10):
            print(i, end=' ')
        print('finish')

    for i in greeting():
        print(i)

    g = greeting()

    print(next(g))  # 미리 만들지 않는다는 장점
    print(next(g))  # 메모리 절약, 시간 절약 때 사용하면 좋음
    print(next(g))
    print(next(g))  # 없어서 에러 발생(StopIteration)
    ```

60. 리스트 내포 표기
61. 사전 내포 표기
62. 집합 내포 표기
63. 제너레이터 내포 표기

    튜플이 아닌점만 유의하면 됨

    ``` python
    def g():
        for i in range(10):
            yield i

    g = g()

    g = (i for i in range(10))
    print(type(g))  # <class 'generator'>, 튜플이 아님
    print(next(g))  # 0
    print(next(g))  # 1
    print(next(g))  # 2
    ```
64. 이름 공간과 스코프

    ``` python
    locals()  # 함수 같은 로컬의 정보를 알 수 있음
    globals()  # 해당 스크립트의 정보를 알 수 있음
    ```

65. 예외 처리

    에러 목록 보는 링크 -> [(https://docs.python.org/3/library/exceptions.html#exception-hierarchy)](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

    ``` python
    l = [1, 2, 3]

    try:
        k[4]
    except IndexError as ie:  # 인덱스에러로 실패 했을 때 실행
        print('error: {}'.format(ie))
    except NameError as ex:  # 해당 유형으로 실패 했을 때 실행
        print('Name error:', ex)
    except Exception as ex:  # 뭔지 모를 에러에 실패 했을 때 실행
        print('other: {}'.format(ex))  # 좋은 코드는 아님
    else:  # 성공했을 때 실행
        print('done') 
    finally:  # 항상 실행, 실패하든 성공하든
        print('clean up')
    ```

66. 독자 예외의 작성

    자신이 만든 프로그램에서 에러 처리를 할 때 왜 에러가 났는지 설명할 때 좋음

    ``` python
    class UppercaseError(Exception):
        pass

    def check():
        words = ['APPLE', 'orange', 'banana']
        for word in words:
            if word.isupper():
                raise UppercaseError

    try:
        check()
    except UppercaseError as exc:
        print('This is uppercase error')
    ```

### Section 06: Modules and Packages

67. 커맨드라인 인수

    콘솔 창에서 `ls`: 파일명, `pwd`: 현재 폴더 위치 를 알려주고 python 파일명.py 는 파이썬을 실행함
    windows 는 `dir`: 파일명, `cd`: 현재 폴더 위치 를 알려줌

    ``` python
    import sys
    print(sys.argv)
    ```

    콘솔창에서 `python lesson.py option1 option2` 를 입력하면 -> `lesson.py, option1, option2` 가 출력됨

    파이참에서 Run -> Edit Configurations -> Select Python -> Click '+' button -> Parameters 에 option1 option2 입력

68. Import 문 과 AS

    패키지 생성 방법

    패키지를 만들 때 폴더안에 **\_\_init\_\_.py** 파일을 **반드시** 만들어 줘서 패키지 파일임을 알려야 함  
    이 파일이 없을 경우 패키지로 인식되지 않음  

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

    파이썬에 lesson_package에서 talk에 동물과 사람 울음소리를 각각 넣어놨을 경우에  
    둘다 import 하는 방법이 *(asterisk)를 사용하는 방법


    ``` python
    from lesson_package.talk import animal
    from lesson_package.talk import human
    from lesson_package.talk import *
    ```
    
    하지만 error 발생 이유는 \_\_init\_\_ 파일에 \_\_all\_\_ 을 정의하지 않았기 때문이

    \_\_init\_\_ 파일에 \_\_all\_\_ 정의하는법  

    ``` python
    __all__ = ['animal', 'human']
    ```

    *를 사용하는 것은 추천하지 않음  
    어떤 모듈을 불러올지 모를 때 사용하기 때문에 불필요한 모듈들도 불러올 수 있기 때문

71. ImportError 의 쓰임

    ``` python
    try:
        from lesson_package import utils
    except ImportError:
        from lesson_package.tools import utils
    ```

    패키지를 불러올 때 옛날 버전과 새 버전의 차이가 있을 때 사용하면 유용함

72. setup.py 로 패키지로 만들어 배부하기

    파이참에서 하는 방법

    Tools -> Create setup.py -> 입력 후 ok -> setup.py 에 첫줄 'from distutils.core import setup'로 수정  
    Tools -> Run setup.py Task -> sdist -> not fill-in and ok -> MANIFEST 파일 생성 확인 -> dist 폴더 -> 압축파일 확인

    콘솔창에서 하는 방법

    우선 배포판인 MANIFEST 파일과 dist폴더를 삭제해야 함(없을경우 생략)  
    명령어로 `mv dist/ /tmp`, `mv MANIFIST /tmp` 두개를 입력해서 지워야 함  

    `python setup.py sdist` 입력하면 dist폴더 생성과 안에 압축파일 생성  
    이 압축파일을 배포하면 됨

73. 내장 함수

    우리가 사용하는 print() 함수는 사실 builtins 패키지에 함수임  
    파이썬 인터프리터가 자동으로 패키지를 임포트하기 때문에 우리가 사용할 수 있는 것

    ```python
    import builtins
    builtins.print()
    ```

    기본 내장함수 보기 링크 -> [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)  

74. 표준 라이브러리

    표준 라이브러리 보기 링크 -> [https://docs.python.org/3.7/library/index.html](https://docs.python.org/3.7/library/index.html)
    
    ``` python
    from collections import defaultdict
    ```

    > 표준 라이브러리는 임포트 해서 사용해야 함  
    > 내장함수는 임포트 할 필요가 없음

75. 서드파티의 라이브러리

    다른 사람들이 만든 라이브러리를 download 후 install 해서 쓸 수 있음

    서드파티 라이브러리 보기 링크 -> [https://pypi.org/](https://pypi.org/)

    파이참에서 install 하는 방법

    File -> Settings -> Project -> Project Interpreter -> '+' button click -> find package -> install

    콘솔에서 install 하는 방법

    `pip install 'package name'`

76. import 적는 방법

    암묵적인 룰  
    **표준 라이브러리**를 알파벳 순으로 따로 적어줌  
    **third-party 패키지**를 한줄 띄우고 적어줌  
    **다른 회사의 패키지**를 한줄 띄우고 적어줌  
    **내가 만든 패키지**를 한줄 띄우고 적어줌

    ``` python
    # import collections, os, sys (x)
    import collections
    import os
    import sys

    import termcolor

    import lesson_package

    import config
    ```

77. \_\_name\_\_ 과 \_\_main\_\_

    실행한 스크립트의 \_\_name\_\_은 \_\_main\_\_으로 실행되고  
    다른 스크립트의 \_\_name\_\_은 다른 스크립트 이름으로 실행됨

    스크립트는 다음과 같이 만드는 것이 좋음

    ``` python
    def main():
        pass

    if __name__ == "__main__":
        main()
    ```

### Section 07: Objects and Classes

78. 클래스의 정의

    파이참에서 원하는 메소드 기능 보기 -> 해당 메소드 드래그 -> 오른쪽 클릭 -> Go to -> Declaration or Usages

    ``` python
    # object 는 생략 가능
    class Person(object):
        pass
    ```

79. 클래스의 초기화와 클래스 변수
80. 생성자와 소멸자

    ``` python
    class Person(object):
        def __init__(self, name='name'):  # 생성자
            self.name = name
            print('객체 생성시 무조건 실행')

        def say_something(self):
            print('I am {}. hello'.format(self.name))
            self.run(10)

        def run(self, num):
            print('run ' * num)

        def __del__(self):  # 소멸자
            print('객체 소멸시 무조건 실행')

    person = Person('Mike')
    person.say_something()

    print('#######')
    ```

81. 클래스의 계승
82. 메소드의 오버라이드와 super 로 기반 클래스의 메소드 불러오기

    Inheritance(계승, 상속)
    Overide(오버라이드)

    ``` python
    class Car():
        def __init__(self, model=None):
            self.model = model
        def run(self):
            print('run')

    class HyundaiCar(Car):
        def run(self):
            print('fast')

    class TeslaCar(Car):
        def __init__(self, model='S model', enable_auto_run=False):  # 오버라이드
            super().__init__(model)
            self.enable_auto_run = enable_auto_run

        def run(self):
            print('super fast')
        
        def auto_run(self):
            print('auto run')
    ```

83. Property 를 사용한 속성의 설정

    - ```_``` -> 명시적으로 클래스 안의 값을 안바꿨으면 좋겠다는 표현
    - ```__``` -> 명시적, 기능적으로 클래스 안의 값을 외부에서 접근 불가(Private)

    메소드를 통해 값을 가져오거나 저장하는 경우 Property를 사용

    ``` python
    class Car():
        def __init__(self, model=None):
            self.model = model
        def run(self):
            print('run')

    class HyundaiCar(Car):
        def run(self):
            print('fast')

    class TeslaCar(Car):
        def __init__(self, model='S model',
                    enable_auto_run=False,
                    passwd='123'):
            super().__init__(model)
            self._enable_auto_run = enable_auto_run
            self.passwd = passwd
            self.__now_speed = 10  # private 설정, 외부에서 접근 불가

        @property  # getter
        def enable_auto_run(self):
            return self._enable_auto_run

        @enable_auto_run.setter  # setter
        def enable_auto_run(self, is_enable):
            if self.passwd == '456':
                self._enable_auto_run = is_enable
            else:
                raise ValueError

        def run(self):
            print(self.__now_speed)
            print('super fast')
        
        def auto_run(self):
            print('auto run')

    tesla_car = TeslaCar(passwd='456')
    print(tesla_car.enable_auto_run)  # getter로 값 보기
    tesla_car.enable_auto_run = True  # setter로 값 변경
    print(tesla_car.enable_auto_run)  # getter로 값 보기
    tesla_car.run()
    # tesla_car.__now_speed  # __-> private으로 설정했기 때문에 attribute Error 발생
    ```

84. 클래스를 구조체로서 쓸 때의 주의점
    
    클래스 안에 속성값이 없어도 새로 만들거나 재정의를 하기 때문에 주의할 필요가 있음

    ``` python
    class T():
        pass

    T.name = 'mike'
    print(T.name)  # 'mike' 출력
    # T 클래스의 속성에는 name이 없지만 위에 덮어써서 생성함
    # 좋은 코드스타일은 아님
    ```

85. 덕타이핑

    덕타이핑이란? -> [https://wikidocs.net/16076](https://wikidocs.net/16076)

    덕타이핑 구현 예시

    ``` python
    class Person(object):
        def __init__(self, age=1):
            self.age = age

        def drive(self):
            if self.age >= 18:
                print('ok')
            else:
                raise Exception('No drive')

    class Baby(Person):
        def __init__(self, age=1):
            if age < 18:
                super().__init__(age)
            else:
                raise ValueError

    class Adult(Person):
        def __init__(self, age=18):
            if age >= 18:
                super().__init__(age)
            else:
                raise ValueError

    class RideCar(object):

        def ride(self, person):
            person.drive()

    baby = Baby()
    adult = Adult()
    car = RideCar()

    # car.ride(baby)
    car.ride(adult)
    ```

86. 추상 클래스

    추상 클래스로 정의된 클래스로 상속받은 클래스는 반드시 추상 클래스를 포함해야 한다.

    추상 클래스 정의 방법

    ``` python
    import abc  # 추상클래스 불러오기
    class Person2(metaclass=abc.ABCMeta):  # 추상 클래스로 정의
        
        @abc.abstractmethod  # 추상 클래스로 정의
        def drive(self):
            pass
    ```

87. 다중계승

    다중 계승은 두 가지 다 상속받는다. 단 오버라이드 경우 앞에서 부터 순서를 지킨다.

    ``` python
    class Person3(Person1, Person2):
        # 생략
        
    # 오버라이드일 경우
    # 순서 Person3 -> Person1 -> Person2 -> ... 상위 클래스 -> object
    ```

88. 클래스 변수
89. 클래스 메소드와 스태틱 메소드

    - 클래스 메소드를 만들면 오브젝트를 만들지 않아도 메소드 사용 가능, 현재 클래스의 속성을 불러옴
    - 스태틱 메소드를 만들면 오브젝트틀 만들지 않아도 메소드 사용 가능, 단 상속시 클래스 메소드와 차이가 있음

    [차이 보기 링크 https://medium.com/@hckcksrl/](https://medium.com/@hckcksrl/python-%EC%A0%95%EC%A0%81%EB%A9%94%EC%86%8C%EB%93%9C-staticmethod-%EC%99%80-classmethod-6721b0977372)

    ``` python
    class Person(object):

        kind = 'human'  # 클래스 변수, 클래스로 만든 객체들이 공통으로 공유함

        def __init__(self):
            self.x = 100

        def what_is_your_kind(self):
            return self.kind

        @classmethod  # 클래스 메소드
        def what_is_your_kind2(cls):
            return cls.kind

        @staticmethod  # 스테틱 메소드
        def about(year):
            print(f'about human {year}')

    a = Person()
    print('a.kind:', a.kind)
    print('a.kind_fun: ',a.what_is_your_kind())
    b = Person  # 객체로 생성 x 클래스 자체로 생성
    print('b.kind:',b.kind)
    # print(b.what_is_your_kind())  # TypeError 발생
    print('class_method: ', b.what_is_your_kind2())  
    Person.about(1999)
    ```

90. 특수 메소드

    특수 메소드(Special Method)란 파이썬에서 이미 정한 특별한 메소드  
    예) ```__init__```  

    ``` python
    class Word(object):

        def __init__(self, text):
            self.text = text

        def __str__(self):
            return 'Word!!!'

        def __len__(self):
            return len(self.text)

        def __add__(self, word):
            return self.text.lower() + word.text.lower()

        def __eq__(self, word):
            return self.text.lower() == word.text.lower()

    w = Word('test')
    print(w)  # from __add__
    print(len(w))  # from __len__

    w2 = Word('####')
    print(w + w2)  # from __add__

    w3 = Word('test')
    print(w == w3)  # from __eq__
    ```

### Section 08: File I/O and System

91. 파일의 작성

    파일 작성 및 쓰기
    ``` python
    f = open(file_path, 'w')
    f.write('wansang\n')
    f.write('한글\n')
    ```

    프린트 문으로 파일에 쓰기
    ``` python
    print('한글 I want to write Korean!', file=f)
    f.close()
    ```

92. with 구문으로 파일을 open 하기

    ``` python
    with open(file_path, 'w') as f:
        f.write('Test\n')
    ```

93. 파일 읽어오기

    한꺼번에 읽어오기
    ``` python
    with open(file_path, 'r') as f:
        print(f.read())
    ```

    한줄씩 읽어오기
    ``` python
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            print(line, end='')
            if not line:
                break
    ```

    chuck 단위로 읽어오기  
    (네트워크 프로그래밍때도 chuck 단위로 읽어오기 가능)
    ``` python
    with open(file_path, 'r') as f:
        while True:
            chuck = 2
            line = f.readline(chuck)
            print(line)
            if not line:
                break
    ```

94. seek를 써서 이동하기

    - tell 메소드는 현재 커서의 위치를 알려줍니다.
    - read 메소드는 현재 커서에서 몇글자를 읽어올지 알려줍니다.
    - seek 메소드는 커서 위치를 해당 번호로 이동합니다.

    tell, read, seek 예시

    ``` python
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
    ```

95. 쓰기와 읽어오기 모드

    w+ 쓰고 보기, r+ 읽고 보기

    ``` python
    with open(file_path, 'w+') as f:
        # f.read() !!!주의!!! -> 읽기 부터 하면 파일이 날라감 
        f.write(s)
        f.seek(0)  # 커서 위치 이동 0번째로
        print(f.read())  # 읽기 가능
    ```

96. 템플릿

    템플릿을 사용하면 원본 문서를 수정하지 않고 외부에서 접근하기 때문에 다양한 기능으로 씁니다.

    ``` python
    import string

    s = """\
    Hi $name.
    $contents
    Have a good day
    """

    with open(file_path, 'w+') as f:
        f.write(s)
        f.seek(0)
        t = string.Template(f.read())

    contents = t.substitute(name='Wansang', contents='How are you?')
    print(contents)
    ```

97. CSV 파일에 쓰고 읽어오기

    ``` python
    import csv

    # window 같은 경우 \r\n이 되서 2번 엔터효과 때문에 newline=''로 설정
    with open(file_path, 'w', newline='') as csv_file:
        field_name = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=field_name)
        writer.writeheader()  # 파일 생성
        writer.writerow({'Name': 'A', 'Count': 1})  # 줄 추가1
        writer.writerow({'Name': 'B', 'Count': 2})  # 줄 추가2

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row i n reader:
            print(row['Name'], row['Count'])
            # A 1
            # B 2
    ```

98. 파일 조작

    경로에 파일이 있는지 확인
    ``` python
    import os
    print(os.path.exists(file_path + 'test.csv'))  # True
    ```

    경로가 폴더인지 확인
    ``` python
    print(os.path.isdir(file_path))  # True
    ```

    파일 이름 바꾸기
    ``` python
    os.rename(file_path + 'test.txt', file_path + 'renamed.txt')
    ```

    바로가기 만들기
    ``` python
    os.symlink(file_path + 'renamed.txt', file_path + 'symlink.txt')
    ```

    디렉토리 만들기(해당 이름의 디렉토리가 없을 때 가능)
    ``` python
    os.mkdir(file_path + 'test_dir')
    ```

    디렉토리 삭제하기(디렉토리 안 아무것도 없을 때 가능)
    ``` python
    os.rmdir(file_path + 'test_dir')
    ```

    현재 실행되는 디렉토리를 반환
    ``` python
    cwd = os.getcwd()  # current working directory
    ```

    파일 만들기
    ``` python
    import pathlib  # python -v >= 3.0
    pathlib.Path(file_path + 'empty.txt').touch()
    ```

    해당 디렉토리의 하위 목록을 리스트로 반환
    ``` python
    import glob
    print(glob.glob(cwd + '\\*'))
    ```

    파일 복사하기
    ``` python
    import shutil
    shutil.copy('복사하고 싶은 파일', '복사한 파일 이름')
    ```

    해당 디렉토리 모두 삭제
    ``` python
    shutil.rmtree('삭제하고 싶은 디렉토리')
    ```

99. tarfile 의 압축 및 풀기

    ``` python
    import tarfile

    # tarfile 로 압축하기
    with tarfile.open(file_path + 'test.tar.gz', 'w:gz') as tr:
        tr.add('test_dir')

    # tarfile 로 압축풀기
    with tarfile.open(file_path + 'test.tar.gz', 'r:gz') as tr:
        # tr.extractall(path='test_tar')  # 압축 풀기
        with tr.extractfile('test_dir/sub_dir/sub_text.txt') as f:  # 압축 풀고 읽어오기
            print(f.read())
    ```

0. zipfile 의 압축 및 풀기

    ``` python
    import zipfile
    import glob

    with zipfile.ZipFile('test.zip', 'w') as z:
        # z.write('test_dir')
        # z.write('test_dir/empty.txt')
        for f in glob.glob('test_dir/**', recursive=True):
            print(f)
            z.write(f)

    with zipfile.ZipFile('test.zip', 'r') as z:
        # 압축하기
        # z.extractall('zip_file')
        with z.open('test_dir/empty.txt') as f:
            print(f.read())
    ```

1. tempfile

    tempfile 라이브러리는 파일이나 폴더를 만들고 바로 지울 때 사용합니다.  
    임시보관용이라고 생각하면 좋습니다.

    ``` python
    import tempfile

    # 파일 만들기
    with tempfile.TemporaryFile(mode='w+') as t:
        t.write('hello')
        t.seek(0)
        print(t.read())

    # 버퍼가 아닌 temp 폴더에 파일 만들기
    with tempfile.NamedTemporaryFile(delete=False) as t:
        print(t.name)
        with open(t.name, 'w+') as f:
            f.write('test\n')
            print(f.read())

    # temp 폴더에 폴더 만들기
    with tempfile.TemporaryDirectory() as td:
        print(td)

    # 폴더 지우기 방지
    temp_dir = tempfile.mkdtemp()
    print(temp_dir)
    ```

2. subprocess 로 명령어 실행하기

    subprocesss는 쉘 명령어를 파이썬에서도 쓸 수 있습니다.
    ``` python
    import os
    import subprocess

    # 옛날 방식
    os.system('ls')

    # 요즘 방식
    subprocess.run(['ls', '-al'])

    # 쉬운 방식
    # 단점: 보안상 안전하지 않다. 명령어에 다 지우기 등을 추가할 수 있다.
    print('=' * 10)
    subprocess.run('ls -al | grep test', shell=True)

    # 리턴 코드를 이용해서 exception 발생 가능, 또는 check 옵션으로 가능
    r = subprocess.run('ls', shell=True, check=True)
    print(r)

    # 파이프를 써서 shell injection attack 을 피하는 방법
    print('=' * 10, 'defense shell injection')
    p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(
        ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
    )
    p1.stdout.close()
    output = p2.communicate()[0]
    print(output)
    ```

3. datetime

    datetime 패키지로는 시간을 편하게 쓸 수 있습니다.
    ``` python
    import datetime

    now = datetime.datetime.now()
    print(now)  # 2020-07-24 18:46:11.346924
    print(now.strftime('%d/%m/%y - %H:%M:%S.%f'))

    today = datetime.date.today()
    print(today)  # 2020-07-24
    print(today.isoformat())  # 2020-07-24
    print(today.strftime('%d-%m-%y'))  # 24-07-20

    t = datetime.time(hour=1, minute=30, second=30, microsecond=30)
    print(t)

    # timedelta 메서드를 활용하면 시간을 빼고 더할 수 있습니다.
    datetime.timedelta(days=365)
    datetime.timedelta(hours=3)
    d = datetime.timedelta(minutes=5)
    print(now - d)  # 5분 전
    ```

    시간 로그가 적힌 백업 파일에 만들기
    ``` python
    import os
    import shutil

    file_name = 'text.txt'

    with open(file_name, 'w') as f:
        f.write('test')

    if os.path.exists(file_name):
        # text.txt.2020_07_24_23_03_40 파일 생성
        shutil.copy(file_name, "{}.{}".format(file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))
    ```

### Section 09: Ending the Introduction - Coding the Simple Application

4. Windows 와 Mac의 명령어

    - where: 검색하고싶은 명령어를 지정
    - cls: 표시를 클리어
    - dir: 파일이나 디렉토리 정보를 표시
    - cd: 디렉토리 간 이동
    - md: 디렉토리 작성
    - type: 텍스트 파일의 내용을 표시
    - move: 디렉토리를 이동 
    - xcopy /e /c /h: 디렉토리를 복사
    - rd: 디렉토리를 삭제 
    - move: 파일을 이동
    - copy: 파일을 복사
    - del: 파일을 삭제
    - dir 또는 cd: 현재 디렉토리의 장소를 확인

5. 간단한 애플리케이션을 만들어 봅시다.
6. 데모 애플리케이션의 흐름을 설명한 pdf 파일
7. 데모 애플리케이션 압축 풀기

    zip 파일의 경우
    
    ```window``` + ```R``` -> ```cmd``` -> ```tar -xf <file_name>.zip```

8. 샘플 데모 애플리케이션 코드

    데모 애플리케이션 다운로드 후 setup.py 설정하는 방법

    setup.py 파일이 있는지 확인 후 있다면 한번 읽어보고 설정하기

    ```python setup.py develop``` 해당 콘솔 창에 입력하면 setup.py의 셋팅을 해줍니다.

    ``` python
    # 저번시간에는 distutils.core로 셋팅을 했다면 이번에는
    # setuptools에 setup으로 셋팅을 합니다. setuptools를 더 많이 씁니다.
    try:
        from setuptools import setup, find_packages
    except ImportError:
        from distutils.core import setup

    setup(
        name='python_programming_demo_app',
        version='0.0.1',
        packages=['roboter', 'roboter.models', 'roboter.controller', 'roboter.views'],
        # You could use find_packages if setuptools is installed. 
        ### find_packages()를 사용하면 패키지를 자동으로 찾아서 다운로드 해줍니다.###
        # packages=find_packages(),
        package_data={ 'roboter': ['templates/*.txt'] },
        url='http://sakaijunsoccer.appspot.com',
        license='MIT',
        author='jsakai',
        author_email='example@example.com',
        # You can specify install_requires if setuptools is installed
        ### install_requires 안에 있는 패키지를 자동으로 찾아서 다운로드 해줍니다.###
        # install_requires=['termcolor==1.1.0'],
        long_description=open('README.txt').read(),
    )
    ```

9.  샘플 코드의 설계와 폴더 구조의 해설

    MVC(Model–View–Controller) 모델

    - Model: 무엇을 할지 정의(알고리즘, DB의 CRUD등)
    - View: 무엇을 보여줄지 정의(UI화면 등)
    - Controller: 어떻게 처리할지 정의(요청을 분석하여 Model과 View 업데이트 요청 등)
    
    ![mvc_role_diagram](./09.%20Coding%20the%20Simple%20Application/image/mvc_role_diagram.png)

10. 샘플 코드의 Views 와 템플릿의 해설

    ``` python
    """Utils to display to be returned to the user on the console."""
    import os
    import string

    import termcolor

    # template 주소 찾기
    def get_template_dir_path():
        """Return the path of the template's directory.

        Returns:
            str: The template dir path.
        """
        template_dir_path = None
        try:
            import settings
            if settings.TEMPLATE_PATH:
                template_dir_path = settings.TEMPLATE_PATH
        except ImportError:
            pass

        if not template_dir_path:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            template_dir_path = os.path.join(base_dir, 'templates')

        return template_dir_path


    class NoTemplateError(Exception):
        """No Template Error"""

    # template 주소에서 원하는 파일이름 찾기
    def find_template(temp_file):
        """Find for template file in the given location.

        Returns:
            str: The template file path

        Raises:
            NoTemplateError: If the file does not exists.
        """
        template_dir_path = get_template_dir_path()
        temp_file_path = os.path.join(template_dir_path, temp_file)
        if not os.path.exists(temp_file_path):
            raise NoTemplateError('Could not find {}'.format(temp_file))
        return temp_file_path

    # 원하는 파일 템플릿 가져와서 보여주기
    def get_template(template_file_path, color=None):
        """Return the path of the template.

        Args:
            template_file_path (str): The template file path
            color: (str): Color formatting for output in terminal
                See in more details: https://pypi.python.org/pypi/termcolor

        Returns:
            string.Template: Return templates with characters in templates.
        """
        template = find_template(template_file_path)
        with open(template, 'r', encoding='utf-8') as template_file:
            contents = template_file.read()
            contents = contents.rstrip(os.linesep)
            contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
                contents=contents, splitter="=" * 60, sep=os.linesep)
            contents = termcolor.colored(contents, color)
            return string.Template(contents)
    ```

11. 샘플 코드의 models 와 controller 의 해설

    controller를 보면 흐름과 제어방법을 알 수 있습니다.

    ``` python
    """Controller for speaking with robot"""
    from roboter.models import robot


    def talk_about_restaurant():
        """Function to speak with robot"""
        restaurant_robot = robot.RestaurantRobot()
        restaurant_robot.hello()
        restaurant_robot.recommend_restaurant()
        restaurant_robot.ask_user_favorite()
        restaurant_robot.thank_you()
    ```

    model을 보면 데이터 구조와 DB 등을 볼 수 있습니다.

### Section 10: Code Style

12. 코드 스타일을 체크하는 툴의 확인

    파이썬 코드를 체크해주는 툴들

    pip install pep8
    pip install flake8
    pip install pylint

13. 스타일 룰

    PEP8 Style Guide for Python Code [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

14. Python 쓰는 방법

    ``` python
    # 1. 함수를 import 하지말고 모듈을 import 합니다.
    # 2. 표준라이브러리, third-party 패키지, local 패키지, 나의 패키지 순으로 적습니다.
    # 3. try, except에 Exception을 적는 것은 좋지 않습니다.
    # Exception은 포괄적 개념이기 때문에 코드 해석이 어려울 수 있습니다.
    def main():
        try:
            pass
        except Exception:
            pass
    # 4. 자신의 class를 만들어서 Exception을 상속받아 예외처리를 하면 좋습니다.
    class MainError(Exception):
        pass

    def main2():
        raise MainError('Main error')

    # 5. 컴프리핸션이 길어지면 코드 해석이 어려움으로 피해야 합니다.
    k = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]


    d = {'key1': 'value1', 'key2': 'value2'}

    # 6. 불필요한 함수 호출을 하지 않습니다.
    for key in d:  # d.keys() 로 적지 않기
        print(key)

    # 7. key, value 처럼 변수는 확실하게 적어주면 좋습니다.
    for key, value in d.items():
        pass

    # 8. 제너레이터는 yield 를 사용하면 속도가 빨라집니다.
    def t():
        # num = []
        for i in range(10):
            yield i
            # num.append(i)
        # return num

    for i in t():
        print(i)

    # 9. 간단한 함수는 lambda로 적으면 좋습니다.
    def other_func(f):
        print(f(10))

    def test_func(x):
        return x * 2

    other_func(test_func)
    other_func(lambda x: x * 4)

    # 10. 한줄로 작성은 기업마다 다릅니다.
    y = None
    x = True if y else False
    print(x)

    # 11. 리스트의 default 인수로 빈 리스트를 사용하지 않습니다.
    # 다음과 같은 방법으로 작성합니다.
    def my_function(not_list=None):
        if not_list is None:
            not_list = []
        
        # 빈 리스트는 not을 써서 판단할 수 있습니다.
        elif not not_list:
            return None

    # 12. 클로저의 장점은 글로벌 변수를 은폐하여 다른사람이 고칠 수 없게 합니다.
    # 클로저를 안 쓴 경우(더하기 함수의 예)
    i = 1
    def add_num():
        def plus(x):
            return i + x
        return plus

    f = add_num()
    print(f(10))
    i = 20  # i 값을 누군가가 바꾸면 값이 변경됩니다.
    print(f(10))

    # 클로저를 쓴 경우
    def closure(i):
        def plus(x):
            return i + x
        return plus

    f2 = closure(1)
    print(f2(10))

    # 13. 데코레이터 방식들
    def _deco_func(func):
        def wrapper(func):
            pass
        return wrapper

    # 요즘방식
    @_deco_func
    def fff():
        pass

    # 옛날 방식
    fff = _deco_func(fff)
    ```

15. 도큐먼트와 Pylint

    - 도큐먼트는 영어로 작성하면 많은 사람들이 알아들을 수 있습니다.
    - 도큐먼트는 큰따음표(""")로 작성합니다. (''' (x))
    - 함수나 메소드 마다 설명을 적어두면 좋습니다. 너무 간단하면 안적어도 됩니다.
      - Args: 자료형과 설명
      - Returns: 자료형과 설명
    - TODO 작성법은 ()에 자신의 아이디나 이메일을 작성하여 누구나 소통할 수 있게 합니다.
      - \# TODO (wansang93@naver.com) 내용 

16. 문장처럼 Python 적기

    가장 깔끔하고 읽기 쉬운 코드란, 완벽한 도큐먼트 없이 Python 의 코드를 읽는 것만으로도 어떤 것이 쓰여져 있는지 알 수 있는 코드 입니다.

    Python 의 코드 자체가 설계서의 도큐먼트라고 할수 있는 만큼 Python 의 코드를 읽는 것만으로도 다른 사람이 이해할 수 있는 프로그램을 작성해 주시기 바랍니다.

    영어도 우리말도 언어지만 Python 도 언어입니다. 작문을 하는 것 처럼, Python 의 코드 자체도 다른 사람이 읽는 문장 처럼 알기 쉽게 씁시다.

    미국 실리콘밸리에서는 agile 개발이 주류이기 때문에 그다지 설계서나 도큐먼트에 시간을 들이지 않고 개발을 시작하는 케이스가 많습니다. Google 등에서도 3 페이지 정도만의 간단한 설계서로 코드를 쓰기 시작한다고 하지만 코드 자체가 깔끔하게 쓰여있기 때문에 도큐먼트 없이 코드를 훑어보는 것 만으로도 무엇을 개발하는지 알수 있다고 합니다.

    Python 의 띄워쓰기 (인덴트) 를 제차 강조하는 것도 깔끔한 코드를 쓰셨으면 하는 바램이니까 여러가지 코드 스타일을 마스터 하셔서 꼭 pythonic 한 프로그래머가 되시기 바랍니다!

## Application

### Section 11: Config and Logging

### Section 12: Database

### Section 13: Web and Network

### Section 14: Test

### Section 15: Parallel system

### Section 16: Encryption

6. 문자 코드

    - 참고 문서
      - [한글 인코딩 이야기](https://heyjimin.tistory.com/14)
      - [문자열 인코딩 개념 정리](https://onlywis.tistory.com/2)
      - [한글 인코딩의 이해 1편](https://d2.naver.com/helloworld/19187)
      - [한글 인코딩의 이해 2편](https://d2.naver.com/helloworld/76650)
      - [유니코드란? UTF-8, EUC-KR 비교](https://dowhathewanna.tistory.com/2)

    - ASCII(American Standard Code for Information Interchange)
      - 구성: 7bits
      - 특징: 영어, 숫자, 특수문자, 기호를 위한 문자 코드
      - 문제점: 128개 밖에 못쓰다보니 영어를 제외한 문자 표시에 제한사항 발생
    - ANSI Code(American National Standard Institute Code)
      - 구성: 8bits(ASCII(7bits) + CodePage(1bit))
      - 특징: ASCII의 문제점을 개선 확장판으로 CodePage가 추가됨으로 글자 128개 추가 사용 가능
      - 개선: 128개의 문자가 추가되다 보니 독일, 프랑스 등 라틴개열 글자 추가 가능
      - 문제점: 128개로는 한글, 한자, 가나(일본 글자)를 표시하기에 턱없이 부족
    - EUC-KR(Extended Unix Code - Korea)
      - 구성: 1byte or 2bytes(2,350자의 한글)
      - 특징: 한글 지원을 위해 Unix 계열에서 나온 완성형 코드 조합
      - KS X 1001과 KS X 1003 표준안의 인코딩 방식
      - 문제점: 여전히 적은 한글 갯수, 특정 한글 글자 입력 불가
    - CP949(Code Page 949)
      - 구성: 1byte or 2bytes(11,172자의 한글)
      - 특징: 한글 지원을 위해 Windows 계열에 나온 완성형 코드 조합
      - 949의 의미는 코드페이지가 949이며 중국어 간체자는 936, 일본어는 932 
      - MS949(MicroSoft)라고도 불리며 EUC-KR을 확장하여 MS에서 만든 한글 코드
      - 엄연히 CP949와 MS949는 다르지만 대부분 같은 의미로 말함
        - 예) JAVA에서는 CP949는 MS가 아닌 IBM에서 처음 지정한 코드 페이지가 기준
      - EUC-KR와 다른 인코딩이지만 EUC-KR을 확장하였기 때문에 혼동이 올 수 있음
        - 예) JAVA에서는 CP949와 EUC-KR이 사실상 같으며, MS949로 지정해야 함
    - UNICODE(Unique Universal and Uniform character enCoding)
      - 특징: 전 세계 모든 문자와 컴퓨터에서 일관되게 표현할 수 있도록 고안된 코드 조합
      - UNICODE는 인코딩이 아니며 모든 문자를 2bytes 숫자로 1:1 매핑시키는 방식임
    - UTF-8
      - 구성: 1 ~ 4bytes(최대 1,112,064자 표현 가능)
      - UNICODE를 위한 가변 길이 문자 인코딩 방식 중 하나

7. pycrypto의 암호화와 해독

    AES 과정 -> [https://www.youtube.com/watch?v=mlzxpkdXP58](https://www.youtube.com/watch?v=mlzxpkdXP58)

    AES의 CBC 방법으로 암호화 하기

    1. pip install pycryptodome 설치
    2. 키와 iv 생성
    3. 패딩 작업
    4. 암호문으로 생성

    ``` python
    import string
    import random

    from Crypto.Cipher import AES

    # 킷값 생성
    key = ''.join(
        random.choice(string.ascii_letters) for i in range(AES.block_size)).encode("utf8")

    # iv값 생성
    iv = ''.join(
        random.choice(string.ascii_letters) for i in range(AES.block_size)).encode("utf8")

    file_path = r'C:\Users\wansang\Desktop\Gitrep\Python\How to use Python in Silicon Valley\16. Encryption'

    with open(file_path + r'\plaintext.txt', 'r') as f, open(file_path + r'\enc.dat', 'wb') as e:
        # 파일 읽어오기
        plaintext = f.read()

        # 패딩하기
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padding_length = AES.block_size - len(plaintext) % AES.block_size
        plaintext += chr(padding_length) * padding_length
        plaintext = plaintext.encode("utf-8")
        
        # 암호화
        cipher_text = cipher.encrypt(plaintext)
        print(cipher_text)
        e.write(cipher_text)

    with open(file_path + r'\enc.dat', 'rb') as f:
        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = f.read()
        decrypted_text = cipher2.decrypt(ciphertext)
        print(decrypted_text[:-decrypted_text[-1]])
    ```

8. hashlib의 해쉬

    - 비밀번호를 hash로 통해 db에 저장하기
      - sha256으로 hash값 생성
      - salt값을 해쉬값에 더함
      - stretch 방법으로 해쉿값으로 해쉿값을 반복 생성
      - 그 값을 비밀번호 최종값으로 저장

    ``` python
    import base64
    import os
    import hashlib

    print(hashlib.sha256(b'password').hexdigest())
    print(hashlib.sha256(b'password').hexdigest())

    user_name = 'wansang93'
    user_pass = 'password'

    db = {}

    salt = base64.b64encode(os.urandom(32))
    print(salt)

    # digest 만들기(암호화 작업)
    def get_digest(password):
        password = bytes(user_pass, 'utf-8')
        print(password)
        # salt 기법
        digest = hashlib.sha256(salt + password).hexdigest()
        # stretch 기법
        for _ in range(10000):
            digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
        return digest

    db[user_name] = get_digest(user_pass)

    print(db)

    def is_login(user_name, password):
        return get_digest(password) == db[user_name]

    print(is_login(user_name, user_pass))


    # 위에 함수를 한번에 하기
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(user_pass, 'utf-8'), salt, 10000)

    db[user_name] = digest

    def is_login2(user_name, password):
        digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(user_pass, 'utf-8'), salt, 10000)
        return digest == db[user_name]

    print(is_login2(user_name, user_pass))
    ```

### Section 17: Automate infrastructure deployment

### Section 18: Libraries, Tools and Tips

### Section 19: Graphic

44. 어린이도 즐길 수 있는 그래픽 turtle
45. turtle로 그림 그리기

    [Turtle graphics Document](https://docs.python.org/3/library/turtle.html)

    ``` python
    from turtle import Screen, Turtle

    screen = Screen()
    turtle = Turtle()

    turtle.color('red', 'yellow')
    turtle.begin_fill()
    turtle.shape('turtle')
    speed = 1
    while True:
        speed += 0.5
        turtle.speed(speed)
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()

    turtle.pencolor('white')
    turtle.backward(200)
    turtle.pencolor('blue')
    turtle.color('green', 'blue')
    for i in range(100):
        turtle.fd(i * 2)
        turtle.left(360 / 5 * 2)
        turtle.speed(3+i)

    screen.mainloop()
    ```

46. GUI 툴 킷 tkinter

    tkinter를 사용할 때 참고하면 좋은 문서

    tkinter docs eng-> [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
    tkinter 문서 한글-> [https://docs.python.org/ko/3/library/tkinter.html](https://docs.python.org/ko/3/library/tkinter.html)

47. tkinter로 계산기 애플리케이션을 만들어보기

    [내가 만든 소스 코드](./19.%20Graphic/calculator.py)

48. 계산기 애플리케이션의 소스코드

    [선생님 소스 코드](./19.%20Graphic/calculator)

49. Mac 에서 애플리케이션 작성하기

    py2app 설명 -> [https://py2app.readthedocs.io/en/latest](https://py2app.readthedocs.io/en/latest)

    py2app으로 애플리케이션 작성하기

       1. 터미널에서 ```virtualenv myapp``` 으로 가상환경 설정
       2. ```source myapp/bin/activate``` 로 가상환경 실행
       3. ```pip install py2app``` 을 실행하여 py2app을 다운로드
       4. ```python setup.py py2app``` 을 실행하면 애플리케이션 완성

50. Windows 에서 인스톨러 작성하기

    cx_Freeze 설명 -> [https://cx-freeze.readthedocs.io/en/latest/distutils.html](https://cx-freeze.readthedocs.io/en/latest/distutils.html)

    cx_Freeze로 애플리케이션 작성하기

    1. terminal에서 ```pip install cx_Freeze```을 실행
    2. setup.py 파일에 들어가 TCL_LIBRARY 경로와 TK_LIBRARY 경로를 적음
    3. MS의 installer의 룰에 따라서 setup.py를 작성했음
    4. ```python setup.py build```로 실행
    5. ```python setup.py bdist_msi```로 실행하면 애플리케이션 완성

51. kivy로 간단한 게임 애플리케이션 개발의 소개

    Python GUI Progarmming list -> [https://wiki.python.org/moin/GuiProgramming](https://wiki.python.org/moin/GuiProgramming)

    Kivy doc -> [https://kivy.org/doc/stable/gettingstarted/intro.html](https://kivy.org/doc/stable/gettingstarted/intro.html)

### Section 20: Data Analysis

52. 데이터 해석의 개념

    ![데이터 해석 개념](./20.%20Data%20Analysis/Data%20Analysis/concept.png)

    데이터 웨어하우스: 데이터베이스와 비슷한 개념, 사람에 따라 같은 개념으로 보기도 함  
    데이터만 보존하는 곳 or 데이터 보존 및 데이터베이스 기능 추가

53. Jupyter Notebook

    help 함수 대신에 ? 로 부를수도 있다.  
    ?? 두개를 쓰면 함수 정보를 볼 수 있다.
    ``` python
    import os
    os ?  # help(os)
    os.path.join??
    ```

54. numpy

    ``` python
    # 0 부터 100까지 10개를 균일하게 나눠서 배열 만들기
    np.linspace(0, 100, 10)
    """
    array([  0.        ,  11.11111111,  22.22222222,  33.33333333,
        44.44444444,  55.55555556,  66.66666667,  77.77777778,
        88.88888889, 100.        ])
    """

    # 넘파이 프린트 세팅을 10000개로 하기
    np.set_printoptions(threshold=10000)

    # 넘파이 한번에 합치기
    a = np.arange(5)
    b = np.arange(0, 10, 2)
    z = np.arange(0, 100, 20)
    np.vstack([a, b, z])
    """
    array([[ 0,  1,  2,  3,  4],
       [ 0,  2,  4,  6,  8],
       [ 0, 20, 40, 60, 80]])
    """
    np.hstack([a, b, z])
    """
    array([ 0,  1,  2,  3,  4,  0,  2,  4,  6,  8,  0, 20, 40, 60, 80])
    """

    import matplotlib.pyplot as plt

    # 주피터 노트북 안에서 그리기
    %matplotlib inline

    # 평균 2, 표준편차 0.5, 10,000개의 데이터
    v = np.random.normal(2, 0.5, 10000)

    plt.hist(v, bins=50, density=1)
    plt.show()
    ```

55. pandas

    ``` python
    df = DataFrame(np.random.randn(6, 4),
                   index=pd.date_range('20200628', periods=6))
    ```

56. matplotlib


57. scikit-learn

    1. 데이터를 우선 가저온다.
    2. 데이터를 교차 검증 부분에서 훈련용, 테스트용으로 나눈다.
    3. 알고리즘을 불러온다.
    4. 기계학습을 시킨다.
    5. 검증을 한다.
    6. 예측을 한다.

58. 주가의 데이터 해석과 예측

    1. 설계
    2. 데이터 웨어하우스 구축: 구축 후 데이터 확인
    3. 데이터 마이닝: 필요한 정보들을 추출해 변환
    4. 머신러닝: 데이터를 적절하게 변환
    5. 머신러닝을 돌린 후 정확도 확인
    6. 예상값 획득
    7. REST API 사용해 예상값 전달 후 결과 예측
    
    [딥러닝 텐서플로 튜토리얼 링크](https://www.tensorflow.org/tutorials/deep_cnn)

59. 데이터 해석 섹션의 소스코드

    [소스 코드](./20.%20Data%20Analysis/Data%20Analysis/)

### Section 21: Queuing system

### Section 22: Async/await asyncio

### Section 23: Final Message

thanks! さかい じゅん! :sunglasses::+1:
