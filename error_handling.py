# Error - Handling in Python


# result = 100/num
# print(result)

# try:
#     num = int(input("Enter a number: "))
#     result = 100/num
# except Exception as e:
#     print("Error -", e)
    
# try:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("Please enter positive values")
#     else:
#         result = 100/num
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# except ValueError:
#     print("Please enter a valid integer for division")


# try:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         raise "Please enter positive values"
#     else:
#         result = 100/num
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# except ValueError:
#     print("Please enter a valid integer for division")
    
# result = "Unknow"   
# try:
#     a = 10
#     b = 20
#     result = a + b
# except TypeError as e:
#     print(e)
# else:
#     print("result - ", result)

 
result = "Unknown"   
try:
    a = 10
    b = "20"
    result = a + b
except TypeError as e:
    print(e)
finally:
    print("result - ", result)