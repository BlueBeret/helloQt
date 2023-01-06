import sys
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QLabel
from time import sleep

class MyThread(QThread):
    # Define a signal that will be used to communicate with the main thread
    signal = pyqtSignal(str)
    
    def run(self):
        # Perform some task in the thread
        sleep(5)
        result = "Task completed"
        
        # Emit the signal to communicate with the main thread
        self.signal.emit(result)

# Create the application and a label
app = QApplication(sys.argv)
label = QLabel("Waiting for task to complete...")
label.show()

# Create and start the thread
thread = MyThread()
thread.signal.connect(label.setText)
thread.start()

# Run the application's event loop
sys.exit(app.exec())
