import lesson_package.tools.utils
from lesson_package.tools import utils, utils as ut
from lesson_package.tools.utils import say_twice

r = lesson_package.tools.utils.say_twice('hello')
r2 = utils.say_twice('hello')
r3 = say_twice('hello')

print(r)  # hello!hello!
print(r2)
print(r3)

print(ut.say_twice('hello'))


from lesson_package.talk import human
print(human.sing())
print(human.cry())
