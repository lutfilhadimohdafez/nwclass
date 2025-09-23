
# find gpa

msg = "Average_GPA_NetworkSecurity :   3.18"
colon_position = msg.find(':')
#print(colon_position)

final_msg = msg[colon_position+1:].strip()
print(final_msg)
