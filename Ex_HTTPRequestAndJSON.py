import requests
import json
import html
import random
print("Program for a quizzing game")

url = "https://opentdb.com/api.php?amount=1"
score = 0
endGame = ""


while endGame.lower() != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = input("There is some issue with the url press enter or type 'quit' to end the game.")
    else:
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "- " + answer)
            answer_number += 1

        userAnswer = input("Ans: " + "\n")
        endGame = input("Press enter to keep playing or type 'quit' to end the game: " )

        if(userAnswer == correct_answer):
            print("Your answer is correct")
            score += 1
            print("Your Score: ", score)
        else:
            print("Your answer is incorrect")
            print("Your Score: ", score)

        if(endGame == "quit"):
            print("Your final score: ", score)
            break

        
        
    
        


 

