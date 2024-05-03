class Person:
    def __init__(self, id, name, age, courses=None, email=None):
        self._id = id
        self._name = name
        self._age = age
        self._courses = courses if courses is not None else []
        self._email = email if email is not None else ""

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_courses(self):
        return self._courses

    def set_courses(self, courses):
        self._courses = courses

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Age: {self._age}, Courses: {self._courses}, Email: {self._email}"
