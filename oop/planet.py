from human import Human
from robot import Robot


class Planet:

    def __init__(self):
        self.inhabitants = []


    def __str__(self):
        return f"This planet contains :{self.inhabitants}"

    def __repr__(self):
        return f"Planet (inhabitants = {self.inhabitants}"

    def add(self, inh):
        self.inhabitants.append(inh)

    def remove_human(self, inh):
        if inh in self.inhabitants:
            self.inhabitants.remove(inh)


if __name__ == "__main__":
    h1 = Human()
    h2 = Human()
    r1 = Robot()
    r2 = Robot()
    r3 = Robot()
    earth = Planet()
    earth.add_human(h1)
    earth.add_robot(r1)
    print(earth)
    print("-"*20)
    earth.add_human(h1)
    earth.add_robot(r3)
    print(earth)
    print("-"*20)
    earth.add_robot(r2)
    earth.remove_human(h2)
    print(earth)
