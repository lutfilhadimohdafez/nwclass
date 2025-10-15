#if line starts with

fhand = open("words.txt","r")
for lines in fhand:
    if lines.startswith("sun"):
        print(lines)
