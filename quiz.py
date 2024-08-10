#Welcome user to the game
print("Welcome to my NBA Quiz! ")

#check if user wants to play the game
interest = input("Would you like to try the quiz? ").lower()

#quit if user does not want to play the game
if interest != "yes":
    quit()

#begin the quiz
print("Lets Begin! ")

#storing the user's score in a variable
score = 0

#creating a function that increments the score if correct and prints incorrect if the answer is wrong
def check(UserAnswer, CorrectAnswer):
    global score #declare global score variable
    if UserAnswer == CorrectAnswer:
        print("Correct! ")
        score += 1
    else:
        print("Incorrect :( ")

#Ask 4 questions to the user 
answer = input("Which team has the most NBA Championships? ").lower()
CorrectAnswer = "boston celtics"
check(answer,CorrectAnswer)


answer = input("Who won the 2016 NBA Finals? ").lower()
CorrectAnswer = "cleveland cavaliers"
check(answer,CorrectAnswer)

answer = input("What's Aarnav's favourite NBA team? ").lower()
CorrectAnswer = "los Angeles clippers"
check(answer,CorrectAnswer)


answer = input("Who was the first pick in the 2024 NBA Draft? ").lower()
CorrectAnswer = "victor wembanyama"
check(answer,CorrectAnswer)


#Total up the user's score and print results
print("Congrats on completing the quiz! You got a final score of " + str((score/4)*100) + "%")
