# @property 方法->属性

class Test(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,val):
        self._birth = val

    @property
    def age(self):
        return 2017-self._birth


t = Test()
t.birth=2011
print(t.birth)
print(t.age)