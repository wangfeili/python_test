class Foo:
    def __getitem__(self, item):
        print('getitem')

    def __setitem__(self, key, value):
        self.__dict__[key]=value
        print('setitem')

    def __delitem__(self, key):
        print('delitem')
        self.__dict__.pop(key)

f1 = Foo()
f1['name'] = 'egon'  #类似字典的方式操作
print(f1.__dict__)
print(f1.name)       #通过点方式是触发getattr，而不是getitem
print(f1['name'])    #通过字典方式是触发getitem