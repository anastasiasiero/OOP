class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade_hw(self, grades):
        sum_of_grades = 0
        for key, value in self.grades:
            sum_of_grades += sum(self.grades.values()) / len(self.grades.values())
        return round(sum_of_grades / len(grades), 2)

    def __str__(self):
        info = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания:\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return info


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname, )
        self.grades = {}

    def __str__(self):
        info = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции:'
        return info


class Reviewer(Mentor):


    def __init__(self, name, surname,):
        super().__init__(name, surname,)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

    def avg_grade_hw(self, grades):
        sum_of_grades = 0
        for key, value in self.grades:
            sum_of_grades += sum(self.grades.values()) / len(self.grades.values())
        return round(sum_of_grades / len(grades), 2)


ivan_ivanov = Student('Иван', 'Иванов', 'мужчина')
ivan_ivanov.courses_in_progress += ['Python']
ivan_ivanov.courses_in_progress += ['Git']
ivan_ivanov.finished_courses += ['Введение в программирование']

nikita_nikitin = Student('Никита', 'Никитин', 'мужчина')
nikita_nikitin.courses_in_progress += ['Python']
nikita_nikitin.courses_in_progress += ['Git']
nikita_nikitin.finished_courses += ['Введение в программирование']

denis_denisov = Reviewer('Денис', 'Денисов')
denis_denisov.courses_attached += ['Python']

vasily_petrovich = Reviewer('Василий', 'Петрович')
vasily_petrovich.courses_attached += ['Git']

ruslan_ruslanovich = Lecturer('Руслан', 'Русланович')
ruslan_ruslanovich.courses_attached += ['Python']

olya_olegovna = Lecturer('Оля', 'Олеговна')
olya_olegovna.courses_attached += ['Git']

vasily_petrovich.rate_hw(ivan_ivanov, 'Git', 10)
denis_denisov.rate_hw(ivan_ivanov, 'Python', 9.5)
vasily_petrovich.rate_hw(nikita_nikitin, 'Git', 8)
denis_denisov.rate_hw(nikita_nikitin, 'Python', 9)

ivan_ivanov.rate_lecturer(ruslan_ruslanovich, 'Python', 8.5)
ivan_ivanov.rate_lecturer(olya_olegovna, 'Git', 10)
nikita_nikitin.rate_lecturer(ruslan_ruslanovich, 'Python', 9)
nikita_nikitin.rate_lecturer(olya_olegovna, 'Git', 10)

#print(ivan_ivanov)
# print(nikita_nikitin)
# print(vasily_petrovich)
# print(denis_denisov)
# print(ruslan_ruslanovich)
# print(olya_olegovna)

