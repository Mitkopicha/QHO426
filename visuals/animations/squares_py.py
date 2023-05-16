import matplotlib.pyplot as plt
import matplotlib.animation as a


boxes = []
fig,ax = plt.subplots()
format = ["bo--","r-","y-.","gx--","p--","wo"]


def init():
    boxes.append({"x":[2,10,10,2,2], "y":[10,10,2,2,10]}) #first outside square
    boxes.append({"x":[4,8,8,4,4], "y":[8,8,4,4,8]}) #smaller inside square
    boxes.append({"x":[5,7,7,5,5], "y":[7,7,5,5,7]}) #smallest inside square


def animate(f):
    ax.cla()
    ax.set_xlim(0,12)
    ax.set_ylim(0,12)
    ax.plot(boxes[f%3]["x"],boxes[f%3]["y"] ,format[f%6]) #the mod operator can be 0,1,2  of the the 3 lists

def run():
    garry = a.FuncAnimation(fig,animate, frames=100,interval=1000,init_func=init)
    # init_func needs to be used!!!! or at the top just use init()
    plt.show()

run()
