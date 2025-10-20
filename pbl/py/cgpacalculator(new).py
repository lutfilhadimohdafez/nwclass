def CGPACalculator():
    # Make a list to store all GPA values
    gpa_list = []

    print("Welcome to CGPA Calculator")
    print("You can enter as many GPA as you want.")
    print("Type 'finish' when you are done.\n")

    # Let the user enter GPA until they type finish
    while True:
        gpa_input = input("Enter GPA (or type 'finish'): ")

        if gpa_input.lower() == "finish":
            break  # stop asking for GPA

        # Try changing the input to a number
        try:
            gpa = float(gpa_input)
            # Check if GPA is between 0.0 and 4.0
            if gpa >= 0.0 and gpa <= 4.0:
                gpa_list.append(gpa)
            else:
                print("GPA must be between 0.0 and 4.0")
        except:
            print("Please enter a number (example: 3.5)")

    # If no GPA entered, go back
    if len(gpa_list) == 0:
        print("No GPA entered. Going back to main menu.")
        return

    # Function 1: Show total CGPA
    def show_total_cgpa():
        total = sum(gpa_list) / len(gpa_list)
        print("Your total CGPA is:", round(total, 2))

    # Function 2: Count total semesters
    def show_total_semesters():
        print("You have studied", len(gpa_list), "semesters.")

    # Function 3: Next GPA needed for 3.0
    def next_gpa_for_3():
        current_cgpa = sum(gpa_list) / len(gpa_list)
        if current_cgpa >= 3.0:
            print("Your CGPA is already 3.0 or higher.")
        else:
            next_gpa = (3.0 * (len(gpa_list) + 1)) - sum(gpa_list)
            if next_gpa > 4.0:
                print("Even if you get 4.0 next semester, you cannot reach 3.0 yet.")
            else:
                print("You need a GPA of", round(next_gpa, 2), "next semester to reach 3.0.")

    # The menu after entering all GPAs
    while True:
        print("\n===== CGPA Menu =====")
        print("1. Show total CGPA")
        print("2. Show total semesters")
        print("3. Calculate GPA needed for 3.0")
        print("4. Back to main menu")
        print("=====================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_total_cgpa()
        elif choice == "2":
            show_total_semesters()
        elif choice == "3":
            next_gpa_for_3()
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice, please try again.")
