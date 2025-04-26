class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        try:
            grade = float(grade)
            if 0 <= grade <= 10:
                self.grades.append(grade)
            else:
                print(f"Ошибка: оценка {grade} вне допустимого диапазона (0–10).")
        except:
            print(f"Ошибка: недопустимое значение оценки: {grade}")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print("Информация о студенте:")
        print(f"Имя: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")


student = Student("Maxim", "A001")
student.add_grade("8")
student.add_grade(9.5)
student.display_info()