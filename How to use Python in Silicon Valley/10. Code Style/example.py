### 113

# 문장 끝에 ;콜론은 안쓰는 것이 좋습니다.
x = 1
y = 2

# 한줄에 80개 이내로 하면 좋습니다.
x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# 괄호는 맞추면 좋습니다.
def text_func(x, y, z,
              ffffffffffffffffffffffffffffffffffffffffff='test'):
    
    """
    # Document에는 80개가 넘어도 됩니다.
    See details at: http://naver.com/wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    """

# 기본적으로 tab은 spase가 4개로 설정합니다.
if x and y:  # 필요 없는 괄호는 안쓰는 것이 좋습니다. ex. (x and y)
    print('True')

    x = {
        'test': 'sss'  # 여기서도 4개로 들여씁니다.
    }

# 다 알아서 패스!

### 114

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
