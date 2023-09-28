def bmi(weight, height):
    index = weight / (height * height)
    print(index)
# The code defines a function that displays the Body Mass Index (BMI)

#Defining function
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back

#Calling function and using return value
patient_5 = bmi(61, 1.83) #stores return value
print("underweight:", patient_5 < 18.5)

#Another call
patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)