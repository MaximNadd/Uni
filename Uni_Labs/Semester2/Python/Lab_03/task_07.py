from task_05 import Student
from task_02 import Teacher

class Assistant(Student, Teacher):
    def __init__(self, name, student_id, subject, age):
        Student.__init__(self, name, student_id)  
        Teacher.__init__(self, name, age, subject)        

    def help_student(self):
        print(f"Assistant {self.name} is helping students with {self.subject}.")


assistant = Assistant("Maxim", "S001", 21, "Математика")
assistant.help_student()