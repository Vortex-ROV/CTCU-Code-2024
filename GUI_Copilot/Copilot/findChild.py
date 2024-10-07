from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QComboBox, QTableView, QTableWidget
from PyQt5.uic import loadUi
from Csv.csv import Csv
from Float.float import Float


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        loadUi("copilot.ui", self)  

        # Csv
        self.csv_manual = self.findChild(QPushButton, "csv_manual")
        self.csv_auto = self.findChild(QPushButton, "csv_auto")
        self.csv = Csv(self.csv_manual, self.csv_auto)

        # Float
        self.float_table = self.findChild(QTableWidget, "float_table")
        self.display_float = self.findChild(QPushButton, "display_float")
        try:
            self.float = Float(self.float_table, self.display_float)
        except Exception as e:
            print(f"Error Connecting to Float: ")
            # print(f"Error Connecting to Float: {e}")

        self.show()
