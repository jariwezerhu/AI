# here all the requests to players will be written

def reqCode():     # request code from user
    print("Pick a 4-digit code. The digits can be 1-6")
    while True:
        try:
            code = input("What's your code:")
            if len(code) != 4:
                raise Exception
            for i in code:
                if not int(i) in (1, 2, 3, 4, 5, 6):
                    raise Exception
            else:
                return code
        except:
            print("Pick a 4-digit code. The digits can be 1-6")


def reqDifficulty():
    print("Now we need a difficulty. Pick 0 for brain dead, 1 for easy, 2 for normal, 3 for hard")
    while True:
        try:
            chosenDifficulty = int(input("Pick a difficulty: "))
            if len(str(chosenDifficulty)) == 1 and 0 <= chosenDifficulty <= 3:
                return chosenDifficulty
            else:
                raise Exception
        except:
            print("Pick 0 for brain dead, 1 for easy, 2 for normal, 3 for hard")


def playerFeedback(code):
    print("The computer has guessed", code)
    print("{}\n{}\n{}".format("For each number in the correct place, type 2", "For each correct number in the wrong place, type 1", "For each wrong number, type 0"))
    while True:
        try:
            feedback = input("Give your response: ")
            if len(feedback) != 4:
                raise Exception
            for i in feedback:
                if not int(i) in (0, 1, 2):
                    raise Exception
            else:
                return str(feedback)
        except:
            print("Input four digits. 0, 1, or 2")
            continue

def playerGuess():
    while True:
        try:
            guess = input("Guess the 4-digit code, existing of numbers 1-6")
            if len(guess) != 4:
                raise Exception
            for i in guess:
                if not int(i) in (1, 2, 3, 4, 5, 6):
                    raise Exception
            else:
                return guess
        except:
            print("Enter a 4-digit code from numbers 1-6")
