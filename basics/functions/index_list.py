def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    n = movements()
    print(f" {n[0]} for {n[1]} steps")
    print(f" {n[2]} for {n[3]} steps")
    print(f" {n[4]} for {n[5]} steps")
    print(f" {n[6]} for {n[7]} steps")




run()
