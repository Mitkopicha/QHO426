import json
import matplotlib.pyplot as plt


def save(dictio={}):
    with open("data.json" ,"w") as f:
        json.dump(dictio,f)


def load():
    with open("data.json")as f:
        d=json.load(f)
    return d


def survey(n=3):
    c={}
    for i in range(n):
        resp=input("Who rules in your house? Me , Parter,Child,pet").lower()
        if resp not in{"child","pet","partner","me"}:
            resp="pet"
        c[resp]=c.get(resp,0)+1
    return c


def run():
    data ={}
    while True:
        print("Menu:\n1-New Survey\n2-Load Last Survey")
        opt = int(input("Enter your choice"))
        if opt == 1:
            n =int(input("Number of respondents:"))


d ={"name": "piotr" , "age":98,"dog":True}

save(d)
run()