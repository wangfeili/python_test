# l = list('hello')
#
# print(l)
#
# class Foo:
#     # def __str__(self):
#         pass
#
# f1 = Foo()
# print(f1)  #系统默认的__str__()方法就是返回<__main__.Foo object at 0x000001FECC9C6208>

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这里是str，名字是%s 年龄是%s' %(self.name,self.age)

    def __repr__(self):
        return '这里是repr,名字是%s 年龄是%s' %(self.name,self.age)


f1 = Foo('egon',18)
print(f1)    #先找str，没有找自定义的__str__,再没有找repr,repr主要是在解释器中实现,解释器中的类如果定义了repr，则按照repr显示
