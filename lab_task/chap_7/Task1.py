# Task 1

# OPen file
fileHandler = open("mbox-short.txt","r")

# Variable init
fileLines = 0

# Loop
for line in fileHandler:
    fileLines += 1
    if line.startswith("From:"):
        print(str(fileLines) + "\t"+line.rstrip("\n"))
    #else:
        #print(str(fileLines))

# Printing
print("Total lines: " + str(fileLines))


# Close file
fileHandler.close()
