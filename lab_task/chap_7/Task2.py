# Program to put new name included with erorr handling and list number recognition



# Defining functions to check for the numbers
def checklastline(filehandlername):
    for line in filehandlername:
        pass
    last_line = line
    return last_line


# Error Handling
inputerrnum= 0
while inputerrnum < 3:
    try:
        fileName = "namelist.txt"
        #fileName = str(input("Please enter file name : "))
        fileHandler = open(fileName,"a+")
        break
    except:
        print("Input error! ")
        inputerrnum += 1
    else:
        print("Too many wrongs. Exiting.. ")
        exit()

# Looping for input
userAddmore = "Y"
while userAddmore == "Y":
    new_name = str(input("Enter new name: "))
    namesNumber = fileHandler.readline()
    print(namesNumber)
    lastline = checklastline(fileHandler)
    print(last_line)
    fileHandler.write(namesNumber+"\051" + new_name + "\n")
    userAddmore = str(input("Do you want to continue?(Y/n) : "))
#close
fileHandler.close()
