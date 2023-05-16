import matplotlib.pyplot as plt
import matplotlib.animation as a
import numpy as np

fig, ax = plt.subplots()

def animate(f):
    ax.cla()
    ax.set_xlim(0,720)
    ax.set_ylim(-1,1)
    angels = np.arange(0,720) #generate an array from 0 to 720
    ang_rad = angels*np.pi/180
    y = np.sin(ang_rad - f/20)
    ax.plot(angels,y,"gx")

def run():
    larry = a.FuncAnimation(fig , animate, frames=720,interval=100)
    plt.show()

run()


