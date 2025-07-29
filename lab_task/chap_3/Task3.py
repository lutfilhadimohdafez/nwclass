#Task3 chap_3


#grade list

grade_min = 0
grade_repeat = 2
grade_dean = 3.5
grade_max =4.0
 
#error handling



try:
    student_name = str(input("Please enter your name:"))
    student_grade = float(input("\nPlease enter your CGPA:"))

    if student_grade < grade_repeat:
        print("You failed! Repeat!")
        
    elif student_grade >= grade_repeat and student_grade < grade_dean:
        print("You passed")

    elif student_grade >= grade_dean and student_grade <= grade_max:
        print("Dean's List! Congratx!")

    else:
        print("Grade must be more than 0 and less than 4!")

except:
    print("\nInput error!")
        

