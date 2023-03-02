print("What phrase do you see? ")
p = input()

for i in range(len(p)-1 , -1, -1):
    print(p[i], end="")


