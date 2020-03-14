import time as t
import matplotlib.pyplot as plt

times = []
mistakes = 0

print("Program to type faster. Type 'coder'")
input("Press enter to continue")

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != "coder"):
        mistakes += 1

print("You made " + str(mistakes) + " mistakes. ")
print("Now let's see your evolution")
t.sleep(3)

x =[1,2,3,4,5]
y = times
plt.plot(x,y)
plt.show()
    
