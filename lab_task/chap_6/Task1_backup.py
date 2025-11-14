# Task 1
# find gpa

msg = "Average_GPA_NetworkSecurity :   3.18"
colon_position = msg.find(':')
print(colon_position)

space_position = msg.find(' ' ,colon_position)
print(space_position)

avg_pointer = msg[space_position+1:40]
print(avg_pointer)

cleaned_avg = avg_pointer.strip()
print(cleaned_avg)
