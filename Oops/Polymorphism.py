#Polymorphism simply means having many forms
class Animal:
    def Hello(self):
        print("there are many animals")
    def swim(self):
        print("All the animals can't swim like aquatic animals only some of the animals can swim")

class Frog(Animal):
    def swim(self):
        print("It can swim by birth itself")

class monkey(Animal):
    def swim(self):
        print("it can't swim like fish")
        
object_fr = Frog()
object_ani = Animal()
object_mon = monkey()
object_fr.swim()
object_mon.swim()
object_mon.Hello()
       