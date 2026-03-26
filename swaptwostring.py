# a = "Hello"
# b = "Vipul"
# temp = a
# a = b
# b = temp
# print(a,b)



# swap without using extra variable
def swap_strings_pop(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    swapped_string1 = "".join(list2)
    swapped_string2 = "".join(list1)
    return swapped_string1, swapped_string2

str1 = "vipul"
str2 = "Hitan"

swapped1, swapped2 = swap_strings_pop(str1, str2)
print("Swapped strings:")
print("First string:", swapped1)
print("Second string:", swapped2)