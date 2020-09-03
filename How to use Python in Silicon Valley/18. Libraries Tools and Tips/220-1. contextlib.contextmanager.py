def tag(f):
    def _wrapper():
        print('<h2>')
        r = f()
        print('</h2>')
        return r
    return _wrapper

@tag
def f():
    print('f: test')


def g():
    print('g: test')


# 요즘 방식
f()

# 옛날 방식
g = tag(g)
g()