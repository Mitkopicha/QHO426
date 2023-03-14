# Get input from the user
r = int(input("How many numbers should I sum up? "))
# Blank space
print("")
# Declaring control variable
i = 0
# Total sum of the numbers
total = 0
# Introducing while loop
while r > i:
    n = int(input(f"Please enter number {i+1} of {r}:\n"))
    i = i + 1
    total = total + n
# Display answer
print(f"\nThe answer is {total}")
