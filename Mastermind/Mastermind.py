# this will be the code for the main game

import algo.py
import computer.py
import player.py

def game():
    while True:
        try:
            gamestyle = int(input("Guess[1] or let the computer guess[2]? "))
            if gamestyle == 1:    # computer guesses
                tries = 10
                code = computer.generateCode()
                while tries > 0:
                    guess = player.playerGuess()
                    if str(code) == str(guess):
                        print("You won. The code is", code)
                        break
                    elif code != guess:
                        feedback = computer.generateFeedback(code, guess)
                        print("The computer gave you feedback. You got", feedback[1], "in the right location, and", feedback[0], "in the wrong location")
                        tries -= 1
                    if tries == 0:
                        print('You lost. The code was', code)
                        break
            if gamestyle == 2:      # player guesses
                player.reqCode()
                while True:
                    difficulty = player.reqDifficulty()
                    if difficulty == 0:
                        algo.comBraindead()
                        break
                    if difficulty == 1:
                        algo.comEasy()
                        break
                    if difficulty == 2:
                        print("Not yet developed, try 0")
                        continue
                    if difficulty == 3:
                        print("Not yet developed, try 0")
                        continue
                    else:
                        raise Exception
            else:
                raise Exception
        except:
            print("Enter '1' to guess and '2' to let the computer guess")

game()
