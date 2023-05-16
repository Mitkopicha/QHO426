from tech import Tech

class Laser(Tech):

    MAX_RANGE = 100

    def __init__(self):
        pass

    def __str__(self):
        return "Laser object with max_range 100m"

    def __repr__(self):
        return "Laser()"

    def fire(self,range):
        if range <= Laser.MAX_RANGE:
            print("PEW PEW PEW, ENEMY IS IN TROUBLE!!")
        else:
            print("Enemy is safe")

    def activate(self):
        print("Laser ready to fire!")

    def deactivate(self):
        print("Laser shuts down!")


if __name__ == "__main__":
    las = Laser()
    las.fire(80)
    las.fire(120)