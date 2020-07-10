# class Person(object):
#     def __init__(self, name='name'):  # 생성자
#         self.name = name
#         print('객체 생성시 무조건 실행')

#     def say_something(self):
#         print('I am {}. hello'.format(self.name))
#         self.run(10)

#     def run(self, num):
#         print('run ' * num)

#     def __del__(self):  # 소멸자
#         print('객체 소멸시 무조건 실행')

# person = Person('Mike')
# person.say_something()

# print('#######')

############### 82 ~ 84 ####################

class Car():
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class HyundaiCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='S model',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd
        self.__now_speed = 10  # private 설정, 외부에서 접근 불가

    @property  # getter
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter  # setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print(self.__now_speed)
        print('super fast')
    
    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar(passwd='456')
print(tesla_car.enable_auto_run)  # getter로 값 보기
tesla_car.enable_auto_run = True  # setter로 값 변경
print(tesla_car.enable_auto_run)  # getter로 값 보기
tesla_car.run()
# tesla_car.__now_speed  # __-> private으로 설정했기 때문에 attribute Error 발생

print('####')

class T():
    pass

T.name = 'mike'
print(T.name)

#################### 85 ~ 90 ####################

# # 85
# print('##### 85 #####')

# class Person(object):
#     def __init__(self, age=1):
#         self.age = age

#     def drive(self):
#         if self.age >= 18:
#             print('ok')
#         else:
#             raise Exception('No drive')

# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError

# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError

# class RideCar(object):

#     def ride(self, person):
#         person.drive()

# baby = Baby()
# adult = Adult()
# car = RideCar()

# # car.ride(baby)
# car.ride(adult)

# 86
print('##### 86 #####')

import abc
class Person2(metaclass=abc.ABCMeta):  # 추상 클래스로 정의
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod  # 추상 클래스로 정의
    def drive(self):
        pass

class Baby1(Person2):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    # drive 메소드를 반드시 구현해야 함
    def drive(self):
        raise Exception('No drive')

class Adult1(Person2):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    # drive 메소드를 반드시 구현해야 함
    def drive(self):
        print('drive ok')

adult = Adult1()  # drive를 구현하지 않으면 에러 발생

# 89
print('##### 89 #####')

class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return self.kind

    @classmethod  # 클래스 메소드
    def what_is_your_kind2(cls):
        return cls.kind

    @staticmethod  # 스테틱 메소드
    def about(year):
        print(f'about human {year}')

a = Person()
print('a.kind:', a.kind)
print('a.kind_fun: ',a.what_is_your_kind())
b = Person
print('b.kind:',b.kind)
# print(b.what_is_your_kind())  # TypeError 발생
print('class_method: ', b.what_is_your_kind2())  
Person.about(1999)

# 90
print('##### 90 #####')

class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
print(w)  # from __add__
print(len(w))  # from __len__

w2 = Word('####')
print(w + w2)  # from __add__

w3 = Word('test')
print(w == w3)  # from __eq__