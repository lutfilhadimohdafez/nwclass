
# Task 1 Chap 4

# Rewrite previous pay computation. Use functions instead

# Create functions for normal or overtime


#Formula is
#IF total working hours is more than 40, the balance after the 40 must multiply by 10  because its OT
#BUT IF total working hours <= 40 then rate is 5

# Below is function def

def pay_salary(employee_hours):
    #print(f"\nYour working hours are {employee_hours}")
    if employee_hours <=40:
        pay_normal(employee_hours)
    elif employee_hours >= 40 and employee_hours <100:
        pay_overtime(employee_hours)
    else:
        print("\nAre you a robot lol")

# Below sub functions

# global variable


def pay_normal(x):
    z = x * 5
    print(f"You get normal pay!\nYour pay is: {z}")

def pay_overtime(y):
    overtime = y-40
    overtime_salary = overtime * 10
    normal_rate = 200
    z = normal_rate + overtime_salary
    print(f"You get extra overtime pay!\nYour pay is: {z}")
    

# Main Program Below

try:
    employee_hours = float(input("\nEnter Hours:"))
    #print(type(employee_hours))

    # Below function
    pay_salary(employee_hours)




except:
    print("\n Input Error. ")
