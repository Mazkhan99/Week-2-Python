#Lists--->Ordered and can be indexed using positions
#Dictionaries--->Unordered and can be indexed using keys
#Sets--->Unordered and cannot be indexed

s={1,2,3,4}
print(type(s))
s={"name":"atin"}
print(type(s))


a={1,2,3,4}
for i in a:
    print(i)

a={1,2,3,4}
b={3,4,5,6}
print(a-b)
print(a.union(b))
print(a.intersection(b))

#Tic Tac Toe
a=[
    ['','',''],
    ['','',''],
    ['','','']
]
#OR
a=[['']*3]*3
print(a)

a[1][1]="x"
print(a)

print(id(a[0][1]))
print(id(a[1][1]))
print(id(a[2][1]))

a=[1,2,3,4,5]
print(a)
a[0]=100
print(id(a))
print(id(1))
'''
Id of list changes
It represents multiple different values
(mutable)
'''

class Student:
    name="Jatin"
    marks=50
'''
It can also change id 
'''

a=225
b=225
print(a==b)
print(a is b)
c=258
d=258
print(a==b)
print(c is d)

#Hashing can only be implemented on immutable object
#By default immutable object is hashable
#Since we don't know that what will the mutable object store in future

'''
NOTE: Keys of dictionary can only be a immutables object is wrong.
      Keys of dictionary can only be a hashable object.        
'''

