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

# Defining functions

# maleList() function , to read the male list names
def maleList():
    print("List of Male Students")
    # Establih list of male students
    maleLines = []
    counter = 1
    # Looping to readline
    for line in fileHandler:
        line = line.rstrip()
        splitted_line = line.split(',')
        # 10/15/2025 : Urh tak lutfil kalau tak bagi complicated lagi -Lutfil
        if 'student' in splitted_line:
            name_sub_split = splitted_line[0].split()
            if 'bin' in name_sub_split or 'a/l' in name_sub_split:
                # Uncomment below to enable sub processing
                #maleLines.append(splitted_line)

                # Uncomment below to add line to list
                #maleLines.append(line)
                
                # Uncoment below to debug list
                #print(maleLines)

                print(counter,line)
                counter += 1
    #count = 1
    #print(maleLines)
    #for maleStudents in maleLines:
     #   print(f"{count}. {maleStudents}")
      #  count+=1
    #male_Lines = fileHandler.read()
    #print(male_Lines)
    #for lines in male_Lines:
     #   print(lines)

# exit function
def progExit():
    print("Confirm exit ?(Y/n):")
    userExitChoice= str(input())
    if userExitChoice != 'Y':
        return 'y'
    else:
        return 'n'


# Looping for menu
menu_options = 'y'
while menu_options == 'y':
    print("Data Extractor")
    print("1. List of Male Students")
    print("2. List of Female Students")
    print("3. Total number of students and TTO in the list")
    print("4. List of students email address")
    print("5. Exit")
    menu_choice = int(input("Please enter choice:"))
    if menu_choice == 1:
        print("1")
        maleList()
    elif menu_choice == 2:
        print("2")
    elif menu_choice == 3:
        print("3")
    elif menu_choice == 4:
        print("4")
    elif menu_choice == 5:
        print("To the exit menu..")
        menu_options = progExit()

    else:
        print("wrong input")

# Jap nak kena buat function dekat atas



