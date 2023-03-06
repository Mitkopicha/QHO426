# Get user input
steps = int(input("How far are we from the cave? "))
# Use for loop
for i in range (0,steps,1):
    print(f"{steps} steps remaining")
    steps= steps-1
#Display result
print("\nWe have reached the cave!")