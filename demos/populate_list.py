def directions():
    directions = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right" ]
    return directions


def menu():
    print("\nPlease select a direction: ")
    x = directions()
    for index in range(len(x)):
        print(f"{index} : {x[index]}")
    res = int(input())
    return x[res]


def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
       route.append(menu())
    print(f"Escape route: {route}")


run()


