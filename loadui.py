from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        # load ui file
        uic.loadUi("app.ui", self)

        # set window title
        self.setWindowTitle("Hello Qt")

        # change label
        self.label.setText("Hello From Main")
        
app = QApplication([])
window = UI()
window.show()
app.exec()