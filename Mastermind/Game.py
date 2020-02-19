import random
from itertools import permutations


def concatenate_list_data(list):   # https://www.w3resource.com/python-exercises/python-basic-exercise-27.php
    result= ''
    for element in list:
        result += str(element)
    return result


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


def comBraindead():     # niet te verliezen. gokt alleen maar
    tries = 10
    while tries > 0:
        codeGuess = (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
        feedback = playerFeedback(codeGuess)
        if feedback == 2222:
            print("You lost?!")
            break
        else:
            tries -= 1
    print("You win!")


def comEasy():         # zelf bedachte algoritme. krijgt de juiste ints en gokt uit die mogelijkheden
    tries = 10
    possibleInt = [1, 2, 3, 4, 5, 6]
    potentialCode = ''
    possibleAnswer = []
    while tries > 0:
        correct = [0, 0]
        if len(potentialCode) == 4 and possibleAnswer == []:
            for i in permutations(potentialCode):  # puts all permutations in lists
                possibleAnswer.append(concatenate_list_data(i))     # puts lists into strings and adds permutations to possibleAnswers
            generatedGuess = random.choice(possibleAnswer)
            feedback = playerFeedback(generatedGuess)
            if int(feedback) == 2222:
                print("You lost!")
                break
        elif not possibleAnswer == []:
            generatedGuess = random.choice(possibleAnswer)
            feedback = playerFeedback(generatedGuess)
            if int(feedback) == 2222:
                print("You lost!")
                break
        else:
            generatedInt = random.choice(possibleInt)       # random int
            possibleInt.remove(generatedInt)
            generatedGuess = int(str(generatedInt)*4)       # that random int repeated four times, example '1111'
            feedback = playerFeedback(generatedGuess)     # request player feedback
            if feedback == 2222:
                print("You lost!")
                break
            for i in feedback:
                if int(i) == 2:
                    correct[0] += 1
            for y in range(0, correct[0]):
                potentialCode += str(generatedInt)
        tries -= 1
    print('You win!')


def generateCode():
    code = int(str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))
    return code

def generateFeedback(code, guess):
    correct = [0, 0]    # [correct number, correct place]
    a1, b1, c1, d1 = str(code)[0], str(code)[1], str(code)[2], str(code)[3]
    a2, b2, c2, d2 = str(guess)[0], str(guess)[1], str(guess)[2], str(guess)[3]
    if a2 == a1:                        # first it checks for correct locations, changes them to 0 so they aren't reused
        correct[1] += 1
        a1 = 0
    if b2 == b1:
        correct[1] += 1
        b1 = 0
    if c2 == c1:
        correct[1] += 1
        c1 = 0
    if d2 == d1:
        correct[1] += 1
        d1 = 0
    if a2 == b1:                        # next it checks if in other locations, changes them to 0 so they aren't reused
        correct[0] += 1
        b1 = 0
    if a2 == c1:
        correct[0] += 1
        c1 = 0
    if a2 == d1:
        correct[0] += 1
        d1 = 0
    if b2 == a1:
        correct[0] += 1
        a1 = 0
    if b2 == c1:
        correct[0] += 1
        c1 = 0
    if b2 == d1:
        correct[0] += 1
        d1 = 0
    if c2 == a1:
        correct[0] += 1
        a1 = 0
    if c2 == b1:
        correct[0] += 1
        b1 = 0
    if c2 == d1:
        correct[0] += 1
        d1 = 0
    if d2 == a1:
        correct[0] += 1
    if d2 == b1:
        correct[0] += 1
    if d2 == c1:
        correct[0] += 1
    return correct

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


def game():
    while True:
        try:
            gamestyle = int(input("Guess[1] or let the computer guess[2]? "))
            if gamestyle == 1:    # computer guesses
                tries = 10
                code = generateCode()
                while tries > 0:
                    guess = playerGuess()
                    if str(code) == str(guess):
                        print("You won. The code is", code)
                        break
                    elif code != guess:
                        feedback = generateFeedback(code, guess)
                        print("The computer gave you feedback. You got", feedback[1], "in the right location, and", feedback[0], "in the wrong location")
                        tries -= 1
                    if tries == 0:
                        print('You lost. The code was', code)
                        break
            if gamestyle == 2:      # player guesses
                reqCode()
                while True:
                    difficulty = reqDifficulty()
                    if difficulty == 0:
                        comBraindead()
                        break
                    if difficulty == 1:
                        comEasy()
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
