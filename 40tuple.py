a=(1,2.5,"Ram")
print(type(a))
print(a[:1])
print(a[:-1])
print(a[0:2])
print(a[-1])

for i in a:
    print(i,end=" ")

if "Ram" in a:
    print("\nFound")
else:
    print("\nNot found")
    
a=(1,)
print(type(a))

b=list(a)
print(type(b))
b.append("AJAY")
print(b)
b.pop(0)
a=tuple(b)
print(a)
print(type(a))
b=list(a)
b.insert(0,"ragul")
print(b)
print(" ".join(b))
a=tuple(b)
print(type(a))
print(a)
del a
a=(1,3,4,5,6,7)
b=(1,2,3,4,5,6,7)
c=a+b
print(c)
print(c.count(7))

c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
print(c[1][0])

