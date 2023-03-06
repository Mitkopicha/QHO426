# Ask user for phrase 
print("What phrase do you see? ")
p = input()
# Use a for loop with the function len to determine the lenght of the phrase and print it backwards witha negative stop and step
for i in range(len(p)-1 , -1, -1):
    print(p[i], end="")


