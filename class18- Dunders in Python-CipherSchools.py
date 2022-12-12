#The __init__ method
#Dunders(magic methods)
'''
__<name of dunder>__
'''
class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello, My Name is",self.name)
p=Person("Nikhil")
p.say_hi()

a=1
print(a+1)
print(str(a))

class a:
    def __init__(self):
        print(self)
        print("initialized")
    def __del__(self):
        print(self)
        print("I am dying")
b=a()
'''
class a:
    def __init__(self):
        raise Exception()
        print(self)
        print("initialized")
    def __del__(self):
        print(self)
        print("I am dying")
b=a()
'''

a=1
print(type(a))
print(a.__add__(5))
'''
a=1 has a dunder add
'''

print("Jatin"*2)
print("Jatin".__mul__(2))

class A:
    a=1
    b=2
    def __add__(self,x):
        return self.a+self.b+x
a=A()
a+3