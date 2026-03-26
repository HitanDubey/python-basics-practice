# First method
a = "hello hitan dubey"
k = ""
for i in range(0,len(a)):
    if a[i] == " ":
        k = k + ""
    else:
        k = k + a[i]     # for reverse = k = a[i] + k   #
print(k)       
print()

# # Second method
p = " hello vipul dubey"
no_spaces = p.replace(" ", "")
print(no_spaces) 