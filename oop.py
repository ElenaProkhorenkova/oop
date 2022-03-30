class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_list = []

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        for course in self.grades:
            for grade in self.grades[course]:
                self.grade_list += [grade]
            if len(self.grade_list) == 0:
                average_grade = 0
            else:
                average_grade = sum(self.grade_list) / len(self.grade_list)
            return average_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'\
               f'Курсы в процессе изучения: {self.courses_in_progress}\n'\
               f'Завершенные курсы: {self.finished_courses}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    grades = {}
    grade_list = []

    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.surname}\nСредняя оценка за лекции: {self.lect_average_grade()}\n'

    def lect_average_grade(self):
        for course in self.grades:
            for grade in self.grades[course]:
                self.grade_list += [grade]
            if len(self.grade_list) == 0:
                average_grade = 0
            else:
                average_grade = sum(self.grade_list) / len(self.grade_list)
            return average_grade


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_rev = Reviewer('Some', 'Buddy')
cool_rev.courses_attached += ['Python', 'Git']
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']
cool_lect = Lecturer('Jake', 'Smith')
cool_lect.courses_attached += ['Python', 'Git']

best_student.rate_lect(cool_lect, 'Git', 9)
best_student.rate_lect(cool_lect, 'Git', 8)

cool_rev.rate_hw(best_student, 'Python', 10)
cool_rev.rate_hw(best_student, 'Python', 10)
cool_rev.rate_hw(best_student, 'Python', 10)

print(best_student)
