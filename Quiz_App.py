#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     02/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#--------------------------------
import sys
def new_game():
    guesses=[]
    guess_correct=0
    question_num=1
    total_questions = len(questions)

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        display_progress(question_num, total_questions)
        guess=input("Enter(A,B,C,D)")
        guess=guess.upper()
        guesses.append(guess)

        guess_correct+= check_answer(questions.get(key), guess)
        question_num+=1

    display_score(guess_correct,guesses)



#--------------------------------
def display_progress(current, total):
    progress = (current / total) * 100
    bar_length = 40
    block = int(round(bar_length * progress / 100))
    progress_bar = "█" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\rProgress: [{progress_bar}] {current}/{total} Question(s) Answered")
    sys.stdout.flush()
#--------------------------------
def check_answer(answer,guess):
    if answer==guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
#--------------------------------
def display_score(guess_correct,guesses):
    print("-----------------")
    print("Result")
    print("-----------------")
    print("Answers:",end="")
    for i in questions:
        print(questions.get(i),end="")
    print()

    print("Guesses:",end="")
    for i in guesses:
        print(i,end="")
    print()

    score = int((guess_correct / len(questions)) * 100)
    print("Your Score is " + str(score) + "%")

    display_performance(score)

#----------------------
def display_performance(score):
    if score > 90:
        print("Excellent! Great job!")
    elif score > 75:
        print("Good! You did well!")
    elif score > 60:
        print("Not bad! Keep it up!")
    else:
        print("You should try again! Keep practicing.")

#--------------------------------
def play_again():
    response = input("Enter Do U want to play again? (Yes or No):")
    response=response.upper()
    if response.startswith("Y"):

       return True
    else:
       return False




questions = {
    "What is the correct extension of a Python file?": "B",
    "Which of the following is NOT a Python data type?": "D",
    "What will print(2**3) output?": "C",
    "Which keyword is used to define a function in Python?": "A",
    "How do you take user input in Python?": "A",
    "What does len(\"Python\") return?": "B",
    "What will print(10 % 3) output?": "B",
}

# Multiple choice options
options = [
    ["A. .python", "B. .py", "C. .pyt", "D. .pt"],
    ["A. int", "B. str", "C. float", "D. real"],
    ["A. 5", "B. 6", "C. 8", "D. 9"],
    ["A. def", "B. function", "C. define", "D. fun"],
    ["A. input()", "B. scan()", "C. read()", "D. get_input()"],
    ["A. 5", "B. 6", "C. 7", "D. error"],
    ["A. 0", "B. 1", "C. 2", "D. 3"],
]


new_game()




while play_again():
    print("--------------------------")
    print("Game Start Again")
    new_game()



print("Byeeeeeeeeee!")











