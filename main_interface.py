import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from creation_interface import CreationWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setMinimumSize(500, 500)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.create_subject_button = QPushButton('Create Subject')
        self.create_subject_button.clicked.connect(self.create_subject)

        self.create_teacher_button = QPushButton('Create Teacher')
        self.create_teacher_button.clicked.connect(self.create_teacher)

        self.create_class_button = QPushButton('Create Class')
        self.create_class_button.clicked.connect(self.create_class)

        self.create_student_button = QPushButton('Create Student')
        self.create_student_button.clicked.connect(self.create_student)

        self.layout.addWidget(self.create_subject_button)
        self.layout.addWidget(self.create_teacher_button)
        self.layout.addWidget(self.create_class_button)
        self.layout.addWidget(self.create_student_button)

    def create_subject(self):
        self.creation_window = CreationWindow('Subject')
        self.creation_window.show()

    def create_teacher(self):
        self.creation_window = CreationWindow('Teacher')
        self.creation_window.show()

    def create_class(self):
        self.creation_window = CreationWindow('Class')
        self.creation_window.show()

    def create_student(self):
        self.creation_window = CreationWindow('Student')
        self.creation_window.show()

def run_interface():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())