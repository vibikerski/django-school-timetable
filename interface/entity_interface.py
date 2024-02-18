from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
import actions.create as Creator
import actions.update as Updater
import actions.get as Getter
import actions.delete as Deleter

operation_to_handler = {
    'create': Creator,
    'update': Updater,
    'get': Getter,
    'delete': Deleter
}

class EntityWindow(QWidget):
    def __init__(self, entity, operation):
        super().__init__()
        self.entity = entity
        self.operation = operation
        self.setWindowTitle(f'{operation.capitalize()} {entity}')
        self.layout = QVBoxLayout()

        if operation == 'update':
            text = 'Only type the ID and the fields that you wish to change.'
            self.caution_label = QLabel(text)
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
        return operation_to_handler[self.operation].get_fields(self.entity)

    def submit_operation(self):
        values = {
            field_name: field_widget.text()
            for field_name, field_widget in self.input_fields.items()
        }
        result = ''
        try:
            handler = operation_to_handler[self.operation]
            result = handler.entity(values, self.entity.lower())
        except Exception as e:
            self.error_label.setText(str(e))
            return

        if result and result["error"]:
            self.error_label.setText(result["error"])
        else:
            self.success_operation(result["data"])

    def success_operation(self, data):
        if self.operation == "get":
            self.success_get(data)
        else:
            msg = f"{self.entity} {self.operation}d successfully."
            QMessageBox.information(self, "Success", msg)
            self.close()

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
