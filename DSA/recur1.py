def count(n,m):
    if n==0:
        return 1
    elif m==0 or n<0:
        return 0
    else:
        return count(n-m,m)+count(n,m-1)
    
print(count(5,3))