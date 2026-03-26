# a*b/hcf(a*b)
# 1st method
import math
a = 2793
b = 9
result = max(a,b)
while True:
    if result%a==0 and result%b==0:
        break
    result +=max(a,b)
print(result)    

#2nd method2

a = 17 
b = 34
k = math.gcd(a,b)
result = (a*b)//k
print(result)