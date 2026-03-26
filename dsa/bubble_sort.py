# Worst-case: O(n²) 
# Average-case: O(n²) 
# Best-case: O(n) with a flag to detect if any swaps occurred during a pass; otherwise, it remains O(n²) 

arr = [67,23,88,97,11,13,45]
arr.sort()
print(arr)

arr1 = [67,23,88,97,11,13,45]
#manually buble sort
n  = len(arr1)
for i in range(0,n-1):
    for j in range (0,n-i-1):

        if(arr1[j]>arr1[j+1]):
            temp = arr1[j]
            arr1[j] = arr1[j+1]
            arr1[j+1] =  temp


print(arr1)

#Best-case: O(n) with a flag to detect if any swaps occurred during a pass; otherwise, it remains O(n²) 