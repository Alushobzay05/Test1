class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number
    
    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, CID Number: {self.cid_number}"

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa
    
    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def write_exam(self):
        print(f"{self.name} is writing an exam.")
    
    def get_student_details(self):
        details = self.get_details()
        return f"{details}, Student ID: {self.student_id}, Course: {self.course}, Year: {self.year}, GPA: {self.gpa}"

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    
    def grade_students(self):
        print(f"{self.name} is grading students.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")
    
    def get_teacher_details(self):
        details = self.get_details()
        return f"{details}, Subject: {self.subject}, Salary: {self.salary}, Department: {self.department}, Designation: {self.designation}"

# Creating objects of Student and Teacher classes
student = Student("Kinga", 22, "11106003781", "02030232", "Instrumentation and Control", 2, 3.8)
teacher = Teacher("Mrs. Sonam Yangchen", 25, "11504002303", "ICT", 62000, "Computer Department", "Professor")

# Displaying the details
print(student.get_student_details())
print(teacher.get_teacher_details())

# Demonstrating behaviors
student.walk()
student.talk()
student.eat()
student.sleep()
student.study()
student.attend_class()
student.write_exam()

teacher.walk()
teacher.talk()
teacher.eat()
teacher.sleep()
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()
