#class use of the function
class student:
    name="ajay"
    age=21
    
    def print():
        print("name:",student.name)
        print("age:",student.age)
        
#dot notation
student.print()

#get attribute
print(getattr(student,"print"))
getattr(student,"print")()                               #use of () circular bracket


#dict function
print(student.__dict__)

student.__dict__["print"]()