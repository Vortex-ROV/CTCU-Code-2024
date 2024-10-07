# auto.py
from PyQt5.QtWidgets import QPushButton, QFileDialog, QLabel, QMainWindow
import csv
from PyQt5 import uic
import pandas as pd
from .plot import plotting, plotting_3d,find_highest_sturgeon


class Auto(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        uic.loadUi("csv_auto.ui", self)

        self.output_screen = self.findChild(QLabel, "output_screen")

        self.upload_data = self.findChild(QPushButton, "upload_data")
        self.upload_data.clicked.connect(self.load_data)

        self.twod_plot = self.findChild(QPushButton, "twod_plot")
        self.twod_plot.clicked.connect(self.plot_data)

        self.threed_plot = self.findChild(QPushButton, "threed_plot")
        self.threed_plot.clicked.connect(self.plot_3d_data)

    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(
        self, "Load Data", "", "All Files (*)"
    )

        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                if self.data.empty:
                    self.output_screen.setText("Failed to load data.")
                else:
                    self.output_screen.setText("Data loaded successfully.")
            except pd.errors.ParserError:
                # If it's not a CSV, try loading as Excel
                try:
                    self.data = pd.read_excel(file_path)
                    if self.data.empty:
                        self.output_screen.setText("Failed to load data.")
                    else:
                        self.output_screen.setText("Data loaded successfully.")
                except Exception as e:
                    print(e)
                    self.output_screen.setText("Failed to load data.")

    def plot_data(self):
        try:
            if self.data.shape[0] == 3:
                days = self.data.columns[0:].values
                days[0] = ""
                receiver1 = self.data.iloc[0, 0:].values
                receiver2 = self.data.iloc[1, 0:].values
                receiver3 = self.data.iloc[2, 0:].values
                receiver1[0] = receiver2[0] = receiver3[0] = None
                print("Days:", days)
                print("Receiver 1:", receiver1)
                print("Receiver 2:", receiver2)
                print("Receiver 3:", receiver3)
                highest_receiver, highest_value = find_highest_sturgeon(self.data)
                print(f"The highest number of sturgeon over a five-day period is found at {highest_receiver} with a count of {highest_value}.")
                self.graph = plotting(receiver1, receiver2, receiver3, days,highest_receiver)
            elif self.data.shape[0] == 15:
                days = self.data.iloc[0:, 0].values
                receiver1 = self.data.iloc[0:, 1].values
                receiver2 = self.data.iloc[0:, 2].values
                receiver3 = self.data.iloc[0:, 3].values
                print("Days:", days)
                print("Receiver 1:", receiver1)
                print("Receiver 2:", receiver2)
                print("Receiver 3:", receiver3)
                highest_receiver, highest_value = find_highest_sturgeon(self.data)
                print(f"The highest number of sturgeon over a five-day period is found at {highest_receiver} with a count of {highest_value}.")
                self.graph = plotting(receiver1, receiver2, receiver3, days,highest_receiver)

        except Exception as e:
            print(e)
            self.output_screen.setText("Failed to Plot Data")

    def plot_3d_data(self):
        try:
            if self.data is not None:
                if self.data.shape[0] == 3:
                    days = self.data.columns[1:].values.astype(int) 
                    receiver1 = self.data.iloc[0, 1:].values
                    receiver2 = self.data.iloc[1, 1:].values
                    receiver3 = self.data.iloc[2, 1:].values
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
                self.output_screen.setText("Data not loaded.")
        except Exception as e:
            print(e)
            self.output_screen.setText("Failed to Plot 3D Data")


