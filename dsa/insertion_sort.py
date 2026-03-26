# Best-case: O(n) when the array is already sorted.
# Worst-case: O(n²) when the array is sorted in reverse order.    
              
arr = [67,23,87,98,196,45,67,55,11,13,45]
n = len(arr)
for i in range(1,n):
    for j in range(i,-1,-1):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] =  temp

print(arr)
