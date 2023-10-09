# named function
def polynomial(x):
    return x**2 + 5*x + 4


print(polynomial(-4))

# lambda
print((lambda x: x**2 + 5*x + 4)(-4))

# lambda function that returns the square of it's argument
a = (lambda x: x*x)(8)


price = int(input())
perc = int(input())

res = (lambda x, y: x * y/100)(price, perc)

print(res)
