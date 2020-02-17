import random
# parts 1,2,3,4 request digits 0-6 and assign to letters a,b,c,d respectively
def part_1_code():
    while True:
        try:
            a = int(input("What will be your first digit? Pick from 0 to 6: "))
            if len(str(a)) == 1 and 0 <= a <= 6:
                return a
            else:
                raise Exception
        except:
            print("Enter one digit from 0 to 6")
            continue

def part_2_code():
    while True:
        try:
            b = int(input("What will be your first digit? Pick from 0 to 6: "))
            if len(str(b)) == 1 and 0 <= b <= 6:
                return b
            else:
                raise Exception
        except:
            print("Enter one digit from 0 to 6")
            continue

def part_3_code():
    while True:
        try:
            c = int(input("What will be your first digit? Pick from 0 to 6: "))
            if len(str(c)) == 1 and 0 <= c <= 6:
                return c
            else:
                raise Exception
        except:
            print("Enter one digit from 0 to 6")
            continue

def part_4_code():
    while True:
        try:
            d = int(input("What will be your first digit? Pick from 0 to 6: "))
            if len(str(d)) == 1 and 0 <= d <= 6:
                return d
            else:
                raise Exception
        except:
            print("Enter one digit from 0 to 6")
            continue

def req_code():     # request code from user
    print("First, we'll need to create a 4-digit code.")
    code = (part_1_code(), part_2_code(), part_3_code(), part_4_code())
    print("The code", code, "has been created! The computer will now try to guess the code")
    return code

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
            continue

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
                return feedback
        except:
            print("Input four digits. 0, 1, or 2")
            continue

def com_braindead(code):
    tries = 10
    while tries > 0:
        code_guess = (random.randint(0, 6), random.randint(0, 6), random.randint(0, 6), random.randint(0, 6))
        if code_guess == code:
            print("You lost!")
            break
        else:
            player_feedback(code_guess)
            tries -= 1
    print("You win!")

def game_style():
    print("Welcome to Mastermind")
    try:
        style = int(input("Type 1 to let the computer guess, type 2 to guess yourself"))
        if style == 1:
            difficulty = req_difficulty()
            code = req_code()[0, 1, 2, 3]
            if difficulty == 0:
                com_braindead(code)
            if difficulty == 1:
                print("still in development")
            if difficulty == 2:
                print("still in development")
        if style == 2:
            print("still in development")
    except:
        print("Something went wrong.")

game_style()
