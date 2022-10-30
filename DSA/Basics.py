import math
mystr = "Hello is a "
print(mystr.lower())
print(mystr.find("is"))
print(mystr.split("is"))
#lists are mutable and strings are immutable
#tuple is immutable, like a string. A tuple cannot be changed. Tuples are written as
#comma-delimited values enclosed in parentheses.
mytup =(1,2,3,"eee","fer")
print(mytup*3)
print(mytup[0:2])
#A set is an unordered collection of zero or more immutable Python data objects
myset = {1,2,3,"cat","dog",False}
print(myset)
set2 = {7,3,56,78}
set3 = myset.union(set2)
print(set3)
#set is mutable but elements are immutable
#set1.intersection(set2),set1.difference(set2),set1.issubset(set2)
#set.add(item)
myset.pop()
print(myset)
#dictonaries 
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
 print(capitals[k]," is the capital of ", k)
del capitals['California']
print(capitals)
print(capitals.get('cfjdh','Utah')) #(key,alt)
####
for i in range(5):
    print(i*2)
    
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
 for a_letter in a_word:
  letter_list.append(a_letter)
print(letter_list)
n = input()
n = int(n)
if n < 0:
 n = abs(n)
print(math.sqrt(n))
num = int(input("enter the number: "))
try:
    print(math.sqrt(num))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(num)))
 



