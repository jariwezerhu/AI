# here will be the code for generating codes etc.

import random

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
