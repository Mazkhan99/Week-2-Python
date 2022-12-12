#Other than 3 Data Type all the data types in python are immutable
a=[1,2,3,4]
print(a)

b=["jatin",1,2,print]
print(b)

a=[1,2,3]
a[0]=100 #mutable
print(a)

print(len("jatin")) #It says that it can be broken down into four atomic elements

print("jatin"+"katyal")
print([1,2,3]+[4,5,6])

print([1]*4)

a=[1,2,3,4,5]
for i in a:
    print(i)

print("a" in "jatin")
print(1 in [1,2,3,4])

#Indexing and list Slicing
a=[1,2,3,4,5]
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

#Update the list
#insert
a=[1,2,3]
a.insert(1,100)
print(a)

#append
a=[1,2,3,4]
a.append(5)
print(a)

#Deleting list Elements
#pop
a=[1,2,3,4]
a.pop()
print(a)
a.pop(1)
print(a)

#remove
a=[1,2,1,4]
a.remove(1) #It remove the 1st occurance of the given object
print(a)
a.remove(1)
print(a)

#del
a=[1,2,1,4]



#Sorting and reversing
a=[1,5,3,7,9,5]
a.sort()
print(a)

b=[1,5,3,7,9,5]
print(sorted(b)) #It returns the sorted array but keep your actual array intact
print(b)

c=[3,6,2,8,6,1,9,0]
c.reverse()
#print(c.sort()) or print(c.reverse())--->None

d=[3,6,2,8,6,1,9,0]
print(reversed(d)) #It returns the reverse sorted array but keep your actual array intact
print(d) #It is lazy loading d instead of eager loading
for i in reversed(d): #Now we can see
    print(i)
'''
Lazy Loading - fetching resources in some patches one by one
Eager Loading - fetching all resouces in one go 
'''

#map
b=[1,2,3,4,5]
for i in map(lambda x: x**2,b):
    print(i)

def sqr(x):
    return x**2
for i in map(sqr,b):
    print(i)


#input
#Python default limiter is \n
a=input().split()
print(a)
a=map(int,input().split())
print(a) #<map object at 0x0000013B1E0EFFD0>


#join
print(",".join(["jatin","samarth","molly"]))