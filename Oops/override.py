#method overloading is the same method in a class taking different number of parameters
#method overriding same method in parent and child class
class Hello:
    def show(self):
        print("hello,there")
class hey(Hello):
    def show(self):
        print("hey!,hey!")
        
a1 = hey()
a1.show()
# child method overrides parent method
    