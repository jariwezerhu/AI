# here all algorithms for cracking codes will be written

import random
from itertools import permutations


def concatenate_list_data(list):   # https://www.w3resource.com/python-exercises/python-basic-exercise-27.php
    result= ''
    for element in list:
        result += str(element)
    return result


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
