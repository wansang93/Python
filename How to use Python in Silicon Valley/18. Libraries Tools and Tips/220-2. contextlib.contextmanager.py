def tag(name):
    def _tag(f):
        def _wrapper(content):
            print(f'<{name}>')
            r = f(content)
            print(f'</{name}>')
            return r
        return _wrapper
    return _tag

@tag('h2')
def f(content):
    print(content)

f('test')

# 옛날 스타일

def g(content):
    print(content)

g = tag('ggg')(g)
g('g: test')