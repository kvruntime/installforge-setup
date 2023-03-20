from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        self.counter: int = 0

        self.initalize_component()
        self._binding()
        self.refresh_ui()
        pass

    def initalize_component(self):
        self.btnCounter = QPushButton("Counter")
        self.lblCounter = QLabel("--")
        self.lblCounter.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lay = QVBoxLayout(self)
        lay.addWidget(self.btnCounter)
        lay.addWidget(self.lblCounter)
        return None

    def _binding(self):
        self.btnCounter.clicked.connect(self.increment_counter)
        return None

    def increment_counter(self):
        self.counter += 1
        self.refresh_ui()
        return

    def refresh_ui(self):
        _time = "times" if self.counter != 0 else "time"
        _msg = f"pressed {self.counter} {_time}"
        self.lblCounter.setText(_msg)
        return None
