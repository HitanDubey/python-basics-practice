# Enter your code here. Read input from STDIN. Print output to STDOUT
# n,a = map(int, input().strip().split())
# s = input()
s = 'hitan'
rev = s[::-1]
print(rev)
k = len(s)
p = k-1
print(k)
for i in range(0,k):
    print(s[p],end="")
    p = p-1 
print()    
rek = s[::-1]
print(rek)