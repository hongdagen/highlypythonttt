import timeit


def test1():
    list_test = []
    for i in range(10000):
        list_test = list_test + [i]


def test2():
    list_test = [i for i in range(10000)]


def test3():
    list_test = list(range(10000))


def test4():
    list_test = []
    for i in range(10000):
        list_test.append(i)


def test5():
    list_test = []
    for i in range(10000):
        list_test.extend([i])


timer1 = timeit.Timer("test1()", "from __main__ import test1")
print('test1:', timer1.timeit(1000))

timer2 = timeit.Timer("test2()", "from __main__ import test2")
print('test2:', timer2.timeit(1000))

timer3 = timeit.Timer("test3()", "from __main__ import test3")
print('test3:', timer3.timeit(1000))

timer4 = timeit.Timer("test4()", "from __main__ import test4")
print('test4:', timer4.timeit(1000))

timer5 = timeit.Timer("test5()", "from __main__ import test5")
print('test5:', timer5.timeit(1000))
