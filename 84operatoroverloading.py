class addition:
    def __init__(self,a):
        self.a=a
        
    #operator overload magic method
    def __add__(o,o1):
        return o.a+o1.a
    
o=addition(10)
o1=addition(20)
print("Total=",o+o1)