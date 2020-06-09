import lesson_package.utils
from lesson_package import utils
from lesson_package.utils import say_twice

r = lesson_package.utils.say_twice('hello')
r2 = utils.say_twice('hello')
r3 = say_twice('hello')

print(r)  # hello!hello!
print(r2)
print(r3)


from lesson_package import utils as ut

print(ut.say_twice('hello'))