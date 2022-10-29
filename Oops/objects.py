from re import A


class Test:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __repr__(self) -> str:
        return "test a:%s b:%s"%(self.a,self.b)
    def __str__(self) -> str:
        return "by str method test a:%s,""b is %s" %(self.a,self.b)

t = Test(1234,1235)
print(t)#for str()
print([t])#for repr()
#if str()is not used then print(t)prints repr only