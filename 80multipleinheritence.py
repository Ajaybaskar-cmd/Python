class father:
    def land(self):
        print("Owned for 20 acres land")
class mother:
    def gold(self):
        print("Owned for 100 gram gold")
class son(father,mother):
    @property
    def car(self):
        print("Owned for audi car")
        
o=son()
o.land()
o.gold()
o.car