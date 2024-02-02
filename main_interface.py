import sys
from PyQt6.QtWidgets import QSizePolicy, QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView
from entity_interface import EntityWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setMinimumSize(500, 500)

        self.main_scene = QGraphicsScene()
        self.main_view = QGraphicsView(self.main_scene)

        self.scene_buttons_mapping = {
            'create': {'text': 'Create', 'operation': self.create_entity},
            'update': {'text': 'Update', 'operation': self.update_entity},
            'get': {'text': 'Get', 'operation': self.get_entity},
            'delete': {'text': 'Delete', 'operation': self.delete_entity}
        }

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_view)
        self.central_widget.setLayout(self.main_layout)

        self.create_buttons()
        self.populate_main_scene()

    def populate_main_scene(self):
        self.main_scene.clear()
        text = 'Press buttons below to interact with the database.'
        self.main_scene.addText(text)

    def create_buttons(self):
        for scene_type, properties in self.scene_buttons_mapping.items():
            button = QPushButton(f'{properties["text"]}')
            button.clicked.connect(lambda _, st=scene_type: self.switch_scene(st))
            self.main_layout.addWidget(button)

    def switch_scene(self, scene_type):
        self.main_scene.clear()
        entity_types = ['Subject', 'Teacher', 'Class', 'Student']
        layout = QVBoxLayout()
        layout.setSpacing(20)

        for entity_type in entity_types:
            base_text = self.scene_buttons_mapping[scene_type]["text"]
            button_text = f'{base_text} {entity_type}'
            button = QPushButton(button_text)
            button.setSizePolicy(
                QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Minimum
            )
            func = self.scene_buttons_mapping[scene_type]["operation"]
            button.clicked.connect(func(entity_type))
            layout.addWidget(button, 1)

        widget = QWidget()
        widget.setLayout(layout)

        scene = QGraphicsScene()
        scene.addWidget(widget)

        self.main_view.setScene(scene)

    def create_entity(self, entity_type):
        def create():
            self.creation_window = EntityWindow(entity_type, 'create')
            self.creation_window.show()
        return create

    def update_entity(self, entity_type):
        def update():
            self.update_window = EntityWindow(entity_type, 'update')
            self.update_window.show()
        return update

    def get_entity(self, entity_type):
        def get():
            self.get_window = EntityWindow(entity_type, 'get')
            self.get_window.show()
        return get

    def delete_entity(self, entity_type):
        def delete():
            self.delete_window = EntityWindow(entity_type, 'delete')
            self.delete_window.show()
        return delete


def run_interface():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
