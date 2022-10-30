""" from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
   #if we  fail to create a abstract method we get a error
class laptop(computer):
    def process(self):
        print("its running")
class mobile():
    pass
com1 = laptop()
com1.process()
com2 = mobile() """
#############iterators#############
#nums = [1,2,3,4,5,]
#it = iter(nums)
#print(it.__next__())
#print(next(it))
class Numbers:
    def __init__(self) -> None:
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
       if self.num<=10:
         val = self.num
         self.num+=2
        
         return val
       else:
           raise StopIteration
    
values = Numbers()
print(next(values))
print(values.__next__())
for i in values:
    print(i)