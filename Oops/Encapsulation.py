class Base:
    def __init__(self) -> None:
        self.a ="hello"
        self.b ="bye"
class Define(Base):
   def __init__(self) -> None:
       
       Base.__init__(self)
       print("calling private member:")
       print(self.b)
       
       self.b = 4
       print("calling b:",self.b)
obj1 = Define()
obj2 = Base()
print(obj1.b)
print(obj2.b)

