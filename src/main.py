from PyQt6.QtWidgets import QApplication
import sys
from pages.homepage import HomePage

app = QApplication(sys.argv)



win = HomePage()
win.show()
app.exec()
