#First method 
a = "nitin"
rev = ""
for i in a:
    rev = i + rev
if rev == a:
    print("Same")
else :
    print("Not Same") 

#Second method

a = "Viv"
rev = a[::-1]
if rev == a:
    print("Same")
else :
    print("Not Same")