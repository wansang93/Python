from lesson_package.tools import utils
# from ..tools import utils

def sing():
    return 'dfdafdfasfasdf'


def cry():
    return utils.say_twice('ㅜㅜ  ㅜㅜ ..')

if __name__ == '__main__':
    print(sing())
    print(cry())
    print('animal:', __name__)