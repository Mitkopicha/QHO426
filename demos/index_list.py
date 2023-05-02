def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    x = movements()
    for index in range(0,len(x),2):
        print(f"{x[index]} for {x[index+1]} steps")



run()