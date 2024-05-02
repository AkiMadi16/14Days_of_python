# for num in range(1, 100):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fizz"
#     if num % 5 == 0:
#         string = string + "Buzz"
#     if num % 5 != 0 and num % 3 != 0:
#         string = string + "str(num)"
#         print(string)

# print(*map(lambda i: 'Fizz' * (not i % 3) + 'Buzz' *
#       (not i % 5) or i, range(100), sep='\n'))


def fizzBuzz(n):
    # Write your code here
    # result = list(map(lambda i: "Fizz" * (not i % 3) +
    #               "Buzz" * (not i % 5) or i, range(1, n+1)))
    # print(result)
    result = list(map(lambda i: 'Fizz' * (not i % 3) +
                  'Buzz' * (not i % 5) or i, range(1, n+1)))

    for numStr in result:
        print(numStr)


print(fizzBuzz(16))


# if __name__ == '__main__':
#     n = int(raw_input().strip())

#     fizzBuzz(n)
