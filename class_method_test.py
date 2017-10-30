"""类属性、方法测试"""


class ClassMethodTest(object):
    num = 10

    @classmethod
    def test(cls):
        print(cls.num + 10)


print(ClassMethodTest.num)
ClassMethodTest.test()
