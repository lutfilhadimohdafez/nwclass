# Made by Lutfil CBS5 CBS24070032

# Data Extractor Program

# Requirements
# -Accept a file from user (need to create data)
# -LIST OF OPTIONS BELOW:
# 1) List of Male Students
# 2) List of Female Students
# 3) Total number of students in the list, and the total number 
#	of TTO in the list
# 4) List of students email address.

# <------PROGRAM STARTS BELOW ------->

# File, Error Handling
file_error_int = 0
while file_error_int < 3:
    try:
        filename =str(input("Please enter file name:"))
        fileHandler= open(filename,"r+")
        break
    except:
        print("File name error. Try again."+str(file_error_int+1)+"/3")
        file_error_int = file_error_int + 1

# Exit if 3 times file error
if file_error_int ==3:
    print("Too many wrong filename. Exiting..")
    exit()

menu_options = 'y'
while menu_options == 'y':
    print("Data Extractor")
    print("1. List of Male Students")
    print("2. List of Female Students")
    print("3. Total number of students in the list and total number of TTO in the list")
    print("4. List of students email address")
    menu_choice = int(input("Please enter choice:"))
