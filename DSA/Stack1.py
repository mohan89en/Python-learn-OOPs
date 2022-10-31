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
    
if __name__ == "__main__":
 s = Stack()
 print(s.is_empty())
 s.Push(4)
 print(s.peek())
 print(s.size())
 print(s.is_empty())
 s.Push(8.4)
 print(s.pop())
 print(s.pop())
 print(s.size()) 
    