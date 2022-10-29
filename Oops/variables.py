#instance variable and class variable
from yaml import BlockSequenceStartToken


class car:
    #claass varaibles
    def __init__(self) -> None:
        #instance variable 
        self.colour = "blue"
        self.com = "BMW"
c1=car()
print(c1.colour)


    