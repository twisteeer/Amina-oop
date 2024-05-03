class Course:
    def __init__(self, id, name, instructor=None):
        self.__id = id
        self.__name = name
        self.__instructor = instructor
        self.__students = []

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_instructor(self):
        return self.__instructor

    def set_instructor(self, instructor):
        self.__instructor = instructor

    def get_students(self):
        return self.__students

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
        else:
            print(f"Student {student.get_name()} not found in course {self.__name}.")

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Instructor: {self.__instructor.get_name() if self.__instructor else 'None'}, Students: {[student.get_name() for student in self.__students]}"
