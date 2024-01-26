import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from school_timetable.models import Subject, Teacher, Class, Student

class SchoolInterface(QWidget):
    def __init__(self, subjects, teachers, classes, students):
        super().__init__()
        self.subjects = subjects
        self.teachers = teachers
        self.classes = classes
        self.students = students
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('School Timetable')
        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Subjects: {', '.join(subject.title for subject in self.subjects)}"))
        layout.addWidget(QLabel(f"Teachers: {', '.join(teacher.name for teacher in self.teachers)}"))
        layout.addWidget(QLabel(f"Classes: {', '.join(class_.title for class_ in self.classes)}"))
        layout.addWidget(QLabel(f"Students: {', '.join(student.name for student in self.students)}"))

        self.setLayout(layout)

def run_interface():
    app = QApplication(sys.argv)

    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    classes = Class.objects.all()
    students = Student.objects.all()

    school_interface = SchoolInterface(subjects, teachers, classes, students)
    school_interface.show()
    sys.exit(app.exec())