from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from create_validation import Creator

class CreationWindow(QWidget):
    def __init__(self, entity):
        super().__init__()
        self.entity = entity
        self.setWindowTitle(f'Create {entity}')
        self.layout = QVBoxLayout()
        
        self.input_fields = {}
        for field_name, _ in Creator.get_fields(entity):
            label = QLabel(field_name)
            input_field = QLineEdit()
            self.layout.addWidget(label)
            self.layout.addWidget(input_field)
            self.input_fields[field_name] = input_field

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: red")
        self.layout.addWidget(self.error_label)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_creation)
        self.layout.addWidget(self.submit_button)

        self.back_button = QPushButton('Back to Main Window')
        self.back_button.clicked.connect(self.close)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def submit_creation(self):
        values = {}
        for field_name, field_widget in self.input_fields.items():
            values[field_name] = field_widget.text()
        result = ''
        try:
            if self.entity == 'Subject':
                result = Creator.create_subject(values)
            elif self.entity == 'Teacher':
                result = Creator.create_teacher(values)
            elif self.entity == 'Class':
                result = Creator.create_class(values)
            elif self.entity == 'Student':
                result = Creator.create_student(values)
        except Exception as e:
            self.error_label.setText(str(e))
            return

        if result:
            self.error_label.setText(result["error"])
        else:
            self.success_creation()
    
    def success_creation(self):
        QMessageBox.information(self, "Success", f"{self.entity} created successfully.")
        self.close()