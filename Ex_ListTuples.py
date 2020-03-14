print("Program to print the users birthday")
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
userInput = input("Enter your birthday: ")

print("You were born in ", month[int(userInput[3:5])-1])

print("Program to add new element in list")
names = ["John", "Kate", "Smith", "Betty"]
userName = input("Enter your name: ")
names.append(userName)
print(names)
