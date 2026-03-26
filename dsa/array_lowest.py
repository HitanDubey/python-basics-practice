arr = [22,333,4,5,66]
print(min(arr))

#manually method

min = arr[0]
l = len(arr)
for i in range(1,l):
    if(arr[i] <  min):
        min = arr[i]
print(min)