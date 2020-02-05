def count(l, x):
    countx = 0
    for i in l:
        if i == x:
            countx = countx + 1
    return countx

def dif(l):
    maxdif = 0
    cnt = 0
    try:
        while True:
            diff = abs(l[cnt] - l[cnt + 1])
            if diff > maxdif:
                maxdif = diff
            cnt = cnt + 1
    except:
        pass
    return maxdif

def zeroone(l):
    zerocount = count(l, 0)
    onecount = count(l, 1)
    if int(zerocount) > 12:
        print("More than 12 zero's >:(")
    if zerocount > onecount:
        print("More zero's than ones >:(")
    else:
        print("Good job :)")

a1 = [0, 3, 1, 23, 6432, 12, 235, 3, 12, 32, 23, 12, 12]
a2 = [0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0]

print(count(a1, 12))
print(dif(a1))
zeroone(a2)
