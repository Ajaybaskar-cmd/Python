class student:
    def __init__(self,total):
        self._total=total
    
    @property    
    def avg(self):
        return self._total/5.0
    
    #getter
    @property
    def total(self):
        return self._total
    
    #setter
    @total.setter
    def total(self,t):
        self._total=t
    
o=student(450)
print("Total:",o._total)
print("Average:",o.avg)

print(o.total)

o.total=250
print("total:",o.total)
print("Average:",o.avg)