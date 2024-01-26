import sys
from PyQt6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView
from creation_interface import CreationWindow
from update_interface import UpdaterWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setMinimumSize(500, 500)

        self.main_scene = QGraphicsScene()
        self.main_view = QGraphicsView(self.main_scene)

        self.create_button = QPushButton('Create')
        self.update_button = QPushButton('Update')
        self.get_button = QPushButton('Get')
        self.delete_button = QPushButton('Delete')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.main_view)
        self.main_layout.addWidget(self.create_button)
        self.main_layout.addWidget(self.update_button)
        self.main_layout.addWidget(self.get_button)
        self.main_layout.addWidget(self.delete_button)

        self.central_widget.setLayout(self.main_layout)

        self.create_button.clicked.connect(self.switch_to_create_scene)
        self.update_button.clicked.connect(self.switch_to_update_scene)
        self.get_button.clicked.connect(self.switch_to_get_scene)
        self.delete_button.clicked.connect(self.switch_to_delete_scene)
        
        self.populate_main_scene()

    def populate_main_scene(self):
        self.main_scene.clear()
        self.main_scene.addText("Press buttons below to interact with the database.")
    
    def switch_to_create_scene(self):
        self.main_scene.clear()
        self.create_subject_button = QPushButton('Create Subject')
        self.create_subject_button.clicked.connect(self.create_subject)

        self.create_teacher_button = QPushButton('Create Teacher')
        self.create_teacher_button.clicked.connect(self.create_teacher)

        self.create_class_button = QPushButton('Create Class')
        self.create_class_button.clicked.connect(self.create_class)

        self.create_student_button = QPushButton('Create Student')
        self.create_student_button.clicked.connect(self.create_student)

        self.create_layout = QVBoxLayout()

        self.create_layout.addWidget(self.create_subject_button)
        self.create_layout.addWidget(self.create_teacher_button)
        self.create_layout.addWidget(self.create_class_button)
        self.create_layout.addWidget(self.create_student_button)

        create_widget = QWidget()
        create_widget.setLayout(self.create_layout)

        create_scene = QGraphicsScene()
        create_scene.addWidget(create_widget)

        self.main_view.setScene(create_scene)

    def switch_to_update_scene(self):
        self.main_scene.clear()
        
        self.update_subject_button = QPushButton('Update Subject')
        self.update_subject_button.clicked.connect(self.update_subject)

        self.update_teacher_button = QPushButton('Update Teacher')
        self.update_teacher_button.clicked.connect(self.update_teacher)

        self.update_class_button = QPushButton('Update Class')
        self.update_class_button.clicked.connect(self.update_class)

        self.update_student_button = QPushButton('Update Student')
        self.update_student_button.clicked.connect(self.update_student)

        self.update_layout = QVBoxLayout()

        self.update_layout.addWidget(self.update_subject_button)
        self.update_layout.addWidget(self.update_teacher_button)
        self.update_layout.addWidget(self.update_class_button)
        self.update_layout.addWidget(self.update_student_button)
        
        update_widget = QWidget()
        update_widget.setLayout(self.update_layout)
        
        update_scene = QGraphicsScene()
        update_scene.addWidget(update_widget)
        
        self.main_view.setScene(update_scene)

    def switch_to_get_scene(self):
        self.main_scene.clear()

        get_widget = QWidget()
        get_layout = QVBoxLayout()
        get_layout.addWidget(QLabel("Get Scene Content"))
        get_widget.setLayout(get_layout)

        get_scene = QGraphicsScene()
        get_scene.addWidget(get_widget)

        self.main_view.setScene(get_scene)

    def switch_to_delete_scene(self):
        self.main_scene.clear()

        delete_widget = QWidget()
        delete_layout = QVBoxLayout()
        delete_layout.addWidget(QLabel("Delete Scene Content"))
        delete_widget.setLayout(delete_layout)

        delete_scene = QGraphicsScene()
        delete_scene.addWidget(delete_widget)

        self.main_view.setScene(delete_scene)


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
    
    def update_subject(self):
        self.update_window = UpdaterWindow('Subject')
        self.update_window.show()
    
    def update_teacher(self):
        self.update_window = UpdaterWindow('Teacher')
        self.update_window.show()
    
    def update_class(self):
        self.update_window = UpdaterWindow('Class')
        self.update_window.show()
    
    def update_student(self):
        self.update_window = UpdaterWindow('Student')
        self.update_window.show()

def run_interface():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())