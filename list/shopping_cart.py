shopping_cart = [
    "laptop",
    "smartphone",
    "headphones",
    "backpack"
]
print(shopping_cart)
# ['laptop', 'smartphone', 'headphones', 'backpack']

print('laptop' in shopping_cart)
# True
print('laptop' not in shopping_cart)
# False
print('dcwd' in shopping_cart)
# False

for i in shopping_cart:
    print(i)
# laptop
# smartphone
# headphones
# backpack

# Slicing allows you to extract a portion of a list. Starting and stopping indexes are separated by a colon :

print(shopping_cart[1:2])
# ['smartphone']

print(shopping_cart[:2])
# ['laptop', 'smartphone']

print(shopping_cart[2:])
# ['headphones', 'backpack']
