class Student(object):
    def __init__(self,name,idnum) -> None:
        self.name = name
        self.idnum = idnum
    def Display(self):
        print("Name:{}".format(self.name))
        print("id number:{}".format(self.idnum))

class Performance(Student):
    def __init__(self, name, idnum,marks) -> None:
        super().__init__(name, idnum)
        self.marks = marks
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnum))
        print("marks: {}".format(self.marks))
        
student1 = Performance("Rahul",36,99.1)
student1.Display()
student1.details()