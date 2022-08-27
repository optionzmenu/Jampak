def numberguessinggame():
    import random
    number = random.randint(1, 10)
    print("\nWelcome to the Number Guessing Game!!\n")
    print("Play as much as you'd like! This game deals with numnbers. Type 9000 to quit after game starts!")

    playername = input('\nHello, I am the the Number Guessing Bot! What is your name? ')
    print('Okay! '+ playername+ ' I am thinking of a number between 1 and 10. Can you guess it ' + playername + '?')
    gameover = False
    totalguesses = 0
    while gameover is False:
        try:
            guess = int(input())
            if totalguesses > 5:
                print('You did not guess the number, The number was ' + str(number))
                gameover = True
            elif guess == 9000:
                break
            elif guess > 10 or guess < 1:
                print("I said between 1 and 10 silly!")
                totalguesses += 1
            elif guess < number:
                print('Nope! Too low!')
                totalguesses += 1
            elif guess > number:
                print('Sorry! Too high!')
                totalguesses += 1
            elif guess == number:
                print('Congrats! You guessed the number in ' + str(totalguesses) + ' tries!')
                gameover = True
            else:    
                print('Please enter a valid choice!')
                totalguesses += 1
        except ValueError:
            print('Wrong input')
            totalguesses += 1