print(1,2,3,4,5,sep=",")

#Positional Arguments
#Mapping w.r.t position
def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(1,2,3)

#keyworded arguments
def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(a=1,b=2,c=3)

def func(a):
    print(a)
#func() ---> Raise error
func(1)

def hello():
    print("Hello World !")
hello #<function__main__.hello()>
hello()
#hello=<function defination>
a=1
a=hello
a()
'''
Everything in python is a object,
even functions
'''
print(type(a))
hello=2
print(hello) #hello is no mroe a function
a() #a is still a fumnction

'''
python doesn't have a concept of function overloading 
'''
def b():
    print("Hi")
def b():
    print("Bye")
'''
It is same as saying,
a=1
a=2
'''

#Non default argument can't follow default argument
'''
def func(a,b=10,c):
    print(a,b,c)
'''

# *args **kwargs
'''print can except any number of arguments'''

'''
Arguments in Other Languages:
    - required arguments
    - default arguments

Arguments in Python:
    - required arguments
    - default arguments
    - optional arguments
    - required keyworded only arguments
    - default keyworded only arguments
    - optional keyworded only arguments
'''

#required arguments
def func(a,b):
    print(a,b)
func(1,2)

#default arguments
def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(1,2)

#optional arguments
def func(*a):
    print(*a)
func(1,2,3,4)

#required keyworded only arguments
def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,4,"jatin",1.5)
'''
1
2
(3, 4, 'jatin', 1.5)
'''
"""
def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,5,6,7,8)

#TypeError: func() missing 1 required keyword-only argument: 'd'
Computer acts in a very deterministic manner since thier iq is 0
If i give any asterisk argument in my function defination then 
all the rest of the argument will become keyword only arguments

So,
def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,5,6,7,d=8)
"""
#default keyworded only arguments
def func(a,b,*c,d,e="jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,3,4,5,6,7,d=8)

#optional keyworded only arguments
'''
def func(**k):
    print(k)
func(1,2,3,4,5)

#TypeError: func() takes 0 positional arguments but 5 were given
'''
def func(**k):
    print(k)
func(a=1,b=2)

'''
Order that we should follow
def func(a,b=1,*c,d,e="",**k):
'''
print(sorted([1,4,3,8,6]))
#Anonymous functions or lambda functions
#lambda is always a one liner function, it can only contain a single expression inside it
a=lambda a,b: a+b #Expression that return a function
print(a(1,2))

a=1
b=2
c=print(a,b)
print(c) #return None
 
