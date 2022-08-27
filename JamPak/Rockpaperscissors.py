
def rps():
    from random import randint
    print("\nWelcome to the Rock, Paper, Scissors Game!\n")
    print("Play as much as you'd like! just be sure to type Q or Quit when you're done to return back")
    
    thegame = ["rock", "paper", "scissors"]

    computer = thegame[randint(0,2)]

    gameover = False

    while gameover is False:
        try:
            player = input("Rock, Paper, Scissors?").lower()
            if player == computer:
                print("It's a tie!")
            elif player == "rock":
                if computer == "paper":
                    print("You lose!", computer, "covers", player)
                else:
                    print("You win!", player, "smashes", computer)
            elif player == "paper":
                if computer == "scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", player, "covers", computer)
            elif player == "scissors":
                if computer == "rock":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
            elif player == "q" or "quit":
              print("Thanks for playing!")
              break
            else:
                print("That's not a valid play. Check your spelling!")
        except ValueError:
            print("invalid input")