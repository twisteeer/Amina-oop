from Person import Person

class Instructor(Person):
    def __init__(self, id, name, age, courses=None, email=None, degree=None, salary=0.0):
        super().__init__(id, name, age, courses, email)
        self.__degree = degree
        self.__salary = salary

    def get_degree(self):
        return self.__degree

    def set_degree(self, degree):
        self.__degree = degree

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def add_course(self, course):
        self._courses.append(course)

    def raise_salary(self, amount):
        self.__salary += amount

    def list_courses(self) -> str:
        res = ""
        for course in self._courses:
            res += f"{course.get_name()}, "
        return res[:-2]

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Age: {self._age}, Courses: {self.list_courses()}, Email: {self._email}, Degree: {self.__degree}, Salary: {self.__salary}"
