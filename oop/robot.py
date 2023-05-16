class Robot:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = Robot.MAX_ENERGY

    def __str__(self):
        return f"{self.name} of age {self.age} has {self.energy} energy"

    def __repr__(self):
        return f"Robot (name={self.name}, age={self.age}, energy={self.energy})"

    def display(self):
        print(f"I am {self.name}")

if __name__ == "__main__":
    r = Robot()
    r.display()
    print(r)
    print(repr(r))