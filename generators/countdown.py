# **Generators** are a type of iterable, like lists or tuples.

# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with **for** loops.

# They can be created using functions and the **yield** statement. The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)
# 5
# 4
# 3
# 2
# 1


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(numbers(11)))
# [0, 2, 4, 6, 8, 10]
