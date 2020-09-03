import contextlib

def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        # return True
    except Exception:
        return False

def cleanup():
    print('clean up')

def cleanup2():
    print('clean up2')

# try:
#     is_ok = is_ok_job()
#     print('more task')
# finally:
#     if not is_ok:
#         cleanup()

# callback으로 이런 처리를 꼭 해주세요라는 명시적으로 처리 가능함
# 코드가 읽기 쉬워짐, 대규모 코드개발에서 많이 쓰이는 방법

with contextlib.ExitStack() as stack:
    stack.callback(cleanup)
    stack.callback(cleanup2)

    @stack.callback
    def cleanup3():
        print('clean up3')

    is_ok = is_ok_job()  # False
    print('more task')

    if is_ok:
        stack.pop_all()