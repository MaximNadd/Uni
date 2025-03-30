def get_top_students(students, n):
    sorted_students = sorted(students, key=lambda x: x['average_grade'], reverse=True)
    return sorted_students[:n]

def get_average_age(students):
    total_age = sum(student['age'] for student in students)
    return total_age / len(students)

def filter_students_by_grade(students, min_grade):
    return [student for student in students if student['average_grade'] > min_grade]