#instance attribute
class user:
    course="java"

print(getattr(user,'course'))
print(user.__dict__)
o=user()
print(o.__dict__)
print(o.course)
o.course="c++"
print(o.course)

print(o.__dict__)
print(user.__dict__)
