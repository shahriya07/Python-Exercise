print("Program to check age Booleans ")
myAge = 21
userAge = int( input("Enter your age: "))

if(myAge < userAge):
    print("He's older than you")
elif(myAge > userAge):
    print("He's younger than you")
else:
    print("You two have the same age")
