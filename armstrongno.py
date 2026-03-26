def p(n,c):
    return n**c
n = 407     #take input and use len() function  for taking length
# 370, 371, 407, 1634, 8208, and 9474
temp = n
count = 0
while temp!=0:
    temp = temp // 10
    count +=1
sum = 0
k = n
r = k
for i in range (0,count):
    r = k % 10
    sum = sum + p(r,count)
    k = k // 10

if(n == sum):
    print("Number is Armstrong")
else :
    print("It is not armstrong number")  