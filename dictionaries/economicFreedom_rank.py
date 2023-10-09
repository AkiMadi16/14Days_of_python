# You are working on data that represents the economic freedom rank by country.

# Each country name and rank are stored in a dictionary, with the key being the country name.

# Complete the program to take the country name as input and output its corresponding economic freedom rank.

# In case the provided country name is not present in the data, output "Not found".
data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

country_name = input()

if country_name in data:
    print(data.get(country_name))
else:
    print("Not", "found")
