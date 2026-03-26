a = "thIs is my name vIpUl"
vo = "aeiouAEIOU"
count = 0
for i in range(0,len(vo)):
    for j in range(0,len(a)):
        if vo[i] == a[j]:
            count +=1
print(count)            