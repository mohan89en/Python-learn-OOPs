#to convert a decimal number into binary number
class Stack:
    def __init__(self) -> None:
        self.item =[]
    def is_empty(self):
        return self.item ==[]
    def Push(self,data):
        return self.item.append(data)
    def pop(self):
     return self.item.pop()
    def peek(self):
        return self.item[len(self.item)-1]
    def size(self):
        return len(self.item)
    
def divide(num):
    rem = Stack()
    while num>0:
        rem1= num%2
        rem.Push(rem1)
        num = num//2
    str_bin = ""
    while not rem.is_empty():
        str_bin = str_bin+str(rem.pop())
    return str_bin

print(divide(42))
        

