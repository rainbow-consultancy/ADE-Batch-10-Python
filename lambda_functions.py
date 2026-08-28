# lambda function - single line func/ anonymous functions

num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))

def validate_number(num: int) -> str:
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

validate_number(num)


validate_number = lambda n: n % 2 == 0
print(f"{num} is an even number" if validate_number(num) else f"{num} is an odd number")


validate_number = lambda n: f"{num1} is an even number" if n % 2 == 0 else f"{num1} is an odd number"
print(validate_number(num1))

multiply = lambda a, b : a * b
print(multiply(num1, num2))


# 1. map - it applies a function to each value inside a iterable datatype (tuple, list, string)

nums = [1, 2, 3, 4, 5]

def get_squares(n: list) -> list:
    result = []
    for i in n:
        v = i**2
        result.append(v)
    return result

print(get_squares(nums))

def get_squares(n: int) -> int:
    return n**2

result = list(map(get_squares, nums))
print(result)


result = list(map(lambda n: n**2, nums))
print(result)


# 2. filter - this filters the data

result = list(filter(lambda n: n%2 == 0, nums))
print(result)

result = list(map(lambda n: n%2 == 0, nums))
print(result)
