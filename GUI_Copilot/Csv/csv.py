from PyQt5.QtWidgets import QMainWindow
from .auto import Auto
from .manual import Manual


class Csv(QMainWindow):
    def __init__(self, csv_manual, csv_auto):
        super(Csv, self).__init__()

        self.csv_manual = csv_manual
        self.csv_manual.clicked.connect(self.manual_data)

        self.csv_auto = csv_auto
        self.csv_auto.clicked.connect(self.auto_data)

    def auto_data(self):
        self.auto_plot = Auto()
        self.auto_plot.show()

    def manual_data(self):
        self.manual_plot = Manual()
        self.manual_plot.show()
