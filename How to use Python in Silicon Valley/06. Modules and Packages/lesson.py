# # # import lesson_package.tools.utils
# # # from lesson_package.tools import utils, utils as ut
# # # from lesson_package.tools.utils import say_twice
# # # from lesson_package.talk import *

# # # print(animal.sing())
# # # print(animal.cry())

# # # # r = lesson_package.tools.utils.say_twice('hello')
# # # # r2 = utils.say_twice('hello')
# # # # r3 = say_twice('hello')
# # # #
# # # # print(r)  # hello!hello!
# # # # print(r2)
# # # # print(r3)
# # # #
# # # # print(ut.say_twice('hello'))
# # # #
# # # #
# # # # from lesson_package.talk import human
# # # # print(human.sing())
# # # # print(human.cry())

# # # try:
# # #     from lesson_package import utils
# # # except ImportError:
# # #     from lesson_package.tools import utils

# # import builtins

# # builtins.print('dd')

# # ranking = {
# #     'A': 100,
# #     'B': 85,
# #     'C': 90,
# # }

# # for key in ranking:
# #     print(key)

# # print(sorted(ranking, key=ranking.get))  # value값이 작은것부터 리턴
# # print(sorted(ranking, key=ranking.get, reverse=True))

# from collections import defaultdict

import config
import lesson_package.talk.animal  # import 한 순간부터 내부 파일 전부가 실행이 됨

print('lesson:', __name__)  # __main__
print('config:', config.__name__)  # config

