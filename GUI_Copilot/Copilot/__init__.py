from PyQt5.QtWidgets import QApplication
import sys
from .findChild import UI

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
