class student:
    
    school = "JNU SOE"
    def __init__(self,m1,m2,m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3+3)/3
s1= student(32,3,45)
print(s1.school)
print(s1.avg())
