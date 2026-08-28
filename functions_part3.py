# advanced functions with key-word arguments

# *args

def add(*args) -> int:
    print(args)
    # ls = list(args)
    return sum(args)

# print(add(10, 20))
# print(add(10, 20, 20))
# print(add(10, 20, 40, 50))
# print(add(10, 20, 40, 50, 60))

# def stu_details(**kwargs) -> dict:
#     return kwargs

# result = stu_details(name="Umesh", age=30, city="Bangalore")
# print(result)


# def my_func(*args, **kwargs):
#     print(f"Args - {args}")
#     print(f"KWARGS - {kwargs}")
    
# my_func(10, 20, 30, 40, name="Kalyan", age=28, city="Bangalore")


# def get_tax(amount: int) -> int:
#     return amount*0.30

# tax = get_tax(50000)
# print(tax)


def get_tax(amount: int) -> int:
    print(amount*0.30)

tax = get_tax(50000)
print(tax)




