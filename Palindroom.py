def palindromecheck(word):
    word = word.casefold()
    pali = True
    for i in range(0, len(word)):
        if word[i] != word[-1 - i]:
            pali = False
            break
    if pali:
        print("Het woord is een palindroom!")
    if not pali:
        print("Het woord is geen palindroom")

palindromecheck("racecar")
