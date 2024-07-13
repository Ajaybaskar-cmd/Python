class nokia:
    name='Nokia'
    website='www.nokia.com'
    
    def contact(self):
        print("Address:")
        print("97,thalpal,engan")
class nokia_1100(nokia):
    def __init__(self):
        self.model="Nokia 1100"
        self.year='1998'
        
    def productdetails(self):
        print("Name:",self.name)
        print("Model:",self.model)
        print("Model year:",self.year)
        print("Website:",self.website)
        
mobile=nokia_1100()
mobile.productdetails()