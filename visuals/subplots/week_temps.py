import csv
import matplotlib.pyplot as plt


def read_data():
    with open("temps.csv") as f:
        reader = csv.reader(f)
        next(reader)
        dicto = {"week1": [], "week2":[]}
        for row in reader:
            dicto["week1"].append(row[0])
            dicto["week2"].append(row[1])
        return dicto

def run():
    data = read_data()
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)

    ax1.plot(range(1,8), data["week1"], "r^--") # r for red ; ^ for the
    ax2.plot(range(1,8), data["week2"], "bx-") # b for blue ; x for crosses and - for straight line

    plt.show()

run()