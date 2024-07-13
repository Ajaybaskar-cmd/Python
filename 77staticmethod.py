class student:
    def __init__(self,name="ajay",age=21):
        self.name=name
        self.age=age
    @property
    def print(self):
        print("Name:",self.name,"Age:",self.age)
     
    @staticmethod   
    def welcome():
        print("Welcome our institution")
        
o=student("ajay",21)
o.print
o.welcome()