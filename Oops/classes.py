class Mobile: #class is a blueprint
    def __init__(self,model,ram) -> None:
        self.model = model
        self.ram =ram
    def config(self): #methods
        print("The mobile is:",self.model, "and has a ram of",self.ram)
    def compare(self,other):
        if self.model == other.model:
            return True
        else:
            return False

mob1 = Mobile('note8',2) #constructor
mob2 = Mobile('note8',6)
mob2.config()
#print(id(mob1))#to print the address
if mob1.compare(mob2):
    print("they both are same models") 
else:
    print("They are not same")
