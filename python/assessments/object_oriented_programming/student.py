# https://www.programmingexpert.io/object-oriented-programming/assessment/2

class Student:
    all_students = []

    @classmethod
    def get_average_grade(cls):
        if len(cls.all_students) == 0:
            return -1
        
        grade_total = 0
        for student in cls.all_students:
            grade_total += student._grade

        return grade_total / len(cls.all_students)

    @classmethod
    def get_best_student(cls):
        best_student = None
        best_grade = 0

        for student in cls.all_students:
            if student._grade >= best_grade:
                best_student = student
                best_grade = student._grade
        
        return best_student


    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        else:
            self._grade = grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1
        
        grades = 0
        nb_students = 0
        for student in students:
            grades += student._grade
            nb_students += 1

        return grades / nb_students