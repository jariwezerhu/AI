def mean(l):
    x = 0
    y = 0
    for i in l:
        x = x + i
        y = y + 1
    return (x / y)

lijst = [0, 4, 3, 1, 5, 3, 2]
lijst2 = [3, 2, 5, 4, 6, 13, 4]
lijst3 = [2, 43, 12, 45, 21, 12, 3]
print(mean(lijst))

def meanlists(*l):
    total = 0
    count = 0
    for i in l:
        total = total + mean(i)
        count = count + 1
    totalmean = total / count
    return totalmean

print(meanlists(lijst, lijst2, lijst3))
