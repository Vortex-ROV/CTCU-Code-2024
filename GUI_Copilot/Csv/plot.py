# plot.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtWidgets import QPushButton, QFileDialog, QLabel, QMainWindow
import csv
from PyQt5 import uic
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def find_highest_sturgeon(data):
    highest_receiver = None
    highest_value = -1

    if data.shape[0] == 3:  # Check if the data is in vertical format
        for i in range(len(data.columns) - 4):
            rec1_sum = sum(data.iloc[0, i+1:i+6])  # Skip the first column
            rec2_sum = sum(data.iloc[1, i+1:i+6])
            rec3_sum = sum(data.iloc[2, i+1:i+6])

            if rec1_sum > highest_value:
                highest_value = rec1_sum
                highest_receiver = 'Receiver 1'

            if rec2_sum > highest_value:
                highest_value = rec2_sum
                highest_receiver = 'Receiver 2'

            if rec3_sum > highest_value:
                highest_value = rec3_sum
                highest_receiver = 'Receiver 3'
    elif data.shape[0] == 15:  # Check if the data is in horizontal format
        for i in range(len(data) - 4):
            rec1_sum = sum(data['Receiver 1'][i+1:i+6])  # Skip the first column
            rec2_sum = sum(data['Receiver 2'][i+1:i+6])
            rec3_sum = sum(data['Receiver 3'][i+1:i+6])

            if rec1_sum > highest_value:
                highest_value = rec1_sum
                highest_receiver = 'Receiver 1'

            if rec2_sum > highest_value:
                highest_value = rec2_sum
                highest_receiver = 'Receiver 2'

            if rec3_sum > highest_value:
                highest_value = rec3_sum
                highest_receiver = 'Receiver 3'

    return highest_receiver, highest_value

def plotting(rec1, rec2, rec3, days,highest_rece):
    plt.figure(figsize=(10, 5))

    plt.plot(days, rec1, label="Receiver 1")
    plt.plot(days, rec2, label="Receiver 2")
    plt.plot(days, rec3, label="Receiver 3")

    plt.xlabel("Day")
    plt.ylabel("# of sturgeon")
    plt.title(f"Number of sturgeon detected at each Receiver over time\n{highest_rece} is the highest value ")

    plt.xlim(0, 15)
    plt.xticks(range(0, 16, 1))
    plt.ylim(0, 15)
    plt.yticks(range(0, 16, 1))

    plt.grid(True)

    plt.legend()

    plt.show()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotting_3d(rec1, rec2, rec3, days,highest_rece):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    bar_width = 0.2  # Adjust the width of the bars as needed

    # Positions for the bars (1, 2, 3 for receivers 1, 2, 3)
    x_positions = [1, 2, 3]

    # Adjust the x-coordinates for each receiver
    x_rec1 = [x_positions[0]] * len(days)
    x_rec2 = [x_positions[1]] * len(days)
    x_rec3 = [x_positions[2]] * len(days)

    ax.bar3d(x_rec1, days, [0]*len(days), bar_width, 0.5, rec1, color='b', label="Receiver 1")
    ax.bar3d(x_rec2, days, [0]*len(days), bar_width, 0.5, rec2, color='g', label="Receiver 2")
    ax.bar3d(x_rec3, days, [0]*len(days), bar_width, 0.5, rec3, color='r', label="Receiver 3")

    ax.set_xlabel("Receiver")  # Set the x-axis label to Receiver
    ax.set_ylabel("Day")       # Set the y-axis label to Day
    ax.set_zlabel("# of sturgeon")
    ax.set_title(f"Number of sturgeon detected at each Receiver over time\n{highest_rece} is the highest value")

    ax.legend()

    # Set the tick labels for the x-axis to display receiver names instead of a range
    ax.set_xticks([0,1,2])  # Custom x-ticks positions
    ax.set_xticklabels(["Receiver 1", "Receiver 2", "Receiver 3"])
    # Adjust y-axis limits and tick labels
    ax.set_ylim(0, len(days) + 1)
    ax.set_yticks(range(1, len(days) + 1, 1))
    ax.set_yticklabels(days)

    # Set the viewing angle to adjust orientation
    ax.view_init(elev=15, azim=20)  # Adjust the elevation and azimuth angles as needed

    plt.show()

