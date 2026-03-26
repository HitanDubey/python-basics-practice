# arr = [67,23,88,97,11,13,45]
# print(sorted(arr))
# Worst-case: O(n²) 
# Average-case: O(n²) 
# Best-case: O(n²) 

arr1 = [67,23,87,98,196,45,67,55,11,13,45]

l = len(arr1)
index = None
print(l)
for i in range(0,l):
    min = arr1[i]
    k = 0
    for j in range(i+1,l):
        if min > arr1[j]:
            min = arr1[j]
            index = j
            k = 1
    if(k==1):  
         temp = arr1[i]
    arr1[i] = min
    arr1[index] = temp    
   

print(arr1)
            

#alternative
my_array = [64, 34, 25, 5, 22, 11, 90, 12,67,23,87,98,196,45,67,55,11,13,45]

n = len(my_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_array[min_index] > my_array[j]:
            min_index = j

    temp = my_array[i]
    my_array[i] = my_array[min_index]     # my_array[i], my_array[min_index] = my_array[min_index], my_array[i] (without using thrt variaable )
    my_array[min_index] = temp    

print(my_array)          