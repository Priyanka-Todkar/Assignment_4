# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

def square_list(numbers):
    square_numbers = list(map(lambda x: x ** 2, numbers))
    return square_numbers
user_input = input("Enter a list of numbers, seperated by sapaces: ")
numbers = list(map(int,user_input.split()))
squared_number = square_list(numbers)
print(squared_number)

