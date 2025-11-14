import re
fhand =open('randg.txt')

for line in fhand:
    line = line.rstrip()
    phone = re.findall('\\+60[0-9]+',line)

    if (len(phone) != 0):
        print(phone)
   # print(phone)
