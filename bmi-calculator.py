# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

#Write your code below:
bmi = weight / (height * height)

if bmi <= 18.5:
  print(f"Your BMI is {bmi}, you are underweight")

elif bmi < 25.0:
  print(f"Your BMI is {bmi}, you have a normal weight")

elif bmi < 30.0:
  print(f"Your BMI is {bmi}, you are slightly overweight")

elif bmi <= 35.0:
  print(f"Your BMI is {bmi}, you are obese")

else:
  print(f"Your BMI is {bmi}, you are clinically obese")