import contextlib

class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'

    def __enter__(self):
        print(self.start_tag)
        # contextlib decorator에서 함수들을 실행 할 수 있음
        # print(self.start_tag + self.end_tag)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print(self.end_tag)

with tag('h5'):
    print('test')
    # Exception에서 에러 캐치 후 에러 발생 핸들링 가능
    raise Exception('error')
