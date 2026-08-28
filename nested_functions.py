# nested functions/methods


def outer_func():
    
    def inner_func():
        print("Hello, I'm an inner function!")
    
    inner_func()
    print("This is an outer function")

# outer_func()


# def calculate_tax(gross_salary: int) -> int:
#     return gross_salary * 0.10

# def calculate_net_salary(gross_salary: int) -> int:
#     tax_amount = calculate_tax(gross_salary)
#     print(f"tax liability is: {tax_amount}")
    
#     net_salary = gross_salary - tax_amount
#     print(f"Net Salary for gross salary of {gross_salary} is - {net_salary}")
    
# calculate_net_salary(145000)



def calculate_net_salary(gross_salary: int) -> int:
    # func_name = "outer_function"
    
    def calculate_tax(gross_salary: int) -> int:
        return gross_salary * 0.10
    
    tax_amount = calculate_tax(gross_salary)
    print(f"tax liability is: {tax_amount}")
    
    net_salary = gross_salary - tax_amount
    print(f"Net Salary for gross salary of {gross_salary} is - {net_salary}")

calculate_net_salary(145000)