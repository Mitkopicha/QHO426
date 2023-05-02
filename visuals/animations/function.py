import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
    print(frame)


def run():
    fig = plt.figure()
    bob = animation.FuncAnimation(fig, animate, interval=1000,frames = 10, repeat = False)  # FuncAnim is repeatedly calling animate function
    #repeat is by default true... setting it to false will stop iterating
    plt.show()


run()
