import random

def req_code():     # request code from user
    print("Pick a 4-digit code. The digits can be 0-4")
    while True:
        try:
            code = input("What's your code:")
            if len(code) != 4:
                raise Exception
            for i in code:
                if not int(i) in (0, 1, 2, 3, 4):
                    raise Exception
            else:
                return code
        except:
            print("Pick a 4-digit code. The digits can be 0-4")

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

def com_braindead(feedback):
    tries = 10
    while tries > 0:
        code_guess = (random.randint(0, 6), random.randint(0, 6), random.randint(0, 6), random.randint(0, 6))
        if code_guess == feedback:
            print("You lost!")
            break
        else:
            player_feedback(code_guess)
            tries -= 1
    print("You win!")

def com_easy(feedback):
    tries = 10
    correct = ()
    a = [0, 1, 2, 3, 4]
    b = [0, 1, 2, 3, 4]
    c = [0, 1, 2, 3, 4]
    d = [0, 1, 2, 3, 4]
    potential_a = []
    potential_b = []
    potential_c = []
    potential_d = []
    while tries > 0:
        if tries == 10:
            code_guess = str('0011')
            feedback1 = player_feedback(code_guess)
            if feedback1 == 2222:
                print("You lost!")
                break
            for i in feedback1:
                if i == 0:
                    pass
                if i == 1 or i == 2:
                    potential_a.append(['0', '1'])
                    potential_b.append(['0', '1'])
                    potential_c.append(['0', '1'])
                    potential_d.append(['0', '1'])
        if tries == 9:
            code_guess = str('2233')
            feedback2 = player_feedback(code_guess)
            if feedback2 == 2222:
                print("You lost!")
                break
            for i in feedback2:
                if i == 0:
                    pass
                if i == 1 or i == 2:
                    potential_a.append(['2', '3'])
                    potential_b.append(['2', '3'])
                    potential_c.append(['2', '3'])
                    potential_d.append(['2', '3'])
        if tries == 8:
            code_guess = str('1144')
            feedback2 = player_feedback(code_guess)
            if feedback2 == 2222:
                print("You lost!")
                break
            for i in feedback2:
                if i == 0:
                    pass
                if i == 1 or i == 2:
                    potential_a.append(['2', '3'])
                    potential_b.append(['2', '3'])
                    potential_c.append(['2', '3'])
                    potential_d.append(['2', '3'])
        else:
            tries -= 1
    if tries == 0:
        print("You win!")

