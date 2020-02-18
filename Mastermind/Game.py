import random
from itertools import product

def req_code():     # request code from user
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

def req_difficulty():
    print("Now we need a difficulty. Pick 0 for brain dead, 1 for easy, 2 for normal, 3 for hard")
    while True:
        try:
            chosen_difficulty = int(input("Pick a difficulty: "))
            if len(str(chosen_difficulty)) == 1 and 0 <= chosen_difficulty <= 3:
                return chosen_difficulty
            else:
                raise Exception
        except:
            print("Pick 0 for brain dead, 1 for easy, 2 for normal, 3 for hard")

def player_feedback(code):
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
                return sorted(feedback)
        except:
            print("Input four digits. 0, 1, or 2")
            continue

def com_braindead():
    tries = 10
    while tries > 0:
        code_guess = (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
        feedback = player_feedback(code_guess)
        if feedback == 2222:
            print("You lost!")
            break
        else:
            tries -= 1
    print("You win!")

def com_easy(feedback):
    tries = 10
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 4, 5, 6]
    c = [1, 2, 3, 4, 5, 6]
    d = [1, 2, 3, 4, 5, 6]
    possibilities = []
    for i in product(a, b, c, d):
        possibilities.append(int(''.join(str(x) for x in i)))       # berekent alle mogelijkheden
    while tries > 0:
        correct = [0, 0]
        if tries == 10:
            code_guess = str('1122')
            feedback1 = player_feedback(code_guess)
            if feedback1 == 2222:
                print("You lost!")
                break
            for i in feedback1:
                if int(i) == 0:
                    pass
                if int(i) == 1:
                    correct[0] += 1
                if int(i) == 2:
                    correct[1] += 1
            if correct == [0, 0]:     # https://stackoverflow.com/a/3416473
                possibilities = [x for x in possibilities if '1' not in x and '2' not in x]
            if correct == [1, 0]:
                possibilities = [x for x in possibilities if '11' not in x and '22' not in x]
                possibilities = [x for x in possibilities if '1' in x or '2']
            if correct == [2, 0]:
                possibilities = [x for x in possibilities if '11' in x or '22' in x]
            tries -= 1
    if tries == 0:
        print("You win!")

def generate_code():
    code = int(str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))
    return code

def generate_feedback(code, guess):
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

def player_guess():
    while True:
        try:
            guess = input("Guess the 4-digit code, existing of numbers 0-6")
            if len(guess) != 4:
                raise Exception
            for i in guess:
                if not int(i) in (1, 2, 3, 4, 5, 6):
                    raise Exception
            else:
                return guess
        except:
            print("Enter a 4-digit code from numbers 0-6")


def game():
    while True:
        try:
            gamestyle = int(input("Guess[1] or let the computer guess[2]? "))
            if gamestyle == 1:
                tries = 10
                code = generate_code()
                while tries > 0:
                    guess = player_guess()
                    if str(code) == str(guess):
                        print("You won. The code is", code)
                        break
                    elif code != guess:
                        feedback = generate_feedback(code, guess)
                        print("The computer gave you feedback. You got", feedback[1] ,"in the right location, and", feedback[0],"in the wrong location")
                        tries -= 1
                    if tries == 0:
                        print('You lost. The code was', code)
                        break
            if gamestyle == 2:
                player_code = req_code()
                while True:
                    difficulty = req_difficulty()
                    if difficulty == 0:
                        com_braindead()
                        break
                    if difficulty == 1:
                        print("Not yet developed, try 0")
                        continue
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
