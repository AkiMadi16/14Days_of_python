# developing a finance app that helps users to grow their savings.
# **Task**

# Complete the code to take the savings, calculate the end amount, then display a message on the screen

# Asks the user to enter the savings
savings = input()

# Convert the user input into a float value and update the variable
savings = float(savings)

# Savings grow after 1 year at a 5% annual interest rate
balance = round(savings * 1.05, 2)

# Convert the balance into a string and update the variable
balance = str(balance)

# Concatenate the 2 strings to produce a message
message = "Amount in 1 year: " + balance

# Display the message
print(message)

# TDD - tests
# input => 24.5
# output => Amount in 1 year: 25.7
# input => 150
# output => Amount in 1 year: 157.5
# input => 250
# output => Amount in 1 year: 262.5

# lessons learned 
# in Javascript we used  `.toFixed()` method to format a floating-point number to a specific number of decimal places.
# in python we can achieve similar functionality using `round()`  
# #round(2.357, 2) => 2.36 round up a floating-point number 

