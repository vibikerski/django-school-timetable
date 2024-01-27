from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from create_validation import Creator
from update_validation import Updater
from get_validation import Getter

class EntityWindow(QWidget):
    def __init__(self, entity, operation):
        super().__init__()
        self.entity = entity
        self.operation = operation
        self.setWindowTitle(f'{operation.capitalize()} {entity}')
        self.layout = QVBoxLayout()

        if operation == 'update':
            self.caution_label = QLabel("Only type the ID and the fields that you wish to change.")
            self.layout.addWidget(self.caution_label)
        elif operation == "get":
            self.result_widget = QVBoxLayout()
            self.layout.addLayout(self.result_widget)
        
        self.input_fields = {}
        fields = self.get_fields()
        for field_name, _ in fields:
            label = QLabel(field_name)
            input_field = QLineEdit()
            self.layout.addWidget(label)
            self.layout.addWidget(input_field)
            self.input_fields[field_name] = input_field

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: red")
        self.layout.addWidget(self.error_label)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_operation)
        self.layout.addWidget(self.submit_button)

        self.back_button = QPushButton('Back to Main Window')
        self.back_button.clicked.connect(self.close)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def get_fields(self):
        if self.operation == 'create':
            return Creator.get_fields(self.entity)
        elif self.operation == 'update':
            return Updater.get_fields(self.entity)
        elif self.operation == 'get':
            return Getter.get_fields(self.entity)
        elif self.operation == 'delete':
            pass

    def submit_operation(self):
        values = {}
        for field_name, field_widget in self.input_fields.items():
            values[field_name] = field_widget.text()
        result = ''
        try:
            if self.operation == 'create':
                result = getattr(Creator, f'create_{self.entity.lower()}')(values)
            elif self.operation == 'update':
                result = getattr(Updater, f'update_{self.entity.lower()}')(values)
            elif self.operation == 'get':
                result = getattr(Getter, f'get_{self.entity.lower()}')(values)
            elif self.operation == 'delete':
                pass
        except Exception as e:
            self.error_label.setText(str(e))
            return

        if result and result["error"]:
            self.error_label.setText(result["error"])
        else:
            self.success_operation(result["data"])
    
    def success_operation(self, data):
        if self.operation == "update" or self.operation == "create":
            QMessageBox.information(self, "Success", f"{self.entity} {self.operation}d successfully.")
            self.close()
        elif self.operation == "get":
            self.success_get(data)
            
    def success_get(self, data):
        for _, input_field in self.input_fields.items():
            input_field.hide()
            self.layout.itemAt(self.layout.indexOf(input_field) - 1).widget().hide()
        self.submit_button.hide()
        dictionary = data.__dict__
        for name, value in dictionary.items():
            if name == "_state":
                continue
            label = QLabel(f'{name}: {value}')
            self.result_widget.addWidget(label)
        