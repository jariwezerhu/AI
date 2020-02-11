def cyc(ch, n):
    if n > 0:
        x = str()
        for i in range(n, len(ch)):
            x = x + ch[i]
        for i in range(0, n):
            x = x + ch[i]
        return x
    if n < 0:
        x = str()
        for i in range(n, len(ch) + n):
            x = x + ch[i]
        return x

print(cyc("1011100qwet154", 4))
