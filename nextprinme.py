def prime(n):
    count = 0
    for i in range(1,n+1):
         if(n%i==0):
             count = count+1
    if(count==2):
        return 2
    
n = 14
for i in range(1,n):
     n = n+1
     k = prime(n)
     if (k == 2):
         print("hello",n)
         break
        
        
    
 