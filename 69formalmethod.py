class student:
    name="ajay"
    age=21
    
    def print(self,gender):
        print("name:",student.name)
        print("age:",student.age)
        print("gender:",gender)
        
o=student()
student.print(o,"male")