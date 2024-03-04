age = int(input("Enter your age: "))

is_student = input("Are you a student? (Yes/No): ")

if age <= 12 and is_student == "yes":
    print("You are eligible for a discount on ticket.")
elif age < 13 or age <= 18:
    print("You are eligible for a discount on ticket.")

elif age > 12 or (is_student == "no"):
    print("Sorry, you are not eligible for a discount on ticket.")
else :
    print("Entered input is invalid")