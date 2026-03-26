def pr(n):
        for i in range(2,n+1):
            if n%i==0:
                return i
                break
            
            
def printPrimeFactorization(n):
        while n!=1:
            k = pr(n)
            print(k)
            n = n//k

n = 1256
printPrimeFactorization(n)        
        
        
   