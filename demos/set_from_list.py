def observed():
    observations = []
    for i in range(7):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def run():
    print("Counting observations...\n")
    n = observed()

    #populate set
    my_set = set()
    for x in n:
        data = (x,n.count(x))
        my_set.add(data)
    #display set
    for data in my_set:
        print(f"{data[0]} observed {data[1]} times")


run()
