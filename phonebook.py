# Tuples can be created without the parentheses by just separating the values with commas.

contacts = [
    ('James', 424619346),
    ('Amy', 24352955),
    ('John', 319572957),
    ('Amanda', 65872753),
    ('Bob', 18587279)
]

userInput = input()

if 'James' == userInput:
    print(userInput, "is", contacts[0][1])
elif 'Amy' == userInput:
    print(userInput, "is", contacts[1][1])
elif 'John' == userInput:
    print(userInput, "is", contacts[2][1])
elif 'Amanda' == userInput:
    print(userInput, "is", contacts[3][1])
elif 'Bob' == userInput:
    print(userInput, "is", contacts[4][1])
else:
    print("Not", "Found")


    # Tuple unpacking
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) # 1
print(b) # 2
print(c) #[3, 4, 5, 6, 7, 8]
print(d) # 9
