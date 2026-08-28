name = "Lokesh"
age = 29
place = "Bangalore"

print("Hello Everyone, my name is", name, "and I'm from", place, "and my age is", age)
print("Hello Everyone, my name is {0} and I'm from {1} and my age is {2}".format(name, place, age))
print("Hello Everyone, my name is {my_name} and I'm from {my_place} and my age is {my_age}".format(my_name=name, my_place=place, my_age=age))
print(f"Hello Everyone, my name is {name} and I'm from {place} and my age is {age}")