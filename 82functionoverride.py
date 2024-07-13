class employee:
    def wh(self):
        self.hrs=50
    def print(self):
        print("Total working hours:",self.hrs)
class trainee(employee):
    def wh(self):              #function override
        self.hrs=60
        
e=employee()
e.wh()            #first class working hour called
e.print()

t=trainee()
t.wh()            #inherit class working hours class 
t.print()           #function overriding call