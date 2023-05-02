import matplotlib.pyplot as plt

def coffee_sleep(n=5):
    coffee = []
    sleep = []
    for i in range(n):
        coffee.append(int(input("Enter amount of coffee you drink per week: ")))
        sleep.append(int(input("Enter average sleep duration per night per week: ")))
    return coffee,sleep # returning two things they become a tuple of lists and can be viewed only


#print(coffee_sleep(3)) #
#([3, 3, 39], [9, 9, 44]) to access 9 we need coffee_sleep[2][2]???????


def movies(n=5):
    movie = {}
    for i in range(n):
        genre = input("Enter your favourite movie genre: ")
        movie[genre] = movie.get(genre, 0) + 1
    return movie


def music(n=5):
    songs = {}
    for i in range(n):
        genre = input("Enter your favourite music genre: ")
        songs[genre] = songs.get(genre, 0) + 1
    return songs


def mm_vs_dd(n = 5):
    mm, dd = 0, 0
    for i in range(n):
        ans = input("Who wins? Mickey Mouse or Donald Duck? ")
        if ans.lower() == "mm":
            mm += 1
        elif ans.lower() == "dd":
            dd += 1
        else:
            print("That's not a valid answer!")
    return [mm , dd] #We treat the return value as a list


def run():
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    n = int(input("Enter number of respondents: "))
    c_s = coffee_sleep(n)
    ms = movies(n)
    ss = music(n)

    ax1.plot(c_s[0], c_s[1], "rx")
    ax1.set_xlabel("Coffee intake(cups per day)")
    ax1.set_ylabel("Sleep in h per night")
    ax1.set_title("Coffee vs Sleep")

    ax2.pie(ms.values(), labels= ms.keys(), autopct="%1.1f%%")
    # format of the number in pie chart "autopct" with one deciamal positions and a percentage sign
    ax2.set_title("Movies preferences ") #putting title to the chart
    #CREATING PIE CHART


    ax3.pie(ss.values(), labels = ss.keys(), autopct= "%.f%%")
    ax3.set_title("Music preferences")

    ax4.bar(["MM", "DD"], mm_vs_dd(n))#CREATING BAR CHART
    ax4.set_xlabel("Characters")#putting label on x to the chart
    ax4.set_ylabel("Frequency")# putting label on y to the chart
    ax4.set_title("The battle of the titans")

    plt.tight_layout()
    plt.show()


run()

