# Дополнительная задача 2: "Генератор отчётов"
# Описание задачи:
# У вас есть файл students.csv, который содержит данные о студентах в формате CSV:

# Имя,Возраст,Средний балл
# Иван,20,4.5
# Мария,21,4.8
# Петр,19,3.9

# Задание:

# Напишите программу, которая:

# - Читает данные из файла students.csv.

# - Используя модуль csv, преобразует данные в список словарей.

# Создаёт модуль student_utils.py, который содержит функции:

# - get_top_students(students, n) — возвращает список из n студентов с наивысшим средним баллом.

# - get_average_age(students) — возвращает средний возраст студентов.

# - filter_students_by_grade(students, min_grade) — возвращает список студентов, у которых средний балл выше min_grade.

# - Используя лямбда-функции, отсортируйте студентов по возрасту и выведите результат.

# - Сохраните результаты в файл report.txt.


import csv
from student_utils import get_top_students, get_average_age, filter_students_by_grade

students = []
with open('./additional_task/additional_task_2/students.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        student = {
            'name': row['Имя'],
            'age': int(row['Возраст']),
            'average_grade': float(row['Средний балл'])
        }
        students.append(student)


top_students = get_top_students(students, 5)
average_age = get_average_age(students)
filtered_students = filter_students_by_grade(students, 4.0)
sorted_by_age = sorted(students, key=lambda x: x['age'])


with open('./additional_task/additional_task_2/report.txt', mode='w', encoding='utf-8') as file:
    file.write("Топ 5 студентов с наивысшим средним баллом:\n")
    for student in top_students:
        file.write(f"{student['name']}\n")
    
    file.write(f"\nСредний возраст студентов: {average_age}\n")

    file.write("\nСтуденты с минимальным баллом выше 4.0:\n")
    for student in filtered_students:
        file.write(f"{student['name']}\n")
    
    file.write("\nСтуденты, отсортированные по возрасту:\n")
    for student in sorted_by_age:
        file.write(f"{student['name']}\n")

