

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def average_score(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating



    def add_courses(self, course_name):
        self.finished_courses.append( course_name )



    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя:{self.name}\n" f"Фамилия:{self.surname}\n" f"Средняя оценка за домашние задания:{self.average_score()}\n" f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n" f"Завершенные курсы: {self.finished_courses}"


some_student = Student("Ruoy", "Eman", 19)
some_student.finished_courses = "Введение в программирование"
some_student.courses_in_progress = [" Python", " Git"]


def __lt__(self, other):
    if not isinstance(other, Student):
        print("Преподователей и студентов между собой не сравнивают!")
        return
    return self.average_score() < other.average_score()


print(some_student)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):

    def average_score(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum( course )
            len_rating += len( course )
        average_rating = round( sum_rating / len_rating, 2 )
        return average_rating

    def __str__(self):
        self.grades = {}
        return f"Имя:{self.name}\n" f"Фамилия:{self.surname}\n" f"Средняя оценка за лекции:{self.average_score()}\n"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.average_score() < other.average_score()


some_lecturer = Lecturer("Some", "Buddy",)
print(some_lecturer)


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя:{self.name}\n" f"Фамилия:{self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

some_reviewer = Reviewer("Some", "Buddy")

print(some_reviewer)



student_1 = Student('Мария', 'Сергеевна', 'Ж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в програмирование"]

student_2 = Student('Петр', 'Владимирович', 'М')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Введение в програмирование"]

lecturer_1 = Lecturer('Олег', 'Иванович')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Сергей', 'Кузнецов')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Антон', 'Михайлович')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Ольга', 'Дмитриевна')
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)

student_1.rate_lw(lecturer_1, 'Python', 2)
student_1.rate_lw(lecturer_1, 'Python', 7)
student_1.rate_lw(lecturer_1, 'Python', 10)

student_2.rate_lw(lecturer_2, 'Python', 10)
student_2.rate_lw(lecturer_2, 'Python', 8)
student_2.rate_lw(lecturer_2, 'Python', 7)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer( 'Some', 'Buddy' )
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw( best_student, 'Python', 10 )
cool_reviewer.rate_hw( best_student, 'Python', 10 )
cool_reviewer.rate_hw( best_student, 'Python', 10 )


def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating

def average_rating_for_course(course, lecturer_list):
    sum_rating = 0
    quantity_rating = 0
    for lect in lecturer_list:
        for course in lect.grades:
            lect_sum_rating = lect.av_rating_for_course(course)
            sum_rating += lect_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating
