from PySide6.QtWidgets import QApplication
from .main_window import MainWindow
import os
import sys

class MainApp(QApplication):
    def __init__(self, args):
        super().__init__(args)

    def config(self):

        # first set styles from styles.qss
        with open(os.path.join(os.path.dirname(__file__), "styles.qss"), "r") as f:
            self.setStyleSheet(f.read())
        

    
    def run_app(self):
        self.config()

        window = MainWindow()
        window.show()
        
        sys.exit(self.exec())
        
