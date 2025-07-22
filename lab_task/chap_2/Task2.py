#Task 2
#Program to prompt user for hours and rate per hour to compute
#gross pay

#Formula is pay = hours * rate


#User Input
employee_hours = float(input("\nEnter hours:"))
employee_rate = float(input("Enter rate:"))

#calculating the gross pay
employee_gross_pay = employee_hours * employee_rate

#printing
print("Your Pay is :"+ str(employee_gross_pay))


