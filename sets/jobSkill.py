# You are working on a recruitment platform, which should match the available jobs and the candidates based on their skills.
# The skills required for the job, and the candidate's skills are stored in sets.
# Complete the program to output the matched skill.

# level

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}


def matchedSkills(skills, job_skills):
    matched = skills & job_skills
    if matched:
        print(*matched, sep=",")
    else:
        print("Skills are not Matched with job skills")


# //calling the function
matchedSkills(skills, job_skills)
# HTML

# Sets can be combined using mathematical operations.

# union operator - combines two sets to form a new one containing items in either.
print(skills | job_skills)
# {'NodeJS', 'JS', 'CSS', 'Scala', 'Python', 'C++', 'Java', 'C#', 'SQL', 'HTML'}

# intersection operator - ets items only in both.
print(skills & job_skills)
# {'HTML'}

# difference operator
print(skills - job_skills)
# {'Scala', 'Python', 'C++', 'Java', 'SQL'}

# symetrical difference operator -gets items in either set, but not both.
print(skills ^ job_skills)
# {'CSS', 'C++', 'C#', 'NodeJS', 'JS', 'Scala', 'Python', 'Java', 'SQL'}
