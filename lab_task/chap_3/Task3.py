#Task3 chap_3


#grade list

grade_repeat = 2
grade_dean = 3.5
 
#error handling



try:
    student_name = str(input("Please enter your name:"))
    student_grade = float(input("\nPlease enter your CGPA:"))

    if student_grade < grade_repeat:
        print("You failed! Repeat!")
        
    elif student_grade >= grade_repeat and student_grade < grade_dean:
        print("You passed")

    else:
        print("Dean's List! Congrats!")

except:
    print("\nInput error!")
        

