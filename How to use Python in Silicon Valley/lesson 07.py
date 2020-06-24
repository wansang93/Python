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


class Car():
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class HyundaiCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='S model', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        print('super fast')
    
    def auto_run(self):
        print('auto run')