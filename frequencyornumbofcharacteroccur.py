s = "banbana"
freq = {}
for char in s:
        freq[char] = freq.get(char,0) +  1
print(freq) # Output: {'b': 1, 'a': 3, 'n': 2} 