print("Program to calculate the BMI ")
userHeight = float( input("Enter your Height in meters"))
userWeight = float( input("Enter your Weight in Kg"))
bmi = userWeight / (userHeight * userHeight)

print("Your BMI is: ", round(bmi, 2))

if( bmi <= 18.5 ):
    print("Underweight")
elif( bmi > 18.5 or bmi <= 24.9):
    print("Normal weight")
elif( bmi > 24.9 or bmi <= 29.9):
    print("Overweight")
elif( bmi >= 30):
    print("Obesity")
