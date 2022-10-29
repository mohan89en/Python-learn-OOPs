#acessing of hidden variables
class Myclass:
    __hiddenvar = 10#we can hide it from seeing using"__"
    def add(self,increment):
        self.__hiddenvar +=increment
        print(self.__hiddenvar)
        
myobject = Myclass()
myobject.add(2)
#print(myobject.__hiddenvar)
#to acess the hidden we use
print(myobject._Myclass__hiddenvar)