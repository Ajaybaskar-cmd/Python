class student():
    name="ajay"
    age=25
    
#get attribute
print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','no attribute'))

#dot notation
print(student.name)
print(student.age)
print("--------------------------------")

#set attribute
setattr(student,'name','AJAY')
setattr(student,'age',25)
setattr(student,'newvalue','65')

print(student.name)
print(student.age)
print(student.newvalue)

#set dotnotation
student.city="thiruvarur"
print(student.city)

#delete attribute
delattr(student,'city')
#print(student.city)

#del dotnotation
del student.name

#print(getattr(student,'name'))
print(student.__dict__)

class biodata():
    name="ajay"
    age=25
    gender="male"
    
print(biodata.__dict__)