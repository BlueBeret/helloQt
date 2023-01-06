from widget1 import Ui_Form
from PyQt6.QtCore import Qt, pyqtSignal


class AlertWidget(Ui_Form):
    def __init__(self, text="alert widget", slot=None):
        super().__init__()
        self.setupUi(self)
        self.slot = slot


        self.signalapa = 

    def close(self):
        self.hide()

    

# input box - button.