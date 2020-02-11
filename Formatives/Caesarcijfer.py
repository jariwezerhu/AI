lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = str(input("Geef een tekst: "))
rotation = int(input("Geef een rotatie: "))

while True:
    if rotation > 26:
        rotation -= 26
    else:
        break

def caesarcipher(x):
    caesartext = str()
    for i in x:
        if i in lower:
            caesartext += lower[lower.find(i) + rotation]
            continue
        if i in upper:
            caesartext += upper[upper.find(i) + rotation]
            continue
        else:
            caesartext += i
            continue
    return caesartext

print(caesarcipher(text))
