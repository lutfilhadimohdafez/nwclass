# Task 1

# File name input
# fileName = str(input("Please enter your file name : "))

# Open file command
# fileHandler = open(fileName,"r")

# Error Handling
file_error_int = 0
while file_error_int < 3:
    try:
        fileName = str(input("Please enter your file name : "))
        fileHandler = open(fileName,"r")
        break
    except:
        print("File name error. Try again.")
        file_error_int += 1
# Exit if 3 times
if file_error_int == 3:
    exit()
# Variable init
fileLines = 0
# Loop
for line in fileHandler:
    fileLines += 1
    if line.startswith("From:"):
        print(str(fileLines) + "\t"+line.rstrip("\n"))
    #Below to print all lines number
    #else:
        #print(str(fileLines))
# Printing
print("Total lines: " + str(fileLines))
# Close file
fileHandler.close()
