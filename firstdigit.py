def firstDigit(n):
    while n>=10:
        n = n//10
    return n   
n = 9812345
print(firstDigit(n))