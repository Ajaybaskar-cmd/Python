class student:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1
        
    @property
    def print(self):
        print("Name:",self.name,"Age:",self.age)
    @classmethod
    def total(cls):
        return cls.count
        
        
o=student("ajay",21)
o.print
o1=student("ragul",21)
o1.print
o2=student("Rajaji",21)
o2.print
print("total admission:",o.total())
print("Student admission:",student.total())