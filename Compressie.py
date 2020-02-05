def compressor(file):
    with open(file, 'r') as x:
        content = x.read()
    content = content.replace(" ", "")
    content = content.replace("\n", "")
    content = content.replace("\t", "")
    content = content.replace("\r", "")
    x = open(file, "w")
    x.write(content)
    x.close()
