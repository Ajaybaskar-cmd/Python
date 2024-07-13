class grandfather:
    def land(self):
        print("Owned land")
class father(grandfather):
    def house(self):
        print("Owned house")
class son(father):
    def car(self):
        print("Owned audi car")
        
o=son()
o.land()
o.house()
o.car()