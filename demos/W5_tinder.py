def interests():
    print("Enter all your interests, one after another or \"stop\" to stop")
    s1 = set()
    interest = ""
    while True:
        interest = input()
        if interest.lower() == "stop":
            break
        # if isinstance(interest, str) # Not trusting the user if its not a string
        s1.add(interest)
    return s1


def tinderDaSecond():
    print("First person: ")
    p1 = interests()
    print("Second person: ")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
        print(f"You are a match made in heaven! You have {len(common)} interest in common")
    else:
        print("Oh no. It's not gonna work. Find another person")



tinderDaSecond()