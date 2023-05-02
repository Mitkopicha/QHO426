import matplotlib.pyplot as plt
import matplotlib.animation as a

fig, ax = plt.subplots(1,1)


def animate(f):
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.plot(f,f, "o")

def run():
    karen = a.FuncAnimation(fig,animate,frames = 10,interval = 1000)
    plt.show()

run()