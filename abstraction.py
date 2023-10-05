from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, title, duration, price, instructor):
        self.title = title
        self.duration = duration
        self.price = price
        self.instructor = instructor
        self.enrolled_students = []

    @abstractmethod
    def get_details(self):
        pass

    def enroll(self, student):
        self.enrolled_students.append(student)

class ProgrammingCourse(Course):
    def __init__(self, title, duration, price, instructor, progLang):
        super().__init__(title, duration, price, instructor)
        self.progLang = progLang

    def get_details(self):
        return f"\n\nProgramming Course: {self.title}\nDuration: {self.duration} weeks\nPrice: ${self.price}\nInstructor: {self.instructor}\nProgramming Language: {self.progLang}"

class MathCourse(Course):
    def __init__(self, title, duration, price, instructor, level):
        super().__init__(title, duration, price, instructor)
        self.level = level

    def get_details(self):
        return f"\n\nMath Course: {self.title}\nDuration: {self.duration} weeks\nPrice: ${self.price}\nInstructor: {self.instructor}\nLevel: {self.level}"

class LanguageCourse(Course):
    def __init__(self, title, duration, price, instructor, language):
        super().__init__(title, duration, price, instructor)
        self.language = language

    def get_details(self):
        return f"\n\nLanguage Course: {self.title}\nDuration: {self.duration} weeks\nPrice: ${self.price}\nInstructor: {self.instructor}\nLanguage: {self.language}"


progCource = ProgrammingCourse("Python Programming", 8, 199, "Sandip Kankhare", "Python")
math_course = MathCourse("Calculus I", 12, 149, "Gopal Patil", "Intermediate")
language_course = LanguageCourse("German for Beginners", 6, 99, "Piyush Nichave", "German")

print(progCource.get_details())
print(math_course.get_details())
print(language_course.get_details())

student1 = "Emma Johnson"
progCource.enroll(student1)
print(f"\n{student1} has enrolled in {progCource.title}")
