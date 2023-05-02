def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods),max(likelihoods)

def run():
    x = likelihood()
    print(f"Minimum likelihood of falling: {x[0]}%\nMaximum likelihood of falling: {x[1]}%")

run()