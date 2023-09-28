# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
 #Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]


def triple(num):
    return num * 3
input_list = [1, 2, 3, 4, 5, 6, 7]
result = list(map(triple,input_list))

print("Triple of list numbers: ")
print(result)