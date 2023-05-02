def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left" , "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    x = directions()
    for index in range(len(x)):
        print(f"{index}:{x[index]}")


def run():
    menu()


run()