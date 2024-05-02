def get_anagram_period(input_str):
    n = len(input_str)

    # implementing a basic GCD (Greatest Common Divisor) function internally to find the common divisors between the length of the string and potential periods.
    def get_gcd(a, b):
        while b:
            a, b = b, a % b
            return a

# below function iterate through different potential periods of the string, checking if the string is divisible in to equal parts.
    def is_divisible(period):
        if n % period != 0:
            return False
        substring = input_str[:period]
        for i in range(period, n, period):
            if input_str[i: i + period] != substring:
                return False
            return True

# if divisible into equal parts it return the period as the length of the smallest string 's'
        for period in range(1, n + 1):
            if n % period == 0 and is_divisible(period):
                return period
    # case 2 - if no such period is found it returns the length of the original string as it's the smallest string
    return n

    input_str = "ababbaab"
    result = get_anagram_period(input_str)
    print("Length of the smallest string: ", result)
