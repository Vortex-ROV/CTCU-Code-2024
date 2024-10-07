from PyQt5.QtWidgets import QPushButton, QFileDialog, QMainWindow, QTableWidget, QLabel
import csv
from PyQt5 import uic
import pandas as pd
from .plot import plotting, plotting_3d,find_highest_sturgeon


class Manual(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        uic.loadUi("csv_manual.ui", self)

        self.output_screen = self.findChild(QLabel, "output_screen")

        self.save_button = self.findChild(QPushButton, "save_button")
        self.save_button.clicked.connect(self.save_data)

        self.data_plot = self.findChild(QPushButton, 'twod_plot')
        self.data_plot.clicked.connect(self.plot_data)

        self.threed_plot = self.findChild(QPushButton, "threed_plot")
        self.threed_plot.clicked.connect(self.plot_3d_data)

        self.table = self.findChild(QTableWidget, "table")

        # self.table = QTableWidget(4, 15)
        self.table.setVerticalHeaderLabels(
            ["Days", "Receiver 1", "Receiver 2", "Receiver 3"]
        )
        self.table.setHorizontalHeaderLabels(
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        )
        self.table.setColumnWidth(0, 20)
        self.table.setColumnWidth(1, 20)
        self.table.setColumnWidth(2, 20)
        self.table.setColumnWidth(3, 20)
        self.table.setColumnWidth(4, 20)
        self.table.setColumnWidth(5, 20)
        self.table.setColumnWidth(6, 20)
        self.table.setColumnWidth(7, 20)
        self.table.setColumnWidth(8, 20)
        self.table.setColumnWidth(9, 20)
        self.table.setColumnWidth(10, 20)
        self.table.setColumnWidth(11, 20)
        self.table.setColumnWidth(12, 20)
        self.table.setColumnWidth(13, 20)
        self.table.setColumnWidth(14, 20)
        self.table.setColumnWidth(15, 20)

    def save_data(self):
        with open("manual.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                writer.writerow(row_data)

    def load_data(self):
        self.data = pd.read_csv("manual.csv")
        if not self.data.empty:
            self.output_screen.setText("Data loaded successfully.")
        else:
            self.output_screen.setText("Failed to load data.")

    def plot_data(self):
        try:
            self.save_data()
            self.load_data()
            if self.data.shape[0] == 3:
                days = self.data.columns[0: ].values
                reciever1 = self.data.iloc[0, 0:].values
                reciever2 = self.data.iloc[1, 0:].values
                reciever3 = self.data.iloc[2, 0:].values
            highest_receiver, highest_value = find_highest_sturgeon(self.data)
            print(f"The highest number of sturgeon over a five-day period is found at {highest_receiver} with a count of {highest_value}.")

            self.graph = plotting(reciever1, reciever2, reciever3, days, highest_receiver)
        except:
            self.output_screen.setText("Failed to Plot Data")
            print("Failed to Plot Data")

    def plot_3d_data(self):
        try:
            self.save_data()
            self.load_data()
            if self.data.shape[0] == 3:
                days = self.data.columns[0:].values.astype(int) 
                receiver1 = self.data.iloc[0, :].values
                receiver2 = self.data.iloc[1, :].values
                receiver3 = self.data.iloc[2, :].values
                print("Days:", days)
                print("Receiver 1:", receiver1)
                print("Receiver 2:", receiver2)
                print("Receiver 3:", receiver3)
                highest_receiver, highest_value = find_highest_sturgeon(self.data)
                print(f"The highest number of sturgeon over a five-day period is found at {highest_receiver} with a count of {highest_value}.")
                plotting_3d(receiver1, receiver2, receiver3, days,highest_receiver)
            elif self.data.shape[0] == 15:
                days = self.data.iloc[:, 0].values.astype(int)
                receiver1 = self.data.iloc[:, 1].values
                receiver2 = self.data.iloc[:, 2].values
                receiver3 = self.data.iloc[:, 3].values
                print("Days:", days)
                print("Receiver 1:", receiver1)
                print("Receiver 2:", receiver2)
                print("Receiver 3:", receiver3)
                highest_receiver, highest_value = find_highest_sturgeon(self.data)
                print(f"The highest number of sturgeon over a five-day period is found at {highest_receiver} with a count of {highest_value}.")
                plotting_3d(receiver1, receiver2, receiver3, days,highest_receiver)
            else:
                self.output_screen.setText("Invalid data format.")
        except Exception as e:
            print(e)
            self.output_screen.setText("Failed to Plot 3D Data")

