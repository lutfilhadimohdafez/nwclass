# Task 3 Chapter 4
# Create all numeric operator functions
# Operator controller function
def ControlTheFunc():
    user_input = input("Enter number split by space: ")
    user_operator = str(input("\nEnter operator: "))
    number_strings = user_input.split()
    numbers_to_use = []
    for num in number_strings:
        #convert each to int
        integer_num = int(num)
        #then add to numbers_to_add list
        numbers_to_use.append(integer_num)

    return numbers_to_use,user_operator
# Operator functions
def operator_exec(operator,*numbers_to_use):
    if operator == "+":
        return Add(*numbers_to_use)
    elif operator == "-":
        return Minus(*numbers_to_use)
    elif operator == "*":
        return Multiply(*numbers_to_use)
    elif operator == "/":
        return Divide(*numbers_to_use)
    else:
        print("Wrong operator input, just use + , - , * , /")

# Operator operator's function
def Add(*args):
    return sum(*args)
def Minus(*args):
    totalMinus = 0
    numberArray = args[0]
    for number in numberArray:
        totalMinus = totalMinus-number
        print(totalMinus)
    return totalMinus
def Multiply(*args):
    cart = 1
    totalMultiply = args[0]
    for number in totalMultiply:
        cart = number * cart
    return cart

def Divide(*args):
    totalDivide = args[0]
    result = args[0][0]
    for number in totalDivide[1:]:
        result = result/number
        print(result)
    return result
        


# Main function below
cont = 'n'
while cont != 'y':
    *number_list, user_operator = ControlTheFunc()
    print(f"User asked for {user_operator}")
    user_answer = operator_exec(user_operator,*number_list)
    print(f"Answer: {user_answer}")
    print("\n")
    cont = str(input("Exit?(y/n): "))
