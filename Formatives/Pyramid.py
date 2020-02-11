pyrsize = input("(while)Hoe groot? ")
x = 1

while True:
    print(x * "*")
    x = x + 1
    if x == int(pyrsize):
        while True:
            print(x * "*")
            x = x - 1
            if x == 0:
                break
    if x == 0:
        break

pyrsize2 = input("(for)Hoe groot? ")

for i in range(1, int(pyrsize2)):
    print(i*"*")
for i in range(int(pyrsize2), 0, -1):
    print(i*"*")
