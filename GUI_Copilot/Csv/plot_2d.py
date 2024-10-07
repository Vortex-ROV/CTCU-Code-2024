import matplotlib.pyplot as plt

def plotting_2d(rec1, rec2, rec3, days, rows):
    plt.figure(figsize=(10, 5))

    plt.plot(days, rec1, label="Receiver 1")
    plt.plot(days, rec2, label="Receiver 2")
    plt.plot(days, rec3, label="Receiver 3")

    plt.xlabel("Day")
    plt.ylabel("# of sturgeon")
    plt.title("Number of sturgeon detected at each Receiver over time")

    # plt.xlim(0, rows)
    # plt.xticks(range(0, rows+1, 1))
    # plt.ylim(0, rows)
    # plt.yticks(range(0, rows+1, 1))

    plt.grid(True)

    plt.legend()

    plt.show()