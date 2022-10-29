#dealing with more than one class
class Engineer:
    def __init__(self) -> None:
        self.name = "engineer"
        self.cse = self.computer()
        self.ece = self.electronics()
    def show(self):
        print("in the outside class")
        print("name: ",self.name)
    
    class computer:
        def __init__(self) -> None:
            self.name = "dr.computer"
            self.degree = "cse"
            
        def show(self):
            print("name: ",self.name)
            print("degree:",self.degree)
            
    class electronics:
        def __init__(self) -> None:
            self.name = "dr.volt"
            self.degree = "ece"
            
        def show(self):
            print("name: ",self.name)
            print("degree:",self.degree)

outer = Engineer()
outer.show()
s1 = outer.cse
s2 = outer.ece
s1.show()
s2.show()
            
    