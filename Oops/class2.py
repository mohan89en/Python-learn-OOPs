#class in class
class Student :
    def __init__(self,name,rollno) -> None:
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name,"\n",self.rollno)
        self.lap.show()
    
    class Laptop:
        def __init__(self) -> None:
            self.brand = "lenovo"
            self.cpu = "i5"
            self.ram = 16
            
        def show(self):
            print(self.brand)

s1 = Student("mohan",36)
s1.show()
print("hello")
