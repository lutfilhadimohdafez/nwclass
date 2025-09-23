# Task 2 
# write program to chose upper case or lower case

user_input = str(input("Please enter your String: "))
user_choice = int(input("Please choose the following option: \n1) Upper Case\n2) Lower Case\nChoice: "))

if user_choice == 1:
    new_string = user_input.upper()
elif user_choice ==2:
    new_string = user_input.lower()
else:
    print("wrong input")

print(new_string)
