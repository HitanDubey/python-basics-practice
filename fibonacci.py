n = 9
if(n==0):
    print("0")
elif(n==1):
    print("0 1")
else:
    first = 0
    second = 1
    print(first,second,end=" ")
    next = first+second
    while next<=n-1:
        print(next,end=" ")
        first = second
        second = next
        next = first + second