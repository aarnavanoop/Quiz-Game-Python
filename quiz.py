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

#Ask 4 questions to the user 
answer = input("Which team has the most NBA Championships? ").lower()
if answer == "boston celtics":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("Who won the 2016 NBA Finals? ").lower()
if answer == "Cleveland Cavaliers":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What's Aarnav's favourite NBA team? ").lower()
if answer == "Los Angles Clippers":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("Who was the first pick in the 2024 NBA Draft? ").lower()
if answer == "Victor Wembanyama":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")


#Total up the user's score and print results
print("Congrats on completing the quiz! You got a final score of " + str((score/4)*100) + "%")
