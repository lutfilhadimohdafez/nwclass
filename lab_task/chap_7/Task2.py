

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
    namesNumber =fileHandler.readline()
    print(namesNumber)
    fileHandler.write(namesNumber+"\051" + new_name + "\n")
    userAddmore = str(input("Do you want to continue?(Y/n) : "))

def checklastline(f):
    for line in f:
        pass
    last_line = line
    return find("\051")


# Close file
fileHandler.close()
