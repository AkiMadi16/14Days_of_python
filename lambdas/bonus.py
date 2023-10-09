# You work on a payroll program.

# Given a **list** of salaries, you need to take the **bonus** everybody is getting as input and increase all the salaries by that amount.

# Output the resulting list.
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())
result = list(map(lambda x: x + bonus, salaries))
print(result)
