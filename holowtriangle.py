n = 9
for i in range(1,n+1):
    k = n+2-i
    for j in range(1,k):
          if i > 1 and i< n:
                 if  j ==1 or j ==k-1:
                   print("*",end=" ")
                 else: 
                     print(" ",end=" ")
          else :    
            print("*",end=" ")
    print()    