class A:
    def __init__(self) -> None:
        print("hello")
        
class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("I am here")
        
class D(A,B): #method resolution order
    def __init__(self) -> None:
        super().__init__()
        print("bye")
    
a1 = D() #prefer left class (methods also)

