#  func 1 - defining a function to calculate with  measurements
def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter #2 values

x, y = rect(50, 100) #2 variables
print(x, y) 
# 5000 300

#func 2 - defining a function to calculate area and price per area
def rect(d1, d2):
  area = d1 * d2
  perimeter = 2 * d1 + 2 * d2
  price = 1000 * area
  return area, perimeter, price


# func 3 - defining a function to calculate with  measurements
# more readable

def rect(d1, d2):
  area = d1 * d2
  perimeter = 2 * d1 + 2 * d2
  return area, perimeter

x, y = rect(5, 10)
print("Area:", x)
print("Perimeter:", y)
Area: 50
Perimeter: 30

# func 4 - logical operation -returns boolean true or false 
def profitable(d1, d2):
  area = d1 * d2
  invest = area > 700
  return invest

buy = profitable(90, 120)
print(buy) 
# True