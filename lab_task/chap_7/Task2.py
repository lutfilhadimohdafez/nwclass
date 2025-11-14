# Program to put new name included with error handling and list number recognition

# Function to get the next list number by reading an existing list of lines
def get_next_number(lines):
    if not lines:
        return 1
    
    last_line = lines[-1].strip()
    try:
        # Assumes the format is "Number) Name"
        current_number_str = last_line.split(')')[0]
        current_number = int(current_number_str)
        return current_number + 1
    except (IndexError, ValueError):
        return 1

# Error Handling and Initial File Reading
fileName = "namelist.txt"
inputerrnum = 0
file_lines = []
fileHandler = None

while inputerrnum < 3:
    try:
        # Open in 'r' mode to read all existing content first
        with open(fileName, "r") as f_read:
            file_lines = f_read.readlines()
        
        # Get the starting number for the new entries
        starting_number = get_next_number(file_lines)
        
        # Now open in 'a' (append) mode for writing
        fileHandler = open(fileName, "a")
        break
    except FileNotFoundError:
        # If the file doesn't exist, start number is 1. Open in 'w' (write) mode to create it.
        starting_number = 1
        fileHandler = open(fileName, "w")
        break
    except Exception:
        inputerrnum += 1
else:
    print("Too many wrongs. Exiting.. ")
    exit()

# Looping for input
userAddmore = "Y"
current_number = starting_number
while userAddmore.upper() == "Y":
    new_name = input("Enter new name: ")
    
    # Write the new line to the file
    line_to_write = f"{current_number})\t{new_name}\n"
    fileHandler.write(line_to_write)
    
    current_number += 1
    userAddmore = input("Do you want to continue?(Y/n) : ").strip()

# Close the file
if fileHandler:
    fileHandler.close()
