def CGPACalculator():
    gpa_list = []

    def get_total_cgpa():
        if len(gpa_list) == 0:
            print("No GPA entered yet!")
        else:
            total_cgpa = sum(gpa_list) / len(gpa_list)
            print(f"Your current CGPA is: {total_cgpa:.2f}")

    def count_semesters():
        print(f"You have completed {len(gpa_list)} semester(s).")

    def next_gpa_for_3():
        if len(gpa_list) == 0:
            print("Please enter some GPA first.")
        else:
            current_cgpa = sum(gpa_list) / len(gpa_list)
            if current_cgpa >= 3.0:
                print("Your CGPA is already 3.0 or higher!")
            else:
                required_gpa = (3.0 * (len(gpa_list) + 1)) - sum(gpa_list)
                print(f"You need a GPA of {required_gpa:.2f} in your next semester to reach CGPA 3.0.")

    while True:
        print("\n============== CGPA Calculator ==============")
        print("1. Enter GPA")
        print("2. Get total CGPA")
        print("3. Count total semesters")
        print("4. Calculate next GPA for 3.0 CGPA")
        print("5. Back to main menu")
        print("=============================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                gpa = float(input("Enter GPA for this semester: "))
                if 0.0 <= gpa <= 4.0:
                    gpa_list.append(gpa)
                else:
                    print("Invalid GPA. Must be between 0.0 and 4.0.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            get_total_cgpa()
        elif choice == '3':
            count_semesters()
        elif choice == '4':
            next_gpa_for_3()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
