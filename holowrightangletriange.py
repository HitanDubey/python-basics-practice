n = 5
for i in range(1,n+1):
    for j in range(0,i):
         if i>1 and i< n:
              if j==0 or j==i-1:
                   print("*",end=" ")
              else:    
                  print(" ",end=" ")
         else:  
              print("*",end=" ")
    print() 