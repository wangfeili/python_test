class Foo:
    '文档属性'
    __slots__ = 'name'

f1 = Foo()
f1.name = 'egon'

print(f1.name)
#f1.age=18 #这样就不能自己添加实例属性了，因为已经没有__dict__了
#print(f1.__dict__) #AttributeError: 'Foo' object has no attribute '__dict__'
print(f1.__slots__)
print(f1.__doc__)  #__doc__属性无法继承
print(f1.__module__)
print(f1.__class__)