n = 20
first = 0
second = 1

if(n == 0):
    print(first)
elif(n==1):
    print(second)
else:
    next = first
    while next<=n-1:
        print(next,end=" ")
        first = second
        second = next
        next = first + second
