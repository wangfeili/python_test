class Foo:
    def __init__(self,name):
        self.name = name

    def __del__(self):
        print('im done')

f1 = Foo('alx')
print('------->')
#整个实例删除的时候触发