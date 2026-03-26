n = 'aaabbcccccddddzzzaa'
k = list(n)
print(k)
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if k[i] == k[j]:
            k[j] = ''

print(k)
r = ''.join(k)      
print(r)
