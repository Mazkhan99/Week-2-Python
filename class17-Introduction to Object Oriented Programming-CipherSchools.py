#Abstraction
#Encasulation
#Polymorphism
#Inheritance

#Encasulation
student1={
    "name":"Jatin Katyal",
    "Marks":50
}
student2={
    "name":"samarth",
    "Marks":100
}
'''
This is also encapsulation
'''

#Abstraction
'''
Only know thathow print() function take input and gives output
You only know what you are need to know
'''

#Polymorphism
'''
Python objects can have multiple traits
    - Callable, e.g: Functions and classes
    - Iterable, e.g: list, string, generator
    - Contextable, e.g: files
'''
class Person:
    pass
p=Person() #If we call a class it will create new object of the class
print(p)
print(hex(id(p)))

"""
a=1
def square(a):
    print(a**2)
with a:
    square()
""" 

class Person:
    name="Jatin"
    def say_hi(self):
        print(f"Hello Everyone! I am {self.name}")
p=Person()
p.say_hi() #Python automatically places this p as the 1st argument, this means that this function is being treated as a method
Person.say_hi(p)
"""
class Person:
    name="Jatin"
    def say_hi(thisS):
        print(f"Hello Everyone! I am {self.name}")
p=Person()
p.say_hi() #Method Call
Person.say_hi(p) #Function Call
"""