#Dictionary

car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

userInput = input()

if userInput == 'brand':
    print(car['brand'])
elif userInput == 'year':
    print(car['year'])
elif userInput == 'color':
    print(car.get('color'))
elif userInput == 'mileage':
    print(car.get('mileage'))
elif userInput == 'price':
     print(car.get('price', 'Not Found - Talk to helpdesk'))
else:
    print('Please check our list and enter a valid item')


# nums = {
#     1: "one",
#     2: "two",
#     3: "three",
# }
# print(1 in nums)
# print("three" in nums)
# print(4 not in nums)
# True
# False