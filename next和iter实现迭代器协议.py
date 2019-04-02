class Foo:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        '''
        把一个对象变成可迭代对象
        :return:
        '''
        return self

    def __next__(self):
        '''

        :return:
        '''
        if self.n == 15:
            raise StopIteration
        self.n += 1
        return self.n

f1 = Foo(11)
# print(f1.__next__())
# print(f1.__next__())

for i in f1:
    '''
    for 循环可以自动捕捉stopiteration异常从而退出循环，而不会终止程序
    '''
    print(i)
