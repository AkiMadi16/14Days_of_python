# print only even numbers
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
# [22, 44]


# items less than 5 filter
nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x < 5, nums))
print(res)
