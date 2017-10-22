# 类定义装饰器
'''
class Mydecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print('这是函数执行后发生的')
        return result


@Mydecorator
def test():
    print('我是函数')


test()
'''
'''
# 带参数的装饰器
def repeat(num=5):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num):
                result = func(*args, *kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat(2)
def test_two():
    print([i for i in range(5)])

test_two()
'''
# 上面例子 用print(test_two.__name__) 查看名称 会变为 wrapper
# 解决办法 引入functools包wraps()装饰器
import functools


def repeat(num=5):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num):
                result = func(*args, *kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat(2)
def test_two():
    print([i for i in range(5)])

print(test_two.__name__)