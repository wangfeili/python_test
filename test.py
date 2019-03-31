import time

 # from time import ctime,sleep
#
#
# def test(func):
#     def wrappedFunc():
#         print('[%s] %s() called' %(
#             ctime(),func.__name__))
#         return func()
#     return wrappedFunc
#
#
# @test
# def foo():
#     pass
#
# foo()
# sleep(4)
#
# for i in range(2):
#     sleep(1)
#     foo()

# def aa(arg1,arg2='defaultB',**theRest):
#     print('formal arg 1:',arg1)
#     print('formal arg 2:',arg2)
#     for eaacX in theRest.keys():
#         print('another arg:',eaacX)
#
# aa(23,d=333)

# true = lambda :True
# print(true())

# from random import randint
#
# allNums = []
# for eachNum in range(9):
#     allNums.append(randint(1,99))
#
# print(allNums)
# a =list(filter(lambda n: n % 2, allNums))
# '''
# python3在这里需要加一个list()函数才能print filter返回的list
# '''
# print(a)

# '''
# 重构3
# '''
# from random import randint as ri
# print([n for n in [ri(1,99) for i in range(9)] if n % 2])

# a = map((lambda x: x + 2),[1,2,3,4,5])
#
# print(list(a))
from operator import add
from functools import reduce,partial

# '''
# 为啥在python中不自带reduce？？？
# '''
# a = reduce((lambda x,y: x+y),range(5))
# print(a)

# addl = partial(add,1)
# print(addl(1))

#
# def foo():
#     m = 3
#     def bar():
#         n =4
#         print(n+m)
# print(m)
# bar()

'''
closuer
'''
# def counter(s=0):
#     count = [s]
#     def incr():
#         count[0] += 1
#         return count[0]
#     return incr()
#
# count = counter(5)
# print(count)
# print(count())


'''
lambda和作用域
'''
# x = 10
# def foo():
#     y = 5
#     bar = lambda :x+y
#     print(bar())
#
# foo()

#
# x = 10
# def foo():
#     y = 5
#     bar = lambda y=y:x+y
#     print(bar())
#     y = 10
#     print(bar())
#
# foo()

'''
test
'''
# j, k = 1, 2
#
# def proc1():
#     j, k = 3, 4
#     print("j == %d and k == %d" % (j, k))
#     k = 5
#
#
# def proc2():
#     j = 6
#     proc1()
#     print("j == %d and k == %d" % (j, k))
#
# k = 7
# proc1()
# print("j == %d and k == %d" % (j, k))
#
# j = 8
# proc2()
# print("j == %d and k == %d" % (j, k))


# class Test(object):
#
#     feature = "ugly"
#
#     def __init__(self,name):
#         self.name = name
#
#     def sell_house(self):
#         print("%s 正在抠脚" % self.name)
#
#     def __getattr__(self, item):
#         print("调用__getattr__")
#
#     def __delattr__(self, item):
#         print("调用__delattr__")
#
#     def __setattr__(self, key, value):
#         print("调用__setattr__")
#         self.__dict__[key] = [value] #把属性加进去
#
#
#
#
# b1 = Test("felix") #设置属性的时候就会调用__setattr__
# b1.sssssssssss  #调用不存在的属性的时候调用__getattr__
# del b1.name #删除的时候调用
#
# b1.sell_house()
# fun = getattr(b1,"sell_house")
# fun()
# print(getattr(b1,"xxx","ssss"))
#
# setattr()
# hasattr()
# delattr()

# class FileHandle:
#
#     def __init__(self,filename,mode='r',enconding='utf-8'):
#         self.file = open(filename,mode,encoding=enconding)    #文件操作里面有什么就提供什么
#         self.mode = mode
#         self.enconding = enconding
#
#     def __getattr__(self, item):
#         return getattr(self.file, item)
#
#
# f1 = FileHandle('a.txt','w+')
# f1.write('11111')

class FileHandle:

    def __init__(self,filename,mode='r',enconding='utf-8'):
        self.file = open(filename,mode,encoding=enconding)    #文件操作里面有什么就提供什么
        self.mode = mode
        self.enconding = enconding

    def write(self,line): #重新改写write方法，加上时间打印
        t = time.strftime('%Y-%m-%d %X')
        self.file.write('%s %s'%(t,line))

    def __getattr__(self, item):
        return getattr(self.file, item)


f1 = FileHandle('a.txt','r+')
f1.write('11111\n')
f1.write('内存不足')
f1.seek(0)
print(f1.read())



