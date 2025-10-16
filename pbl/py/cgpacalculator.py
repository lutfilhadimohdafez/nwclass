def CGPACalculator():

    gpa_list = []

    total_semesters = int(input("How many semesters have you taken? "))

    for i in range(total_semesters):
        while True:
            try:
                gpa = float(input("Enter GPA for semester " + str(i + 1) + ": "))
                if 0.0 <= gpa <= 4.0:
                    gpa_list.append(gpa)
                    break
                else:
                    print("GPA must be between 0.0 and 4.0. Try again.")
            except ValueError:
                print("Please enter a number (example: 3.5).")

    def show_total_cgpa():
        total = sum(gpa_list) / len(gpa_list)
        print("Your current CGPA is:", round(total, 2))

    def show_total_semesters():
        print("You have studied", len(gpa_list), "semesters so far.")

    def next_gpa_for_3():
        current_cgpa = sum(gpa_list) / len(gpa_list)
        if current_cgpa >= 3.0:
            print("Wow! Your CGPA is already 3.0 or higher!")
        else:
            next_gpa = (3.0 * (len(gpa_list) + 1)) - sum(gpa_list)
            print("You need a GPA of", round(next_gpa, 2),
                  "next semester to reach 3.0 CGPA.")

    while True:
        print("\n========== CGPA Calculator ==========")
        print("1. Show total CGPA")
        print("2. Show total semesters")
        print("3. Calculate GPA needed for 3.0 CGPA")
        print("4. Back to main menu")
        print("=====================================")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_total_cgpa()
        elif choice == "2":
            show_total_semesters()
        elif choice == "3":
            next_gpa_for_3()
        elif choice == "4":
            print("Going back to main menu...")
            break
        else:
            print("Invalid choice, please try again.")
