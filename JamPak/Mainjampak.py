from Numberguess import numberguessinggame
from Rockpaperscissors import rps
from Quiz import quizgame
yes = ["y", "yes"]
no = ["n", "no"]
Or = ["o", "or"] 

def yesorno():
    while True:
        try:
            answer = input("Yes or No?").lower()
        except ValueError:
            print("Wrong input")
        if answer in yes:
            return True
        elif answer in no:
            return False
        elif answer in Or:
            print ("Very Funny!")
            continue
        else:
            print("Did you read the question?")
            continue

def mainmenu():
    print("Welcome to JAMPAK!")
    print("Select your game:\n 1. Number Guessing Game \n 2. Marvel Quiz \n 3. Rock Paper Scissors")

    while True:
        try:
            choice = int(input("Select your game: "))
            if choice == 1:
                numberguessinggame()
            elif choice == 2:
                quizgame()
            elif choice == 3:
                rps()
            else:
                print("Please enter a valid choice!")

            print("Do you want to return to Main Menu?")
            answer = yesorno()
            if answer is True:
                mainmenu()
            else:
                print('Gameover!')
                break

        except ValueError:
            print("Wrong input")

mainmenu()
