class a:
    def dis(self):
        print("i am a")
class b(a):
    def display(self):
        print("I am b")
class c(a):
    def display(self):
        print("I am c")
class d(b,c):
    #def display(self):
       # print("I am d")
       pass
        
o=d()
o.display()
o.dis()