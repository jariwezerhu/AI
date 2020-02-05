import random
while True:
    num = random.randint(0, 10)
    while True:
        try:
            guess = int(input("Try guessing the number between 0 and 10"))
            if guess == num:
                print("You got it!")
                break
            else:
                print("Try again!")
        except:
            print("Try a number between 0 and 10")
