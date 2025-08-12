# Task 2


# Variables
count = 0
total = 0
average =0

while True:
    number = input('Enter number:')

    if number == 'Finish' or number == 'finish':
        break

    try:
        checknumber = float(number)
    except:
        print('Invalid input, please enter number!')

    count+=1
    total+=checknumber

average = total/count

print("Count\t: " + str(count))
print("Total\t: " + str(total))
print("Average\t:" + str(average))
