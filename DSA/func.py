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

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
from collections import Counter
 
# declaring the list
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
 
# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))