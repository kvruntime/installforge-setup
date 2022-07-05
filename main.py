from PyQt6.QtWidgets import *
import sys
from app.homepage import HomePage
from pathlib import Path

app = QApplication(sys.argv)

print(sys.argv)


win = HomePage()
win.show()
app.exec()
