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
#file_error_int = 0
#while file_error_int < 3:
 #   try:
  #      filename =str(input("Please enter file name:"))
  #      with open(filename,"r+") as fileHandler:
  #          break
   # except:
   #     print("File name error. Try again."+str(file_error_int+1)+"/3")
    #    file_error_int = file_error_int + 1

# Exit if 3 times file error
#if file_error_int ==3:
 #   print("Too many wrong filename. Exiting..")
  #  exit()

# Defining functions

# maleList() function , to read the male list names
def maleList(filename):
    print("List of Male Students")
    with open(filename,'r+') as fileHandler:
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

# Female list function
def femaleList(filename):
    with open(filename,'r+') as fileHandler:
        counter = 1
        print("Female List")
        for line in fileHandler:
            line = line.rstrip()
            split_line = line.split(',')
            if 'student' in split_line:
                sub_name_split = split_line[0].split()
                if 'binti' in sub_name_split or 'a/p' in sub_name_split:
                    print(counter,line)
                    counter +=1

# Total number of students and TT
def numStuTTO(filename):
    with open(filename,'r+') as fileHandler:
        counter = 1
        totalNo = {}
        for line in fileHandler:
            line = line.rstrip()
            stripped_line = line.split(',')
        #print(stripped_line[-1])
            if 'role' in stripped_line[-1]:
                continue
            elif stripped_line[-1] not in totalNo:
                totalNo[stripped_line[-1]]= 1
            else:
                totalNo[stripped_line[-1]]= totalNo[stripped_line[-1]] + 1
        for key,val in totalNo.items():
            print(f"{key}\t: {val}")
            
        
# List for students email address
def emailList(filename):
    with open(filename,'r+') as fileHandler:
        print("==== Students Email Addresses ====")
        for line in fileHandler:
            line = line.rstrip()
        #stripped_line = line.split(',')
            if '@student.gmi.edu.my' in line:
                splittedLine = line.split(',')
                print(splittedLine[2])


# exit function
def progExit():
    print("Confirm exit ?(Y/n):")
    userExitChoice= str(input())
    if userExitChoice != 'Y':
        return 'y'
    else:
        return 'n'

# Since theres an error in file IO nak loop due to filehandling ,I am proposing to do
# function for below
# so it will run via the with open() block
# Looping for menu
def dataExtractorMenu(filename):
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
            print("==== Male List ====")
            maleList(filename)
        elif menu_choice == 2:
            print("==== Female List ====")
            femaleList(filename)
        elif menu_choice == 3:
            print("==== Total number of Students and TTO ====")
            numStuTTO(filename)
        elif menu_choice == 4:
            print("==== Students Email List ====")
            emailList(filename)
        elif menu_choice == 5:
            print("To the exit menu..")
            menu_options = progExit()
            return menu_options
        else:
            print("wrong input")
    

# Jap nak kena buat function dekat atas for the sub functions
# Below to make it as a function to be called in main.py
def DataExtractor():
    file_error_int = 0
    while file_error_int <= 3:
        try:
            filename = str(input("Please enter file name:"))
            with open(filename,"r+") as checkFile:
                pass
                dataExtractorMenu(filename)
            # Break the code
                break
            #finish_operations = dataExtractorMenu()
            #if finish_operations =='y':
            #    break
        except:
            print("File name error. Try again."+str(file_error_int+1)+"/3")
            if file_error_int == 3:
                print("Too many wrong filename. Exiting ..")
                exit()
            else:
                file_error_int += 1
