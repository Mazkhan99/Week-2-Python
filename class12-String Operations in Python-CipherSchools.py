#Common String Operations

#String Formatting or String Interpoltion
a=5
print("value of a is %d" % (a)) #Not very dynamic and is not used mostly
print("value of a is {}".format(a))
print("value of a is {} {}".format(a,2))

a,b,c=1,2,3
print("a = {}, b = {}, c = {}".format(a,b,c))
#If we want correct order
#Give index
print("a = {2}, b = {1}, c = {0}".format(c,b,a))
name="Jatin Katyal"
company="shuttl"
print("name = {name} company = {company}".format(name=name,company=company))
print("Hello I am {name} and I work at {company}".format(name=name,company=company))
print("Hello {name} Welcome to my Facebook".format(name=name,company=company))

print(f"name = {name}") #anything written inside the curly braces is taken as expression and the result of the expression will be converted to string and placed here
print(f"name = {10/3}")

print("a\nb")
print(len("a\nb")) #3
print(r"a\nb") #raw strings, it doesn't parse \n character
for i in "a\nb":
    print(i)
for i in r"a\nb":
    print(i)


#strip
a="    jatin   "
print(a.strip()) #Removes spaces from both side

#split
b="1,2,3,4,5"
print(b.split(",")) #Returns List

#replace
c="jatin Katyal"
print(c.replace("a","z"))

#count
print(c.count("a"))