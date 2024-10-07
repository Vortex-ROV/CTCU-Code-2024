# from scipy.interpolate import spline
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import math 
def plotting(depth, time, rows):
    plt.figure(figsize=(10, 5))

    #cubic_interpolation_model = interp1d(time,depth,kind = "cubic")
    # Plotting
    plt.plot(time, depth, marker='o', linestyle='-',label="Depth Vs Time")
    # plt.plot(time, depth, label="Depth Vs Time")

    #x = np.linspace(time.min(),time.max(),50)
    #y = cubic_interpolation_model(x)

    #plt.plot(x, y, label="Depth Vs Time")

    # print(depth)
    # print(time)

    plt.xlabel("Time")
    plt.ylabel("Depth (m)")
    plt.title("Incoming Data from Float")

    # plt.xlim(0, rows%100)
    # plt.xticks(range(0, rows+1, rows%10))
    # plt.ylim(0, rows%100)
    # plt.yticks(range(0, rows+1, rows%10))

    # xnew = np.linspace(time.min(), time.max(), 50)
    # print(time.min())
    # power_smooth = spline(time, depth, xnew)
    # plt.plot(xnew,depth)
    # plt.show()

    plt.grid(True)

    plt.legend()

    plt.show()