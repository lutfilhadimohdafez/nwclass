fileHandler = open("f.txt","r")
#print(fileHandler.read())
for line in fileHandler:
    if line.startswith("From"):
        line = line.rstrip()
        #print(line)
        linesplit= line.split()
        print(linesplit[1])

