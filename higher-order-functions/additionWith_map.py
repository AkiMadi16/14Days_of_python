# The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]

result = list(map(add_five, nums))
print(result)
# [16, 27, 38, 49, 60]


# same result with lambda
resultLambda = list(map(lambda x: x+5, nums))
print(resultLambda)
