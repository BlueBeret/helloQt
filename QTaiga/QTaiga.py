from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from app_ui import Ui_MainWindow
from Task import Task

class MainUI(QMainWindow):


    def __init__(self):
        super().__init__()

        # init ui from py file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addButton.clicked.connect(self.add)

    def add(self):
        widget = Task(self.ui.taskInput.text())
        self.ui.taskInput.setText("")
        widget.doneSignal.connect(self.done)
        self.ui.tasksListContainer.layout().addWidget(widget)

    def done(self, taskName):
        label = QLabel(taskName)
        self.ui.doneTab.layout().insertWidget(0, label)

    def save(self):
        self.setCentralWidget(self.widget)

app = QApplication([])
window = MainUI()
window.show()
app.exec()