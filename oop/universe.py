from planet import Planet
from human import Human
from robot import Robot
from random import randint
import matplotlib.pyplot as plt

class  Universe:

    def __init__(self):
        self.planets = []

    def __str__(self):
        return f"Universe contains planets: {self.planets}"

    def __repr__(self):
        return f"Universe contains planets {self.planets}"

    def generate(self):
        p = Planet()
        hum_num = randint(1, 10)
        rob_num = randint(1, 10)
        for hum in range(hum_num):
            h = Human()
            p.add(h)
        for rob in range(rob_num):
            r = Robot()
            p.add(r)
        self.planets.append(p)



    def show_populations(self):
        num_planets = len(self.planets)
        fig = plt.figure()
        num_hum , num_rob = 0,0
        for i in range(num_planets):
            planet = self.planets[i]

            for dude in planet.inhabitants:
                if isinstance(dude,Human): #method to verify the class
                    num_hum += 1
                elif isinstance(dude,Robot):
                    num_rob += 1


            ax = fig.add_subplot(num_planets, 1, i+1)
            ax.bar(["Humans","Robots"], [num_hum , num_rob])
        plt.tight_layout
        plt.show()




if __name__ == "__main__":
    u1 = Universe()
    for i in range(2):
        u1.generate()
    u1.show_populations()

