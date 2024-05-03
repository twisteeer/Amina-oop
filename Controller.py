from Course import Course
from Instructor import Instructor
from Student import Student


class Controller:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__instructors = []
    #
    def add_student(self) -> None:
        print("Enter student details: ")
        try:
            id = int(input("Enter student ID: "))
            # while True:
            #     try:
            #         id = int(input("Enter student ID: "))
            #         break
            #     except ValueError:
            #         print("Invalid input. Please enter valid values.")
            name = input("Enter student name: ")
            while name.strip() == "":
                name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            email = input("Enter student email: ")
            while email.strip() == "":
                email = input("Enter student email: ")
            graduate_year = int(input("Enter student's graduation year: "))
            balance = float(input("Enter student's account balance: "))
            student = Student(id, name, age, email, graduate_year, balance)
            self.__students.append(student)
            print("Student added successfully")
        except ValueError:
            print("Invalid input. Please enter valid values.")
    #
    def add_course(self) -> None:
        print("Enter course details: ")
        try:
            id = int(input("Enter course ID: "))
            name = input("Enter course name: ")
            while name.strip() == "":
                name = input("Enter course name: ")
            course = Course(id, name)
            self.__courses.append(course)
            print("Course added successfully")
        except ValueError:
            print("Invalid input. Please enter valid values.")
    #
    def add_instructor(self) -> None:
        print("Enter instructor details: ")
        try:
            id = int(input("Enter instructor ID: "))
            name = input("Enter instructor name: ")
            while name.strip() == "":
                name = input("Enter instructor name: ")
            age = int(input("Enter instructor age: "))
            email = input("Enter instructor email: ")
            while email.strip() == "":
                email = input("Enter instructor email: ")
            degree = input("Enter instructor degree: ")
            while degree.strip() == "":
                degree = input("Enter instructor degree: ")
            salary = int(input("Enter instructor salary: "))
            instructor = Instructor(id,name,age,[],email)
            instructor.set_degree(degree)
            instructor.set_salary(salary)
            self.__instructors.append(instructor)
            print("Instructor added successfully")
        except ValueError:
            print("Invalid input. Please enter valid values.")
    #
    def show_instructors(self) -> None:
        for instructor in self.__instructors:
            print(instructor)
    def show_students(self) -> None:
        for student in self.__students:
            print(student)
    def show_courses(self) -> None:
        for course in self.__courses:
            print(course)
    def set_instructor(self, instructorId : int, courseId : Course) -> None:
        # Find course from list of courses
        course = next((c for c in self.__courses if c.get_id() == courseId), None)
        if course is None:
            print(f"Course with ID {courseId} not found.")
            return

        # Find instructor from list of instructors
        instructor = next((i for i in self.__instructors if i.get_id() == instructorId), None)
        if instructor is None:
            print(f"Instructor with ID {instructorId} not found.")
            return

        # Set course new instructor and add new course to instructor course list
        course.set_instructor(instructor)
        instructor.add_course(course)

    def register_student(self, studentId : int, courseId : int) -> None:
        # Find student from list of students
        student = next((s for s in self.__students if s.get_id() == studentId), None)
        if student is None:
            print(f"Student with ID {studentId} not found.")
            return
        # Find course from list of courses
        course = next((c for c in self.__courses if c.get_id() == courseId), None)
        if course is None:
            print(f"Course with ID {courseId} not found.")
            return
        course.add_student(student)
        student.add_course(course)

    def remove_student(self, studentId: int, courseId: int) -> None:
        # Find student from list of students
        student = next((s for s in self.__students if s.get_id() == studentId), None)
        if student is None:
            print(f"Student with ID {studentId} not found.")
            return

        # Find course from list of courses
        course = next((c for c in self.__courses if c.get_id() == courseId), None)
        if course is None:
            print(f"Course with ID {courseId} not found.")
            return

        course.remove_student(student)
        student.drop_course(course)


def display_menu():
    print("                                                ")
    print("---------------Student Controller---------------")
    print("1. Add Student / Course / Instructor")
    print("2. Register Course for instructors")
    print("3. Add / Drop Course for student")
    print("4. Show Students / Courses / Instructors")
    print("0. Exit")

def main():
    controller = Controller()

    while True:
        display_menu()
        try:
            num = int(input("Enter a number: "))
            if num == 1:
                while True:
                    word = input("Choose course / instructor / student / back :")
                    if (word == "course"):
                        controller.add_course()
                    elif (word == "instructor"):
                        controller.add_instructor()
                    elif (word == "student"):
                        controller.add_student()
                    elif (word == "back"):
                        break
                    else:
                        print("Invalid input. Please enter a valid word.")
            elif num == 2:
                while True:
                    try:
                        instructorId = int(input("Enter instructor ID: "))
                        courseId = int(input("Enter course ID: "))
                        controller.set_instructor(instructorId, courseId)

                        break
                    except ValueError:
                        print("Invalid input. Please enter valid values.")
            elif num == 3:
                while True:
                    word = input("Choose Add / Drop / back : ")
                    if (word == "add"):
                        studentID = int(input("Enter student ID: "))
                        courseID = int(input("Enter course ID: "))
                        controller.register_student(studentID, courseID)
                        print("Student successfully registered.")
                    elif (word == "drop"):
                        studentID = int(input("Enter student ID: "))
                        courseID = int(input("Enter course ID: "))
                        controller.remove_student(studentID, courseID)
                        print("Student successfully removed.")
                    elif (word == "back"):
                        break
                    else:
                        print("Invalid input. Please enter a valid word.")
            elif num == 4:
                while True:
                    word = input("Choose course / instructor / student / back : ")
                    if (word == "course"):
                        controller.show_courses()
                    elif (word == "instructor"):
                        controller.show_instructors()
                    elif (word == "student"):
                        controller.show_students()
                    elif (word == "back"):
                        break
                    else:
                        print("Invalid input. Please enter a valid word.")
            elif num == 0:
                break
        except ValueError:
            print("Invalid input. Please enter valid values.")
if __name__ == "__main__":
    main()