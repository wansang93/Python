import functools

def d(f):
    def w():
        """Wraper docstring"""
        return f()
    return w

@d
def example():
    """Example docstring"""
    print('example')

example()
help(example)  # Wraper docstring
print(example.__doc__)  # Wraper docstring

# 개선
def d2(f):
    @functools.wraps(f)
    def w():
        """Wraper docstring"""
        return f()
    return w

@d2
def example2():
    """Example docstring"""
    print('example')

help(example2)  # Example docstring
print(example2.__doc__)  # Example docstring