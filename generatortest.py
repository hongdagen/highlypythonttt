# 利用生成器循环运行函数
'''
def generator_test(func):
    yield func()

def test():
    print("12345")

for _ in range(5):
    next(generator_test(test))
'''

'''
# 装饰器模仿一下效果

def repeat(num):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func()

        return wrapper

    return actual_decorator


@repeat(5)
def test():
    print(12345)


test()
'''

# send方法
def psycho():
    print('please say something')
    while True:
        answer = (yield)
        if answer.endswith('?'):
            print('jiayou')
        elif 'good'in answer:
            print('jianchi')
        elif 'bad' in answer:
            print('woxing')

free=psycho()
next(free)
free.send('bad')
free.send('good')