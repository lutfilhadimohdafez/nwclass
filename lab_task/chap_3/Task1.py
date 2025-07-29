#Task 2
#Program to prompt user for hours and rate per hour to compute
#gross pay

#Formula is pay = hours * rate



#Formula is
#IF total working hours is more than 40, the balance after the 40 must multiply by 10  because its OT
#BUT IF total working hours <= 40 then rate is 5


#1)	Rewrite your previous pay computation program to give the employee for normal time working is 5 and for overtime is 10 for hourly rate for hours worked above 40 hours.


#User Input
employee_hours = float(input("\nEnter hours:"))
normal_rate = 5
ot_rate =10

#calculating the gross pay
#employee_gross_pay = employee_hours * employee_rate

#conditional statements
if employee_hours <= 40:
    pay = normal_rate *employee_hours
    print(f"Your pay is {pay}")
else:
    pay = normal_rate * 40 + (employee_hours-40)*10
    print("You get extra overtime pay!")
    print(f"Your pay is {pay} ")
#printing
#print("Your Pay is :"+ str(employee_gross_pay))


