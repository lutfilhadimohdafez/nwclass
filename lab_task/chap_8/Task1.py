#Python lab task number 8

# Error Handling
file_error_int = 0
while file_error_int <3:
    try:
        filename = str(input("Please enter your file name:"))
        fileHandler = open(filename,"r+")
        break
    except:
        print("File name error . Try again. ")
        file_error_int += 1

# Exit if 3 times error
if file_error_int == 3:
    exit()

# Variable init
malestudents = 0
femalestudents = 0


# The loop to check exact
# List init



# The loop to check total male or female
for line in fileHandler:
    if "BINTI" in line:
        femalestudents += 1
    elif "BIN" in line:
        malestudents +=1
    else:
        pass

# Printing how many 
print(f"\nMale :{malestudents}\nFemale :{femalestudents}")

# Close file
fileHandler.close()
