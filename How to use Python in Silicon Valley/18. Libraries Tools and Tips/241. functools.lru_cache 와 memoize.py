import functools

def memoize(f):
    memo = {}
    def _wrapper(n):
        if n not in memo:
            memo[n] = f(n)
            print('hit')
        return memo[n]
    return _wrapper

# @memoize
@functools.lru_cache(maxsize=10)
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r

for i in range(10):
    print(long_func(i))

print('next run')
for i in range(10):
    print(long_func(i))

print(long_func.cache_info())

# rest_api 에서 네트워크에서 여러가지 값을 가져올 때 가지고 온 결과를 lru 캐쉬에 넣으면
# 몇번씩이나 다른 웹서버에 access 해서 api_limit 초과해 못가져오는 경우를 방지한다.