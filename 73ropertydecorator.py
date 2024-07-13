class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
       # self.msg=self.name+" is "+str(self.age)+" year old"
    @property
    def msg(self):
        return self.name+" is "+str(self.age)+" years old"
        
o=user("Ajay",21)
print(o.msg)
o.name="ragul"
print(o.msg)