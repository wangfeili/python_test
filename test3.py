# class Foo:
#
#     def __init__(self,x):
#         self.x = x
#
#     def __getattr__(self, item):
#         print("exec getattr")
#
#     def __getattribute__(self, item):
#         print("exec getattribute")
#         raise AttributeError("error")
#
# foo = Foo(10)
# foo.x
# foo.xxxx
# #不管有没有属性都执行__getattribute__,如果有attributeerror则会转去执行__getattr__


class Foo():
    pass

class Bar(Foo):
    pass

b1 = Bar()
print(isinstance(b1,Foo))
print(type(b1))
