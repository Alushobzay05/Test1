num_students = int(input("Enter the number of students: "))
i = 1
while i <= num_students:
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subjects for students {i}: "))

    for j in range(1, num_subjects + 1) :
        grade = float(input(f"Enter subjects {j} grade for students {i}: "))
        total_grade += grade

    average_garde = total_grade / num_subjects
    print(f"average grade for students {i}: {average_garde:.2f}")
    i += 1
    