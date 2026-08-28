# methods/functions

# static functions - this does not take any input parameters-always it returns static output

# def greetings():
#     return "Hello People, good morning!"

# print(greetings())

# def add(num1, num2):
#     return num1+num2

# def add(num1: int, num2: int) -> int:
#     return num1+num2


# print(add(100, 300))
# print(add(300, 400))
# print(add(1234, 324))
# print(add(89, 12))


# deafult parameters

# def add(num1, num2, num3):
#     return num1+num2+num3


def add(num1, num2, num3=0):
    return num1+num2+num3

# print(add(1, 2, 3))
# print(add(1, 2))


# 1. given a string as input extract the count of vowels 

# def get_vowel_count(string: str) -> int:
#     cnt = 0

#     for i in string:
#         if i in 'aeiouAEIOU':
#             cnt += 1
#     return cnt

# value = input("Enter the string: ")
# print(get_vowel_count(value))


# list comprehension

#  given a list of integers, extract all even numbers into a new list and print them

# result = []
nums = [1, 2,3, 4, 5, 6, 7, 8, 9]
# for i in nums:
#     if i%2 == 0:
#         result.append(i)

# result = [i for i in nums if i%2 == 0]
# print(result)


# in-line conditional statements
result = "yes" if 10 < 2 else "No"
print(result)


