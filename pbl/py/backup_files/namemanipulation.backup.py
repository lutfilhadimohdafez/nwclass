def NameManipulation():
    name = input("Enter your name: ")

    while True:
        print("\n============== Name Manipulation ==============")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Add another name")
        print("4. Count total characters")
        print("5. Reverse your name")
        print("6. Back to main menu")
        print("===============================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Uppercase: {name.upper()}")
        elif choice == '2':
            print(f"Lowercase: {name.lower()}")
        elif choice == '3':
            extra = input("Enter another name to add: ")
            name = name + " " + extra
            print(f"Updated name: {name}")
        elif choice == '4':
            print(f"Total characters (including spaces): {len(name)}")
        elif choice == '5':
            print(f"Reversed name: {name[::-1]}")
        elif choice == '6':
            break
        else:
            print("Invalid choice!")
