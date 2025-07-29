#Task 2
#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully


#Formula is
#IF total working hours is more than 40, the balance after the 40 must multiply by 10  because its OT
#BUT IF total working hours <= 40 then rate is 5


#User Input
#employee_hours = float(input("\nEnter hours:"))
#normal_rate = 5
#ot_rate =10

#calculating the gross pay
#employee_gross_pay = employee_hours * employee_rate


#error handling

try:
    employee_hours = float(input("\nEnter hours:"))
    normal_rate = 5
    ot_rate = 10

    #conditional statements
    if employee_hours <= 40:
        pay = normal_rate *employee_hours
        print(f"Your pay is {pay}")
    else:
        pay = normal_rate * 40 + (employee_hours-40)*10
        print("You get extra overtime pay!")
        print(f"Your pay is {pay} ")
except:
    print("\nERROR! Please enter numbers only!")
