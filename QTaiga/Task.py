from task_ui import Ui_Task
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal

class Task(QWidget):

    doneSignal = pyqtSignal(["QString"])

    def __init__(self, taskName, parent=None):
        super().__init__()
        self.ui  = Ui_Task()
        self.ui.setupUi(self)

        self.ui.taskName.setText(taskName)
        self.ui.delete_2.clicked.connect(self._delete)
        self.ui.done.clicked.connect(self._done)

    def _delete(self):
        self.hide()
        self.deleteLater()

    def _done(self):
        self.doneSignal.emit(self.ui.taskName.text())
        self._delete()