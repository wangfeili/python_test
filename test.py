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
j, k = 1, 2

def proc1():
    j, k = 3, 4
    print("j == %d and k == %d" % (j, k))
    k = 5


def proc2():
    j = 6
    proc1()
    print("j == %d and k == %d" % (j, k))

k = 7
proc1()
print("j == %d and k == %d" % (j, k))

j = 8
proc2()
print("j == %d and k == %d" % (j, k))