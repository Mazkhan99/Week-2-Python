#COMPREHENSION

a=[]
for i in range(5):
    a.append(i)
print(a)

print(list(map(lambda x:x, range(5))))

#LIST COMPREHENSION
a=[i for i in range(5)]
print(a)


a=[] #Normal Approach
for i in range(5):
    a.append(i**2)
print(a)

print(list(map(lambda x:x**2, range(5)))) #Functional Approach

a=[i**2 for i in range(5)] #LIST COMPREHENSION
print(a)

#2D array
'''
In 1D array we append single value in list,
but in 2D array we append list 
'''
a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)

a=[[j for j in range(5)] for i in range(5)]
print(a)

"""
5 5 5 5 5
5 4 4 4 5
5 4 3 4 5
5 4 4 4 5
5 5 5 5 5
"""
n=5
a=[[max(i+1,j+1,n-i,n-j) for j in range(5)] for i in range(n)]
print(a)


#LIST COMPREHENSION
'''
[ <value to append> <for statement> ... <if statement> ...]
'''

s=[]
for i in range(2):
    for j in range(2):
        s.append(j)
print(s)

print([j for i in range(2) for j in range(2)])


#DICTIONARY COMPREHENSION
a={
    2:4,
    3:9,
    4:16
}
print(a)

a={i:i**2 for i in range(5)}
print(a)
type(a)


#SET COMPREHENSION
a={1,2,3,4,5}
print(a)
type(a)

a={i for i in range(5)}
print(a)
type(a)

"""
#NOTE: There is no such thing as Tuple Comprehension
"""

a=(i for i in range(5))
print(type(a)) #generator

for i in a: #Lazy Loading Concept
    print(i)

it=iter(a) 
next(it) #Loaded first value of generator, stop iteration after end
"""
#NOTE: Generator is a lazy loading unlike other comprehension they are eager loading 
"""

