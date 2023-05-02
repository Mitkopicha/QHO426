import json
import matplotlib.pyplot as plt

def save(dictio = {}):
    with open("data.json", "w") as f:
        json.dump(dictio, f)

def load():
    with open("data.json") as f:
        d = json.load(f)
    return d

def survey(n=3):
    c = {}
    for i in range(n):
        resp = input("Who rules in your house? Me, partner, child, pet.").lower()
        if resp not in {"child", "pet", "partner", "me"}:
            resp = "pet"
        c[resp] = c.get(resp, 0) + 1
    return c

def run():
    data = {}
    while True:
        print("Menu:\n1-New Survey\n2-Load last Survey\n3-Save Results\n4-Visualise\n5-Exit")
        opt = int(input("Enter your choice: "))
        if opt == 1:
            n = int(input("Number of respondents: "))
            data = survey(n)
        elif opt == 2:
            data = load()
        elif opt == 3:
            save(data)
        elif opt == 4:
            print("Choose type:\na-Point Graph\nb-Bar Chart\nc-Pie Chart")
            opt2 = input().lower()
            if opt2 == "a":
                plt.plot(data.keys(), data.values(), "y^-")
            elif opt2 == "b":
                plt.bar(data.keys(), data.values(), color = "#e3ff04")
            elif opt2 == "c":
                plt.pie(data.values(), labels = data.keys(), autopct= "%.0f")
            plt.show()
        elif opt == 5:
            break


