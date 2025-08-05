# Task 2 Chapter 4

# Get functions to take input and display

# Function def

def info2():
    nama = str(input("\nEnter your name : "))
    umur = int(input("\nEnter your age : "))

    # Below return dictionary
    return {"nama": nama , "umur":umur}

# Function untuk display

def psps(hasil):
    nama = hasil["nama"]
    umur = hasil["umur"]
    print(f"\nYour name is {nama} and you are {umur} years old.")


#main function

hasil = info2()
psps(hasil)
