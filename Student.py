from Person import Person
from Course import Course
class Student(Person):
    def __init__(self, id, name, age, courses=None, email=None, graduate_year=None, balance=0.0):
        super().__init__(id, name, age, courses=[], email=email)
        self.__graduate_year = graduate_year
        self.__balance = balance

    def get_graduate_year(self):
        return self.__graduate_year

    def set_graduate_year(self, graduate_year):
        self.__graduate_year = graduate_year

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def add_course(self, course:Course)->None:
        self._courses.append(course)

    def drop_course(self, course:Course):
        if course in self._courses:
            self._courses.remove(course)
        else:
            print(f"Course '{course}' not found.")

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Age: {self._age}, Courses: {[course.get_name() for course in self._courses]}, Email: {self._email}, Graduate Year: {self.__graduate_year}, Balance: {self.__balance}"
