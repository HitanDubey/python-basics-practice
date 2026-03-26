arr = input("Enter elements separated by spaces: ").strip().split()
print(arr)
n = len(arr)
for i in range(0,n):
    p = 0
    for j in range(i+1,n):
        if(arr[i] == arr[j]):
            p = 1
    if p==1:
        break
if p == 0:
    print("True")    
else :
    print("False")    