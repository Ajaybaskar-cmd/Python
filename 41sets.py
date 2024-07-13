"""names={"Ragul","Ajay","Hariharan","Rajesh"}
print(names)
print(type(names))

for name in names:
    print(name)
    
#Adding the new value
names.add("Rajaji")
print(names)

names.remove("Ajay")
print(names)

a={1,2,3,4}
names.update(a)
print(names)

#names.remove("AJAY")
names.discard("AJAY")
print(names)
names={"Ajay","Ragul","Sanmugam","Shahul","ram"}
print(names)

names.pop()
print(names)

names.clear()
print(names)

del names

n={"Ajay","Ajay"}
print(n)"""
a={1,2,3,4,5}
b={'a','b','c','d',5}
c=a.union(b)
print(c)

a.update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8}
c=a.intersection(b)
print(c)

print(a.intersection(b))

d=a.symmetric_difference(b)
print(d)
a.symmetric_difference_update(b)
print(a)

a={1,2,3,4,5,6,7}
b={5,6,7}
c=a.isdisjoint(b)
print(c)

c=b.issubset(a)
print(c)

c=b.issuperset(a)
print(c)


