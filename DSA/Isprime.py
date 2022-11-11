def isPrime( N):
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                return 'No'
        return 'Yes'
        
def isSumOfTwo ( N):
    
        if N < 3: return 'No'
        
        elif N % 2 == 0: return 'Yes'
        
        return isPrime(N - 2)
    
print(isSumOfTwo(11))