class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self): #returns a string representation of the object
        return f" Name: {self.name}, Age: {self.age}, Major: {self.major}"

class University:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        if isinstance(student, Student):    #checks if the student parameter is an instance of the "Student" class
            self.student_list.append(student)
            print(f"Added student: {student.name}")
        else:
            print("Invalid student object. Please provide a valid Student instance.")
    def display_students(self):
        print("List of the student in the university:")
        for student in self.student_list:   #Since we defined the __str__ method in the "Student" class, it will print the formatted student information
            print(student)

# Test the University class
if __name__ == "__main__":
    university = University()

    student1 = Student("Alice", 20, "Computer Science")
    student2 = Student("Bob", 22, "Mathematics")
    student3 = Student("Charlie", 21, "Physics")

    university.add_student(student1)
    university.add_student(student2)
    university.add_student(student3)

    university.display_students()