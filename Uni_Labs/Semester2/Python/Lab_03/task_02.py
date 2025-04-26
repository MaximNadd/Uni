class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def list_students(self):
        for student in self.students:   
            print(f"Имя: {student.name}, Возраст: {student.age}")


# Создание преподавателя
teacher = Teacher("Алексей Сергеевич", 45, "Математика")

# Создание студентов
s1 = Person("Иван Иванов", "S001")
s2 = Person("Ольга Петрова", "S002")

# Добавление студентов
teacher.add_student(s1)
teacher.add_student(s2)

# Вывод списка
teacher.list_students()

print("----------------------------")

# Удаление студента
teacher.remove_student(s1)

# Список после удаления
teacher.list_students()


