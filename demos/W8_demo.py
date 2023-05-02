import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(3,2) #first the rows then the columns
#starts from 0 the count
x = range(5, 10)  # the end point is not included (10)
y = range(20, 40, 4)
ax[0, 0].plot(x, y, "ro-") # we want red check of 0-
ax[0, 0].set_xlim(0, 10)
ax[0, 0].set_ylim(0, 40)
ax[0, 0].tick_params(which = "both", width = 2) # creating ticks length and width
ax[0, 0].tick_params(which = "major",length = 6 ,color = "g")
ax[0, 0].tick_params(which = "minor", length = 2, color = "r")

ax[0, 0].yaxis.set_minor_locator(MultipleLocator(5))
ax[0, 0].yaxis.set_major_locator(MultipleLocator(10))
ax[0, 0].xaxis.set_minor_locator(MultipleLocator(0.5))
ax[0, 0].xaxis.set_major_locator(MultipleLocator(2))


ax[2,1].plot(y, x, "y^--")# the color is "y" yellow and the pointer is "^"
ax[1,1].bar(x, y, color = "g")
plt.show()
