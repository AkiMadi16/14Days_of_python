# Selection is like a fork in the road. It allows your programs to decide which path to take.
#sets the value of age

age = 22
if age >= 18:
  # executed only if customer is over-age
  print("Regular price") 
else:
  #executed only if age is less than 18
  print("Discount")

if age >= 18:
	print("Regular price")
else: 
	print("Discount")

age = 41
if age >= 18:
    print("Regular price")
else: 
    print("Discount")

age = 30
if age >= 18:
  print("Regular price")
else:
  print("Discount")
print("Proceed to payment")

age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else: 
  print("Regular price")


  # lessons learned 🌟 the colon : symbol and the use of indentation are needed to prevent errors


age = 30
if age < 18:
  print("Apply Discount")
print("Proceed to payment")

# indentation check
age = 16
if age < 18: 
  print("Apply Discount")
print("Proceed to Payment")

age = 75
if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")
print("Proceed to payment")


age = 16
is_student = True

if age < 18:
  #execute if age is less than 18
  if is_student:
    #execute if under 18 and also a student
    print("20% discount")
  else:
    #execute if under 18 and not a student
    print("10% discount")
else:
  #execute this code customer 18 or over
  print("Regular price")

# 🌟 skip the else statement when it is not needed

# 🌟 check for more conditions with the elif statement

# 🌟 nest if-else statements within each other