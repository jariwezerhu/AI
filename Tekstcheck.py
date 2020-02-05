string1 = input("Geef een string: ")
string2 = input("Geef een string: ")

def difference(string1, string2):
    lettercheck = 0
    if string1 == string2:
        print("Er is geen verschil")
    else:
        for i in string1:
            if i == string2[lettercheck]:
                lettercheck = lettercheck + 1
            else:
                print("Het eerste verschil zit op index:", lettercheck)
                break

difference(string1, string2)
