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

    나중에 사용하고 싶을 때 하는 기술(?)

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

    Decorator: 감싸준다 포괄한다 이런 의미로 알아두기 바람, 함수의 재사용이 용이함

    [데코레이터 설명 link](https://bluese05.tistory.com/30)

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
    # # @print_info를 붙인다.
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

    `lambda 매개변수: 결과`

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

    list comprehension

61. 사전 내포 표기

    dictionary comprehension

62. 집합 내포 표기

    set comprehension

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

    에러 목록 보는 링크[(https://docs.python.org/3/library/exceptions.html#exception-hierarchy)](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

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

    콘솔 창에서 `ls`: 파일명, `pwd`: 현재 폴더 위치 를 알려주고 python 파일명.py 는 파이썬을 실행한다.
    windows 는 `dir`: 파일명, `cd`: 현재 폴더 위치 를 알려준다.

    ``` python
    import sys
    print(sys.argv)
    ```

    콘솔창에서 `python lesson.py option1 option2` 를 입력하면 -> `lesson.py, option1, option2` 가 출력된다.

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

    기본 내장함수 보기: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)  

74. 표준 라이브러리

    표준 라이브러리 보기: [https://docs.python.org/3.7/library/index.html](https://docs.python.org/3.7/library/index.html)
    
    ``` python
    from collections import defaultdict
    ```

    > 표준 라이브러리는 임포트 해서 사용해야 함  
    > 내장함수는 임포트 할 필요가 없음

75. 서드파티의 라이브러리

    다른 사람들이 만든 라이브러리를 download 후 install 해서 쓸 수 있음

    서드파티 라이브러리 보기: [https://pypi.org/](https://pypi.org/)

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

    실행한 스크립트의 \_\_name\_\_은 \_\main\_\_\으로 실행되고
    다른 스크립트의 \_\_name\_\_은 다른 스크립트 이름으로 실행됨

    스크립트는 다음과 같이 만드는 것이 좋음

    ``` python
    def main():
        pass

    if __name__ == "__main__":
        main()
    ```

### Section 07: Objects and Classes

### Section 08: File I/O and System



### Section 23: Final Message

thanks! さかい じゅん! :sunglasses::+1:
