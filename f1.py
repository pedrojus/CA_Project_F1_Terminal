# F1 Trivia Terminal-Based Game
# Made by Pedro Jusino on 06/13/21

from questions import *
import sys

class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.score = 0
        self.playedCategories = []
        
def printMenu():
    print("")
    print("Please choose from the following categories regarding F1 Trivia by entering the letter:")
    print("a. Team Trivia (5 points per question, 2 questions)\nb. Driver Trivia (10 points per question, 3 questions)")
    print("c. Track Trivia (20 points per question, 3 questions)\nd. History Trivia (25 points per question, 3 questions)")
    print("Press Q to Quit")
    
def displayCategoryQuestions(categorySelection):
    f"Now displaying {categorySelection.categoryName} trivia questions..."
    for i in range(0, len(categorySelection.list)):
        print(categorySelection.list[i].question)
        print(categorySelection.list[i].answerChoices)
        playerChoice = input("\nEnter your answer (please just enter a letter)\n")
        if (playerChoice == categorySelection.list[i].correctAnswer):
            print(f"Correct! You earned {categorySelection.points} points!")
            player_instance.score += categorySelection.points
        else:
            print("Incorrect Answer!")
            
print("Welcome to the Formula 1 trivia game!" + "\n" + "Created by Pedro Jusino")
print("""                                     d88b
                     _______________|8888|_______________
                    |_____________ ,~~~~~~. _____________|
  _________         |_____________: mmmmmm :_____________|         _________
 / _______ \   ,----|~~~~~~~~~~~,'\ _...._ /`.~~~~~~~~~~~|----,   / _______ \\
| /       \ |  |    |       |____|,d~    ~b.|____|       |    |  | /       \ |
||         |-------------------\-d.-~~~~~~-.b-/-------------------|         ||
||         | |8888 ....... _,===~/......... \~===._         8888| |         ||
||         |=========_,===~~======._.=~~=._.======~~===._=========|         ||
||         | |888===~~ ...... //,, .`~~~~'. .,\\        ~~===888| |         ||
||        |===================,P'.::::::::.. `?,===================|        ||
||        |_________________,P'_::----------.._`?,_________________|        ||
`|        |-------------------~~~~~~~~~~~~~~~~~~-------------------|        |'
  \_______/                                              _ Seal _  \_______/)""")
print("-------------------------------------------------------------------------------")

player_instance = Player()
questionCount = 0
while True:
    printMenu()
    
    if len(player_instance.playedCategories) == 4:
       print(f"Thank you for playing the game! You earned {player_instance.score} points!")
       sys.exit() 
       
    categoryChoice = input("\nPlease choose one of the categories (please just enter a letter only)\n")
    
    if categoryChoice in player_instance.playedCategories:
        print("Incorrect Option - Category has already been played!")
        continue
    
    if "a" in categoryChoice:
        categorySelection = teamTrivia
        displayCategoryQuestions(categorySelection)
        player_instance.playedCategories.append("a")
    elif "b" in categoryChoice:
        categorySelection = driverTrivia
        displayCategoryQuestions(categorySelection)
        player_instance.playedCategories.append("b")
    elif "c" in categoryChoice:
        categorySelection = trackTrivia
        displayCategoryQuestions(categorySelection)
        player_instance.playedCategories.append("c")
    elif "d" in categoryChoice:
        categorySelection = historyTrivia
        displayCategoryQuestions(categorySelection)
        player_instance.playedCategories.append("d")
    elif "q" in categoryChoice:
        print(f"Thank you for playing the game! You earned {player_instance.score} points!")
        sys.exit()
    