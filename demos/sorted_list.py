def observed():
    observations = []
    for count in range(5):
        print("Enter observation please: ")
        observations.append(input())
    return observations


def remove_observations(observations):
    a = True

    while a:
        print("Do you wish to remove observations (yes/no)?")
        response = input()

        if response == "yes":
            o = input("What observation do you wish to remove? ")
            observations.remove(o)
            print("Done")
        else:
            a = False


def run(): #The third function should be named run and should have no parameters.
    x = observed() #The function should call the first function and store the returned list in a local variable.
    remove_observations(x)#The function should then call the second function with the previously retrieved list.


    #Finally, the function should display a sorted set of the observations
    # populate set
    observations_set = set() #new set
    for y in x:
        data = (y,x.count(y))#how many times each observation has been made.
        observations_set.add(data)#putting the data into the new set

    print("Observations:")
    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]}")


run()