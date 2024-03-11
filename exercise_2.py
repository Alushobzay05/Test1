def initialize_system():
    global students_list, students_dict
    students_list = []
    students_dict = {}

def add_student():
    name = input("Enter the name of the student: ")
    age = int(input("Enter the age of the student: "))
    grade = input("Enter the grade of the student: ")
    students_list.append([name, age, grade])
    students_dict[name] = [age, grade]
    print("Student added successfully.")

def search_student():
    name = input("Enter the name of the student you want to search for: ")
    if name in students_dict:
        print(f"Name: {name}, Age: {students_dict[name][0]}, Grade: {students_dict[name][1]}")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter the name of the student you want to remove: ")
    if name in students_dict:
        students_list.remove([name, students_dict[name][0], students_dict[name][1]])
        del students_dict[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

def main():
    initialize_system()
    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            remove_student()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()