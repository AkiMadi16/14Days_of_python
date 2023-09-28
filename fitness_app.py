# A user is considered to have achieved the daily fitness goal when the number of steps is greater than 10000 or the number of active minutes is greater than 30.

# **Task**

# Complete the code to output True if the user has achieved the daily fitness goal, and False otherwise.

# Take steps and minutes as inputs
steps = int(input())
active_minutes = int(input())

# Store the result of the operations in the variable
goal_achieved = (steps  > 10000) or (active_minutes > 30)

# Display the result on the screen
print(goal_achieved)



# lessons learned
# Logical operations are needed for machines to evaluate complex scenarios.
# type of operation that makes machines evaluate different scenarios and make decisions.
