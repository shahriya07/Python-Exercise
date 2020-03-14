import random
print("Program to store names as per user enter")

x = 0 
people = []

while x < 8:
    userInput = input("Enter a name: ")
    people.append(userInput)
    x += 1

print(people)

randomIndex = random.randint(0,9)
randomName = people[randomIndex]

print("Random Name: ", randomName)

print("-------------------------------------------------")

print("Program to guess a name of random color")

colors = ["red", "pink", "yellow", "Blue", "Green"]

randomIndex1 = random.randint(0,len(colors)-1)
randomColor = colors[randomIndex1]



while True:
    userGuess = input("Guess the color: ")
    while True:
        
        if(userGuess == randomColor):
            break
        else:
            userGuess = input("Nope. Try again: ")

        print("You guessed it! I was thinking about ", userGuess)

        play_again = input("let's play again! Type 'no' to quit ")

    if play_again.lower() == 'no':
        break
        
print("It was fun, thanks for playing!")
        

    




