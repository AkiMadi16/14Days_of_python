# Prints all favorites in CSV using csv.DictReader
import csv

# Counts favorites using variables
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    friends, simpsons, newGirl = 0, 0, 0

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["title"]
        if favorite == "Friends":
            friends += 1
        elif favorite == "The Simpsons":
            simpsons += 1
        elif favorite == "New Girl":
            newGirl += 1

# Print counts
print(f"Friends: {friends}")
print(f"The Simpsons: {simpsons}")
print(f"New Girl: {newGirl}")