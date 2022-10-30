
def topten():
    # yield makes the functionn as generator
    n=1
    while n<=10:
        sq = n*n
        yield sq
        n+=1

values= topten()
print(values.__next__())

for i in values:
    print(i)
    
#it is used to deal with one values at a time than fetching whole the list
