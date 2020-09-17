import functools

# 방법1
def f(x, y):
    return x + y

def task(f):
    print('start')
    print(f(10, 20))

task(lambda x, y: x+y)
# start
# 30 

# 방법2
def outer(x, y):
    def inner():
        return x + y
    return inner

def task2(f):
    print('start')
    print(f())

f = outer(30, 20)
task2(f)
# start
# 50  

# 방법3
def f2(x, y):
    return x + y

def task3(f2):
    print('start')
    print(f2())

p = functools.partial(f2, 10, 20)
task3(p)
# start
# 30   