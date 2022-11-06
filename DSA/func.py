#ceil function returns the integer value greater than  the specified value
#floor returns the integer value less than the specified value
import math
print(math.ceil(1.6))
print(math.floor(1.6))
print(math.floor(-1.6))
print(math.ceil(-1.6))

#arguments => *args and **kwargs
#*args is for variable number of arguments
def my_fun(*args):
    for args in args:
        print(args)
        
my_fun('hello','welcome')
#**kwargs is for variable number of keyword arguments
def my_fun(**kwargs):
    for key,value in kwargs.items():
        print("%s ==%s" % (key,value))
        
my_fun(animal = "dog",bird = "hen",plant = "tulasi")