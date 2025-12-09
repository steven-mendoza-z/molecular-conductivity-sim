from PySide6.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Molecular Conductivity Simulator")
        self.setGeometry(100, 100, 860, 540)

        self.add_ui()

    def add_ui(self):
        test_button = QPushButton("Test Button")
        test_button.clicked.connect(self.pressed_test_button)
        
        self.setCentralWidget(test_button)

    def pressed_test_button(self):
        print("Test button pressed!")

