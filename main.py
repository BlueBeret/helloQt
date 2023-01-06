from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window title
        self.setWindowTitle("Hello Qt")
        # create label
        label = QLabel("Hello World!")
        label2 = QLabel("print hehe")
        # set label alignment
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # set window size to 800 600
        self.resize(800, 600)
        # set label as central widget
        self.setCentralWidget(label2)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()