import contextlib

@contextlib.contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')

def f():
    print('test0')
    with tag('h2'):
        print('test')
        with tag('h5'):
            print('test2')
            
    with tag('h5'):
        print('test2')

f()