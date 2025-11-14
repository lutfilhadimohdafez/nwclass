# Find the biggest number

numbers = [67,43,6,36,93,73]
biggest = numbers[0]

for items in numbers:
    if items > biggest:
        biggest = items

    else:
        continue

print(f"The biggest number is {biggest}")
