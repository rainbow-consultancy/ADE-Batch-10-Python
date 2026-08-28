# loops - This is used when we want to execute the same block of code multiple times.

# 1. for loop
# 2. while loop


# for loop -> this is used when we want to iterate over a sequence like a list, string, tuple, range etc.,

# for i in range(1, 11, 1):
#     print(i)

    
# for i in range(11):
#     print(i)


name = "python"

# for chr in name:
#     print(chr)

# nums = [1, 2, 3, 4, 5]

# for item in nums:
#     print(item)

# for i in range(len(nums)):
#     print(nums[i])


# for i in range(len(name)):
#     print(name[i])


# while loop - it takes a condition until this condition becomes false it keep on executing the code block

# i = 1

# while i <= 10:
#     print(i)
    # i = i + 1
    # i += 1

# if 10 > 2:
#     if 5 > 10:
#         print("yes")
#     else:
#         print("No")

# for i in range(6):
#     for j in range(100, 106):
#         print(i, j)


# 2 table 

# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6

# for i in range(1, 11):
#     print("2 * {0} = {1}".format(i, i*2))
# print("-------------------------------------")
# for i in range(1, 11):
#     print(f"2 * {i} = {i*2}")

for i in range(2, 6):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    print("-----------------------------")
