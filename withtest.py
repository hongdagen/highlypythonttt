# with上下文管理器

# 类实现

'''
class class_with_test(object):
    def __enter__(self):
        # print('entering context')
        print('123')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('leave context')
        print('789')
        if exc_type:
            print('error : %s' % exc_val)
        else:
            print('no error')


with class_with_test():
    print('456')
'''

'''
# contextlib模块实现
from contextlib import contextmanager


@contextmanager
def my_test():
    print('123')
    try:
        yield
    except Exception as e:
        print(e)
    else:
        print('789')
        print('no error')


with my_test():
    print('456')
'''

