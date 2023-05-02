import csv
import matplotlib.pyplot as plt

def gather_data(n=1):
    with open("feb_data.csv", "w") as f:
        csv_writer = csv.writer(f)
        for i in range(n):
            h = float(input("Enter height: "))
            w = float(input("Enter weight: "))
            csv_writer.writerow([h,w])

def retrieve_data():
    with open("feb_data.csv") as f:
        csv_reader = csv.reader(f)
        hs = []
        ws = []
        for row in csv_reader:
            if len(row) != 0:
                hs.append(row[0])
                ws.append(row[1])
    return hs, ws

def graphs():
    x, y = retrieve_data()
    plt.plot(x, y, "ro")
    plt.show()

graphs()
