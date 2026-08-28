# conditional statements

# syntax
# if True:
#     code
# else:
#     code

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are a major")
# else:
#     print("You are a minor")

marks = int(input("Enter your marks: "))

# mark is 35 or below = Fail, >35 or <70 Pass, >=70 Distinction

if marks >= 0 and marks <= 35:
    print("Failed")
elif marks > 35 and marks < 70:
    print("Pass")
elif marks >= 70 and marks <= 100:
    print("Distinction")
else:
    print("Please enter valid marks, entered value is not acceptable", marks)