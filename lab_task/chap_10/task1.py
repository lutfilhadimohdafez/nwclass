# Python lab task number 10

# Error Handling


# Nvm just do the file thing
fileHandler = open("words.txt")

# VARIABLES
counts = dict()
for line in fileHandler:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst = list()
for key,val in counts.items():
    lst.append((val,key))
lst.sort(reverse=True)
for val,key in lst[:40]:
    print(key,val)
