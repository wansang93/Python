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